try:
    hours = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
except:
    print("Error, please enter numeric input")
    exit()

if hours > 40:
    print("Pay:", 40.0 * rate + (hours - 40.0) * (rate * 1.5))
else:
    print("Pay:", hours * rate)

