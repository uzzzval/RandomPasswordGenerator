#Importing required libraries
import random, string

#Getting a random value from system
randomSystemValue = random.SystemRandom()
length=0

#Getting the length of password to be created as an input. User is restricted to provide value less than 8
while(int(length)<8):
    length=raw_input("Please provide the length of random password")
    if(int(length)<8):
        print "\n"+"Please Enter Length of password equal to or greater than 8, length of password less than 8 will generate a weak password"

#Generating random password
if int(length)>=8:
    setOfAllCharacters = string.letters[0:52] + string.digits
    setOfAllCharacters=setOfAllCharacters+"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    password=""
    for i in  range(0,int(length)):
        password=password+randomSystemValue.choice(setOfAllCharacters)
    #Printing Final Password
    print password

    
    

