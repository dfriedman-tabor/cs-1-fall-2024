
content = open(input("enter a file to analyze: "), 'r').read()


def numberWords():
    count = 1
    for letter in content:
        # count new lines as well as spaces
        if letter == ' ' or letter == '\n':
            count += 1
    print("There are", count, "words in the file")


def percentVowels():
    numVowels = 0
    numLetters = 0
    for letter in content:
        # uppercase letters fall between 65 and 90
        if 65 <= ord(letter.upper()) <= 90:
            numLetters += 1
            if letter.lower() in ['a','e','i','o','u']:
                numVowels += 1
    print("The percentage of vowels in the file is", int(numVowels/numLetters*100),'%')


def longestWord():
    word = ""
    longest = ""
    for letter in content:
        # build a word until we find something that isn't a letter
        if 65 <= ord(letter.upper()) <= 90:
            word += letter.lower()
        else:
            # if the current word is longer than our current longest, remember it
            if len(word) > len(longest):
                longest = word
            word = ""
    print("The longest word in the file is", longest)

def wordSearch():
    target = input("Enter a word to search for: ").lower()
    word = ""
    count = 0
    for letter in content:
        if 65 <= ord(letter.upper()) <= 90:
            word += letter.lower()
        else:
            if word == target:
                count += 1
            word = ""
    print("The word", target, "appears", count, "times")


def mostCommonWords():
    # dictionary to hold the length of each word
    wordLengths = {}
    word = ""
    for letter in content:
        if 65 <= ord(letter.upper()) <= 90:
            word += letter.lower()
        else:
            # when we reach the end of a word, check if its in the dictionary.
            # if so, increase its count. if not, add it to the dictionary
            if len(word) > 5:
                if word in wordLengths:
                    wordLengths[word] += 1
                else:
                    wordLengths[word] = 1
            word = ""

    mostCommon = None
    for word in wordLengths:
        # find the highest count in our dictionary
        if mostCommon == None or wordLengths[word] > wordLengths[mostCommon]:
            mostCommon = word
    print("The most common word of at least length 5 is", mostCommon)

numberWords()
percentVowels()
wordSearch()
longestWord()
mostCommonWords()