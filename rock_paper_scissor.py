import random

user_points=0
cpu_points=0
options=["rock","paper","scissors"]

while True:
    user_input = input("Type rock/paper/scissors or q to quit :  ").lower()
    if user_input =="q":
        break
    if user_input not in options:
        continue

    random_number= random.randint(0,2)
    # 0:rock, 1:paper, 2:scissors
    cpu_pick=options[random_number]
    print("Computer picked ",cpu_pick)
    if user_input== cpu_pick:
        print("Draw")
    elif user_input=="rock" and cpu_pick=="scissors":
        print("You won!!")
        user_points+=1
    elif user_input=="paper" and cpu_pick=="rock":
        print("You won!!")
        user_points+=1
    elif user_input=="scissors" and cpu_pick=="paper":
        print("You won!!")
        user_points+=1
    else:
        print("CPU won ")
        cpu_points+=1
print("User points==>",user_points)
print("CPU points==>",cpu_points)
print("thank you for playing")



