from src.deck import Deck
from src.card import Card, SUITS, RANKS

class Player:

    #Instance methods===========================================================================

    #Constructor
    def __init__(self, name):
        self.name=name
        self.hand=[]

    #Deal card from source deck to player; deck is passed so that the card can be removed from it
    def deal(self, deck, card):
        self.hand.append(card)
        deck.cards.remove(card)
        self.hand=Deck.sort(self.hand)


    def __str__(self):
        string=self.name+" ["
        for card in self.hand:
            string+=str(card)+", "
        string+="]"
        return string