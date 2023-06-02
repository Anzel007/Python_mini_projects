import random
up_boundary= input("Enter a number that will be the upper boundary for the range: ")
up_boundary=int(up_boundary)
if up_boundary <= 0:
    print("Enter a number greater than 0")
    quit()

random_number=random.randint(0,up_boundary)
guess_count=0
while True:
    guess_count+=1
    user_guess= input("Enter your guess number: ")
    user_guess= int(user_guess)
    if user_guess==random_number:
        print("you are correct")
        
        break
    elif user_guess<random_number:
            print("your guess is below the number")
    else:
            print("your guess is above the number")

print("You guessed the number in", guess_count,"times")


    
        




