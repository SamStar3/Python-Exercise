print("Demo")

secret_number = 9
i = 3
# count = 0
# limit = 3

while i > 0:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("you win")
        break
    else:
        print("try again")
