fname = input("Enter a file name: ")

try:
    handle = open(fname)
except:
    print("Invalid file name.")
    quit()

hours = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    hour = words[5].split(":")
    hours[hour[0]] = hours.get(hour[0], 0) + 1

hours = sorted(hours.items())

for(k,v) in hours:
    print(k,v)