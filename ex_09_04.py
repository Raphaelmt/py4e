fname = input("Enter a file name: ")

try:
    handle = open(fname)
except:
    print("Invalid file name.")
    quit()

emails = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    emails[words[1]] = emails.get(words[1], 0) + 1

maxEmail = None
maxCount = None
for email,count in emails.items():
    if maxCount == None or count > maxCount:
        maxEmail = email
        maxCount = count

print(maxEmail, maxCount)

