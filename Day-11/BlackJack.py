# Imports
import random
from art import logo



# Deal Card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)

# Calculate Scores
def calculate_score(cards):
    score = sum(cards)
    
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    if len(cards) == 2 and score == 21:
        return 0
    
    return score

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."
    elif user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

def play_game():
    print(logo)

    # Deck
    user_cards = []
    computer_cards = []

    # Game State
    game_end = False

    # Allot Cards to User and Computer
    user_cards.append(deal_card())
    user_cards.append(deal_card())

    computer_cards.append(deal_card())
    computer_cards.append(deal_card())



    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"You cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        else:
            if input("Would you like to draw another card? Type 'yes' or 'no'.\n").lower() == "yes":
                user_cards.append(deal_card())
            else:
                game_end = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n'.\n") == "y":
    play_game()







