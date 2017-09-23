
inputString = "Hello Vishwa! Dear Vishwa!"

inputString = inputString[0:-1]              # Removes the line break "\n" from the line

inputString = inputString.strip().split()    # Splits the string into separate words

inputString = "+".join(inputString)          # Add a '+' between the split words

inputString=inputString.replace('Vishwa','Radhi')

print inputString
