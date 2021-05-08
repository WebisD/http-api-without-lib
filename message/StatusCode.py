import enum

class StatusCode(enum.Enum):
    # Successful 2xx
    OK = ["200", "OK"]
    CREATED = ["201", "Created"]
    ACCEPTED = ["202", "Accepted"]
    NON_AUTHORITATIVE_INFORMATION = ["203", "Non-Authoritative Information"]
    RESET_CONTENT = ["205", "Reset Content"]
    # Redirection 3xx
    MULTIPLE_CHOICES = ["300", "Multiple Choices"]
    NOT_MODIFIED = ["304", "Not Modified"]
    # Client Error 4xx
    BAD_REQUEST = ["400", "Bad Request"]
    NOT_FOUND = ["404", "Not Found", "Page not found"]
    REQUEST_TIMEOUT = ["408", "Request Timeout"]
    UNSUPPORTED_MEDIA_TYPE = ["415", "Unsupported Media Type"]
    # Server Error 5xx
    INTERNAL_SERVER_ERROR = ["500", "Internal Server Error"]
    NOT_IMPLEMENTED = ["501", "Not Implemented"]
    BAD_GATEWAY = ["502", "Bad Gateway"]
    GATEWAY_TIMEOUT = ["504", "Gateway Timeout"]
    HTTP_VERSION_NOT_SUPPORTED = ["505", "HTTP Version Not Supported"]
