from typing import Any, Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

# BASE RESPONSE
class BaseResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None

# SUCCESS RESPONSE
class SuccessResponse(BaseResponse):
    success: bool = True

# ERROR RESPONSE
class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error_code: Optional[str] = None
    details: Optional[Any] = None

# PAGINATION MODEL
class Pagination(BaseModel):
    page: int
    size: int
    total: int
    pages: int

# PAGINATED RESPONSE
class PaginatedResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str
    data: list[T]
    pagination: Pagination

# RESPONSE HELPERS
def success_response(message: str, data: Any = None):
    return {
        "success": True,
        "message": message,
        "data": data
    }

def error_response(message: str, error_code: str = None, details: Any = None):
    return {
        "success": False,
        "message": message,
        "error_code": error_code,
        "details": details
    }

def paginated_response(message: str, data: list, page: int, size: int, total: int):
    pages = (total + size - 1) // size

    return {
        "success": True,
        "message": message,
        "data": data,
        "pagination": {
            "page": page,
            "size": size,
            "total": total,
            "pages": pages
        }
    }