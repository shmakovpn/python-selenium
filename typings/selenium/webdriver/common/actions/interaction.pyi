"""
This type stub file was generated by pyright.
"""

KEY = "key"
POINTER = "pointer"
NONE = "none"
SOURCE_TYPES = set([KEY, POINTER, NONE])
POINTER_MOUSE = "mouse"
POINTER_TOUCH = "touch"
POINTER_PEN = "pen"
POINTER_KINDS = set([POINTER_MOUSE, POINTER_TOUCH, POINTER_PEN])
class Interaction(object):
    PAUSE = ...
    def __init__(self, source) -> None:
        ...
    


class Pause(Interaction):
    def __init__(self, source, duration=...) -> None:
        ...
    
    def encode(self):
        ...
    


