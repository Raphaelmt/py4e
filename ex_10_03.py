fname = input("Enter a file name: ")

try:
    handle = open(fname)
except:
    print("Invalid file name.")
    quit()

letters = dict()
for line in handle:
    line = line.lower()
    for letter in line:
        if letter.isalpha():
            letters[letter] = letters.get(letter, 0) + 1

freqLetters = list()
for k,v in letters.items():
    freqLetters.append((v,k))

freqLetters = sorted(freqLetters, reverse=True)

for(v,k) in freqLetters:
    print(k,v)