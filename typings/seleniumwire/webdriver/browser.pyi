"""
This type stub file was generated by pyright.
"""

from selenium.webdriver import Chrome as _Chrome, Edge as _Edge, Firefox as _Firefox, Remote as _Remote, Safari as _Safari
from .request import InspectRequestsMixin

class Firefox(InspectRequestsMixin, _Firefox):
    """Extends the Firefox webdriver to provide additional methods for inspecting requests."""
    def __init__(self, *args, seleniumwire_options=..., **kwargs) -> None:
        """Initialise a new Firefox WebDriver instance.

        Args:
            seleniumwire_options: The seleniumwire options dictionary.
        """
        ...
    
    def quit(self):
        ...
    


class Chrome(InspectRequestsMixin, _Chrome):
    """Extends the Chrome webdriver to provide additional methods for inspecting requests."""
    def __init__(self, *args, seleniumwire_options=..., **kwargs) -> None:
        """Initialise a new Chrome WebDriver instance.

        Args:
            seleniumwire_options: The seleniumwire options dictionary.
        """
        ...
    
    def quit(self):
        ...
    


class Safari(InspectRequestsMixin, _Safari):
    """Extends the Safari webdriver to provide additional methods for inspecting requests."""
    def __init__(self, seleniumwire_options=..., *args, **kwargs) -> None:
        """Initialise a new Safari WebDriver instance.

        Args:
            seleniumwire_options: The seleniumwire options dictionary.
        """
        ...
    
    def quit(self):
        ...
    


class Edge(InspectRequestsMixin, _Edge):
    """Extends the Edge webdriver to provide additional methods for inspecting requests."""
    def __init__(self, seleniumwire_options=..., *args, **kwargs) -> None:
        """Initialise a new Edge WebDriver instance.

        Args:
            seleniumwire_options: The seleniumwire options dictionary.
        """
        ...
    
    def quit(self):
        ...
    


class Remote(InspectRequestsMixin, _Remote):
    """Extends the Remote webdriver to provide additional methods for inspecting requests."""
    def __init__(self, *args, seleniumwire_options=..., **kwargs) -> None:
        """Initialise a new Firefox WebDriver instance.

        Args:
            seleniumwire_options: The seleniumwire options dictionary.
        """
        ...
    
    def quit(self):
        ...
    


