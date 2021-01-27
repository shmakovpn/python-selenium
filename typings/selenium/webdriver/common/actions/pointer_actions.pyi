"""
This type stub file was generated by pyright.
"""

from .interaction import Interaction

class PointerActions(Interaction):
    def __init__(self, source=...) -> None:
        ...
    
    def pointer_down(self, button=...):
        ...
    
    def pointer_up(self, button=...):
        ...
    
    def move_to(self, element, x=..., y=...):
        ...
    
    def move_by(self, x, y):
        ...
    
    def move_to_location(self, x, y):
        ...
    
    def click(self, element=...):
        ...
    
    def context_click(self, element=...):
        ...
    
    def click_and_hold(self, element=...):
        ...
    
    def release(self):
        ...
    
    def double_click(self, element=...):
        ...
    
    def pause(self, duration=...):
        ...
    


