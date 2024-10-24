import random
number = random.randint(1,100)
guess = 0
while number != guess:
    guess = int(input("Guess my random number. "))
    if number!= guess:
        print("Thats incorrect ")
    else:
        print("Your guess is correct. ")
        break


