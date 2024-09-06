# example of Adventure project step 1

# the first step of the project
def intro():
    print("you've crash landed in a jungle. what should you do? ")

    answer = input("A. climb a tree \nB. jump in the river \nC. go to sleep ")

    if answer =="A":
        climbedTree()
    elif answer == "B":
        jumpInRiver()
    else:
        goToSleep()

# in future progress for this project, these 3 actions will be more filled in
def climbedTree():
    print("you climbed the tree, but run into a python at the top")

def jumpInRiver():
    print("you jump in the water and start swimming downstream")

def goToSleep():
    print("you start trying to sleep but the mosquitoes just won't leave you alone")


# this tells python to run the intro command (which starts our game)
intro()





