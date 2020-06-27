import random

#2.1
def deck():
    deck = []
    figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
        
    # c-trefl  d - Karo  h - kier  s - pik    
    colors = ['c','d','h','s']
        
    for figure in figures:
        for color in colors:
            deck.append({figure, color})

    return deck


#2.2
def shuffle_deck(deck: list):
    return random.shuffle(deck)


#2.3
def deal(deck: list, n: int):
    deals = []
    for i in range(n):
        cards = []
        for j in range(5):
            cards.append(deck.pop())
        deals.insert(i, cards)

    return deals
            

#Zad 2.1
#print(deck())


#zad 2.2
#deck = deck()
#shuffle_deck(deck)
#print(deck)


#zad 2.3
deck = deck()
shuffle_deck(deck)
game = deal(deck,4)

for i in range(len(game)):
    print("Gracz",i+1,game[i])
