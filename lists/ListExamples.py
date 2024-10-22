from tabnanny import check


# print each number in a list
def printNumbers(nums):
    for i in range(0, len(nums)):
        print(nums[i])

printNumbers([5, 2, 9, 7])


# check if each number in a list is positive or negative
def checkSign(numbers):
    for i in range(0, len(numbers)):
        if numbers[i] > 0:
            print("positive")
        else:
            print("negative")

checkSign([9, -4, 2, -3, -1])

# sum all the numbers in the list
def sum(nums):
    total = 0
    for i in range(0, len(nums)):
        total += nums[i]
    print(total)

sum([6, 3, 5, 4])

# count how many even numbers are in a list
def countEvens(myList):
    count = 0
    for i in range(0, len(myList)):
        if myList[i] % 2 == 0:
            count += 1
    print(count)
    
countEvens([8, 5, 4, 2, 6])


