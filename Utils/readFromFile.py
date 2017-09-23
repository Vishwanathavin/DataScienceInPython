import sys

def getDataFromText():

    inputFilepPath = sys.argv[1]   # Input file name is given as system argument. Here [1] refers to the second argument in "python readFromFile.py ../Data/inputNames.txt"

    inputFile = open(inputFilepPath, 'r')

    data = []
    while 1:                           # Keep running until you break it
        line = inputFile.readline()    # Read each line
        line = line[0:-1]              # Removes the line break "\n" from the line
        if len(line) > 0:              # If line has some content. Do not have empty lines in the middle of your input file
            data.append(line)          # Append each line into an array ( This does not have the line break)
        else:
            inputFile.close()          # Close the file and exit loop
            break
    print('Names read ....')
    return data

if __name__ == '__main__':             # Purpose of calling the function inside this condition is, we can either run the individual file
    getDataFromText()                  # or just call the module from another routine