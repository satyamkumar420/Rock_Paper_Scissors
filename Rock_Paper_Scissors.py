import random

print("-------------------------------------------------------")
print("💖\033[01;36mWELCOME TO MY GAME ROCK, PAPER and SCISSOR 💖")
print("-------------------------------------------------------")
options = {1: "Rock 👊", 2: "Paper ✋", 3: "Scissor ✌"}
print("""\033[5;32mThe Winning Rules of this game are:
Rock 👊 vs Paper ✋ --> Paper wins ✋
Rock 👊 vs Scissor ✌ --> Rock wins 👊
Paper ✋ vs Scissors ✌ --> Scissor wins ✌\033[0m""")
print("-------------------------------------------------------")
print("***** GET READY TO PLAY *****")
print("-------------------------------------------------------")

user = 0
computer = 0
tie = 0
playAgain = "Yes"

while playAgain.lower() == "yes":
    try:
        # TODO : If type string throw fix that
        print("\033[1;35mChoose your option (1-Rock, 2-Paper, 3-Scissor)")
        user_choose = int(input("\033[01;32m => \033[0m"))

        while user_choose not in [1, 2, 3]:
            print(
                "\033[01;31mInvalid option. Please choose among 1, 2, and 3 only.❌\033[0m")
            user_choose = int(
                input("Choose your option (1-Rock, 2-Paper, 3-Scissor): "))

        print("Your choice is", options[user_choose])

        comp_choose = random.randint(1, 3)
        print("The choice of computer is", options[comp_choose])

        if user_choose == comp_choose:
            print("IT'S A DRAW/TIE 👔")
            tie += 1
        elif ((user_choose == 1 and comp_choose == 2) or (user_choose == 2 and comp_choose == 3) or (user_choose == 3 and comp_choose == 1)):
            print("Huhh 😰 The WINNER IS COMPUTER 👑")
            computer += 1
        else:
            print("CONGRATS USER 🕺, YOU WON THIS GAME 👑")
            user += 1
        print("-------------------------------------------------------")

        playAgain = input(
            "\033[01;32mDo you want to play again? (Yes/No): ")
    except ValueError:
        print("\033[01;31mInvalid input. Please enter a valid Number. ❌\033[0m")
    except KeyboardInterrupt:
        print("\n\033[01;31mThanks for using! ")
        break

print(f"\n\033[01;32mUser 🕺 score is: {user}", )
print(f"\033[01;33mComputer 💻 score is: {computer}", )
print(f"\033[01;34mTie score is : {tie}", )
if user == computer:
    print("\033[01;34mOVERALL It's a TIE ")
elif user > computer:
    print("\033[01;32OVERALL the winner is USER 🕺")
else:
    print("\033[01;33mFinally COMPUTER wins 👑")
