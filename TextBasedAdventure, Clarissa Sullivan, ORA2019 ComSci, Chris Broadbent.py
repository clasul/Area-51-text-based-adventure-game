# Author: Clarissa Sullivan
# Version: 1.3
# Date: 17.07.2019
# I used https://www.derekshidler.com/how-to-create-a-text-based-adventure-and-quiz-game-in-python/ by Derek Shidler to help me get an idea on how I wanted to structure this project.
# The ASCII text-boxes are from https://boxes.thomasjensen.com/ , and were slightly modified.

def tutorial():
    print("\n============================Tutorial=============================\n\n"
          "After every piece of text describing the story, you will be \n"
          "provided with several options to proceed. \n"
          "Your choices will determine the outcome of the story. \n"
          "Write the number of your selection after the '>>>' and press \n"
          "enter to confirm.")

def error():
    print("\n /!\ Please select one of the letters provided. /!\ \n ")

def line():
    print("\n================================================================= \n")


def rush1():
    print("You decide to rush in head first. \n"
          "However, quickly you realise that the guards \n"
          "have a clear shot on you. \n"
          "\nWhat do you do? \n"
          "1) Keep running in \n"
          "2) Bail and run away \n")
    selection = input(">>>")
    if selection == "1":
        getshotclear()
#
    elif selection == "2":
        bail()

    else:
        error()
        rush1()

def getshotclear():
    print("You run in anyways, but as the guards have the clear advantage, \n"
          "you immediately get shot in the face and die. \n"
          "No aliens for you today. Or ever, for that matter. \n")

    badend()


def bail():
    print("You turn around and run away. You survive. \n"
          "However, you also missed out on the chance of stealing \n"
          "an alien. The thought saddens you a little.")
    goodend()

def wait():
    print("You decide to wait a little longer. \n"
          "Suddenly, some of the people who had been standing \n"
          "by the gate start rushing in. \n"
          "\n What do you do? \n"
          "1) Rush in with them. \n"
          "2) Bail and run away. \n")
    selection = input(">>>")
    if selection == "1":
        rush2()

    elif selection == "2":
        bail()

    else:
        error()
        wait()

def rush2():
    print("You rush in with the others. \n"
          "The guards shoot into the masses, but they can't seem to hit anyone. \n"
          "\n"
          "You arrive at the main buildings. \n"
          "Which one do you choose to enter? \n"
          "\n"
          "1) <<Alien Containment Center>> \n"
          "2) <<Government Secrets>> \n")
    selection = input(">>>")
    if selection == "1":
        aliens()

    elif selection == "2":
        govmt()

    else:
        error()
        rush2()

def govmt():
    print("The things you see are so horrible that you \n"
          "immediately go into cardiac arrest and die. \n"
          "\n")

    badend()

def aliens():
    print("You enter a building that looks like a high-security prison, but with \n"
          "aliens incarcerated instead of humans. You walk down the hallway in silence,"
          "until you hear one of the aliens crying out your name. \n"
          "It begs you to save it from here. \n"
          "\nWhat do you do? \n"
          "1) Save it, of course. \n"
          "2) Ignore it. \n")
    selection = input(">>>")
    if selection == "1":
        savealien()

    elif selection == "2":
        ignorealien()

    else:
        error()
        aliens()

def ignorealien():
    print("You ignore the small creature and turn around to leave. \n"
          "However, one of the other raiders decides to free it \n"
          "upon which it immediately lunges at you and kills you for betraying it. \n"
          "You die. \n")
    badend()

def savealien():
    print ("You free the alien from it's containment and escape with it. \n"
          "You call it george, and he lives with you for the rest of your life, \n" 
          "helping you out whenever you need it. \n")

    goodend()

def theend():
    print(
        "/******************/\n"
        "/*                */\n"
        "/*     THE END    */\n"
        "/*                */\n"
        "/******************/\n"
    )

def badend():
    print(
        "\n/******************/\n"
        "/*                */\n"
        "/*     BAD END    */\n"
        "/*                */\n"
        "/******************/\n"
    )

def goodend():
    print(
        "\n/******************/\n"
        "/*                */\n"
        "/*    GOOD END    */\n"
        "/*                */\n"
        "/******************/\n"
    )


def start():
    tutorial()
    line()
    print("You and a few thousand other strangers on the  \n"
          "Internet have decided to storm Area 51, as you \n"
          "firmly believe that they cannot stop all of you \n" 
          "running in at once. \n"
          "It's the 20th of September, and the big day has finally arrived. \n"
          "You and the others stand at the gates, waiting anxiously \n"
          "for someone to make the first move. \n"
          ""
          "\nWhat do you do? \n")

    print("1) Storm the main gate \n"
          "2) Wait for the others to move in first \n"
          "3) Bail and run away \n" )

    selection = input(">>>")

    if selection == "3":
        bail()

    elif selection == "2":
        wait()

    elif selection == "1":
        rush1()

    else:
        error()
        start()


start()
