print("Lets start the game snake water gun")
print("select from 0,1,-1 for this game else another number")
user_input=input("You have to first choose from snake, water and gun: ")
if user_input=='0':
    print("you choose the water")
    computer_input='1'
    print("The computer choose 1 which is snake")
    print("You wins the game bcz you choose o which is water so, as the gun hits the snake and the water destroys that gun")
    
elif user_input=='1':
    print("you choose the snake")
    computer_input='-1'
    print("The computer choose -1 which is gun")
    print("Computer wins the game bcz computer choose -1 which is gun so, you choose 1 which is snake so, as the gun hits the snake and the water destroys that gun")
elif user_input=='-1': 
    print("you choose the gun")
    computer_input='0'
    print("The computer choose 0 which is water")
    print("Computer wins the game bcz computer choose 0 which is water so, you choose -1 which is gun so, as the gun hits the snake and the water destroys that gun")
else:
    computer_input=input("Now the computer can also choose from 0,1,-1: ")
    user_input=input("Now you hve to choose once again")
    if user_input=='0' and computer_input=='0':
        print("Ties the game bcz both choose the water")
    elif user_input=='1' and computer_input=='1':
        print("Ties the game bcz both choose the snake")
    elif user_input=='-1' and computer_input=='-1':
        print("Ties the game bcz both choose the gun")
    else:
        print("Continues the game with new choices")

    


