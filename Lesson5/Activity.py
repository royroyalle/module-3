import random
playing = True
num = random.randint(1,4)
print("Generating numbers from 0 to 9 and you have to guess")
print("Game ends when you get 1")
while playing:
    guess=int(input("Enter your guess"))
    print(num)
    if num == guess:
        print("You got it!")
        break
    else:
        print("Try again")