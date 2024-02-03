import collections

#opens a file to be read, and then normalises the data
def GetFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    fileText=""

    #append all lines to the one continuous string
    for line in lines:
        fileText += line

    #normalise the data, remove any unwanted punctuation
    fileText = fileText.lower().replace(" ","").replace(',',"").replace('.',"").replace('!',"").replace("?","").replace("'","").replace('"',"").replace('`',"")
    return fileText

#ensure user input is valid
def CheckInput(userInput):
    isValidInput = False
    message = "Please enter a positive integer as your number of keyLength Guesses:"
    while not isValidInput:
        try:
            #try to make user input an int
            guess = int(userInput)

            if (guess<=0): #check num is valid
                raise ValueError(message)
            
            isValidInput = True
        except ValueError:
            print(message)
            userInput = input()
    
    return guess

#create a matrix with rows with length equal to the guessLength
#if guessLength = 3:
#matrix = [[a,b,c], 
#          [a,b,c]]
def CreateMatrix(text, guessLength):
    r=0
    c=0
    matrix = []
    temp = []
    for char in text: #create a temporary array containing individual characters from the text
        temp.append(char)
        if (len(temp) == guessLength): #the final few chars in the text won't be appended, but this is negligible with 1000 words
            matrix.append(temp)
            temp = []

    return matrix

#calculate an IoC value for a given string
def CalculateIoC(text):
    # Count the frequency of each letter in the text
    letterDict = collections.Counter(text)
    L = len(text)
    
    # Calculate IoC using the formula
    ioc = 0
    for fi in letterDict.values(): #calculate top half of equation: sigma(26, i=1){ (fi ∗ (fi − 1))}
        ioc += (fi * (fi - 1))

    #calculate bottom half of equation: ans / (L ∗ (L − 1))
    ioc /= (L * (L - 1))
    
    return ioc



def main():
    #request encrypted text file.
    print("Enter the name of your encrypted file (text.txt):")
    filename = input()
    fileText = GetFile(filename)
    
    #request number of keys to try
    print("how many keylength guesses would you like to make?")
    
    numOfGuesses = CheckInput(input())
    keyLengthGuesses = []
    for guessNumCount in range(0, numOfGuesses): #get each individual key and add to array to be looped over
        print("keyLength Guess " + str(guessNumCount + 1) + ": ")
        guessVal = CheckInput(input())
        keyLengthGuesses.append(guessVal)
    
    averages = []

    #create a matrix with row length equal to the length of a key
    #get an IoC value for each column in matrix
    #get an average of the IoC value
    for keyLengthGuess in keyLengthGuesses:
        klg = int(keyLengthGuess)
        matrix = CreateMatrix(fileText, klg) #create a matrix with row length equal to the length of a key
        IOCValues = []
        c = 0
        text = ""

        while c < klg: #get an IoC value for each column in matrix
            for row in matrix:
                if(len(row) == klg):
                    text += row[c]

            rowcalc = CalculateIoC(text)
            text = ""
            c += 1
            IOCValues.append(rowcalc)

        #get an average of the IoC value
        IcEnglish = 0.0686
        average = 0
        for num in IOCValues:
            average += num
        average = average / len(IOCValues)
        
        print("average IC value for " + str(klg) + " = " + str(average))
        averages.append(average)
    

    #calculate the most likely key length by getting the closest average to the IoC of English
    IcEnglish = 0.0686
    #could use lambda instead, something like this maybe?:
    #min(averages, key = lambda x: abs(x-IcEnglish)
    closest = 100
    count = 0
    guess = 0
    for avg in averages: #closest value to IoC of English
        temp = abs(IcEnglish -avg )
        if temp < closest:
            closest = temp
            guess = count
        count+=1

    print ("the most likely keylength guess is: " + str(keyLengthGuesses[guess]))
    
#Begin
main()