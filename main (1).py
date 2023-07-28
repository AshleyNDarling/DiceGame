# Ashley Darling
# CIS 113
# 11/06/2022


# Program to display a dicegame after each roll
# storing in one of 2 dictionaries
# end program when user enters no
# finish by displaying the dictionaries


'''
Algorithm:
1) Create two dictionaries DicDie1 and DicDie2

2) inport random

3a) Ask the user if they want to play
3b) open a while loop that contiues to run until user says 'no'
4) use random to get number for die1 and die2 for numbers 1 - 6
5) disply those values
6) if die1 in dicdie1
increment value for die1
else
at end display both dictionaries


'''

# random is a python function that randomizes numbers
import random


# Dictionaries for each Dice
DicDie1 = {}
DicDie2 = {}



# input statement for whether user wants to play game or not
game = input("Do you want to play? Yes or No?  ")
#While statement that automatically capitalizes
while game.capitalize() != 'No':
  Die1 = random.randint(1,6)
 #Dice is randomized
  Die2 = random.randint(1,6)
  # Dice is randomized

  # Print sttatment output for the dice outcome
  print(f"Die 1 is {Die1}")  
  print(f"Die 2 is {Die2}")

  # Another yes or no play statement 
  game = input("Do you want to play? Yes or No?  ")

  # Die loops through if else statements to become the output for how much there is of each numer
  if Die1 in DicDie1:
    DicDie1[Die1] += 1
   
  else: 
    DicDie1[Die1] = 1

  if Die2 in DicDie2:
    DicDie2[Die2] += 1

  else:
    DicDie2[Die2] = 1

print("Dice one history is:", DicDie1)
print("Dice two history is:", DicDie2)
  





