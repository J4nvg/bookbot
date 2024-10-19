FRANK = "books/frankenstein.txt"
def readBook(filename):
    with open(filename) as f:
        for line in f:
            print(line)

def countWords(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            count += len(line.split())
    return count

def charCount(filename):
    ndict ={}
    with open(filename) as f:
        for line in f:
            for word in line.strip().split():
                for char in word:
                    if ord(char.lower()) >= 97 and ord(char.lower()) <= 122:
                        ndict[char.lower()] = ndict.get(char.lower(),0) + 1
    return ndict

if __name__ == "__main__":
    # readBook(FRANK)
    print(f"--- Begin report of {FRANK} ---")
    print(f"{countWords(FRANK)} words found in the document.\n")
    ndict = charCount(FRANK)
    keylist = list(ndict.keys())
    keylist.sort()
    for key in keylist:
        print(f"the '{key}' character was found {ndict[key]} times.\n")
    print(f"--- End report of {FRANK} ---")