#-------------------- Dice Rolling -------------------

# Using Python GUI package tkinter to create Dice Rolling

# Import necessary libraries -------------------------
import tkinter 
from tkinter import *
from PIL import Image,ImageTk
import random

# Creating GUI Window --------------------------------
root = Tk()
root.title ('Welcome to Dice Rolling!')
root.geometry("600x400")

# Make your dice -------------------------------------
dice =[]
for i in range(1,7):
	img = Image.open(f'{i}.jpeg')
	photo =ImageTk.PhotoImage(img)
	dice.append(photo)

# Rolling option as a button in window ---------------
def rolling_again():
	roll= random.choice(dice)
	roll_label=Label(image=roll)
	roll_label.place(x = 173, y = 50)

# Create the button ----------------------------------
B = tkinter.Button(root, text ="Roll again?", height=3,
 width=10, command = rolling_again)
B.place(x=255,y= 320 )

mainloop()

