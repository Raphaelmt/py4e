fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print("File cannot be opened", fname)
    quit()
count = 0
for line in fhandle:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
