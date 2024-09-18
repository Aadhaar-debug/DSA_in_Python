import random

class Game:
    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['♣', '♦', '♥', '♠']
        self.pot = 0
        self.cards_on_table = []

    def create_deck(self):
        return [f"{rank} {suit}" for rank in self.ranks for suit in self.suits]

class Dealer(Game):
    def __init__(self):
        super().__init__()
        self.deck = self.create_deck()
        random.shuffle(self.deck)
        self.cards = [self.deck.pop(), self.deck.pop()]
    
    def buy_in(self):
        buyin = int(input("How Much do you want to buy in ? : "))

    def next_hand(self):
        if self.deck:
            self.cards_on_table.append(self.deck.pop())
        else:
            print("No more cards in the deck.")

    def cards_on_deck(self):
        print("Cards on the table:", ', '.join(self.cards_on_table))


class Player(Dealer , Game):
    Account = 0
    Buyin_Amount = 0

# Example usage
D = Dealer()
D.create_deck()
D.next_hand()
D.next_hand()
D.cards_on_deck()
