#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def palindrome():
    #plaindrome finder
    #welcome user
    print('Welcome to Palindrome Finder!')
    #user input --word
    user_input=input('Please enter your word here:')
    #reverse the word
    reverse_word=user_input[::-1]
    #if match --> palindrome
    if user_input.lower()==reverse_word.lower():
        print('Yes! It is a palindrome!')
    #else --> simple word
    else:
        print('Sorry! It is just a simple word!')


#import library
import tkinter as tk

#window create
window=tk.Tk()

#change title
window.title('Omkar Python Project')

#change size
window.geometry('500x500')

#label 
tk.Label(window,text='Python Project',font=('Helvetica',24)).place(x=150,y=30)

#button
tk.Button(window,text='Palindrome',width=20,height=2,command=palindrome).place(x=10,y=150)
#mein agar ye nai likhunga, toh window nai dikhegi
window.mainloop()



