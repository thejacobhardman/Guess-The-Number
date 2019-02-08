# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 2/6/19
# Python Version 3.7.2

# Introduction:
# Greetings! Welcome to my game 'Guess The Number' I created this game as part of my 'Intro To Programming' Course at Aims Community College.
# The goal of the game is to guess a random number before the computer does.
# The game features three distinct difficulties: on Easy, the computer will always make random guesses; on Medium, the computer will
# learn from its own guesses; and on Hard, the computer will learn from your guesses as well as its own guesses.
# Good luck!

# Importing the 'random' pkg
import random

# Generating the answer
Answer = random.randint(1,100)

# Creating str variables to store queries (This will save time typing)
Ask_Player = "Please pick a number: "
Ask_Computer = "The computer guessed: "

# Global variables
Number_Guessed = False # Tracks game state
Player_Won = False # Tracks who won the game
Min_Range = 1 # The smallest value that the computer can guess
Max_Range = 100 # The largest number that the computer can guess
Already_Guessed = [] # Stores the numbers that have already been guessed, this is only used by the Computer

########################################################### GAME LOGIC ###################################################################

def Easy_Mode(): # The computer will always guess random numbers

    # Adding the global variables to the function
    global Number_Guessed
    global Player_Won

    # Main Game Loop
    while Number_Guessed == False:
        ### Player Turn
        Player_Guess = input(Ask_Player) # The player guesses a number
        if int(Player_Guess) < Answer: # The player guessed a number higher than the answer
           print("The answer is higher than your guess.\n")
        elif int(Player_Guess) > Answer: # The player guessed a number lower than the answer
            print("The answer is lower than your guess.\n")
        else: # The player guessed the answer
            Number_Guessed = True # Breaks the loop
            Player_Won = True
            break

        ### Computer Turn (Random Guesses)
        Computer_Guess = random.randint(1,100) # The computer always makes a random guess
        if Computer_Guess < Answer:
            print(Ask_Computer + str(Computer_Guess))
            print("The answer is higher than the computer's guess.\n")
        elif Computer_Guess > Answer:
            print(Ask_Computer + str(Computer_Guess))
            print("The answer is lower than the computer's guess.\n")
        else:
            print(Ask_Computer + str(Computer_Guess))
            Number_Guessed = True
            break

def Medium_Difficulty(): # The computer will learn from its own guesses

    # Adding the global variables to the function
    global Number_Guessed
    global Player_Won
    global Min_Range
    global Max_Range
    global Already_Guessed

    # Main Game Loop
    while Number_Guessed == False:
        ### Player Turn
        Player_Guess = input(Ask_Player) # The player guesses a number
        if int(Player_Guess) < Answer: # The player guessed a number higher than the answer
            print("The answer is higher than your guess.\n")
        elif int(Player_Guess) > Answer: # The player guessed a number lower than the answer
            print("The answer is lower than your guess.\n")
        else: # The player guessed the answer
            Number_Guessed = True # Breaks the loop
            Player_Won = True
            break

        ### Computer turn (Learns from self)
        # Determining if the computer has already guessed this number
        Computer_Guess = random.randint(Min_Range, Max_Range) # The computer will narrow down the range of the answer
        if Computer_Guess in Already_Guessed:
            while Computer_Guess in Already_Guessed: # Keep guessing until the Computer's guess has not already been guessed
                Computer_Guess = random.randint(Min_Range, Max_Range)
                if Computer_Guess not in Already_Guessed: # The computer guessed a number that has not already been guessed
                    break
        
        # The Computer makes its guess
        if Computer_Guess < Answer:
            print(Ask_Computer + str(Computer_Guess))
            print("The answer is higher than the computer's guess.\n")
            Min_Range = Computer_Guess # Sets the lowest number that the computer will guess as the number that it just guessed
            Already_Guessed.append(Computer_Guess) # Adds the Computer's guess to the list of already guessed numbers
        elif Computer_Guess > Answer:
            print(Ask_Computer + str(Computer_Guess))
            print("The answer is lower than the computer's guess\n")
            Max_Range = Computer_Guess # Sets the highest number that the computer will guess as the number that it just guessed
            Already_Guessed.append(Computer_Guess) # Adds the Computer's guess to the list of already guessed numbers
        else:
            print(Ask_Computer + str(Computer_Guess))
            Number_Guessed = True
            break

def Hard_Difficulty(): # The computer will learn from its own guesses and the player's guesses

    # Adding the global variables to the function
    global Number_Guessed
    global Player_Won
    global Min_Range
    global Max_Range
    global Already_Guessed

    # Main Game Loop
    while Number_Guessed == False:
        ### Player Turn (Same as previous Player logic except the computer will now learn from the player)
        Player_Guess = input(Ask_Player)
        if int(Player_Guess) < Answer:
           print("The answer is higher than your guess.\n")
           if int(Player_Guess) > Min_Range: # This prevents the player from messing with the Computer
                Min_Range = int(Player_Guess) # The computer learns from the Player's guess
           Already_Guessed.append(int(Player_Guess)) # The Computer won't guess the same number as the player
        elif int(Player_Guess) > Answer:
            print("The answer is lower than your guess.\n")
            if int(Player_Guess) < Max_Range: # This prevents the Player from messing with the Computer
                Max_Range = int(Player_Guess) # The computer learns from the Player's guess
            Already_Guessed.append(int(Player_Guess)) # The Computer won't guess the same number as the player
        else:
            Number_Guessed = True
            Player_Won = True
            break

        ### Computer turn (Learns from self and from Player)
        # Determining if the computer has already guessed this number
        Computer_Guess = random.randint(Min_Range, Max_Range) # The computer will narrow down the range of the answer
        if Computer_Guess in Already_Guessed:
            while Computer_Guess in Already_Guessed: # Keep guessing until the Computer's guess has not already been guessed
                Computer_Guess = random.randint(Min_Range, Max_Range)
                if Computer_Guess not in Already_Guessed: # The computer guessed a number that has not already been guessed
                    break
        
        # The Computer makes its guess
        if Computer_Guess < Answer:
            print(Ask_Computer + str(Computer_Guess))
            print("The answer is higher than the computer's guess.\n")
            Min_Range = Computer_Guess # Sets the lowest number that the computer will guess as the number that it just guessed
            Already_Guessed.append(Computer_Guess) # Adds the Computer's guess to the list of already guessed numbers
        elif Computer_Guess > Answer:
            print(Ask_Computer + str(Computer_Guess))
            print("The answer is lower than the computer's guess.\n")
            Max_Range = Computer_Guess # Sets the highest number that the computer will guess as the number that it just guessed
            Already_Guessed.append(Computer_Guess) # Adds the Computer's guess to the list of already guessed numbers
        else:
            print(Ask_Computer + str(Computer_Guess))
            Number_Guessed = True
            break

############################################################ ACTUAL GAME #################################################################

# Greeting the user at the start of the game
print("Greetings! Welcome to 'Guess The Number'\nI'm thinking of a number between 1 and 100, can you guess it before the computer does?")
print("Please select a difficulty: Easy, Medium, Hard.\n")

# Asks the user to select a difficulty
Difficulty_Level = input("Enter '1' for Easy Mode, '2' for Medium difficulty or '3' for Hard difficulty.\n")

# Selects the difficulty for the game based on the user input
if int(Difficulty_Level) == 1:
    Easy_Mode()
elif int(Difficulty_Level) == 2:
    Medium_Difficulty()
elif int(Difficulty_Level) == 3:
    Hard_Difficulty()
      
# Prints the correct win statement
if Player_Won == True:
    print("\nYou win!!!\n")
elif Player_Won == False:
    print("\nThe computer won!!!\n")

input("Please press 'enter' to end the program.\n")