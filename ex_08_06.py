numbers = list()
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        numbers.append(float(number))
    except:
        print("Invalid input")
        continue
    
low = min(numbers)
high = max(numbers)

        

print("Maximum:", high, "\nMinimum:" ,low)