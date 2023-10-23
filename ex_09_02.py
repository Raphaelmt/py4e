fname = input("Enter a file name: ")

try:
    handle = open(fname)
except:
    print("Invalid file name.")
    quit()

days = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    days[words[2]] = days.get(words[2], 0) + 1

print(days)

