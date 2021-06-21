# -------------------- Binary Search Algorithm --------------------

# note: click on Ouit butten after running the program each time

import random 
import tkinter 
from tkinter import *
import time


root = Tk()
root.title ("Binary Search Engine")
root.geometry ("300x300")
fields= ('Min number in range','Max number in range','Amount of random numbers'
	,'Target Value','The number index position')

# modify function for selected range and the number --------------
def binary_search(entries):
	# The number we want to 'search'
	search = int(entries['Target Value'].get())
	# The maximum in a range
	mx = int(entries['Max number in range'].get())
	# The minimum in a range
	mn = int(entries['Min number in range'].get())
	# The amount of random numbers
	n = int(entries['Amount of random numbers'].get())

	# Binary Search Algorithm
	bar= list(set(random.sample(range(mn, mx), n)))
	print ('List of Numbers:', bar)
	L=0
	R=n-1
	while L!= R:
		tic=time.perf_counter()
		m=round((L+R) /2)
		if bar[m]> search:
			R=m-1
		# I case the process traped in the while loop
		elif tic> 20:
			print ('No exact match have been found!')
			print ('The number is between index: ', L ,'and', R)
			entries['The number index position'].delete(0,tkinter.END)
			entries['The number index position'].insert(0,'not found')
			break
		else:
			L= m
		
	if bar[L]==search:
	    entries['The number index position'].delete(0,tkinter.END)
	    entries['The number index position'].insert(0,L)
	    print ('The number index position:', L)
	else:
		print ('Unsuccessful!')


# Making the form -------------------------------------------
def makeform(root,fields):
	entries={}
	for field in fields:
		print (field)
		row = tkinter.Frame (root)
		lab = tkinter.Label (row,width=22, text= field+": ", anchor='w')
		ent = tkinter.Entry(row)
		ent.insert(0,"0")
		row.pack(side=tkinter.TOP,fill=tkinter.X, padx=5, pady=5)
		lab.pack(side=tkinter.LEFT)
		ent.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.X)
		entries[field] = ent
	return entries


ents = makeform(root, fields)
# Make the Search button ------------------------------------
b1 = tkinter.Button(root,text='Binary Search', command=(lambda e=ents: binary_search(e)))
b1.pack(side=tkinter.LEFT, padx=5, pady=5)
# Make the Quit button --------------------------------------
b2= tkinter.Button(root, text='Quit', command=root.quit)
b2.pack(side=tkinter.LEFT, padx=5, pady=5)

mainloop()