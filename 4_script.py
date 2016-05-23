def AskForNumberCities():

    number = raw_input('Enter the number of cities you would like to visit: ')

    try:
        n=int(number)
    except:
        print 'Enter a valid input!!'
    else:
        AskForCityNames(n)

def AskForCityNames(n):

    cities = raw_input('Enter the city names: ')

    cities= cities.split()
    names = []
    if(len(cities)==n):
        for i in cities:
            if i not in names:
                names.append(i)
        PrintFirstCitySentence(names)

    else:
        print "Enter a valid number of cities!!"


def PrintFirstCitySentence(cities=[],*args):

    cities.insert(0,'1')
 
    print 'You would like to visit',
    for index,item in enumerate(cities):
        if (index > 0):print item, 'as city' ,index,

    PrintAddOneCityNumSentence(cities)
        

def PrintAddOneCityNumSentence(cities = [], *args):

    cities.insert(0,'1')
    print '\nYou would like to visit',
    for index,item in enumerate(cities):
        if (index > 1):print item, 'as city' ,index,
        
AskForNumberCities()
