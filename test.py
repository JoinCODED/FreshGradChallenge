s = 'hamza'
stuff = [str(ord(c)) for c in s]
print (stuff)
print ("".join(stuff))

awesome = ''.join(chr(i) for i in stuff)
print (awesome)
