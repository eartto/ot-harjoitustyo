import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from deck import Deck
import random
import os
import sys



class BlackjackGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Change working directory to src
        os.chdir(sys.path[0])
        
        # Absolute path to the card images
        cardspath = os.path.abspath("gui/cards")
        

        self.deck = Deck()
        d_hand = []
        p_hand = []

        p_card_position = 0
        h_card_position = 0


        # Title and root
        self.title('Blackjack')
        self.geometry('1200x800')
        self.configure(background="green")

        temp_frame = Frame(self, bg="green")
        temp_frame.pack(pady=20)

        # Card frames
        house_frame = LabelFrame(temp_frame, text="House", bd=0)
        house_frame.grid(row=0, column=0, ipadx=20)

        player_frame = LabelFrame(temp_frame, text="Player", bd=0)
        player_frame.grid(row=1, column=0, pady=20, ipadx=20)

        # Insert blank cards into frames

        # House
        house_label_1 = Label(house_frame, text='')
        house_label_1.grid(row=0,column=0)

        house_label_2 = Label(house_frame, text='')
        house_label_2.grid(row=0,column=1)

        house_label_3 = Label(house_frame, text='')
        house_label_3.grid(row=0,column=2)

        house_label_4 = Label(house_frame, text='')
        house_label_4.grid(row=0,column=3)

        house_label_5 = Label(house_frame, text='')
        house_label_5.grid(row=0,column=4)

        # Player
        player_label_1 = Label(player_frame, text='')
        player_label_1.grid(row=0,column=0)

        player_label_2 = Label(player_frame, text='')
        player_label_2.grid(row=0,column=1)

        player_label_3 = Label(player_frame, text='')
        player_label_3.grid(row=0,column=2)

        player_label_4 = Label(player_frame, text='')
        player_label_4.grid(row=0,column=3)

        player_label_5 = Label(player_frame, text='')
        player_label_5.grid(row=0,column=4)

        player_label_6 = Label(player_frame, text='')
        player_label_6.grid(row=0,column=4)


        # Resize function for cards
        def resize_card(card):
            

            card_image = Image.open(card)

            resized_card = card_image.resize((150,218))
            global card_image_tk
            card_image_tk = ImageTk.PhotoImage(resized_card)

            return card_image_tk

        def hide_button(button):
            button.grid_forget()

        def show_deal_button(button):
            button.grid()

        # Deal cards function
        def deal_cards():
            
            # Card position resets on deal_cards function
            global h_card_position, p_card_position
            self.h_card_position = 0
            self.p_card_position = 0

            # Clear all cards
            house_label_1.config(image="")
            house_label_2.config(image="")
            house_label_3.config(image="")
            house_label_4.config(image="")
            house_label_5.config(image="")

            player_label_1.config(image="")
            player_label_2.config(image="")
            player_label_3.config(image="")
            player_label_4.config(image="")
            player_label_5.config(image="")
            player_label_6.config(image="")

            # Dealers first and hidden card
            global hidden_card
            hidden_card = self.deck.deal_cards(d_hand)
            
            # Saving the hidden card image for later reveal
            global hidden_card_image
            hidden_card_image = resize_card(f'{cardspath}/{hidden_card}.png')
            
            # Cardback image
            global cardback_image
            cardback_image = resize_card(f'{cardspath}/cardback.png')
            house_label_1.config(image=cardback_image)

            # Dealers second card
            house_second_card = self.deck.deal_cards(d_hand)

            global house_image
            house_image = resize_card(f'{cardspath}/{house_second_card}.png')
            house_label_2.config(image=house_image)
            
            # Players cards
            player_first_card = self.deck.deal_cards(p_hand)
            player_second_card = self.deck.deal_cards(p_hand)

            # First
            global player_image_1st
            player_image_1st = resize_card(f'{cardspath}/{player_first_card}.png')
            player_label_1.config(image=player_image_1st)
            
            # Second
            global player_image_2nd
            player_image_2nd = resize_card(f'{cardspath}/{player_second_card}.png')
            player_label_2.config(image=player_image_2nd)

        def hit():

            p_card = self.deck.deal_cards(p_hand)

            global player_image1, player_image2, player_image3, player_image4
            
            if self.p_card_position == 0:
                player_image1 = resize_card(f'{cardspath}/{p_card}.png')
                player_label_3.config(image=player_image1)

            elif self.p_card_position == 1:
                player_image2 = resize_card(f'{cardspath}/{p_card}.png')
                player_label_4.config(image=player_image2)

            elif self.p_card_position == 2:
                player_image3 = resize_card(f'{cardspath}/{p_card}.png')
                player_label_5.config(image=player_image3)

            elif self.p_card_position == 3:
                player_image4 = resize_card(f'{cardspath}/{p_card}.png')
                player_label_6.config(image=player_image4)    

            self.p_card_position += 1
      



        # Frame for buttons
        button_frame = Frame(self, bg="green")
        button_frame.pack(pady=20)


        # Buttons

        # Deal button(hides when clicked)
        deal_button = Button(button_frame, text="Deal Cards", font=("Raleway", 14))
        deal_button.configure(command=lambda:  [deal_cards(), hide_button(deal_button)])
        deal_button.grid(row=0,column=0)

        # Hit button
        hit_button = Button(button_frame, text="Hit", font=("Raleway", 14))
        hit_button.configure(command=lambda: hit())
        hit_button.grid(row=0,column=1,padx=22)

        # Stand Button
        stand_button = Button(button_frame, text="Stand", font=("Raleway", 14))
        stand_button.grid(row=0,column=2)



        