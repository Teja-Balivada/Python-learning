import random
import math

#Input lower bound and upper bound
lower_bound, upper_bound = map(int, input("Enter both lower and Upper limits: ").split())
winning_number = random.randint(lower_bound, upper_bound)   #geeting the random winnin number
chances = round(math.log2(upper_bound - lower_bound +1))    # generating minimum chances to guess

count = 0 
#conditions for the game
while count < chances:
    count+=1
    guess = int(input("Enter the Guess Number: "))
    if guess == winning_number: 
        print(f'Congratulations you have own on {count} try!!')
        break
    elif guess > winning_number: print("Guess number is too High!")        
    elif guess < winning_number: print("Guess number is too Low!")

#failure case
if count >= chances: print(f'The winning number is {winning_number}\t\n Better luck Next time..!')