def computepay(hours, rate):
    if hours > 40:
        return 40.0 * rate + (hours - 40.0) * (rate * 1.5)
    else:
        return hours * rate

try:
    hours = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
except:
    print("Error, please enter numeric input")
    exit()

print("Pay:", computepay(hours, rate))

