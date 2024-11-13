#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     W0487099
#Student Name:  Alex Barr

def TypePhrase():
    return input("Type a phrase (or quit to exit program): ")

def LetterRedaction(_redactedLetters):
    _letters = input("Type a comma-seperated list of letter to redact: ")

    for i in range(len(_letters)): # Go through the string as a list
        if i % 2 == 1: # Check every second vslue to make sure that it is a comma (may have to adjust for potential space at the end)
            if _letters[i] != ",": # if its not a comma tell the user to start over
                print("Invalid Input. Please try again")
                LetterRedaction(_redactedLetters)
                break
            else: #If it IS a comma
                continue
        else:
            if _letters[i].isalpha():
                _redactedLetters.append(_letters[i].lower())
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

    condition = ""
    endPhrase = "quit"
    redactedLetters = []

    while True:
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