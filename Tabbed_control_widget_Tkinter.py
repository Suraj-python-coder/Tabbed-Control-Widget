# notebook----> contains two pages
# page1                           page2
# widgets                         widgets
import tkinter as tk       
from tkinter import ttk  
win = tk.Tk() 
win.title('TAB CONTROL')


# here we create notebook object and its constructore
nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)     # here we create pages 
page2 = ttk.Frame(nb)

# adding this two pages in this notebook
nb.add(page1,text='ONE')
nb.add(page2,text='TWO')
# nb.grid(row=0,column=0)
nb.pack(expand=True, fill='both')  # here we use pack function using this we can access the full space of notebook

label1 = ttk.Label(page1, text='this is page1 :')
label1.grid(row=0,column=0)

entry1 = ttk.Entry(page1, width=26)
entry1.grid(row=0,column=1)

label2 = ttk.Label(page2, text='this is page2 :')
label2.grid(row=0,column=0)




win.mainloop()