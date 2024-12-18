class Book:

    def __init__(self, title, author, keywords, pages):
        self.title = title
        self.author = author
        self.keywords = keywords
        self.pages = pages

    def __str__(self):
        return self.title + " by " + self.author

    def findWord(self, targetWord):

        for i in range(len(self.keywords)):
            if targetWord == self.keywords[i]:
                return True
        return False


class Library:

    def __init__(self, books):
        self.books = books
        self.isQuiet = True


    def __str__(self):
        return str(self.books)

    def popularAuthor(self):

        largestCount = 0
        pop = None
        for i in range(len(self.books)):
            count = 0
            for j in range(len(self.books)):
                if self.books[i].author == self.books[j].author:
                    count += 1
            if count > largestCount:
                largestCount = count
                pop = self.books[i].author

        print(pop)


    def findBook(self, word):

        for i in range(len(self.books)):
            if self.books[i].findWord(word):
                print(self.books[i])

            if word in self.books[i].author or word in self.books[i].author:
                print(self.books[i])


lib = Library([ Book("LOTR", "Tolkien", ["ring", "frodo", "wizard"]) ])






