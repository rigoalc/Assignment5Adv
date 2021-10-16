#create main function
def get_specials():
    
    

#create variables and prompt the user for the input

    name = input("Please enter your name:")
    day = input("Please enter the day of the week (Mon, Tue, Wed, Thu, Fri):")
    member = input("Do you have a membership (y/N):")
    
    
    #condition for day of week
    if day == "Mon":
        meal = "Spaghetti"
        price = 12.99
        
        
    if day == "Tue":
        meal = "Lasagna"
        price = 15.99
        #nested for name less than 5 characters
        if len(name)<5:
            meal = "Impossible Burger"
            price = 11.99
            
    if day == "Wed":
        meal = "Minestrone soup"
        price = 8.99
        
    if day == "Thu":
        meal = "Pot pie"
        price = 7.99
        
        if len(name)<5:
            meal = "Beyond Burger"
            price = 11.99
    if day == "Fri":
        meal = "Tacos"
        price = 6.99
    #condition to check discount to members.

    if member == "y": 
        price = price - 2
        
        #print the output 
    
    print ("The special for", day, "is", meal, "for $", price, ".") 

#call the function
get_specials()