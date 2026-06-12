from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.utils.logger import logger


from sqlalchemy.exc import SQLAlchemyError

from app.api.v1.schemas.response import error_response

class AppException(Exception):
    def __init__(self, message: str, error_code: str = "APP_ERROR", status_code: int = 400, details=None):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        self.details = details

class ExceptionMiddleware:
    def __init__(self, app):
        self.app = app
        self.register()

    def register(self):
        self.app.add_exception_handler(Exception, self.unhandled_exception)
        self.app.add_exception_handler(HTTPException, self.http_exception)
        self.app.add_exception_handler(RequestValidationError, self.validation_exception)
        self.app.add_exception_handler(AppException, self.app_exception)
        self.app.add_exception_handler(SQLAlchemyError, self.db_exception)

    # HTTP EXCEPTION (404, 401, 403 etc)    
    async def http_exception(self, request: Request, exc: HTTPException):
        logger.warning(
            f"HTTPException: {exc.detail}",
            extra={"status_code": exc.status_code, "url": str(request.url)}
        )
        return JSONResponse(
            status_code=exc.status_code,
            content=error_response(
                message=exc.detail,
                error_code="HTTP_EXCEPTION",
                details=None
            )
        )

    # VALIDATION ERROR (Pydantic)
    async def validation_exception(self, request: Request, exc: RequestValidationError):
        logger.warning(
            "Validation Error",
            extra={
                "errors": exc.errors(),
                "url": str(request.url)
            }
        )
        return JSONResponse(
            status_code=422,
            content=error_response(
                message="Validation Error",
                error_code="VALIDATION_ERROR",
                details=exc.errors()
            )
        )

    # CUSTOM APP EXCEPTION    
    async def app_exception(self, request: Request, exc: AppException):
        logger.error(
            f"AppException: {exc.message}",
            extra={
                "error_code": exc.error_code,
                "details": exc.details,
                "url": str(request.url)
            }
        )

        return JSONResponse(
            status_code=exc.status_code,
            content=error_response(
                message=exc.message,
                error_code=exc.error_code,
                details=exc.details
            )
        )

    # DATABASE ERROR    
    async def db_exception(self, request: Request, exc: SQLAlchemyError):
        logger.error(
            f"Database Error: {str(exc)}",
            extra={"url": str(request.url)}
        )

        return JSONResponse(
            status_code=500,
            content=error_response(
                message="Database Error",
                error_code="DB_ERROR",
                details=str(exc)
            )
        )

    # FALLBACK (CATCH ALL)    
    async def unhandled_exception(self, request: Request, exc: Exception):
        logger.critical(
            f"Unhandled Exception: {str(exc)}",
            extra={"url": str(request.url)}
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=error_response(
                message="Internal Server Error",
                error_code="INTERNAL_SERVER_ERROR",
                details=str(exc)
            )
        )