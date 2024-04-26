import sys

# Storage
shift = sys.argv[1]
newmessage = ""
message = ""

# Corrects Formatting
count = 0
for x in sys.stdin:
    message = message + x
while message.isalpha() == False:
    if message[count].isalpha() == False:
        message = message.replace(message[count], "")
        count = 0
    else:
        count += 1
message = message.upper()

# Create the Encrypted Message
for x in message:
    n = ord(x)
    for y in range(int(shift)):
        n +=1
        if n > 90:
            n = 65
    newmessage = newmessage + chr(n)

# Divides the message
nm2 = newmessage[0:]
divide = []
while len(nm2) > 5:
    divide.append(nm2[0:5])
    nm2 = nm2[5:]
divide.append(nm2)

# Prints/Output
output = ""
for x in range(len(divide)):
    if (x % 10) == 0:
        print(output.strip())
        output = ""
    output += f' {divide[x]}'
print(output.strip())
