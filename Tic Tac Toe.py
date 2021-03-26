#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output

def display(board):
    clear_output()
    
   # print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
   # print('   |   |')
    print('-----------')
   # print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
   # print('   |   |')
    print('-----------')
   # print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
   # print('   |   |')
    


# In[ ]:


def choice_position(board):
    
    choice= 'wrong'
    
    # Take a valid position to start the game 
    
    while choice not in [1,2,3,4,5,6,7,8,9]:
        choice= int(input('Please choose your next position: (1 to 9)'))
        
        if choice not in [1,2,3,4,5,6,7,8,9]:
            print('Your choice is invalid, please try again!')
        
        elif board[choice] != ' ':
            print('Opss! Already taken, please try another one')
            choice= 'wrong'
            
            
    return choice         
    


# In[ ]:


def replacement(board,sign,position):
    
        board[position]=sign
 


# In[ ]:


def end_game(board):
    
    s1={board[1],board[2],board[3]}
    s2={board[4],board[5],board[6]}
    s3={board[7],board[8],board[9]}
    s4={board[1],board[4],board[7]}
    s5={board[2],board[5],board[8]}
    s6={board[3],board[6],board[9]}
    s7={board[1],board[5],board[9]}
    s8={board[3],board[5],board[7]}
    
    s=[s1,s2,s3,s4,s5,s6,s7,s8]
    
    for item in s:
        if item in [{'X'},{'O'}]:
            display(b)
            return False
        else:
            pass
        
    return True


# In[ ]:


def play_again(): 
    
    play= input('Do you want to play again? yes or no')
    
    if play == 'yes':
        return True
    else:
        return False
    


# In[ ]:


# Introduction

print('WELCOME TO TIC TAC TOE!')

# Controller variables 

again= True
turn= True
count=0

while again== True:
    
    b=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    sign= input('Which sign do you want to be X or O?')
    decision= input('Are you ready to play? yes or no')
    
    
# Starting the game

    if decision == 'yes':
        
        while turn== True:
            
            count +=1
            display(b)
            p=choice_position(b)
            replacement(b,sign,p)
            turn=end_game(b)
            
            
            if turn == False:
                print(f'{sign} won the game!')
                count=0
                again= play_again()
                
            elif count >= 9:
                print('No winner!')
                count=0
                turn= False
                again= play_again()               
            
# change sign by turns
           
            if sign == 'X':
                sign= 'O'
            else:
                sign='X'
                
    else:
        print('OK! BYE BYE')
    

