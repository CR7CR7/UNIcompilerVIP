#program in which the computer randomly chooses a number between 1 to 10 , 1 to 100 or any range
#we have used a random module to generate random numbers that the player has to guess.
import random

number = random.randint(1, 100) # or 1 to 10 or any range 100 to 10000 
print('secret number to guess:',number)
score = 10 #number of attempts of the player 
result = 'You Lost!'   
# every time the user gueses wrong ,he gets another clue and the score gets reduced
while score > 0:
    player_input = int(input())
#The clue can be multiples, divisible, greater or smaller, or a combination of all.
    if player_input == number:
        result = 'You guessed the number!Congratulations!'
        break
    elif player_input > number:
        print(f'{player_input} is greater.\nRemaining scores: {score}.')
        score -= 1
 # the score gets reduced       

    elif player_input < number:
        print(f'{player_input} is smaller.\nRemaining scores: {score}.')
        score -= 1

   

print(result)

