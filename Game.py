'''
Created on Nov 6, 2017

@author: Tyler Meserve
'''
import random

'''
The difference between this program and the java version of the program is everything that is extra credit
on the java version is required on this version. 
'''

def main():
    playAgain = False
    while playAgain == False:
        no = False
        while no == False:
            num = int(input("Please pick a number for me to generate.\n"))
            if num < 1:
                print("Invalid input.")
            elif num > 1:
                rannum = random.randint(1, num)
                rannum2 = random.randint(1,num)
                no = True
            else:
                print("Invalid input.")
        
        ranins = ["You n00b.", "Learn to be 1337.", "Harder than you thought eh?", "Not even MLG are you?", "Get gud bro."]    
        gues = False
        gues1 = False
        while gues == False:
            guess = int(input("Please enter your guess.\n"))
            
            if guess > rannum:
                if guess > num:
                    print("INVALID. Please stay in the defined range of " + num + random.choice(ranins))
                else:
                    print("Your guess is too high from the first number! " + random.choice(ranins))
            elif guess < rannum:
                if guess > num:
                    print("INVALID. Please stay in the defined range of " + num + random.choice(ranins))
                else:
                    print("Your guess is too low from the first number! " + random.choice(ranins))
            elif guess == rannum:
                print("Good job! You got the first number!")
                gues = True
                while gues1 == False:
                    guess = int(input("Please enter your guess.\n"))
                    if guess > rannum2:
                        print("Your guess is too high from the second number! " + random.choice(ranins))
                    elif guess < rannum2:
                        print("Your guess is too low from the second number! " + random.choice(ranins))
                    elif guess == rannum2:
                        print("Good job! You got the second number!")
                        gues1 = True
                    else:
                        print("Invalid input " + random.choice(ranins))
            else:
                print("Invalid input " + random.choice(ranins))
            
            if guess > rannum2:
                if guess > num:
                    print("INVALID. Please stay in the defined range of " + num + random.choice(ranins))
                else:
                    print("Your guess is too high from the second number! " + random.choice(ranins))
            elif guess < rannum2:
                if guess > num:
                    print("INVALID. Please stay in the defined range of " + num + random.choice(ranins))
                else:
                    print("Your guess is too low from the second number! " + random.choice(ranins))
            elif guess == rannum2:
                print("Good job! You got the second number!")
                gues = True
                while gues1 == False:
                    guess = int(input("Please enter your guess.\n"))
                    if guess > rannum:
                        print("Your guess is too high from the first number! " + random.choice(ranins))
                    elif guess < rannum:
                        print("Your guess is too low from the first number! " + random.choice(ranins))
                    elif guess == rannum:
                        print("Good job! You got the first number!")
                        gues1 = True
                    else:
                        print("Invalid input " + random.choice(ranins))
            else:
                print("Invalid input " + random.choice(ranins))
        
        agai = False
        while agai == False:
            again = str(input("Would you like to play again?\n"))
            if again.lower() in ('yes', 'y'):
                agai = True
            elif again.lower() in ('no', 'n'):
                playAgain = True
                agai = True
            else:
                print("Invalid input!")
        

if __name__ == '__main__':
    main()