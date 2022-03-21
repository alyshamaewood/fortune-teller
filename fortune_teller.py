# import kivy
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.config import Config

## idk import random--all the choices are predetermined

import random

## print statements to welcome the user and explain the game

print("Welcome to the virtual paper fortune telling game!")

print("This game will tell your fortune based on choosing colors and numbers.") 

## create a "while True" loop for the whole game using multiple conditions and choices

while True: 

    ## first, we must ask the user if they would like to play the game.

    answer = input("Would you like to play? Enter 'y' for yes and 'n' for no [y/n]") 

    ## conditions if the user chooses to play the game

    if answer == "y": 

        ## give the user choices of colors to play the game--first set of conditionals

        color = input("Choose a color from the following list: [blue, green, yellow, or red]") 

        ## conditional statement if the user chooses blue or green

        if color == "blue" or color == "green": 

            ## give the user choices of numbers to play the game--second set of conditionals    

            number = int(input("Choose a number from the following list: [1, 2, 3, or 4]"))           

            ## list of conditional statements when choosing numbers from the above list

            if number == 1: 

                print("You will meet the love of your life today.") 

            elif number == 2: 

                print("You will have a successful career.") 

            elif number == 3: 

                print("A friend will give you ominous news today.") 

            elif number == 4: 

                print("Don't look up.")       

        ## else if conditional if the user chooses red or yellow

        elif color == "red" or color == "yellow": 

            ## give the user another set of numbers to choose from

            number = int(input("Choose a number from the following list: [5, 6, 7, or 8]"))           

            ## list of conditional statements when choosing numbers from the above list

            if number == 5: 

                print("The cat that crosses your path today is a sign of good luck.") 

            elif number == 6: 

                print("The weather will be beautiful today.") 

            elif number == 7: 

                print("Baba Yaga will request the soul of your first born son.") 

            elif number == 8:

               print("You should eat potato chips today.")
                
        ## else statement out of the loop for if the users chooses the wrong colors
        else:
    
            print("You can only choose the colors blue, green, red, or yellow.")

    ## conditional if the user chooses to not play the game
    if answer == "n":

        print("Awh, we can play again another time :<")

        ## break the statement when the user chooses to not play to begin with OR after playing multiple turns
        break