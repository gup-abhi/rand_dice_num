# importing tkinter
import tkinter as tk
from tkinter import ttk
# importing showinfo from tkinter messagebox
from tkinter.messagebox import showinfo
# importing random module
import random

# creating a window
win = tk.Tk()
# giving a title to our window
win.title("Random Number Generator")


# creating a function randomly generate a number between 1 to 6
def play():
    random_number = random.randint(1, 6)
    number.config(text=f"Number is : {random_number}")
    # if number matches to 6 then user wins
    if random_number == 6:
        showinfo("Congratulations", "You WON !!")


# creating a label to display the number
number = ttk.Label(win, text="")
number.pack(pady=10)

# creating play button to get number
play = ttk.Button(win, text="Play", command=play)
play.pack(padx=50)

# creating window loop
win.mainloop()
