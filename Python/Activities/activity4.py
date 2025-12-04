u1 = input("What is User 1's name? ")
u2 = input("What is User 2's name? ")

	
while True:
    u1_answer = input(u1 + ", do you want to choose rock, paper or scissors? ").lower()
    u2_answer = input(u2 + ", do you want to choose rock, paper or scissors? ").lower()
 
    if u1_answer == u2_answer:
        print("It's a tie!")
    elif u1_answer == 'rock':
        if u2_answer == 'scissors':
            print( u1 + " selected Rock wins!")
        else:
            print(u2 + " selected Paper wins!")
    elif u1_answer == 'scissors':
        if u2_answer == 'paper':
            print(u1 + "  selected Scissors win!")
        else:
            print(u2 + " selected Rock wins!")
    elif u1_answer == 'paper':
        if u2_answer == 'rock':
            print(u1 + " selected Paper wins!")
        else:
            print(u1 + " selected Scissors win!")
    else:
        print("user enterd invalid input! You have not entered rock, paper or scissors, try again.")
    
    repeat = input("Do you want to play another round? Yes/No: ").lower()
    
    if(repeat == "yes"):
        pass

    elif(repeat == "no"):
        raise SystemExit

    else:
        print("You entered an invalid option. Exiting now.")
        raise SystemExit