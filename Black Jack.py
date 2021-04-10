#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
from IPython.display import clear_output

# Suits, Ranks, Valuses

suits= ('Diamonds','Clubs','Hearts','Spades')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values= {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


# In[7]:


# Define Cards

class Card:
    
    
    def __init__(self,rank,suit):
        
        self.rank= rank
        self.suit= suit
        self.value= values[rank]  
        
    def __str__(self):
        
        return f'{self.rank} of {self.suit} (value: {self.value})'
        


# In[8]:


# Define Deck

class Deck:
    
    def __init__(self):
        
        # First create an empty list to add 52 cards in it
        self.all_cards=[]
        
        # Adding cards according to suits and ranks
        for s in suits:
            for r in ranks:
                self.all_cards.append(Card(r,s))
    
    def shuffle(self):
        
        # Shuffle cards in the list 
        # Preparing cards for game
        # From the random package that has been imported
        
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        
        # Giving players cards
        return self.all_cards.pop()
        


# In[9]:


# Define Players

# There is a Human player and a Computer Agent

class Player:
    
    
    def __init__(self,name,balance):
        
        self.name= name
        self.balance= balance
        
        # Each player has empty list of cards at the beginning 
        self.player_cards = []
    
    def bet(self,amount):
        self.balance = self.balance - amount
        
    def bonus(self,amount):
        self.balance = self.balance + amount
    
    def add_card(self,new_card):
        self.player_cards.append(new_card)
        
    def reset_card(self):       
        return self.player_cards.clear()
        
    def __str__(self):        
        return f'{self.name} has {self.balance} coins'


# In[12]:


# Game Logic

print('WELCOME TO BLACK JACK')
name = input('\nPlease enter your name: ')

# Choose players
# Players start with 300 coins by default
player_human= Player(name,300)
player_machine= Player('Mr.Robot',300)
bank =100
game ='on'


while game == 'on':

    # Call a new deck
    new_deck= Deck()
    # Shuffle cards
    new_deck.shuffle()
    # Reset players cards for new round
    player_human.reset_card()
    player_machine.reset_card()
    

    # Spliting cards
    for y in range(2):

        player_human.add_card(new_deck.deal_one())
        player_machine.add_card(new_deck.deal_one())

    # Human player turn

    while True:

        clear_output()
        hand_value=0
        print(f"{player_human.name}'s balance: {player_human.balance}\nYour cards:")

        # Showing available cards and the total value to human player

        for c in range(len(player_human.player_cards)):
            card = player_human.player_cards[c]
            hand_value += card.value
            print(player_human.player_cards[c])

        print('----------------------------')
        print(f'You have total value: {hand_value} now')

        # Hit or Stay

        player_human_decision= input('Please make a choice: (hit or stay)? ')

        if player_human_decision== 'hit':
            player_human.add_card(new_deck.deal_one())
            player_human.bet(50)
            bank += 50
        elif player_human_decision== 'stay':
            break

    # Checking if the game is finished or not

    if hand_value > 21:
        player_machine.bonus(bank)
        print(f' \n BUSTS!, {player_machine.name} wins {bank} bonus\n')
        print(player_human)
        print(player_machine)
        bank =100
    elif hand_value == 21:
        player_human.bonus(bank)
        print(f' \n Black Jack!, {player_human.name} wins {bank} bonus\n')
        print(player_human)
        print(player_machine)
        bank =100
    else:

        # Mr.Robot player turn

        turn = 0

        while True:

            total_value=0
            

            # Showing the total value to machine player

            for x in range(len(player_machine.player_cards)):
                v = player_machine.player_cards[x]
                total_value += v.value

            if total_value >= 17:
                print('----------------------------')
                print(f"{player_machine.name}'s balance: {player_machine.balance}")
                print(f'Total value: {total_value}')
                print(f'STAND!, after {turn} rounds')
                break
            else:
                player_machine.add_card(new_deck.deal_one())
                player_machine.bet(50)
                bank += 50
                turn += 1

        # Find winner

        if total_value > 21 or hand_value > total_value:
            player_human.bonus(bank)
            print(f' \n {player_human.name} wins {bank} bonus\n')
            print(player_human)
            print(player_machine)
            bank =100
        elif total_value > hand_value:
            player_machine.bonus(bank)
            print(f' \n {player_machine.name} wins {bank} bonus\n')
            print(player_human)
            print(player_machine)
            bank =100
        else :
            print(' \n No winner!')
        
        # Asking user for more game
        
        play_again = input('Do you want to play another round? (yes or no)')
        if play_again == 'no':
            game = 'off'
        else:
            pass


# In[ ]:




