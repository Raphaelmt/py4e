fname = input("Enter a file name: ")

try:
    handle = open(fname)
except:
    print("Invalid file name.")
    quit()

domains = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    domain = words[1].split("@")
    domains[domain[1]] = domains.get(domain[1], 0) + 1

print(domains)

