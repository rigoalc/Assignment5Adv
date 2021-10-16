# Rodrigo Alcover
# 08/09/2021
# CIS-216-12292 
# Python Programming

#
#No code has been copied from elsewhere

#(Do not copy the first result for Python Restaurant Menu in Google)

#Every file has a header with your name, date, CRN, and class name

#Explain how designed:
#I used the same code for the last assignment, but i change some of the caracteristictadapting to the expectations. 

#Include total development time
#The totaldevelopment time was 4 hs

#At least 1 of the following:
#Flowchart of main part of program; or
#Paragraph of at least 1 sentence each, explaining what you did for each part of the Development Cycle:
#Analyze: What is the problem?
#Design: How will you solve the problem?
#Develop: What did you actually do to solve the problem?
#Document: Explain your code for your future self and others.
#Functions, if used, must be documented with docstrings
#Your code style should match PEP 8, in general:
#snake_case for variables
#Indentation is with 4 spaces

#3-5 sentence paragraph for end-user on how to use program

#The function of this program is to print the name of the food special for that day and price 
#The program also compare the length of the name and so define the meal for that name. 
#First: The program ask to the user "Please enter your name:" and the user should input his Name.
#Second: The program ask to The user "Please enter the day of the week (Mon, Tue, Wed, Thu, Fri):" and the user should input the day of the week as asked "(Mon, Tue, Wed, Thu, Fri):"
#Third: The program as to the user "Do you have a membership (y/N):"
#Four:If the customer is member the price will suffer a discount of $2.
#The program will print select and print the Day and name as follow: "The special for", day, "is", meal for $,price."

#Double check you have met all of the requirements, before turning in your work!

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
        
        
    #condition to make a discount to members.

    if member == "y": 
        price = price - 2
        
        #print the output 
    
    print ("The special for", day, "is", meal, "for $", price, ".") 

#call the function
get_specials()