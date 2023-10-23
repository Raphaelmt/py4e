import re

fname = input("Enter a file name: ")

try:
    handle = open(fname)
except:
    print("Invalid file name.")
    quit()

regexp = input("Enter a regular expression: ")
count = 0
for line in handle:
    count = count + len(re.findall(regexp, line))

print(fname, "had", count, "lines that matched", regexp)