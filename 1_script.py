''' dream job title and salary calculation'''

import math

dream_job_title = raw_input("Enter your dream job title: ")
# Getting the input from the user for the dream job 

hourly_wage_input = raw_input("Enter the hourly wage you would like to earn: ")
#Getting the hourly wage as input from the user

#checking for any input error
try:
    hourly_wage = float (hourly_wage_input)
    
except ValueError:
    
    print 'The entered hourly wage is not a valid number!'
    
else:
    
    print "The hourly wage is ", hourly_wage
    
    annual_wage = hourly_wage * 8 * 7 * 52

    print 'The annual wage earned by you: ' , annual_wage
    #printing the annual salary
    
    retirement_input = raw_input('Enter the value you would '
                                 'need at the time of retirement: ')
    #Checking for any input error
    try:
        retirement_money= float(retirement_input)
        
    except ValueError:
        
        print 'The retirement money entered is not a valid input!'
        
    else:
        print 'The retirement money entered is: ' , retirement_money
        
        
        num_of_years = retirement_money / annual_wage
        
        #print 'The number of years you need to work', num_of_years
        #printing the number of years to work for the retirement money
        
        number = math.ceil(num_of_years)
        #considering the integer value for number of years
        
 
        #checking for odd/even number
        
        print 'modulo value calculated is',number % 2

        print 'If the value is 1.0 then the number is odd, however, if the value is 0.0 then the number is even.'            
    
    

