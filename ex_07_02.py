fname = input("Enter a file name: ")
fhandle = open(fname)

count = 0
total = 0
for line in fhandle:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    colpos = line.find(":")
    count = count + 1
    total = total + float(line[colpos + 1:])

print("Average spam confidence:", total / count)