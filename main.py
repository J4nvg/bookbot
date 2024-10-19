def readBook(filename):
    with open(filename) as f:
        for line in f:
            print(line)

if __name__ == "__main__":
    readBook("books/frankenstein.txt")