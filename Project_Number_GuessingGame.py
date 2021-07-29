import random

# This program is a guessing game for a user to play

def main():
    print("Hello User, Welcome to the Number Guessing Game ")

    print("The game is simple guess the random number")

      while True:
        Players_nameInput=input(str('What is your name? ')) # asks users name

        checkname=any(chr.isdigit() for chr in Players_nameInput) # this is to check if the user only uses letters
                                                                  # it goes through each letter to make sure its not a digit 


        if checkname==True:                                       
            print("Please do not type any digits in name ")
            continue
        else:
            print(f"That is a cool name {Players_nameInput}")
            break


    while True:                                    
        s = input(str("ARE YOU READY? "))             #asks user if they are to play the game  
        
        if s=="yes" or s=="YES" or s=="Yes":
            
            result=int(startgame(s))                 # Calls the function startgame 
           
            print(f"The number of attempts it took {Players_nameInput} to guess correctly was {result}") #prints out players  name along with the number of attempts it took to
                                                                                                          #guess correctly 
            
            break


        elif(s=="no" or s=="NO" or s=="No"):
            
            print("See ya next time ")
            
            break

        else:
            print("Please input a valid response")
            continue



def startgame(r):
    
    total_attempts=0                                            #intializing total_attepts to 0 
   
    print("What numbers do you want to guess between ")
    
    print("Enter first number here ")                           # users inputs first interval 
   
    while True:                                                 # the while loop is used for users input, if user inputs anything else other than an integer then the user is 
        
        try:                                                   # asked to input an integer again since it will create an error for the input therefore it goes into to the 
                                                                #exception:
            randominterval1=int(input())
            
            break
        
        except:                                                
            print("Please input an integer please ")
            
            continue                                            # goes back up to the while loop 

    print("Now enter second number here ")
   
    while True: 
         try:
            randominterval2=int(input())                        #user inputs second interval 
             
               if randominterval2<=randominterval1:
                
                print("Your second number should be greater than the first number")   # just in case that the user inputs a larger first value then the second 

                print("Please input your numbers again ")

                print("Enter your first number")

                randominterval1 = int(input())

                print("Now enter second number here ")

                continue
            
            break
         
        except:                                                                     
            print("Please input an integer please ")
            
            continue


    randomnumber = int(random.randint(int(randominterval1), int(randominterval2)))      # the random number is generated which can either be the users intervals 
                                                                                        # or between the intervals

    while r == "yes" or r == "YES" or r == "Yes":
        
        print(f"What number are you guessing between {randominterval1} and {randominterval2}? ") # prints out the two intervals what the user inputed

        try:
            guess =int(input())                     # user inputs guess and the following are conditionals and if user does not enter a integer it will prompt the user to input 
                                                    #an integer 


            if int(guess) < int(randominterval1) or int(guess) > int(randominterval2):
                
                print("Please input values between intervals")

            elif int(guess) == randomnumber:
                
                print("Oh wow you guessed perfectly ")
                
                break

            elif int(guess) < randomnumber:
                
                print("Guess a bit higher ")
                
                total_attempts += 1

            elif int(guess) > randomnumber:
                
                print("Guess a bit lower")
                
                total_attempts += 1
        
        except:
            
            print("Invalid input please try entering a integers as inputs ")

    return total_attempts    # returns total number of attempts made by the user before guessing correctly 

if __name__ == "__main__":main()
