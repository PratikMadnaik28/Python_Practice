import random
User_choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper and 2 for Scissor."))
if User_choice >= 0 and User_choice <= 2:
    print(User_choice)
Computer_choice = random.randint(0, 2)
print("Computer_choice")

if User_choice >= 3 and User_choice < 0:
    print("You typed wrong number!")
elif User_choice == 0 and Computer_choice == 2:
    print("You win!")
elif Computer_choice == 0 and User_choice == 2:
    print("You lose!")
elif Computer_choice > User_choice:
    print("You lose!")
elif User_choice > Computer_choice:
    print("You win!")
elif User_choice == Computer_choice:
    print("It's a Draw!")
