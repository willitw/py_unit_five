# Twig Williams
# 11/8/23
# plays a guessing game wither user 3 times then averages the number of tries

import random


def get_number():
    '''
    Generate a random number between 1 and 100 (inclusive).
    :return:
    '''
    return random.randint(1, 100)


def get_guess():
    '''
    Get a valid guess from the player between 1 and 100.
    :return:
    '''
    while True:
        try:

            guess = int(input("Guess my number its between 1 and 100: "))    # Get the player's guess as an integer
            if 1 <= guess <= 100:
                return guess                                                 # If the guess is within the valid range, return it
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    '''
    Play a single game of number guessing.
    :return:
    '''

    number_to_guess = get_number()      # Generate the number to be guessed
    tries = 0
    while True:
        player_guess = get_guess()
        tries += 1

        if player_guess < number_to_guess:
            print("TOO LOW, your so bad at this!🤣🤣🤣 try again")                               # Player guessed too low, provides feedback
        elif player_guess > number_to_guess:
            print("TOO HIGH, you might be the worst guesser!😂😂😂 try again")                   # Player guessed too high, provides feedback
        else:
            print("😱😨😦🤯HOWWWW DID YOU GUESS MY NUMBER IN " + str(tries) + " TRIES?!?!?!.")   # Player guessed correctly, provides feedback
            return tries

def main():
    '''
    Main function to play multiple games and calculate the average.
    :return:
    '''
    total_attempts = 0
    num_games = 3
    print("Welcome to my guessing game, guess my number 3 times and i will tell you how many times on average it takes you , good luck")    # Welcomes user to the game and explains the game
    for game in range(num_games):                   # Loop for playing the game
        print("Game " + str(game + 1))              # Start a new game and display the game number
        attempts = play_game()                      # Start a new game and record the number of attempts it takes to guess the correct number
        total_attempts += attempts                  # Add the number of attempts from the current game to the total attempts for all the games
    average_attempts = total_attempts / num_games   # Takes the total attemps and divides it over the number of games to get the average number of tries








    print("    ⠀⠀⠀⠀⠀⠀⣴⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⣿⣿⠏⣡⣴⣷⡄⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣤⣿⣿⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⢛⠟⣰⣿⣿⣿⣾⡀⡀⠀⠀⣠⣾⣿⣿⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⢉⣵⣿⣿⣿⣷⠀⢸⣿⣿⢿⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣠⡀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⢿⣷⣆⠀⠀⠀⣼⠟⣛⠛⠿⢿⣇⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣶⣿⣿⣾⠝⣋⣴⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣶⣦⣌⣱⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣬⣿⣷⡀⠀⣰⣿⣾⣿⣿⣷⡶⠏⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡏⣽⣿⣿⣿⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣶⡶⠟⠛⠛⠻⣿⣶⣶⣮⣉⣉⡛⠻⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠈⣛⣿⣿⣀⣰⣿⣿⣌⠻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣤⣿⣿⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⡿⢋⣥⣶⡿⢻⣿⣿⣿⣷⣿⣿⣿⣎⡛⠷⣦⡉⢻⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⣶⣿⣿⡿⣿⣿⣿⣿⣼⣷⣿⣭⡅⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣭⣿⣿⡙⢿⣧⡙⢿⣿⡇⠀⠀⠀⠀⠀⠀⢀⣾⣿⣋⣴⣿⣿⣷⣾⡿⠟⠛⠋⠉⠉⠉⠛⠻⢿⣷⣿⣿⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⣿⡿⢁⣶⣿⣿⣿⣾⣿⣯⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⡄⢹⣿⣌⠙⠀⠀⠀⠀⠀⠀⢠⣽⣿⣿⣿⣿⣷⣿⠟⠉⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣯⡆⠀⠀⠀⠀⠹⣷⣿⣿⣛⣧⣯⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣾⡿⠋⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠈⠻⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⡟⢹⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠈⢿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢸⣿⣿⣿⠁  this took so long⠀ ⠈⢿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠘⣿⣿⣿⣷⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣶⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣾⣿⠃⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡿⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⢹⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⣺⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⡆⠞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣠⡿⣿⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⠡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⠻⣿⣿⡿⣿⣿⣿⣿⣿⠟⢙⣷⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣼⣿⣿⣿⣿⣿⣿⣶⣮⣿⣿⣾⣿⣿⠿⠛⠁⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠿⠻⠟⠻⠻⠟⠛⠛⠋ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

    print("Your average number of guesses across " + str(num_games) + " games is: " + "{:.2f}, NICE JOB".format(average_attempts))  # Calculate and display the average number of attempts


    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠜⠟⠉⠉⠛⠛⠳⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀")
    print("⠀⠀⠀⠀⠀                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠟⠛⠛⠛⠛⠓⢦⣄⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀ ⠀⠀")
    print("⠀⠀⠀⠀                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣰⡞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⠀⠸⡆⠀⠀⢰⣶⣶⣄⠀⠀⠀⠹⣿⡆⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀                ⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠁⠀⠀⠈⠉⠛⢶⣄⠀⠀⠀⠀⣼⠋⠀⠀⠀⢀⣤⣤⣤⣄⠀⠀⠀⠀⢻⣷⠐⣿⠀⠀⢸⣿⡇⠙⣷⠀⠀⠀⢹⣿⠀⠀⠀⠀⠀⠀⠀")
    print("⠀             ⠀⠀⠀⠀⠀⣀⣤⠶⠛⠋⠉⠙⢻⣷⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡄⠀⣸⠇⠀⠀⠀⢠⣿⣿⠛⠉⢹⡇⠀⠀⠀⠀⣿⣯⢿⡄⠀⠈⣿⣧⢠⡟⠀⠀⠀⢸⣿⡇⠀ ⠀⠀⠀⠀⠀")
    print("            ⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⢀⣀⣀⣿⣿⠀⠀⢠⡾⠁⠀⠀⠀⣠⣾⣿⠿⣦⡀⠀⠀⠀⠹⣿⡄⣿⠀⠀⠀⠀⣿⣿⠁⠀⠀⢠⡇⠀⠀⠀⠀⢻⣿⠸⡇⠀⠀⢹⠿⠛⠀⠀⠀⠀⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀")
    print("           ⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⢸⡟⠉⠀⠀⠀⢿⣿⡀⣿⠀⠀⠀⠀⢿⣿⠀⠀⠀⣸⠇⠀⠀⠀⠀⣿⣿⠹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠀⢸⡄⠀⠀⠀⠀⢀⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("          ⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⢸⣷⣤⡄⠀⠀⠸⣿⡇⢻⡄⠀⠀⠀⠀⠙⠓⠒⠛⠁⠀⠀⠀⠀⢀⣿⣿⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠀⠀⠸⣷⣤⣴⣶⣾⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀          ⠀⠀⠀⠀⠀⣷⠀⠀⠀⠸⣿⡌⣷⠀⠀⠀⢻⣿⠈⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠇⠀⠀⠀⠙⠻⣶⣤⣤⣤⣤⣤⣶⣿⡿⠟⠁⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀          ⠀⠀⠀⠀⠹⣆⠀⠀⠀⠙⠛⠛⠀⠀⠀⢸⣿⡆⠀⠹⢦⣄⡀⠀⠀⠀⠀⠀⢀⣠⣶⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀          ⠀⠀⠀⠀⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠀⠀⠀⠉⠛⠷⢶⣶⣶⣿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⠶⠶⢶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀          ⠀⠀⠀⠀  ⠀⠈⠛⠶⣶⣤⣴⣶⣿⣿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡤⠶⠒⠛⠛⠛⠛⠓⠦⣄⠀⠘⣧⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠤⠶⠦⢤⣤⣀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⢿⠀⠀⠀⠸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣄⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠉⢷⣄⡀⠘⣧⠀⠀⠀⢶⣶⣶⠀⠀⠀⣰⣿⡇⢸⡆⠀⠀⠀⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⢻⣧⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡄⢻⠀⠀⠀⠈⠉⠀⠀⠀⠰⣿⣿⠁⠀⣷⠀⠀⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠘⣿⡇⠀⣼⠋⠀⠀⠀⣠⣾⣿⠿⠛⣧⠀⠀⠀⠀⢻⣿⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⡀⢻⠀⢀⣀⣨⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⢹⣿⣠⡏⠀⠀⠀⠀⣿⣿⠃⠀⠀⢸⡇⠀⠀⠀⠈⣿⣟⣧⠀⠀⠀⢻⣿⣿⠀⠀⠀⢸⣿⡇⠈⣿⠿⠛⠻⢿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⢿⣿⡀⢀⣠⡟⠀⠀⠀⠀⠀⣿⣿⢹⡄⠀⠀⠈⠛⠉⠀⠀⠀⢸⣿⡏⠀⠋⠀⠀⠀⢈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⣿⠀⠀⠀⢸⣿⡏⢷⡀⠀⠀⠀⠀⠉⠛⠋⠉⠀⠀⠀⠀⠀⣸⣿⡏⠘⣇⠀⠀⠀⠀⠀⠀⢀⣰⣿⡿⠁⠀⠳⣤⣠⣤⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠋⠉⣿⣧⢀⡟⠀⠀⠀⢸⣿⡇⠘⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠁⠀⠹⣄⣀⣀⣤⣤⣶⣿⡿⠛⠁⠀⠀⠀⠈⠉⠛⠉⠁⠀⠀⠀⠀⠀    ")
    print("⠀⠀⠀               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠈⠛⠛⠁⠀⠀⢀⣿⣿⠃⠀⠀⠙⠷⣤⣀⣀⠀⠀⣀⣀⣠⣴⣿⡿⠋⠀⠀⠀⠀⠈⠙⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ")
    print("⠀⠀⠀⠀                 ⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀⠀⠀⠀⣠⣿⣿⠏⠀⠀⠀⠀⠀⠈⠙⠻⠿⠿⠿⠿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           ")
    print("⠀⠀⠀⠀⠀⠀                 ⠀⠀⠀⠀⠀⠀⠉⠳⢶⣤⣴⣶⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           ⠀")


main()
