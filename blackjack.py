import os
from card import Card
from deck import Deck


def clear_terminal():
    ''' Clears the terminal based on the operating system if the TERM environment variable is set. '''
    if os.getenv('TERM'):
        command = 'cls' if os.name in ('nt', 'dos') else 'clear'
        os.system(command)

def play_blackjack():

    clear_terminal()

    player_cards =[]
    dealer_cards = []

    player_score = 0
    dealer_score = 0

    deck = Deck()
    deck.generate()
    deck.shuffle()

    scores = [score for score in range(2, 22)]
    scores.append("Blackjack")
    scores += [score for score in range(22, 31)]
 
    player_cards += deck.draw(2)
    dealer_cards += deck.draw(2)

# PLAYER
    for card in player_cards:
        player_score += card.card_value

    if player_score > 21:
        player_cards[0].card_value = 1
        player_score -= 10

    if player_score == 21:
        player_score = "Blackjack"

    #Show player's cards and score
    print("Player's Cards:")
    card.show(player_cards, False)
    print("Player's Score: {0}".format(player_score))

    input()

    #Show dealer's cards and score
    print("\nDealer's Cards:")
    card.show(dealer_cards[:1], True)
    print("Dealer's Score: {0}".format(dealer_cards[0].card_value))
    
    while scores.index(player_score) < 19:
        while True:
            player_choice = input("Stand or Hit? ")
                
            if player_choice.lower() in ["stand", "hit"]:
                break
            else:
                print("Invalid Choice, try again typing either stand or hit.")
                    
        if  player_choice.lower() == "stand":
            print("Player Stands on {0}".format(player_score))
            break    
        else:
            player_cards += deck.draw(1)
            player_score += player_cards[-1].card_value

            while player_score > 21:
                for card in player_cards:
                    if card.card_value == 11:
                        card.card_value = 1
                        player_score -= 10
                        break
                break
            
            clear_terminal()
            print("Player's Cards")
            card.show(player_cards, False)
            print("Player's Score: {0}".format(player_score))

    if scores.index(player_score) > 20:
        print("Player Busted! Dealer Wins")
        quit()

# DEALER
    for card in dealer_cards:   
        dealer_score += card.card_value
        
    if dealer_score > 21:
        dealer_cards[0].card_value = 1
        dealer_score -= 10

    if dealer_score == 21:
        dealer_score = "Blackjack"   
   
    clear_terminal()
    print("\nDealer's Cards:")
    card.show(dealer_cards[:1], True)
    print("Dealer's Score: {0}".format(dealer_cards[0].card_value))

    input()
    clear_terminal()
    #Show dealer's cards and score
    print("\nDealer's Cards:")
    card.show(dealer_cards, False)
    print("Dealer's Score: {0}".format(dealer_score))
          
    while scores.index(dealer_score) < 15 or scores.index(dealer_score) < scores.index(player_score):
        dealer_cards += deck.draw(1)
        dealer_score += dealer_cards[-1].card_value

        while dealer_score > 21:
            for card in dealer_cards:
                if card.card_value == 11:
                    card.card_value = 1
                    dealer_score -= 10
                    break
            break

        input()
        clear_terminal()
        #Show dealer's cards and score
        print("\nDealer's Cards:")
        card.show(dealer_cards, False)
        print("Dealer's Score: {0}".format(dealer_score))

    if scores.index(dealer_score) > 20:
        print("Dealer Busted! Player Wins")
        quit()      

    # Calculating Player Score
    final_player_score = scores.index(player_score)

    # Calculating Dealer Score
    final_dealer_score = scores.index(dealer_score)

    if final_player_score > final_dealer_score:
        print("\nPlayer has {0}, Dealer has {1}, Player Wins".format(player_score, dealer_score))
    elif final_player_score == final_dealer_score:
        print("\nPlayer and dealer both have {0}. Tie Game!".format(player_score))
    else:
        print("\nPlayer has {0}, Dealer has {1}, Player Loses".format(player_score, dealer_score))

play_blackjack()