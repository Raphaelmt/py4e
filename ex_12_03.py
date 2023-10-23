import urllib.request, urllib.parse, urllib.error

url = input("Enter a URL: ")

try:
    fhand = urllib.request.urlopen(url)
except:
    print("Please enter a valid URL.")
    quit()

charcount = 0

for line in fhand:
    
    for c in range(len(line) - 1):
        characters = list()
        characters = line.decode()
        print(characters[c], end="")
        charcount = charcount + 1
        if charcount >= 3000:
            break
   
    if charcount >= 3000:
        break
print("\nThis document had", charcount, "characters.")