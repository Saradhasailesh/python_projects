import random

#randomly select a number from 1 and 20.

num = random.randint(1,20)

print("Guess a number between 1 and 20:\n")

chances = 0

while(chances<5):
    try:
        guess = int(input())

        if guess==num:
            print("Congratulations you won!!!")
            break
        elif guess>num:
            print("Your guess is greater than the actual number. Kindly select a smaller number than", guess)
        else:
            print("Your guess is smaller than the actual number. Kindly select a greater number than", guess)

        chances+=1 

    except ValueError:
        print("Invalid input. Please enter a valid integer")

if not chances<5:

    print("Sorry,You Lose!!! The number is",num)



