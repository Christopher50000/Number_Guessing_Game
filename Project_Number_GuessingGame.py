import random

# This program is a guessing game for a user to play

def main():
    print("Hello User, Welcome to the Number Guessing Game ")

    print("The game is simple guess the random number")


    Players_nameInput=input(str('What is your name? '))

    print(f"That is a cool name {Players_nameInput}")

    s=input("ARE YOU READY? ")

    if s=="yes" or s=="YES" or s=="Yes":
        result=int(startgame(s))


        print(f"The number of attempts it took {Players_nameInput} to guess correctly was {result}")

    else:
        print("Its all good maybe next time")





def startgame(r):
    total_attempts=0
    print("What numbers do you want to guess between ")
    print("Enter first number here ")
    while True:
         try:
            randominterval1=int(input())
            break
         except:
            print("Please input an integer please ")
            continue

    print("Now enter second number here ")
    while True:
         try:
            randominterval2=int(input())
            break
         except:
            print("Please input an integer please ")
            continue


    randomnumber = int(random.randint(int(randominterval1), int(randominterval2)))

    while r == "yes" or r == "YES" or r == "Yes":
        print(f"What number are you guessing between {randominterval1} and {randominterval2}? ")

        try:
            guess = input()


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

    return total_attempts

if __name__ == "__main__":main()