class Message:
    def __init__(self, module: str):
        self.module = module.strip().replace("_", " ").title()

    def _msg(self, action: str, verb: str):
        return f"{self.module} {verb} successfully"

    def created(self):
        return self._msg("CREATED", "created")

    def updated(self):
        return self._msg("UPDATED", "updated")

    def deleted(self):
        return self._msg("DELETED", "deleted")

    def fetched(self):
        return self._msg("FETCHED", "fetched")

    def listed(self):
        return self._msg("LISTED", "listed")

    def not_found(self):
        return f"{self.module} not found"

    def already_exists(self):
        return f"{self.module} already exists"

    def failed(self):
        return f"Failed to process {self.module}"

    def invalid(self):
        return f"Invalid {self.module} data"


# AUTH MESSAGES
class AuthMessage:
    LOGIN_SUCCESS = "LOGIN_SUCCESS"
    LOGIN_FAILED = "LOGIN_FAILED"
    LOGOUT_SUCCESS = "LOGOUT_SUCCESS"
    TOKEN_EXPIRED = "TOKEN_EXPIRED"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"

# NOTIFICATION MESSAGES
class NotificationMessage:
    CREATED = "NOTIFICATION_CREATED"
    SENT = "NOTIFICATION_SENT"
    READ = "NOTIFICATION_READ"
    DELETED = "NOTIFICATION_DELETED"
    FAILED = "NOTIFICATION_FAILED"

# USER MESSAGES
class UserMessage:
    CREATED = "USER_CREATED"
    UPDATED = "USER_UPDATED"
    DELETED = "USER_DELETED"
    NOT_FOUND = "USER_NOT_FOUND"
    ALREADY_EXISTS = "USER_ALREADY_EXISTS"
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"

# VENDOR MESSAGES
class VendorMessage:
    CREATED = "VENDOR_CREATED"
    UPDATED = "VENDOR_UPDATED"
    DELETED = "VENDOR_DELETED"
    NOT_FOUND = "VENDOR_NOT_FOUND"
    ALREADY_EXISTS = "VENDOR_ALREADY_EXISTS"

# ROLE / RBAC MESSAGES
class RoleMessage:
    CREATED = "ROLE_CREATED"
    UPDATED = "ROLE_UPDATED"
    DELETED = "ROLE_DELETED"
    NOT_FOUND = "ROLE_NOT_FOUND"

class PermissionMessage:
    CREATED = "PERMISSION_CREATED"
    UPDATED = "PERMISSION_UPDATED"
    DELETED = "PERMISSION_DELETED"
    DENIED = "PERMISSION_DENIED"

# SYSTEM / COMMON MESSAGES
class SystemMessage:
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    ERROR = "ERROR"
    INTERNAL_ERROR = "INTERNAL_SERVER_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    DB_ERROR = "DATABASE_ERROR"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"

# FILE / STORAGE MESSAGES
class FileMessage:
    UPLOADED = "FILE_UPLOADED"
    UPLOAD_FAILED = "FILE_UPLOAD_FAILED"
    DELETED = "FILE_DELETED"
    NOT_FOUND = "FILE_NOT_FOUND"
    INVALID_TYPE = "INVALID_FILE_TYPE"
    SIZE_EXCEEDED = "FILE_SIZE_EXCEEDED"