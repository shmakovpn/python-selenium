"""
This type stub file was generated by pyright.
"""

class ErrorCode(object):
    """
    Error codes defined in the WebDriver wire protocol.
    """
    SUCCESS = ...
    NO_SUCH_ELEMENT = ...
    NO_SUCH_FRAME = ...
    UNKNOWN_COMMAND = ...
    STALE_ELEMENT_REFERENCE = ...
    ELEMENT_NOT_VISIBLE = ...
    INVALID_ELEMENT_STATE = ...
    UNKNOWN_ERROR = ...
    ELEMENT_IS_NOT_SELECTABLE = ...
    JAVASCRIPT_ERROR = ...
    XPATH_LOOKUP_ERROR = ...
    TIMEOUT = ...
    NO_SUCH_WINDOW = ...
    INVALID_COOKIE_DOMAIN = ...
    UNABLE_TO_SET_COOKIE = ...
    UNEXPECTED_ALERT_OPEN = ...
    NO_ALERT_OPEN = ...
    SCRIPT_TIMEOUT = ...
    INVALID_ELEMENT_COORDINATES = ...
    IME_NOT_AVAILABLE = ...
    IME_ENGINE_ACTIVATION_FAILED = ...
    INVALID_SELECTOR = ...
    SESSION_NOT_CREATED = ...
    MOVE_TARGET_OUT_OF_BOUNDS = ...
    INVALID_XPATH_SELECTOR = ...
    INVALID_XPATH_SELECTOR_RETURN_TYPER = ...
    ELEMENT_NOT_INTERACTABLE = ...
    INSECURE_CERTIFICATE = ...
    INVALID_ARGUMENT = ...
    INVALID_COORDINATES = ...
    INVALID_SESSION_ID = ...
    NO_SUCH_COOKIE = ...
    UNABLE_TO_CAPTURE_SCREEN = ...
    ELEMENT_CLICK_INTERCEPTED = ...
    UNKNOWN_METHOD = ...
    METHOD_NOT_ALLOWED = ...


class ErrorHandler(object):
    """
    Handles errors returned by the WebDriver server.
    """
    def check_response(self, response):
        """
        Checks that a JSON response from the WebDriver does not have an error.

        :Args:
         - response - The JSON response from the WebDriver server as a dictionary
           object.

        :Raises: If the response contains an error message.
        """
        ...
    


