#Program to demonstrate rock scissor paper game using python programming

import random
l=['rock','paper','scissor']
while True:
    user_count=0
    system_count=0
    userchoice=int(input('''Enter your Choice \n
1 Play
2 No | Exit
\n'''))
    if userchoice==1:
        for i in range(1,6):
            user_choice=int(input('''Enter Your option \n
1 rock
2 paper
3 scissor
'''))
            
            if user_choice==1:
                user_choice='rock'
            elif user_choice==2:
                user_choice='paper'
            elif user_choice==3:
                user_choice='scissor'
            system_choice=random.choice(l)
            if user_choice==system_choice:
                print("User Choice : ",user_choice)
                print("Computer Choice : ",system_choice)
                print("Game Draw")
                user_count=user_count+1
                system_count=system_count+1
                print("************************************************************************************************* \n \n")
            elif (user_choice=='rock' and system_choice=='scissor') or (user_choice=='paper' and system_choice=='rock') or (user_choice=='scissor' and system_choice=='paper'):
                print("User Choice : ",user_choice)
                print("Computer Choice : ",system_choice)
                print(" User Won")
                user_count=user_count+1
                print("************************************************************************************************* \n \n")
            else:
                print("User Choice : ",user_choice)
                print("Computer Choice :",system_choice)
                print("Computer won")
                system_count=system_count+1
                print("************************************************************************************************* \n \n")
        if user_count>system_count:
            print("Final winner is User")
            print('User score : ',user_count)
            print('Compute Score : ',system_count)
            print("************************************************************************************************* \n \n")
        elif user_count<system_count:
            print("Final winner is Computer")
            print('User score : ',user_count)
            print('Compute Score : ',system_count)
            print("************************************************************************************************* \n \n")
        else:
            print("Game is Drawn ")
            print('User score : ',user_count)
            print('Compute Score : ',system_count)
            print("************************************************************************************************* \n \n")
    else:
        print("You have been exited from game")
        break
                   
