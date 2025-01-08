from random import randint
class Card:

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        return str(self.number) + " of " + self.suit


class Deck:

    def __init__(self):
        self.cards = []
        for s in ["spades", "diamonds", "hearts", "clubs"]:
            for n in range(1, 14):
                self.cards.append( Card(s, n) )

    def deal(self):

        hand = []
        # draw 5 random cards from the deck, removing them so we don't get repeats
        for i in range(5):
            card = self.cards.pop( randint(0, len(self.cards)-1) )

            hand.append(card)

        # we just took these 5 cards out of the deck - we need to re-add them
        # or else our deck only holds 47 cards
        for c in hand:
            self.cards.append(c)

        return hand

    def shuffle(self):
        # do 100 random draws and add them to the end of the deck
        for i in range(100):
            card1 = self.cards.pop(randint(0,len(self.cards)-1))
            self.cards.append(card1)

    # generate an output to visualize the deck when printed
    def __str__(self):
        output = ""
        for c in self.cards:
            output += str(c) + "\n"
        return output


deck = Deck()
deck.shuffle()
print(deck)




