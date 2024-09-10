# Mr Friedman
# example of Adventure project step 1
# help from

# the first step of the project
def intro():
    print("you've crash landed in a jungle. what should you do? ")

    answer = input("A. climb a tree \nB. jump in the river \nC. go to sleep ")
    answer = answer.upper()

    if answer =="A":
        climbedTree()
    elif answer == "B":
        jumpInRiver()
    elif answer == "C":
        goToSleep()
    else:
        print("that's not a real answer")

# user climbs a tree and runs into a python
def climbedTree():
    print("you climbed the tree, but run into a python at the top")
    answer = input("A. fight the python\nB. jump off the tree")
    answer = answer.upper()

    if answer =="A":
        fightPython()
    elif answer =="B":
        jumpOffTree()
    else:
        print("huh?")

# this is the step where you fall in the river
def jumpInRiver():
    print("you jump in the water and start swimming downstream. What next?")
    answer = input("A. pretend you're a floating log\nB. ride on the back of an alligator")
    answer = answer.upper()

    if answer == "A":
        floatLikeLog()
    elif answer == "B":
        rideAlligator()
    else:
        print("that doesn't make any sense")

# user decides to get away from python by jumping off the tree
def jumpOffTree():
    print("that wasn't very smart. You break an ankle, and now you're really stuck")

# user chooses to float along the river
def floatLikeLog():
    print("you're floating along like a log, and some turtles crawl up onto you. Now you have some jungle friends :)")

# user chooses to hop on top of an alligator
def rideAlligator():
    print("interesting decision.. you're lunch")

# user chooses to go right to sleep
def goToSleep():
    print("you start trying to sleep but the mosquitoes just won't leave you alone :(")

# results of fighting the python
def fightPython():
    print("you're able to hold the python off, but he leaves you with a nasty bite. What next?")
    answer = input("A. use a wad of leaves as a bandage\nB. cover the bite with mud")
    answer = answer.upper()

    if answer == "A":
        bandage()
    elif answer == "B":
        mud()
    else:
        print("try again")

# results of bandaging your wound
def bandage():
    print("nice work - your bite heals well and you're back to the beginning")
    intro()

# print results of covering your wound in mud
def mud():
    print("uh oh - mud doesn't work well and it becomes very infected. not good")

# this tells python to run the intro command (which starts our game)
intro()




