#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     W0487099
#Student Name:  Alex Barr

def TypePhrase():
    """
    Simplest Function in this program, just returns the phrase typed by the user. I haven't set any limitations on this function.
    """
    return input("Type a phrase (or quit to exit program): ")

def LetterRedaction(_redactedLetters):
    """
    This is the primary function of the program. It takes whatever has been put in the TypePhrase function and checks it to see what letters to redact.
    The requirements are very strict for this function and it will not allow you to use it in the way it is not intended.
    """
    _letters = input("Type a comma-seperated list of letters to redact: ")
    _warningShown = 0

    #Check for spaces at end to remove before the main portion of this function (trying to emulate a C#-like for loop)
    #I'm doing this because normally a special value will give an invalid input, but a space may be a normal reaction to put
    #at the end of an input so I don't want to punish the user for that.

    _tempString = [] #Putting the string into an actual list so I can delete the spaces and then will put that list BACK into the original string
    for letter in _letters:
        _tempString.append(letter)

    _placeInString = len(_tempString) - 1
    while _placeInString > -1:
        if _tempString[_placeInString] == " ": #Get rid of spaces at the end of the string
            del _tempString[_placeInString]
            _placeInString -= 1
        else:
            break
    #Put the temporary string back together
    _letters = ""
    for i in range(len(_tempString)):
        _letters += _tempString[i] # THIS IS REALLY COOL THAT THIS WORKS!!!

    for i in range(len(_letters)): # Go through the string as a list
        if i % 2 == 1: # Check every second vslue in the string -- if it is NOT a comma, end the loop and try again
            if _letters[i] != ",": # if its not a comma tell the user to start over #### <-------- THIS CODE HERE WILL NEVER EXECUTE THE WAY I INTENDED BECAUSE IN THE OCCASSIONS THAT IT IS MISTAKENLY A "," the i % 2 WON'T == 1
                print("Invalid Input. Please try again") # I realize I could set this up so that it counts commas when they aren't the even character in the string, but I want to enforce this
                LetterRedaction(_redactedLetters)
                break
            else: #If it IS a comma
                continue
        else:
            if _letters[i].isalpha(): #This section can be done with replacing any symbol that the user places, but it complicates things sometimes such as when the user places a "_" that is supposed to be replaced by a "_", so for simplicities sake I'm limiting the redacted characters to be letters only
                if _redactedLetters.count(_letters[i]) == 0:
                    _redactedLetters.append(_letters[i].lower())
                else:
                    if _warningShown == 0: #Only show the warning once
                        print("WARNING: Duplicate letters/symbols have not been added.")
                        _warningShown += 1
            else:
                print("Invalid Input (letters only). Please try again")
                _redactedLetters.clear() #BUG FIX <-- so that false-duplicated aren't recorded
                LetterRedaction(_redactedLetters)
                break

def NumberOfRedactedLetters(_phrase, _redactedLetters):
    """
    This uses a double for each loop to count the number of redacted letters in the phrase.
    """

    n = 0
    for letter in _phrase:
        for _redacted in _redactedLetters:
            if letter.lower() == _redacted.lower():
                n += 1

    return n

def PrintRedactedPhrase(_phrase, _redactedLetters, _replacementSymbol):
    """
    This is where I went overboard and created my own version of the .Replace function.
    It was pretty easy, just get the phrase, the redacted letters the symbol the programmer
    would like to replace the redacted letters with.

    It uses a double for each loop going through the phrase string letter by letter and for each letter
    it goes through all the letters to redact. If the current letter is the same as the letter to redact then the current letter
    is replaced with the replacement symbol. At the end of each second for each loop the letter is appeneded to the redacted phrase
    whether it is an original letter or a replacement symbol.

    Then finally, I use a for each loop to concatenate each letter/symbol in _redactedPhrase to a new string called _finalPhrase and this is
    printed to the screen.
    """
    _redactedPhrase = []
    _finalPhrase = ""

    for letter in _phrase:
        for redactedLetter in _redactedLetters:
            if letter.lower() == redactedLetter.lower():
                letter = _replacementSymbol
        
        _redactedPhrase.append(letter)
    
    for letter in _redactedPhrase:
        _finalPhrase += letter
    print(str(_finalPhrase))


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    endPhrase = "quit"
    redactedLetters = [] #Clear the list so it doesn't cause errors on the next try

    while True:
        redactedLetters.clear() #= []
        #Input Message
        phrase = TypePhrase()
        #Exit the loop if the entered phrase is the same as the end phrase
        if phrase == endPhrase:
            break
        print("")
        #Get Letters to Remove
        LetterRedaction(redactedLetters)
        #Show How Many Letters Redacted HOW MANY LETTERS TAKEN AWAY NOT THE NUMBER OF LETTERS TO REDACT
        print(f"Number of letters redacted: {NumberOfRedactedLetters(phrase, redactedLetters)}")
        #Print Redactedn Phrase
        PrintRedactedPhrase(phrase, redactedLetters, "_")
        print("\n")
        #Repeat Input Message








    # YOUR CODE ENDS HERE

main()