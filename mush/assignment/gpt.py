import random


class Deck:
    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.suits = ['C', 'D', 'H', 'S']
        self.deck = [(card, suit)
                     for card in self.cards for suit in self.suits]
        self.dealt_cards = []

    def deal(self):
        if len(self.deck) > 0:
            card = self.deck.pop(0)
            self.dealt_cards.append(card)
            return card
        else:
            return None

    def shuffle(self):
        self.deck = self.dealt_cards
        self.dealt_cards = []
        random.shuffle(self.deck)

    def fan(self):
        return self.deck

    def is_ordered(self):
        for i in range(len(self.deck) - 1):
            if self.deck[i][0] > self.deck[i + 1][0]:
                return False
            elif self.deck[i][0] == self.deck[i + 1][0]:
                if self.suits.index(self.deck[i][1]) > self.suits.index(self.deck[i + 1][1]):
                    return False
        return True

    def order(self):
        self.deck.sort(key=lambda x: (
            self.cards.index(x[0]), self.suits.index(x[1])))


deck = Deck()
STAKE = 100

print('Welcome to Acey Duecy!')
print(f'Player Starting stake is ${STAKE}')
while True:
    print('Player current stake is ${}, and the minimum bet is $5.'.format(STAKE))

    bet = int(input('Enter your bet: '))

    if bet < 5:
        print('Minimum bet is $5.')

        continue
    elif bet > STAKE:
        print('You don\'t have enough money.')
        continue

    STAKE -= bet

    card1 = deck.deal()
    card2 = deck.deal()

    print('Your first two cards are:', card1, card2)

    choice = input(
        'Enter "h" to bet that the next card will be higher, or "l" to bet that it will be lower: ')

    card3 = deck.deal()

    print('The third card is:', card3)

    if choice == 'h':
        if card3[0] > card2[0]:
            print('Congratulations, you win!')
            STAKE += 2 * bet
        else:
            print('Sorry, you lose.')
    elif choice == 'l':
        if card3[0] < card2[0]:
            print('Congratulations, you win!')
            STAKE += 2 * bet
        else:
            print('Sorry, you lose.')
    else:
        print('Invalid choice.')

    if STAKE == 0:
        print('You are out of money')
        break
