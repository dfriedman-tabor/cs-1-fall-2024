
def nameLength(username):

    print("the word ", username, " has ",
          len(username), " letters")


def firstLast(word):
    print("the first letter in ", word, " is ", word[0])
    print("the last letter in ", word, " is ", word[-1])

def firstLast5(sentence):
    print("the first 5 letters are ", sentence[:5])
    print("the last 5 letters are ", sentence[-5:])

def checkPrefix(word):
    if word[:3] == "pre":
        print("your word starts with the prefix 'pre'")
    else:
        print("your word doesn't start with 'pre'")

def countVowels(word):
    count = 0
    for i in range(len(word)):
        if word[i] in ['a','e','i','o','u']:
            count += 1
    print("there are ", count, " vowels in ", word)

def appearances(sentence, word):
    count = 0
    for i in range(0, len(sentence)):
        if sentence[i : i + len(word)] == word:
            count += 1
    print(count)







