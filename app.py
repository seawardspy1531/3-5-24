import colors
import random

class card():
    def __init__(self, _cls, _ty, _val):
        self.cls = _cls
        self.ty  = _ty
        self.val = _val

    def __repr__(self) -> str:
        return f"card({self.cls}, {self.ty}, {self.val})"

#one deck of cards
Deck = [
    card("Clubs", "Num", 1), card("Clubs", "Num", 2), card("Clubs", "Num", 3), 
    card("Clubs", "Num", 4), card("Clubs", "Num", 5), card("Clubs", "Num", 6), 
    card("Clubs", "Num", 7), card("Clubs", "Num", 8), card("Clubs", "Num", 9), 
    card("Clubs", "Jack", 10), card("Clubs", "King", 10), card("Clubs", "Queen", 10),
    card("Clubs", "Ace", 0),
    card("Hearts", "Num", 1), card("Hearts", "Num", 2), card("Hearts", "Num", 3), 
    card("Hearts", "Num", 4), card("Hearts", "Num", 5), card("Hearts", "Num", 6), 
    card("Hearts", "Num", 7), card("Hearts", "Num", 8), card("Hearts", "Num", 9), 
    card("Hearts", "Jack", 10), card("Hearts", "King", 10), card("Hearts", "Queen", 10),
    card("Hearts", "Ace", 0),
    card("Spades", "Num", 1), card("Spades", "Num", 2), card("Spades", "Num", 3), 
    card("Spades", "Num", 4), card("Spades", "Num", 5), card("Spades", "Num", 6), 
    card("Spades", "Num", 7), card("Spades", "Num", 8), card("Spades", "Num", 9), 
    card("Spades", "Jack", 10), card("Spades", "King", 10), card("Spades", "Queen", 10),
    card("Spades", "Ace", 0),
    card("Diamonds", "Num", 1), card("Diamonds", "Num", 2), card("Diamonds", "Num", 3), 
    card("Diamonds", "Num", 4), card("Diamonds", "Num", 5), card("Diamonds", "Num", 6), 
    card("Diamonds", "Num", 7), card("Diamonds", "Num", 8), card("Diamonds", "Num", 9), 
    card("Diamonds", "Jack", 10), card("Diamonds", "King", 10), card("Diamonds", "Queen", 10),
    card("Diamonds", "Ace", 0)
]

class BlackJack():
    def __init__(self, decks: int = 1):
        self.Decks = self.FillDeck(decks)
        self.run = True
        self.house = []
        self.player = []

    def FillDeck(self, decks):
        deck = []
        for i in range(0, decks):
            for card in Deck:
                deck.append(card)
        return deck
    
    def DealCard(self):
        '''
            return a new card with the same properties as the once chosen.
            delete the chosen one.
        '''
        #random.shuffle(self.Decks)
        cIndex = random.randint(0, len(self.Decks))
        choice = self.Decks[cIndex]
        cd = card(choice.cls, choice.ty, choice.val)
        self.Decks.pop(cIndex)
        return cd
    
    def Start(self):
        while self.run:
            print("\t------")
            self.house.append(self.DealCard())
            self.house.append(self.DealCard())
            self.player.append(self.DealCard())
            self.player.append(self.DealCard())

            self.PrintCards()

            cont = input("How do you stand?: ")

    def PrintCards():
        print("")

