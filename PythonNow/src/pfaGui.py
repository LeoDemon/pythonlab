#  -*- coding: gbk -*-
# filename: pfaGui.py
# first GUI programme by using tkinter and partial

import tkinter as tk
from functools import partial
from tkinter import messagebox


root = tk.Tk()
tx1 = tk.Text(root, width=50, height=6)
enVar = tk.StringVar()

def sayHello():
    messagebox.showinfo('Info', 'Hey, Python GUI!')
    tx1.insert(tk.END, 'Hey, Python Gui!\n')
    enVar.set('Hey, Python Gui!')

def HelloGui():
    root.geometry('800x500')
    root.resizable(width=False, height=False)

    #frame
    frmRoot = tk.Frame(root)
    frmLeft = tk.Frame(frmRoot)
    frmRight= tk.Frame(frmRoot)

    #button
    myBut = partial(tk.Button, root, fg='white', bg='blue')
    hgBut = myBut(text='Hello', command=sayHello)
    quitBut = myBut(text='Exit', bg='red', command=root.quit)
    hgBut.pack()
    quitBut.pack(side='bottom')

    #Entry
    enVar.set('pythonic')
    entry1 = tk.Entry(root, textvariable=enVar)
    entry1.pack(side='bottom')

    #label
    frmLab = tk.Label(root, text='律己', font=('Arial', 15))
    frmLab.pack()

    textLab1 = tk.Label(frmLeft, text='Learning', bg='gray', font=('Arial', 15))
    textLab2 = tk.Label(frmLeft, text='Exercising', font=('Arial', 15))
    textLab1.pack(side='top')
    textLab2.pack(side='top')
    frmLeft.pack(side='left')

    textLab3 = tk.Label(frmRight, text='乐观', font=('Arial', 15))
    textLab4 = tk.Label(frmRight, text='平常心', font=('Arial', 15))
    textLab3.pack(side='top')
    textLab4.pack(side='top')
    frmRight.pack(side='right')

    #text
    tx1.insert(1.0, 'Gui-tkinter\n')
    tx1.insert(tk.END, 'text message\n')
    tx1.pack(side='bottom')

    #listbox
    listVar = tk.StringVar()
    ltbox = tk.Listbox(root, listvariable=listVar)
    listItem = ['abc',-123,'hey',688,15000.88,'py-gui']
    for itm in listItem:
        ltbox.insert(tk.END, itm)
    ltbox.delete(1,3)
    listVar.set(('weibo','微信',888, 'wechat', 'orderceter', 'xyz', -123))
    ltbox.bind('<ButtonRelease-1>', lambda event:messagebox.showinfo('select', ltbox.get(ltbox.curselection())))

    #scrollbar
    scrl = tk.Scrollbar(root)
    scrl.pack(side='right', fill='y')
    ltbox.configure(yscrollcommand=scrl.set)
    ltbox.pack(fill='both')
    scrl['command']=ltbox.yview

    frmRoot.pack()
    root.title('Python-Gui')
    root.mainloop()

if '__main__' == __name__:
    HelloGui()
else:
    print('being import by another module...')

