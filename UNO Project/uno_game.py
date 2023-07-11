import random
import time
from card import Card
from deck import Deck
from hand import Hand
from termcolor import colored   

#Funciton to randomly select who starts first
def choose_first():
    if random.randint(0,1)==0:
        return 'Player'
    else:
        return 'Pc'


#Function to check if the card thrown by Player/PC is a valid card by comparing it with the top card
def single_card_check(top_card,card):
    if card.color==top_card.color or top_card.rank==card.rank or card.cardtype=='action_nocolor':
        return True
    else:
        return False


#FOR PC ONLY
#To check if PC has any valid card to throw 
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
        return False

#The gaming loop
def playerVAI():
    while True:

        print('\nWelcome to UNO! Finish your cards first to win')
        time.sleep(1)

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
        print('\nStarting Card is: {}'.format(top_card))
        time.sleep(1)
        playing = True

        turn = choose_first()
        print(turn + ' will go first')

        while playing:

            if turn == 'Player':
                print('\nTop card is: ' + str(top_card))
                print('\nYour cards: ')
                player_hand.cards_in_hand()
                choice = input("\nHit or Pull? (h/p): ")
                if choice == 'h':
                    pos = int(input('Enter index of card: '))
                    temp_card = player_hand.single_card(pos)
                    if single_card_check(top_card, temp_card) == True:
                        if temp_card.cardtype == 'number':
                            top_card = player_hand.remove_card(pos)
                            turn = 'Pc'
                        else:
                            if temp_card.rank == 'Skip' or temp_card.rank == 'Reverse':
                                turn = 'Player'
                                top_card = player_hand.remove_card(pos)
                            elif temp_card.rank == 'Draw2':
                                for i in range(2):
                                    pc_hand.add_card(deck.deal())
                                top_card = player_hand.remove_card(pos)
                                turn = 'Player'
                            elif temp_card.rank == 'Draw4':
                                for i in range(4):
                                    pc_hand.add_card(deck.deal())
                                top_card = player_hand.remove_card(pos)
                                draw4color = input('Change color to (enter in caps): ')
                                if draw4color != draw4color.upper():
                                    draw4color = draw4color.upper()
                                top_card.color = draw4color
                                turn = 'Player'
                            elif temp_card.rank == 'Wild':
                                top_card = player_hand.remove_card(pos)
                                wildcolor = input('Change color to (enter in caps): ')
                                if wildcolor != wildcolor.upper():
                                    wildcolor = wildcolor.upper()
                                top_card.color = wildcolor
                                turn = 'Pc'
                    else:
                        print('This card cannot be used')

                elif choice == 'p':
                    temp_card = deck.deal()
                    print('You got: ' + str(temp_card))
                    time.sleep(1)
                    if single_card_check(top_card, temp_card):
                        player_hand.add_card(temp_card)
                    else:
                        print('Cannot use this card')
                        player_hand.add_card(temp_card)
                        turn = 'Pc'
                if win_check(player_hand) == True:
                    print('\nPLAYER WON!!')
                    playing = False
                    break

            if turn == 'Pc':
                temp_card = full_hand_check(pc_hand, top_card)
                time.sleep(1)
                if temp_card != 'no card':
                    print(f'\nPC throws: {temp_card}')
                    time.sleep(1)
                    if temp_card.cardtype == 'number':
                        top_card = temp_card
                        turn = 'Player'
                    else:
                        if temp_card.rank == 'Skip' or temp_card.rank == 'Reverse':
                            turn = 'Pc'
                            top_card = temp_card
                        elif temp_card.rank == 'Draw2':
                            for i in range(2):
                                player_hand.add_card(deck.deal())
                            top_card = temp_card
                            turn = 'Pc'
                        elif temp_card.rank == 'Draw4':
                            for i in range(4):
                                player_hand.add_card(deck.deal())
                            top_card = temp_card
                            draw4color = pc_hand.cards[0].color
                            print('Color changes to', draw4color)
                            top_card.color = draw4color
                            turn = 'Pc'
                        elif temp_card.rank == 'Wild':
                            top_card = temp_card
                            wildcolor = pc_hand.cards[0].color
                            print("Color changes to", wildcolor)
                            top_card.color = wildcolor
                            turn = 'Player'
                else:
                    print('\nPC pulls a card from deck')
                    time.sleep(1)
                    temp_card = deck.deal()
                    if single_card_check(top_card, temp_card):
                        print(f'PC throws: {temp_card}')
                        time.sleep(1)
                        if temp_card.cardtype == 'number':
                            top_card = temp_card
                            turn = 'Player'
                        else:
                            if temp_card.rank == 'Skip' or temp_card.rank == 'Reverse':
                                turn = 'Pc'
                                top_card = temp_card
                            elif temp_card.rank == 'Draw2':
                                for i in range(2):
                                    player_hand.add_card(deck.deal())
                                top_card = temp_card
                                turn = 'Pc'
                            elif temp_card.rank == 'Draw4':
                                for i in range(4):
                                    player_hand.add_card(deck.deal())
                                top_card = temp_card
                                draw4color = pc_hand.cards[0].color
                                print('Color changes to', draw4color)
                                top_card.color = draw4color
                                turn = 'Pc'
                            elif temp_card.rank == 'Wild':
                                top_card = temp_card
                                wildcolor = pc_hand.cards[0].color
                                print('Color changes to', wildcolor)
                                top_card.color = wildcolor
                                turn = 'Player'
                    else:
                        print('PC doesnt have a card')
                        time.sleep(1)
                        pc_hand.add_card(temp_card)
                        turn = 'Player'
                print('\nPC has {} cards remaining'.format(pc_hand.no_of_cards()))
                time.sleep(1)
                if win_check(pc_hand) == True:
                    print('\nPC WON!!')
                    playing = False

        new_game = input('Would you like to play again? (y/n)')
        if new_game == 'y':
            continue
        else:
            print('\nThanks for playing!!')
            break

while True:
    print("Main Menu")
    print("1. Player VS. Computer")
    print("2. Player VS. Player")
    print("3. Quit")

    option = int(input("Please select an option: "))

    if option == 1:
        playerVAI()

    elif option == 2:
        playerVplayer()

    elif option == 3:
        break

    else:
        print(colored("Invalid choice, please choose a valid option", "black", "on_red"))
        print("")