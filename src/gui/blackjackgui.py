import os
import sys
import time
import tkinter as tk
from tkinter import *
import pygame

from entities.deck import Deck
from entities.handchecker import HandChecker
from PIL import Image, ImageTk


class BlackjackGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Change working directory to src
        os.chdir(sys.path[0])

        # Absolute path to the card images and sounds
        cardspath = os.path.abspath("gui/cards")
        soundpath = os.path.abspath("gui/sounds")

        self.handchecker = HandChecker()

        d_hand = []
        p_hand = []

        # Player money at start
        self.money = 500


        # Title and root
        self.title('Blackjack')
        self.geometry('1200x800')
        self.configure(background="green")

        pygame.mixer.init()

        temp_frame = Frame(self, bg="green")
        temp_frame.pack(pady=20)


        # Card frames
        house_frame = LabelFrame(temp_frame, text="House", bd=0)
        house_frame.grid(row=0, column=0, ipadx=20)

        player_frame = LabelFrame(temp_frame, text="Player", bd=0)
        player_frame.grid(row=1, column=0, pady=20, ipadx=20)

        money_frame = Frame(temp_frame, bd=0)
        money_frame.grid(row=4, column=0, pady=20, ipadx=20)

        money_label = Label(money_frame, text=self.money)
        money_label.grid(row=0,column=0)


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

        house_label_6 = Label(house_frame, text='')
        house_label_6.grid(row=0,column=5)

        house_label_7 = Label(house_frame, text='')
        house_label_7.grid(row=0,column=6)

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
        player_label_6.grid(row=0,column=5)

        player_label_7 = Label(player_frame, text='')
        player_label_7.grid(row=0,column=6)


        # Resize function for cards
        def resize_card(card):


            card_image = Image.open(card)

            resized_card = card_image.resize((150,218))
            global card_image_tk
            card_image_tk = ImageTk.PhotoImage(resized_card)

            return card_image_tk


        def hide_deal_button():
            deal_button.grid_forget()

        def show_deal_button():
            deal_button.grid(row=0,column=0)

        def show_hit_button():
            hit_button.grid(row=0,column=1,padx=22)

        def hide_hit_button():
            hit_button.grid_forget()

        def show_stand_button():
            stand_button.grid(row=0,column=2)

        def hide_stand_button():
            stand_button.grid_forget()


        # Deal cards function
        def deal_cards():

            hide_deal_button()
            show_hit_button()
            show_stand_button()

            take_money(50)

            deal_cards_sound()

            # Clear hands
            self.deck = Deck()
            p_hand.clear()
            d_hand.clear()

            # Card position resets on deal_cards function
            global d_card_position, p_card_position
            self.d_card_position = 0
            self.p_card_position = 0

            # Clear all cards
            house_label_1.config(image="")
            house_label_2.config(image="")
            house_label_3.config(image="")
            house_label_4.config(image="")
            house_label_5.config(image="")
            house_label_6.config(image="")
            house_label_7.config(image="")

            player_label_1.config(image="")
            player_label_2.config(image="")
            player_label_3.config(image="")
            player_label_4.config(image="")
            player_label_5.config(image="")
            player_label_6.config(image="")
            player_label_7.config(image="")

            # Dealers first and hidden "hole" card
            global hidden_card
            hidden_card = self.deck.deal_cards(d_hand)

            # Saving the hidden "hole" card image for later reveal
            global hidden_card_image
            hidden_card_image = resize_card(f'{cardspath}/{hidden_card}.png')

            # Cardback image
            global cardback_image
            cardback_image = resize_card(f'{cardspath}/cardback.png')
            house_label_1.config(image=cardback_image)

            # Dealers second card
            house_second_card = self.deck.deal_cards(d_hand)

            global house_image_2nd
            house_image_2nd = resize_card(f'{cardspath}/{house_second_card}.png')
            house_label_2.config(image=house_image_2nd)

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

            if self.handchecker.hand_total(p_hand) == 21:
                sleep()
                blackjack()



        def hit():

            if self.p_card_position <= 4:

                try:
                    p_card = self.deck.deal_cards(p_hand)

                    hit_sound()

                    global player_image1, player_image2, player_image3, player_image4, player_image5

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

                    elif self.p_card_position == 4:
                        player_image5 = resize_card(f'{cardspath}/{p_card}.png')
                        player_label_7.config(image=player_image5)

                    self.p_card_position += 1

                    # Checks if hand busts, then switches any aces to ones
                    if self.handchecker.bust_hand(self.handchecker.hand_total(p_hand)):

                        self.handchecker.switch_aces(p_hand)

                        if self.handchecker.bust_hand(self.handchecker.hand_total(p_hand)):
                            bust()

                        elif self.handchecker.hand_total(p_hand) == 21:
                            player_hits_21()

                    elif self.handchecker.hand_total(p_hand) == 21:
                        player_hits_21()


                except:
                    limit()


        def stand():

            hide_hit_button()
            hide_stand_button()

            dealer_hit()




        def dealer_hit():
            # Reveal the "hole card"
            house_label_1.config(image=hidden_card_image)
            # Slows dealer down a bit
            sleep()

            if self.handchecker.hand_total(d_hand) == 21:
                standoff()
            elif self.handchecker.hand_total(d_hand) >= 17:
                standoff()
            else:

                while self.handchecker.hand_total(d_hand) < 17:


                    if self.d_card_position <= 4:

                        try:
                            d_card = self.deck.deal_cards(d_hand)

                            global house_image1, house_image2, house_image3, house_image4, house_image5

                            if self.d_card_position == 0:
                                house_image1 = resize_card(f'{cardspath}/{d_card}.png')
                                house_label_3.config(image=house_image1)

                            elif self.d_card_position == 1:
                                house_image2 = resize_card(f'{cardspath}/{d_card}.png')
                                house_label_4.config(image=house_image2)

                            elif self.d_card_position == 2:
                                house_image3 = resize_card(f'{cardspath}/{d_card}.png')
                                house_label_5.config(image=house_image3)

                            elif self.d_card_position == 3:
                                house_image4 = resize_card(f'{cardspath}/{d_card}.png')
                                house_label_6.config(image=house_image4)

                            elif self.d_card_position == 4:
                                house_image5 = resize_card(f'{cardspath}/{d_card}.png')
                                house_label_7.config(image=house_image5)

                            self.d_card_position += 1


                            if self.handchecker.bust_hand(self.handchecker.hand_total(d_hand)):

                                self.handchecker.switch_aces(d_hand)

                                if self.handchecker.bust_hand(self.handchecker.hand_total(d_hand)):
                                        house_bust()

                            elif self.handchecker.hand_total(d_hand) == 21:
                                lose()
                            else:
                                standoff()


                        except:
                            limit()


        def bust():
            # Reveal the "hole card"
            house_label_1.config(image=hidden_card_image)
            print("Bust!")
            lose()


        def player_hits_21():
            dealer_hit()


        def blackjack():
            # Reveal the "hole card"
            house_label_1.config(image=hidden_card_image)

            if self.handchecker.hand_total(d_hand) != 21:
                print("Blackjack!")
                win()
            else:
                push()


        def standoff():
            if self.handchecker.hand_total(p_hand) == self.handchecker.hand_total(d_hand):
                push()
            elif self.handchecker.hand_total(p_hand) > self.handchecker.hand_total(d_hand):
                print("You have better hand")
                win()
            else:
                print("Dealer has better hand")
                lose()


        def house_bust():
            print("House busts!")
            win()


        def push():
            print("Push")
            print("It's a tie!")
            hide_hit_button()
            hide_stand_button()
            show_deal_button()


        def win():
            print("You Win!")
            give_money(100)
            win_sound()
            hide_hit_button()
            hide_stand_button()
            show_deal_button()


        def lose():
            print("You Lose")
            lose_sound()
            hide_hit_button()
            hide_stand_button()
            show_deal_button()


        def limit():
            print("Limit!")
            print("Reset")
            hide_hit_button()
            hide_stand_button()
            show_deal_button()



        def take_money(amount):
            self.money = self.money - amount
            money_label.config(text=self.money)

        def give_money(amount):
            self.money = self.money + amount
            money_label.config(text=self.money)


        def sleep():
            time.sleep(0.4)

        def deal_cards_sound():
            pygame.mixer.music.load(soundpath + "/" + "deal-cards.mp3")
            pygame.mixer.music.play(loops=3)

        def hit_sound():
            pygame.mixer.music.load(soundpath + "/" + "hit.mp3")
            pygame.mixer.music.play(loops=0)

        def win_sound():
            pygame.mixer.music.load(soundpath + "/" + "win.mp3")
            pygame.mixer.music.play(loops=0)

        def lose_sound():
            pygame.mixer.music.load(soundpath + "/" + "lose.mp3")
            pygame.mixer.music.play(loops=0)

        # Frame for buttons
        button_frame = Frame(self, bg="green")
        button_frame.pack(pady=20)


        # Buttons

        # Deal button(hides when clicked)
        deal_button = Button(button_frame, text="Deal Cards", font=("Raleway", 14))
        deal_button.configure(command=deal_cards)
        deal_button.grid(row=0,column=0)

        # Hit button
        hit_button = Button(button_frame, text="Hit", font=("Raleway", 14))
        hit_button.configure(command=hit)

        # Stand Button
        stand_button = Button(button_frame, text="Stand", font=("Raleway", 14))
        stand_button.configure(command=stand)





