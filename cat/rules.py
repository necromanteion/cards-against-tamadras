"""
cat.rules

This submodule contains subclasses of cat.structures.Rules -- implementations of various rules of play for the game.
"""

import abc

# from .structures import Rules


class Rules(metaclass=abc.ABCMeta):
    
    
    @abc.abstractmethod
    def __init__(self):
        pass
    
    
    @abc.abstractmethod
    def new_czar(self, players):
        """Called at the beginning of a round to pick a new Card Czar."""
        pass
    
    