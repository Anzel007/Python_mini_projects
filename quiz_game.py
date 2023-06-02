print("Welcome to my Quiz game")

play = input("Do you want to start the game? ")
if play.lower() != "yes" :
    quit()
print(" OK, lets start the game :) ")
count= 0

answer =  input("how many districts in nepal?")
if answer == '77' :
    print('correct answer')
    count= count+1
else:
    print('wrong answer')

answer =  input("How many continents?")
if answer == '7':
    print('correct answer')
    count +=1
else:
    print('wrong answer')

answer =  input("Full form of CPU?").lower()
if answer == "central processing unit" :
    print('correct answer')
    count +=1
else:
    print('wrong answer')

answer =  input("Full form of CPU?").lower()
if answer == "central processing unit" :
    print('correct answer')
    count +=1
else:
    print('wrong answer')

print("you got", count,"correct answers ")
#just string(count) to cinvert integer into string
print("THANK YOU FOR PLAYING THE QUIZ")


    






