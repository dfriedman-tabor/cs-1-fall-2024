# SA 11 Solutions


def problem1():

    endpoint = int(input("choose a number to stop at: "))

    for i in range(0, endpoint//3 + 1):
        print(i*3)


def problem2():

    num1 = int(input("choose a number: "))
    num2 = int(input("choose another number: "))

    if num1 > num2:
        for i in range(num2, num1 + 1):
            print(i)
    else:
        for i in range(num1, num2 + 1):
            print(i)


from math import sqrt
def problem3():

    endpoint = int(input("choose a number to stop at: "))

    for i in range(0, int(sqrt(endpoint))+1):
        print(i**2)


def problem4():

    total = 0
    endpoint = int(input("choose a number to sum up to: "))

    for i in range(1, endpoint + 1):
        total += i

    print(total)
