fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    print("File cannot be opened", fname)
    quit()
count = 0
for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")


