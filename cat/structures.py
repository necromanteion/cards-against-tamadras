import textwrap


class Deck(object):
    """
    Container class for a deck of black and white cards.
    
    Attributes:
        black: A set of black cards that have not been played.
        current: A single black card that is currently in play and is awaiting a ruling decision from the Czar.
        discarded: A set of white cards that have already been played.
        in_play: A set of white cards that are currently in play.
        white: A set of white cards that have not been drawn or played.
        won: A set of black cards that have recieved a ruling decision from the Czar and are no longer in play.
        _black: A private copy of potential black cards, used for a new game.
        _white: A private copy of potential white cards, used for a new game.
    """
    
    
    __slots__ = ('_black', '_white', 'black', 'current', 'discarded', 'in_play', 'white', 'won')
    
    
    def __init__(self, black, white):
        """
        Initializes a new game deck.
        
        Args:
            black: An iterable of black cards -- open-ended questions or fill-in-the-blank cards.
            white: An iterable of white cards -- answers or values for black cards.
        """
        
        self._black = set(black)
        self._white = set(white)
        
        self.reshuffle()
    
    
    def discard(self, *cards):
        """
        Remove white cards from play.
        
        Args:
            *cards: An iterable of white cards to remove from play.
            
        Raises:
            KeyError: If white card is not found in play.
        """
        
        for card in cards:
            
            try:
                self.in_play.remove(card)
                
            except KeyError:
                raise KeyError('{!r} not found in play'.format(card))
        
            else:
                self.discarded.add(card)
        
        
    def draw(self, n=1):
        """
        Draw white cards from the deck.
        
        Args:
            n: A positive integer number of cards.
        
        Returns:
            A set of len `n` containing the drawn cards.
        """
        
        drawn = {self.white.pop() for i in range(n)}
        
        self.in_play.update(drawn)
        
        return drawn
    
    
    def new(self):
        """
        Draws a new black card into play.
        
        Returns:
            The black card that has been put into play.
        """
        
        if self.current:
            self.won.add(self.current)
            
        self.current = self.black.pop()
        
        return self.current
    
    
    def reshuffle(self):
        """
        Begins a new game using the same sets of black and white cards.
        """        
        
        self.black = self._black.copy()
        self.white = self._white.copy()
        
        self.current = None
        self.discarded = set()
        self.in_play = set()
        self.won = set()
        
        
    def __bool__(self):
        return bool(self.black or (self.current and self.in_play))
    
    
    def __iter__(self):
        """
        Delegates iteration over the deck to the __next__ method.
        """
        return next(self)
    
    
    def __next__(self):
        """
        Iterates over the black cards in the deck, setting a new current card each time.
        """
        
        while self.black:
            yield self.new()
        
        raise StopIteration
    
    
    def __repr__(self):
        black = textwrap.shorten(repr(self.black), width=60, placeholder='[...] }')
        white = textwrap.shorten(repr(self.white), width=60, placeholder='[...] }')
        
        return '{}(black={}, white={})'.format(self.__class__.__name__, black, white)