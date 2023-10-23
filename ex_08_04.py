fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    print("File cannot be opened", fname)
    quit()

uniqueWords = list()
for line in fhandle:
    words = line.split()
    for word in words:
        if word not in uniqueWords:
            uniqueWords.append(word)

uniqueWords.sort()
print(uniqueWords)
