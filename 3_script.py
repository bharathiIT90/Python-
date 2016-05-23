VOWELS = ['a','e','i','o','u'] #GLOBAL list declaration

def AskUserForSentence():
#Function to get the input from the user

    while(True):
        
        words = raw_input("\nEnter three words separated with space: ")

        if words == 'QUIT':
            break
        else:
            LowerCase(words)
            continue

def LowerCase(string):
#Function to convert the sentence to lowercase
    string = string.lower()

    SplitSentecneIntoList(string)

def SplitSentecneIntoList(string):
#Function to split the sentence and generate a list

    words_list = string.split()
    if len(words_list)==3:
        for j in range(len(words_list)):
            new_word = ConvertToPigLatin(words_list[j])
            words_list[j] = new_word
        PrintThreeWordPhrase(words_list)
    elif len(words_list) > 3:
        print 'Phrase is large, Enter a phrase of length 3'
    else:
        print 'Enter a phrase of length 3'


def ConvertToPigLatin(word):
#Function to convert the word to piglatin
    if (word[0] in VOWELS) == True:
        word = word + 'hay'
    else:
        word = word[1:]+word[0]+'ay'
    return word               

def PrintThreeWordPhrase(words=[],*args):
#Function to print the converted word list

    for i in words:print i,

    
                
AskUserForSentence()

    
