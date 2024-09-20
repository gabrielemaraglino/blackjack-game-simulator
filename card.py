class Card:
    def __init__(self, value, suit):
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][value -1]
        self.card_value = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}[self.value]
        self.suit = ["♥", "♦", "♣", "♠"][suit]

    def show(self, deck, face_down):
        c = ""
        for card in deck:
            c += "\t┌──────────┐"
        if face_down:
            c += f"\t┌──────────┐"
        print(c)

        c = ""
        for card in deck:
            if card.value == "10":
                c += f"\t| {card.value}       |"
            else:
                c += f"\t| {card.value}        |"
        if face_down:
            c += f"\t|          |"
        print(c)

        c = ""
        for card in deck:
            c += "\t|          |"
        if face_down:
            c += f"\t|          |"
        print(c)

        c = ""
        for card in deck:
            c += "\t|          |"
        if face_down:
            c += f"\t|          |"
        print(c)

        c = ""
        for card in deck:
            c += f"\t|    {card.suit}     |"
        if face_down:
            c += f"\t|          |"
        print(c)

        c = ""
        for card in deck:
            c += "\t|          |"
        if face_down:
            c += f"\t|          |"
        print(c)


        c = ""
        for card in deck:
            c += "\t|          |"
        if face_down:
            c += f"\t|          |"
        print(c)

        c = ""
        for card in deck:
            if card.value == "10":
                c += f"\t|       {card.value} |"
            else:
                c += f"\t|        {card.value} |"
        if face_down:
            c += f"\t|          |"
        print(c)

        c = ""
        for card in deck:
            c += "\t└──────────┘"
        if face_down:
            c += "\t└──────────┘"
        print(c)

