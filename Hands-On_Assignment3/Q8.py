import random
choice = int(input("Enter choice \n 0. Rock\n 1. paper\n 2. scissor\n"))
if choice == 0:
    choice_name = 'Rock'
elif choice == 1:
    choice_name = 'paper'
else:
    choice_name = 'scissor'

choice_comp=random.randint(0,2)
if choice_comp == 0:
    comp_choice_name = 'Rock'
elif choice_comp == 1:
    comp_choice_name = 'paper'
else:
    comp_choice_name = 'scissor'


if((choice==0 and choice_comp==1 )or (choice==1 and choice_comp==2) or (choice==2 and choice_comp==0)):
    print("The computer is",comp_choice_name,".You are",choice_name,"\nComputer won.")
elif((choice==0 and choice_comp==2) or (choice==1 and choice_comp==0) or (choice==2 and choice_comp==1)):
    print("The computer is",comp_choice_name,".You are",choice_name,"\nYou won.") 
else:
     print("The computer is",comp_choice_name,".You are",choice_name,"too.","\nIt is a draw.")

          

