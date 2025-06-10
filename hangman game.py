import random
import hangmanfig
import wordlist
print('WELCOME TO HANGMAN ')


lives=6
choosen = random.choice(wordlist.words)   
display = []

for i in range(len(choosen)):  
    display += '_'
print(display)

endofgame=False
while not endofgame:
    guess=input('guess a letter :  ').lower()
    for index  in range(len(choosen)):
        l=choosen[index]
        if l==guess:
            display[index]=guess
    print(display)
    if guess not in choosen:
        lives-=1
        if lives==0:
            endofgame=True
            print('you loose ')
    if '_' not in display:
        endofgame=True
        print('YOU WIN!! ')
    print(hangmanfig.stages[lives])



        

  
    


    
       

 
        



    
        

    


 












  