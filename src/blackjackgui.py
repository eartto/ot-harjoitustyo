import tkinter as tk
from tkinter import *
import random



class BlackjackGUI(tk.Tk):
    def __init__(self):
        super().__init__()


        # Title and root
        self.title('Blackjack')
        self.geometry('900x800')
        self.configure(background="green")

        my_frame = Frame(self, bg="green")
        my_frame.pack(pady=20)


        # Card frames
        house_frame = LabelFrame(my_frame, text="House", bd=0)
        house_frame.grid(row=0, column=0, padx=20, ipadx=20)

        player_frame = LabelFrame(my_frame, text="Player", bd=0)
        player_frame.grid(row=0, column=1, padx=20, ipadx=20)


        # Insert cards into frames
        house_label = Label(house_frame, text='')
        house_label.pack(pady=20)

        player_label = Label(player_frame, text='')
        player_label.pack(pady=20)


        # Buttons
        deal_button = Button(self, text="Deal Cards", font=("Raleway", 14))
        deal_button.pack(pady=20)