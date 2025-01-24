import random
class Card:
    def __init__(self, colour, symbol, shading, number):
        self.colour = colour #colour on card (green, purple, red)
        self.symbol = symbol #symbol on card (diamond, oval, squiggle)
        self.shading = shading #shading on card (empty, filled, shaded)
        self.number = number #number on card (1, 2, 3)
        
    def __str__(self):
        #make string
        return f"{self.colour}{self.symbol}{self.shading}{self.number}"
    #check if 3 cards make a set
    def check_set(nest_list):
        for i in range(0, 3):
            for j in range(0, 4):
                if nest_list[i][0][j] == nest_list[(i+1)%3][0][j] and nest_list[i][0][j] != nest_list[i-1][0][j]:
                    return False
                    break
        return True
    #output 3 cards that make a set from 12 cards
    def pick_set(open_cards):
        n = len(open_cards)
        for i in range(0, n-2):
            for j in range(1, n-1):
                for k in range(2, n):
                    if i != j != k and Card.check_set([open_cards[i], open_cards[j], open_cards[k]]) == True:
                        return [open_cards[i], open_cards[j], open_cards[k]]
                        break
        return False
    #pick random card and remove from necessary lists
    def random(nest_list_number, nest_list_word):
        n = len(nest_list_word)-1
        index = random.randint(0, n)
        word_card = nest_list_word[index]
        number_card = nest_list_number[index]
        nest_list_word.remove(word_card)
        nest_list_number.remove(number_card)
        return [number_card, word_card]
