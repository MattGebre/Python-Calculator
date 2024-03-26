# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:02:26 2022

@author: matt1
"""
import PySimpleGUI as sg


def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


layout = [[sg.Text("Select choice of operations: ")], 
        [sg.Button("Addition")], [sg.Button("Subtraction")], [sg.Button("Multiplication")], [sg.Button("Division")], 
        [sg.Text("Result: "), sg.Text(size=(15,1), key='-OUTPUT-')], [sg.Button("Exit")]]

# Create the window
window = sg.Window("Calculator", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event in ["Addition", "Subtraction", "Multiplication", "Division"]:
        num1 = float(sg.popup_get_text("Enter first number: "))
        num2 = float(sg.popup_get_text("Enter second number: "))

        if event == 'Addition':
            result = add(num1, num2)

        elif event == 'Subtraction':
            result = subtract(num1, num2)

        elif event == 'Multiplication':
            result = multiply(num1, num2)

        elif event == 'Division':
            result = divide(num1, num2)

        
        window['-OUTPUT-'].update(result)
window.close()
