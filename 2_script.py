#First function that takes a letter as input
def AskForLetter():
    #print 'hi'
    while True:
        letter = raw_input('Enter a letter: ')

        try:
            input_letter = int(letter)      #user input-error validation
            #print letter

        except:
            if letter == 'quit' or letter == 'Quit' or letter == 'QUIT':
                print 'quit'
                break
            
            elif len(letter) == 1 and letter.isalpha(): #printing the output
                #print 'vowel'
                if IsVowel(letter)== True:
                    print 'The Entered vowel is', letter
                    break
            else:
                print 'Enter a valid letter, try again'
                continue
        else:
            print 'Wrong input, Try again'
            continue
                
#second function to determine whether the letter is a vowel
def IsVowel(letter):

    if  IsLowerCaseVowel(letter)== True or IsUpperCaseVowel(letter)== True:
        return True

    else:
        return False

#third function that returns true if the letter is a lowercase vowel
def IsLowerCaseVowel(letter):

    if letter == 'a' or letter == 'e' or letter == 'o' or letter == 'u' or letter == 'i':
        #print 'test true'
        return True
    else:
        #print 'test false'
        return False

#fourth function that returns true if the letter is a uppercase
def IsUpperCaseVowel(letter):

    if letter == 'A' or letter == 'B' or letter == 'O' or letter == 'U' or letter == 'I':
        return True
    else:
        return False

AskForLetter()
