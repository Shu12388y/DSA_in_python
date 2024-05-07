from random import randint

def randomNumber():
    while(True):
        number = int(input("Enter the number"))
        random_number = randint(1,number)
        guess_number = int(input("Enter your number"))
        if(guess_number > random_number):
            print("Number is too High")
        elif(guess_number < random_number):
            print("Number is too Low") 
        else:
            print("Correct Guess")
            return False
randomNumber()
