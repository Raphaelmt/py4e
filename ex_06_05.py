str = 'X-DSPAM-Confidence:0.8475'

colpos = str.find(":")
fnumber = float(str[colpos + 1:])
print(fnumber, type(fnumber))