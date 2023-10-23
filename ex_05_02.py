number = None
min = None
max = None

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        number = float(number)
    except:
        print("Invalid input")
        continue
    
    if min is None or number < min:
        min = number

    if max is None or number > max:
        max = number

        

print("Maximum:", max, "\nMinimum:" ,min)
