from random import choice
from logo import logo


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def calculate_score(cards):
    sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        print("You went over, you lose.")
    if user_score == computer_score:
        print("It's a draw")
    elif user_score == 0:
        print("You got a blackjack, you win.")
    elif computer_score == 0:
        print("Your opponent has a blackjack, you lose.")
    elif computer_score > 21:
        print("Opponent went over, you win.")
    elif user_score > 21:
        print("You went over, you lose.")
    elif computer_score > user_score:
        print("Opponent has a higher score, you lose.")
    else:
        print("You have a higher score, you win.")


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    is_game_over = False
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    while not is_game_over:
        print(f"Your card: {user_cards}, total score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_user_deal = input("Type 'y' to deal another card, or 'n' to pass: ")
            if should_user_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand {user_cards}, final score: {user_score}")
    print(f"Opponent's final hand {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    play_game()







