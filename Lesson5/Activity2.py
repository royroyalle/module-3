import random
while True:
    ua = input("Rock Paper Scissor Shoot!")
    possible = ["rock", "paper", "scissor"]
    comp = random.choice(possible)
    print("You chose", ua, "and computer chose", comp,)

    if ua == comp:
        print("It's A Tie!")
    elif ua == "scissor" and comp == "paper":
        print("User won!")
    elif ua == "paper" and comp == "rock":
        print("User won!")
    elif ua == "rock" and comp == "scissor":
        print("User Won!")
    elif ua == "rock" and comp == "paper":
        print("Computer Won!")
    elif ua == "paper" and comp == "scissor":
        print("Computer Won!")
    elif ua == "scissor" and comp == "rock":
        print("Computer Won!")
    play_again = input("Want to play again?")
    if play_again != "Yes":
        break