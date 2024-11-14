#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     W0487099
#Student Name:  Alex Barr

def TypePhrase():
    return input("Type a phrase (or quit to exit program): ")

def LetterRedaction(_redactedLetters):
    _letters = input("Type a comma-seperated list of letter to redact: ")

    #Check for spaces at end to remove before the main portion of this function (trying to emulate a C#-like for loop)
    #I'm doing this because normally a special value will give an invalid input, but a space may be a normal reaction to put
    #at the end of an input so I don't want to punish the user for that.

    _tempString = [] #Putting the string into an actual list so I can delete the spaces and then will put that list BACK into the original string
    for letter in _letters:
        _tempString.append(letter)

    _placeInString = len(_tempString) - 1
    while _placeInString > -1:
        if _tempString[_placeInString] == " ":
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
            if _letters[i] != ",": # if its not a comma tell the user to start over
                print("Invalid Input. Please try again")
                LetterRedaction(_redactedLetters)
                break
            else: #If it IS a comma
                continue
        else:
            if _letters[i].isalpha():
                if _redactedLetters.count(_letters[i]) == 0:
                    _redactedLetters.append(_letters[i].lower())
                else:
                    print("WARNING: Duplicate letters have not been added.")
            else:
                print("Invalid Input. Please try again")
                LetterRedaction(_redactedLetters)
                break

def NumberOfRedactedLetters(_phrase, _redactedLetters):
    n = 0
    for letter in _phrase:
        for _redacted in _redactedLetters:
            if letter.lower() == _redacted.lower():
                n += 1

    return n

def PrintRedactedPhrase(_phrase, _redactedLetters, _replacementSymbol):
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

    #condition = ""
    endPhrase = "quit"
    redactedLetters = [] #Clear the list so it doesn't cause errors on the next try

    while True:
        redactedLetters = []
        #Input Message
        phrase = TypePhrase()
        if phrase == endPhrase:
            break
        # condition = phrase
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