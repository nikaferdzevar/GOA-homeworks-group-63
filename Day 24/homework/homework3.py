secret_number = 7 
tries = 3 

while tries > 0:
    guess = int(input("try to guess a number tru 1-10 cuh: "))
    
    if guess == secret_number:
        print("You win!")
        break
    else:
        tries -= 1
        if tries > 0:
            print("Wrong number:", tries)
        else:
            print("You lose")
