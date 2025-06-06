from game_data import data as db
import random

def format_data(account):
    account_name = db.account["name"]
    account_descr = db.account["description"]
    account_country = db.account["country"]
    return(f"{account_name}, a{account_descr}, from{account_country}")

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
score = 0
game_should_continue = True
account_b = random.choice(db)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(db)
    if account_a == account_b:
        account_b = random.choice(db)

    print(f"Compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")

    Guess = input("Who has more followers? 'A' or 'B': ").lower()
    print("\n" * 20)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(Guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right!. Current score is {score}")
    else:
        print("Sorry, that's wrong. Final score is {score}")
        game_should_continue = False


