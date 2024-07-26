import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You lost. Computer has Blackjack."
    elif user_score == 0:
        return "You have Blackjack! You won."
    elif user_score > 21:
        return "You went over 21. You lost."
    elif computer_score > 21:
        return "Computer went over 21. You won."
    elif user_score > computer_score:
        return "You won."
    else:
        return "You lost. Computer has a higher score."

def play_game():
    print(logo)
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    game_ends = False

    while not game_ends:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_ends = True
        else:
            user_should_deal = input("Type 'y' to draw another card, 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_ends = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower() == 'yes':
    play_game()
