from tkinter import *

def calculate_fib():
    x = int(entry.get())
    if x <= 0:
        display_message.config(text=f"The fibonacci sequence to the {x}th is: 0")
    elif x == 1:
        display_message.config(text=f"The fibonacci sequence to the {x}th is: 1")
    else:
        y, z = 0 ,1
        for i in range(2, x + 1):
            y, z = z, y + z

        display_message.config(text=f"The fibonacci sequence to the {x}th is: {z}")




mainGUI = Tk()
Label(mainGUI, text="Enter a number").grid(row=0, column=0)
entry = Entry()
entry.grid(row=0, column=1)

#Temp
Label(mainGUI, text="              ").grid(row=0, column=2)

button = Button(mainGUI, text="Calculate Fibonacci Sequence", command = calculate_fib)
button.grid(row=1, column=1)

display_message = Message(mainGUI, text="", width=400)
display_message.config(bg = 'light grey')
display_message.grid(row=2, column=0, columnspan=2)

mainGUI.mainloop()