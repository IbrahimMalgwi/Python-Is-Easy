from random import shuffle


def create_deck():
    deck = []
    face_values = ["A", "J", "Q", "K"]
    for i in range(4):
        for card in range(2, 11):
            deck.append(card)
        for card in face_values:
            deck.append(card)

    shuffle(deck)
    return deck


class Player:

    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.set_score()
        self.money = money
        self.bet = 0

    def __str__(self):
        current_hand = " "

        for card in self.hand:
            current_hand += str(card) + " "

        final_status = current_hand + "score: " + str(self.score)
        return final_status

    def set_score(self):
        self.score = 0

        face_cad_dict = {"A": 11, "J": 10, "Q": 10, "K": 10,
                         "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                         "7": 7, "8": 8, "9": 9, "10": 10, }
        ace_counter = 0
        for card in self.hand:
            self.score += face_cad_dict[card]
            if card == "A":
                ace_counter += 1
            if self.score > 21 and ace_counter != 0:
                self.score -= 10
                ace_counter -= 1
        return self.score

    def hit(self, card):
        self.hand.append(card)
        self.score = self.set_score()

    def play(self, new_hand):
        self.hand = new_hand
        self.score = self.set_score()

    def bet_money(self, amount):
        self.money -= amount
        self.bet += amount

    def win(self, result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5 * self.bet
            else:
                self.money += 2 * self.bet

            self.bet = 0
        else:
            self.bet = 0


card_deck = create_deck()
print(card_deck)
first_hand = [card_deck.pop(), card_deck.pop()]
second_hand = [card_deck.pop(), card_deck.pop]

Player1 = Player(first_hand)
House = Player(second_hand)
print(Player1)
print(House)
action = input("Do you want another card? (y/n): ")
if action == "y":
    Player1.hit()
