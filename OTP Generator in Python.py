#!/usr/bin/env python
# coding: utf-8

# In[116]:


import random
import tkinter as tk
from tkinter import font

def OTPGenerator(event):
    list=[]
    for i in range(0,int(entry.get())):
       list.append(str(random.randint(0,9)))
    result= "".join(list)
    res.configure(text = "Your OTP is : " + str(result),fg="green",font="Helvetica 10")
    
w = tk.Tk()
w.geometry("450x200")
w.title("OTP Generation Program")
tk.Label(w, text="ONE  TIME  PASSWORD(OTP)  GENERATOR", font="Helvetica 11 bold",fg="Red" ).pack(side="top")
tk.Label(w).pack()
tk.Label(w, text="How many digits do you want in your OTP?", font="Helvetica 10").pack()
tk.Label(w, text="(more than or equals to 4)", font="Helvetica 7").pack()

entry = tk.Entry(w)
entry.bind("<Return>", OTPGenerator)
entry.pack()
res = tk.Label(w)
res.pack()
btn = Button(w, text = '  Exit  ', bd = '3', command = w.destroy)      
btn.place(x=200,y=150) 
w.mainloop()


# In[ ]:




