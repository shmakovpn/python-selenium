"""
This type stub file was generated by pyright.
"""

class Mobile(object):
    class ConnectionType(object):
        def __init__(self, mask) -> None:
            ...
        
        @property
        def airplane_mode(self):
            ...
        
        @property
        def wifi(self):
            ...
        
        @property
        def data(self):
            ...
        
    
    
    ALL_NETWORK = ...
    WIFI_NETWORK = ...
    DATA_NETWORK = ...
    AIRPLANE_MODE = ...
    def __init__(self, driver) -> None:
        ...
    
    @property
    def network_connection(self):
        ...
    
    def set_network_connection(self, network):
        """
        Set the network connection for the remote device.

        Example of setting airplane mode::

            driver.mobile.set_network_connection(driver.mobile.AIRPLANE_MODE)
        """
        ...
    
    @property
    def context(self):
        """
        returns the current context (Native or WebView).
        """
        ...
    
    @property
    def contexts(self):
        """
        returns a list of available contexts
        """
        ...
    
    @context.setter
    def context(self, new_context):
        """
        sets the current context
        """
        ...
    

