import random
print("Hey there! What's your name?")
name = str(input())
print("Hey," + name + "!"+ " Let's play Scissors Paper Rock.")
computerplay = ['Scissors','Paper','Rock']
playerscore = 0
computerscore = 0
for x in range(1,6,1):
    print("Please enter your choice.")
    computerchoice = random.choice(computerplay)
    choice = str(input())
    if choice in ['scissors', 'scisors', 'Scissors','Scissor','SCISSOR','SCISSORS','scissor','paper','Paper','PAPER','Rock','ROCK','rock','stone','STONE','Stone']:
        print(computerchoice)
    if computerchoice in ['Rock'] and choice in ['scissors', 'scisors', 'Scissors','Scissor','SCISSOR','SCISSORS','scissor']:
        print("Computer Wins!")
        computerscore = computerscore+1
        print("Computer's Score:")
        print(computerscore)
        print(name + "'s"+" Score:")
        print(playerscore)
    if computerchoice in ['Rock'] and choice in ['paper','Paper','PAPER']:
        print( name + " Wins!")
        playerscore = playerscore+1
        print("Computer's Score:")
        print(computerscore)
        print(name + "'s"+" Score:")
        print(playerscore)
    if computerchoice in ['Rock'] and choice in ['Rock','ROCK','rock','stone','STONE','Stone']:
        print("It's a draw!")
        print("Computer's Score:")
        print(computerscore)
        print(name + "'s"+" Score:")
        print(playerscore)
    
    if computerchoice in ['Paper'] and choice in ['paper','Paper','PAPER']:
        print("It's a draw!")
        print("Computer's Score:")
        print(computerscore)
        print(name + "'s"+" Score:")
        print(playerscore)
        
    if computerchoice in ['Paper'] and choice in ['Rock','ROCK','rock','stone','STONE','Stone']:
        print("Computer Wins!")
        computerscore = computerscore+1
        print("Computer's Score:")
        print(computerscore)
        print(name + "'s"+" Score:")
        print(playerscore)
        
    if computerchoice in ['Paper'] and choice in ['scissors', 'scisors', 'Scissors','Scissor','SCISSOR','SCISSORS','scissor']:
        print( name + " Wins!")
        playerscore = playerscore+1
        print("Computer's Score:")
        print(computerscore)
        print(name + "'s"+" Score:")
        print(playerscore)
        
    if computerchoice in ['Scissors'] and choice in ['Rock','ROCK','rock','stone','STONE','Stone']:
        print( name + " Wins!")
        playerscore = playerscore+1
        print("Computer's Score:")
        print(computerscore)
        print(name + "'s"+" Score:")
        print(playerscore)
        
    if computerchoice in ['Scissors'] and choice in ['paper','Paper','PAPER']:
        print("Computer Wins!")
        computerscore = computerscore+1
        print("Computer's Score:")
        print(computerscore)
        print(name + "'s"+" Score:")
        print(playerscore)
        
    if computerchoice in ['Scissors'] and choice in ['scissors', 'scisors', 'Scissors','Scissor','SCISSOR','SCISSORS','scissor']:
        print("It's a draw!")
        print("Computer's Score:")
        print(computerscore)
        print(name + "'s"+" Score:")
        print(playerscore)
else:
    print("That's the end of the game!!")
    print("Let's check out the scores of the entire series.")
    print("In a total of 5 rounds:")
    print("The Computer has scored:")
    print(computerscore)
    print("And," + name + " has scored:")
    print(playerscore)
    print("So the winner of the series is:")
    if playerscore > computerscore:
        print(name + " !!!")
    else:
        print("The Computer!!!")