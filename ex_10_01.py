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

toplist = list()
for k,v in emails.items():
    toplist.append((v,k))
toplist = sorted(toplist, reverse=True)

print(toplist[0])