import random
import time
import os
from card import Card
from hand import Hand
from deck import Deck
from termcolor import colored



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Funciton to randomly select who starts first (Player Vs. AI)
def choose_first():
    if random.randint(0,1)==0:
        return 'Player'
    else:
        return 'Pc'

#Funciton to randomly select who starts first (Player Vs. Player)
def choose_first_playerVplayer():
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'


#Function to check if the card thrown by Player/AI is a valid card by comparing it with the top card
def single_card_check(top_card,card):
    if card.color==top_card.color or top_card.rank==card.rank or card.cardtype=='action_nocolor':
        return True
    else:
        return False


#FOR AI ONLY
#To check if AI has any valid card to throw 
def full_hand_check(hand,top_card):
    for c in hand.cards:
        if c.color==top_card.color or c.rank == top_card.rank or c.cardtype=='action_nocolor':
            return hand.remove_card(hand.cardsstr.index(str(c))+1)
    else:
        return 'no card'


#Function to check if either wins
def win_check(hand):
    if len(hand.cards)==0:
        return True
    else:
        print('\nThe ' + ai_name + ' pulled a card from deck')
        time.sleep(1)
        temp_card = deck.deal()
        ai_hand.add_card(temp_card)

    if win_check(ai_hand):
        win = True

    return top_card, win, skip_turn

# Game logic for player vs player option
def playerVplayer():
    while True:
        clear_screen()
        print('\nWelcome to UNO! Finish your cards first to win!')
        time.sleep(1)
        p1_name = input("\nPlayer 1, please enter your name: ")
        p2_name = input("Player 2, please enter your name: ")
        deck = Deck()
        deck.shuffle()

        player1_hand = Hand()
        for i in range(7):
            player1_hand.add_card(deck.deal())

        player2_hand = Hand()
        for i in range(7):
            player2_hand.add_card(deck.deal())

        top_card = deck.deal()
        if top_card.cardtype != 'number':
            while top_card.cardtype != 'number':
                top_card = deck.deal()
        print('\nThe starting card is: {}'.format(top_card))
        time.sleep(1)
        playing = True

        turn = choose_first_playerVplayer()
        if turn == 'Player 1':
            print('\n' + p1_name + ' will go first')
        else:
            print('\n' + p2_name + ' will go first')
        
        time.sleep(2)

        while playing:
            if turn == 'Player 1':
                top_card, win, skip_turn = player_action(p1_name, player1_hand, player2_hand, top_card, deck)
                if win:
                    print('\n' + p1_name + ' WON!!')
                    playing = False
                    break
                if skip_turn:
                    turn = 'Player 1'  # Skip the next player's turn
                else:
                    turn = 'Player 2'
            elif turn == 'Player 2':
                top_card, win, skip_turn = player_action(p2_name, player2_hand, player1_hand, top_card, deck)
                if win:
                    print('\n' + p2_name + ' WON!!')
                    playing = False
                    break
                if skip_turn:
                    turn = 'Player 2'  # Skip the next player's turn
                else:
                    turn = 'Player 1'

        new_game = input('Would you like to play again? (y/n)')
        if new_game != 'y':
            print('\nThanks for playing!')
            break

def playerVAI():
    while True:
        clear_screen()
        print('\nWelcome to UNO! Finish your cards first to win!')
        time.sleep(1)
        player_name = input("\nPlease enter your name: ")
        pc_name = "Computer"
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        for i in range(7):
            player_hand.add_card(deck.deal())

        pc_hand = Hand()
        for i in range(7):
            pc_hand.add_card(deck.deal())

        top_card = deck.deal()
        if top_card.cardtype != 'number':
            while top_card.cardtype != 'number':
                top_card = deck.deal()
        print('\nThe starting card is: {}'.format(top_card))
        time.sleep(1)
        playing = True

        turn = choose_first()
        if turn == 'Player':
            print('\n' + player_name + ' will go first')
        else:
            print('\nThe ' + pc_name + ' will go first')
        
        time.sleep(2)

        while playing:
            if turn == 'Player':
                top_card, win, skip_turn = player_action(player_name, player_hand, pc_hand, top_card, deck)
                if win:
                    print('\nYou have won!')
                    playing = False
                    break
                if skip_turn:
                    turn = 'Player'  # Skip the next player's turn
                else:
                    turn = 'Pc'
            elif turn == 'Pc':
                top_card, win, skip_turn = ai_choice(pc_name, pc_hand, player_hand, top_card, deck)
                if win:
                    print('\nThe computer has won!')
                    playing = False
                    break
                if skip_turn:
                    turn = 'Pc'  # Skip the next player's turn
                else:
                    turn = 'Player'

        new_game = input('Would you like to play again? (y/n)')
        if new_game != 'y':
            print('\nThanks for playing!')
            break


# Main menu
while True:

    print(15*"-" + " Martin's UNO Main Menu " + 15*"-" + "\n\n")
    print(" [1]. Player VS. Computer "+ "\n")
    print(" [2]. Player VS. Player "+ "\n")
    print(" [3]. Quit "+ "\n\n")
    print(54*"-")

    # Lets player(s) choose what they want to play
    option = int(input("Please select an option: "))

    if option == 1:
        playerVAI()
    
    elif option == 2:
        playerVplayer()

    elif option == 3:
        break
    
    # If invalid input is given this error message is given and player will have to input a correct choice
    else:
        print(colored("Invalid choice, please choose a valid option: ", "black", "on_red"))
        print("")
        