# Task: Below are the steps:
# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses




import random
import math

# taking input for lower bound
lower_bound = int(input('Enter Lower Bound: '))

# taking input for upper bound
upper_bound = int(input('Enter Upper Bound: '))


# generating a random number between the lower and upper ranges
x = random.randint(lower_bound,upper_bound)
min_guesses = round(math.log(upper_bound-lower_bound+1,2))
print(f"\n You've only got {min_guesses} chances to guess the integer! \n")

# initializing number of guesses
guesses = 0

# for calculation of minimum number of guesses depends on range
while guesses < min_guesses:
    guesses+=1

    # take the number guessed as input
    new_guess = int(input('Guess a number: '))

    # conditions
    if x == new_guess:
        print(f'Congratulation! You found the number in {guesses} try')
        break
    elif new_guess<x:
        print('You guessed too small!')
    elif new_guess>x:
        print('You guessed too high!')

# if the number of guesses more than the minimum number of guesses
if guesses >= min_guesses:
    print(f'The number is {x}')
    print('Better Luck Next Time :)')
