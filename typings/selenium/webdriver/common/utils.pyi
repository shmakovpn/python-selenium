"""
This type stub file was generated by pyright.
"""

"""
The Utils methods.
"""
def free_port():
    """
    Determines a free port using sockets.
    """
    ...

def find_connectable_ip(host, port=...):
    """Resolve a hostname to an IP, preferring IPv4 addresses.

    We prefer IPv4 so that we don't change behavior from previous IPv4-only
    implementations, and because some drivers (e.g., FirefoxDriver) do not
    support IPv6 connections.

    If the optional port number is provided, only IPs that listen on the given
    port are considered.

    :Args:
        - host - A hostname.
        - port - Optional port number.

    :Returns:
        A single IP address, as a string. If any IPv4 address is found, one is
        returned. Otherwise, if any IPv6 address is found, one is returned. If
        neither, then None is returned.

    """
    ...

def join_host_port(host, port):
    """Joins a hostname and port together.

    This is a minimal implementation intended to cope with IPv6 literals. For
    example, _join_host_port('::1', 80) == '[::1]:80'.

    :Args:
        - host - A hostname.
        - port - An integer port.

    """
    ...

def is_connectable(port, host=...):
    """
    Tries to connect to the server at port to see if it is running.

    :Args:
     - port - The port to connect.
    """
    ...

def is_url_connectable(port):
    """
    Tries to connect to the HTTP server at /status path
    and specified port to see if it responds successfully.

    :Args:
     - port - The port to connect.
    """
    ...

def keys_to_typing(value):
    """Processes the values that will be typed in the element."""
    ...

