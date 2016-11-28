#  -*- coding: utf-8 -*-
# filename: myCalc.py
# author:Demon.Lee
# date:20160708
# description:generate a calculator by Python-GUI

import tkinter as tk
from functools import partial
from tkinter import messagebox
import tkinter.font

nums='0123456789.+-*/'

def getInput(entry, argu):
    if argu not in nums:
        messagebox.showerror('error', 'invalid input!')
    else:
        entry.insert(tk.END, argu)

def backSpace(entry):
    lentry = len(entry.get())
    entry.delete(lentry-1)

def clearInput(entry):
    entry.delete(0, tk.END)

def calc(entry):
    inputStr = entry.get()
    flag = 1
    if len(inputStr) > 0:
        if '=' == inputStr[-1]:
            inputStr = inputStr[0:-1]
    for istr in inputStr:
        if istr not in nums:
            messagebox.showerror('error', 'invalid input!')
            flag = 0
            break
    if 1==flag:
        outputStr = str(eval(inputStr.strip()))
        clearInput(entry)
        entry.insert(tk.END, outputStr)
    else:
        clearInput(entry)


def main():
    root = tk.Tk()
    root.title("Demon's Calc")
    root.resizable(0, 0)
    #root.geometry('300x300')

    enFont = tk.font.Font(size=12)
    inputEntry = tk.Entry(root, justify='right', font=enFont)
    inputEntry.grid(row=0, column=0, columnspan=4, sticky=tk.N+tk.W+tk.S+tk.E, padx=5, pady=5)

    button_bg = '#D5E0EE'
    button_act_bg = '#E5E35B'
    myButton = partial(tk.Button, root, bg=button_bg, padx=10, pady=3, activebackground=button_act_bg)

    #button 7,8,9 4,5,6 1,2,3
    button7 = myButton(text='7', command=lambda:getInput(inputEntry, '7'))
    button7.grid(row=1, column=0, pady=5)

    button8 = myButton(text='8', command=lambda:getInput(inputEntry, '8'))
    button8.grid(row=1, column=1, pady=5)

    button9 = myButton(text='9', command=lambda:getInput(inputEntry, '9'))
    button9.grid(row=1, column=2, pady=5)

    button10 = myButton(text='+', command=lambda:getInput(inputEntry, '+'))
    button10.grid(row=1, column=3, pady=5)

    button4 = myButton(text='4', command=lambda:getInput(inputEntry, '4'))
    button4.grid(row=2, column=0, pady=5)

    button5 = myButton(text='5', command=lambda:getInput(inputEntry, '5'))
    button5.grid(row=2, column=1, pady=5)

    button6 = myButton(text='6', command=lambda:getInput(inputEntry, '6'))
    button6.grid(row=2, column=2, pady=5)

    button11 = myButton(text='-', command=lambda:getInput(inputEntry, '-'))
    button11.grid(row=2, column=3, pady=5)

    button1 = myButton(text='1', command=lambda:getInput(inputEntry, '1'))
    button1.grid(row=3, column=0, pady=5)

    button2 = myButton(text='2', command=lambda:getInput(inputEntry, '2'))
    button2.grid(row=3, column=1, pady=5)

    button3 = myButton(text='3', command=lambda:getInput(inputEntry, '3'))
    button3.grid(row=3, column=2, pady=5)

    button12 = myButton(text='*', command=lambda:getInput(inputEntry, '*'))
    button12.grid(row=3, column=3, pady=5)

    button0 = myButton(text='0', command=lambda:getInput(inputEntry, '0'))
    button0.grid(row=4, column=0, columnspan=2, padx=3, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)

    button13 = myButton(text='.', command=lambda:getInput(inputEntry, '.'))
    button13.grid(row=4, column=2, pady=5)

    button14 = myButton(text='/', command=lambda:getInput(inputEntry, '/'))
    button14.grid(row=4, column=3, pady=5)

    button15 = myButton(text='<--', command=lambda:backSpace(inputEntry))
    button15.grid(row=5, column=0, pady=5)

    button16 = myButton(text='CE', command=lambda:clearInput(inputEntry))
    button16.grid(row=5, column=1, pady=5)

    button17 = myButton(text='=', command=lambda:calc(inputEntry))
    button17.grid(row=5, column=2, columnspan=2, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)

    root.mainloop()


if '__main__' == __name__:
    main()
else:
    print('being imported by another module...')

