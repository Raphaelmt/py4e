number = None
total = 0.0
count = 0

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        number = float(number)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = total + number
        
if count > 0:
    print(total, count, total / count)
else:
    print("0 0 0")