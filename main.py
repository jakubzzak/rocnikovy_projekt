# rocnikovy projekt, prvak, leto
# Jakub Zak
# 24.4

import random
import json
import tkinter
from tkinter import *
from my_pygame import Game


# --- main class ---
class Main:
    def __init__(self):
        # --- TK main window ---
        self.root = Tk()
        self.root.title("Space wars")
        self.root.geometry("500x500+300+200")
        self.background_image = tkinter.PhotoImage(file="vektor/hotove/bg/stars.png")
        self.background = Label(self.root, image=self.background_image)
        self.background.pack()
        # --- all image objects ---
        self.id = None
        self.attributes = {}
        self.current_ship = {}
        self.num = None
        # images
        self.ship_path = []
        self.ship_shop_path = []
        self.ship_current_path = []
        self.bg_current_path = []
        self.bg_path = []
        self.meteor_path = []

        for i in range(1, 5):
            self.ship_path.append(tkinter.PhotoImage(file=f"vektor/hotove/ships/garage/ship{i}.png"))
        for i in range(1, 5):
            self.ship_shop_path.append(tkinter.PhotoImage(file=f"vektor/hotove/ships/shop/ship{i}.png"))
        for i in range(1,5):
            self.ship_current_path.append(tkinter.PhotoImage(file=f"vektor/hotove/ships/spaceship{i}.png"))
        for i in range(1, 4):
            self.meteor_path.append(tkinter.PhotoImage(file=f"vektor/hotove/enemy/meteorit_{i}.png"))
        for i in range(1, 10):
            self.bg_path.append(tkinter.PhotoImage(file=f"vektor/hotove/bg/lvls/space__{i}.png"))
        for i in range(1, 10):
            self.bg_current_path.append(tkinter.PhotoImage(file=f"vektor/hotove/bg/space_{i}.png"))

        # --- initials ---
        self.info_label = None
        self.name_info = None
        self.home_b = None
        self.accounts_b = None
        self.new_player_b = None
        self.help_b = None
        self.exit_b = None
        self.switch_acc_b = None
        self.log_out_b = None
        self.garage_b = None
        self.shop_b = None
        self.levels_b = None
        self.fight_b = None
        self.back_b = None
        self.play_b = None
        self.choose_bc = None
        self.choose_b = None
        self.unlock_b = None
        self.unlock_l = None
        self.right_bc = None
        self.right_b = None
        self.left_b = None
        self.left_bc = None
        self.lock_b = None
        # --- start ---
        self.main_screen()
        self.root.mainloop()

    def main_screen(self):
        self.info_label = None
        self.name_info = None
        self.home_b = None

        def destroy():
            # --- clear screen ---
            self.new_player_b.destroy()
            self.accounts_b.destroy()
            self.help_b.destroy()
            self.exit_b.destroy()

        # --- sign in ---
        def sign_in():
            destroy()
            self.sign_in()

        # --- new player ---
        def register():
            destroy()
            self.register()

        # --- exit game ---
        def exit():
            self.root.destroy()

        # --- help section --- dokoncit
        def help():
            def back():
                # --- clear screen and call main ---
                message.destroy()
                back_b.destroy()
                self.main_screen()
            destroy()
            back_b = Button(self.root, text="Back", command=back, width=8, height=2)
            back_b.place(x=50, y=30, anchor=CENTER)
            message = Message(self.root,
            text="""
This is an old fashioned game created to bring some memories from your childhood.\n
Here are the game's instructions:
        Every time your want to load the game you have to sign in to\n        your account, if you do not have one, register first.
        Once you signed in/registered you are free to use all your money\n        to buy new ships and upgrade their gear.
        You can switch among ships and levels anytime, as long as they\n        are available for you.
        If you wish to play and earn some money, simply go to the\n        garage or the level room and press the 'play' button.
Earning money:
        For a regular meteor you get 5$, for an enemy ship 100$ and\n        there are also special meteors appearing occasionally.
The goal of the game:
        Get to the final level, where there is the main enemy ship waiting\n        for you. Destroy it and save the universe!\n
Usage of buttons:
        <LEFT>, <RIGHT> : control your ship and move it to sides
        <SPACE> : fire a shot, be careful, you can run out of them
        <R> : reload the magazine
        <ESC> : pause the game
    """, width=450)
            # message.place(anchor=W)
            message.place(x=20, y=275, anchor=W)

        if self.back_b:
            self.back_b.destroy()
        # --- main label ---
        self.info_label = Label(self.root, text=f'Welcome to SPACE WAR', width=30, fg="red")
        self.info_label.place(x=250, y=30, anchor=CENTER)
        # --- main buttons ---
        self.accounts_b = Button(self.root, text="Sign in", command=sign_in, width=10)
        self.new_player_b = Button(self.root, text="Register", command=register, width=10)
        self.help_b = Button(self.root, text="Help", command=help, width=10)
        self.exit_b = Button(self.root, text="Exit", command=exit, width=10)
        self.accounts_b.place(x=250, y=200, anchor=CENTER)
        self.new_player_b.place(x=250, y=230, anchor=CENTER)
        self.help_b.place(x=250, y=260, anchor=CENTER)
        self.exit_b.place(x=250, y=290, anchor=CENTER)
        # --- end of buttons section ---

    def update_player_information(self, main):
        if main:
            with open("playersInfo.json", "r") as file:
                data = json.load(file)
                for person in data["players"]:
                    if self.id == person["id"]:
                        self.attributes["id"] = person["id"]
                        self.attributes["level"] = person["level"]
                        self.attributes["ship"] = person["ship"]
                        self.attributes["coins"] = person["coins"]
                        self.attributes["current_ship"] = person["ship"]
                        self.attributes["current_level"] = person["level"]
                        self.attributes["kills"] = person["kills"]
        else:
            with open("playersInfo.json", "r") as file:
                data = json.load(file)
                for person in data["players"]:
                    if self.id == person["id"]:
                        for ship in person["ships"]:
                            if ship["num"] == self.num:
                                self.current_ship["speed"] = ship["speed"]
                                self.current_ship["shield"] = ship["shield"]
                                self.current_ship["guns"] = ship["guns"]
                                self.current_ship["loading"] = ship["loading"]
                                self.current_ship["magazine"] = ship["magazine"]

    def update_file(self, item, change, main):
        if main:
            with open("playersInfo.json", "r") as file:
                data = json.load(file)
                for person in data["players"]:
                    if self.id == person["id"]:
                        person[item] = change
        else:
            with open("playersInfo.json", "r") as file:
                data = json.load(file)
                for person in data["players"]:
                    if self.id == person["id"]:
                        for ship in person["ships"]:
                            if ship["num"] == self.num:
                                ship[item] = change

        with open("playersInfo.json", "w") as file:
            json.dump(data, file, indent=2)

    def getattr(self, attr, main):
        if main:
            with open("playersInfo.json", "r") as file:
                data = json.load(file)
                for person in data["players"]:
                    if person["id"] == self.id:
                        self.attributes[f"{attr}"] = person[f"{attr}"]
                        return self.attributes[f"{attr}"]
        else:
            with open("playersInfo.json", "r") as file:
                data = json.load(file)
                for person in data["players"]:
                    if person["id"] == self.id:
                        for ship in person["ships"]:
                            if self.num == ship["num"]:
                                return ship[f"{attr}"]

    def sign_in(self):
        # dopln okno ktore bud presmeruje hraca na register alebo ukonci hru

        with open("playersInfo.json", "r") as f:
            data = json.load(f)

        def back():
            # --- clear screen and call main ---
            name_entry.destroy()
            password_entry.destroy()
            submit.destroy()
            self.main_screen()

        def submit_info():

            def check_data(password):
                for info in data["players"]:
                    if self.name_info == info["name"]:
                        self.id = info["id"]
                        return password == info["password"]
                return False

            self.name_info = name_entry.get()
            password_info = password_entry.get()
            if check_data(password_info):
                self.update_player_information(True)
                self.update_player_information(False)
                name_entry.destroy()
                password_entry.destroy()
                submit.destroy()
                self.info_label.configure(text=f'Welcome back, {self.name_info}!')
                self.back_b.destroy()
                # print(self.id)
                self.account_screen()
            else:
                self.info_label.configure(text=f'Wrong name or password!')

        # --- create back button ---
        self.back_b = Button(self.root, text="Back", command=back, width=8, height=2)
        self.back_b.place(x=50, y=30, anchor=CENTER)
        # --- info label ---
        self.info_label.configure(text="Sign in")
        # --- enter name ---
        name_entry = Entry(self.root, font="Helvetica  11", width=17, fg="grey")
        name_entry.insert(0, "name")
        name_entry.select_range(0, END)
        name_entry.focus_set()
        name_entry.place(x=250, y=200, anchor=CENTER)
        # --- enter password ---
        password_entry = Entry(self.root, font="Helvetica 11", width=17, fg="gray")
        password_entry.insert(0, "password")
        password_entry.select_range(0, END)
        # passwordEntry.focus_set()
        password_entry.place(x=250, y=230, anchor=CENTER)
        # --- submit button ---
        submit = Button(self.root, text='Log in', command=submit_info)
        submit.place(x=250, y=260, anchor=CENTER)

        # --- new player section ---
    def register(self):

        with open("playersInfo.json", "r") as f:
            data = json.load(f)

        def back():
            # --- clear screen and call main_screen ---
            name_entry.destroy()
            password_entry.destroy()
            submit.destroy()
            self.main_screen()

        def submit_info():

            def save_new_player(password):
                value, ships = {}, []
                ships.append({"num": 1, "unlock": True, "speed": 5, "shield": 10, "guns": 1, "loading": 15, "magazine": 50})
                ships.append({"num": 2, "unlock": False, "speed": 6, "shield": 12, "guns": 1, "loading": 13, "magazine": 55})
                ships.append({"num": 3, "unlock": False, "speed": 7, "shield": 14, "guns": 1, "loading": 11, "magazine": 60})
                ships.append({"num": 4, "unlock": False, "speed": 8, "shield": 16, "guns": 1, "loading": 10, "magazine": 65})
                # --- reads JSON file to a variable ---
                with open("playersInfo.json", "r") as file:
                    data = json.load(file)
                # self.id = len(data["players"])
                value["id"] = len(data["players"])
                value["name"] = f"{self.name_info}"
                value["password"] = f"{password}"
                value["coins"] = 0
                value["kills"] = 0
                value["level"] = 1
                value["ship"] = 1
                value["ships"] = ships
                # --- add value to data ---
                data["players"].append(value)
                # --- add data back to file ---
                with open("playersInfo.json", "w") as file:
                    json.dump(data, file, indent=2)

            def check_data(password):
                for person in data["players"]:
                    if person["name"] == self.name_info:
                        self.info_label.configure(text=f'Name already used!')
                        return False
                if password != "password" and password != "":
                    return True
                self.info_label.configure(text=f'Incorrect format of password!')
                return False

            self.name_info = name_entry.get()
            password_info = password_entry.get()
            if check_data(password_info):
                self.update_player_information(True)
                self.update_player_information(False)
                name_entry.destroy()
                password_entry.destroy()
                submit.destroy()
                save_new_player(password_info)
                self.info_label.configure(text=f'Welcome {self.name_info}!')
                self.back_b.destroy()
                self.account_screen()

        # --- create back button ---
        self.back_b = Button(self.root, text="Back", command=back, width=8, height=2)
        self.back_b.place(x=50, y=30, anchor=CENTER)
        # --- info label ---
        self.info_label.configure(text="Register")
        # --- enter your name ---
        name_entry = Entry(self.root, font="Helvetica  11", width=17, fg="grey")
        name_entry.insert(0, "please, enter your name")
        name_entry.select_range(0, END)
        name_entry.focus_set()
        name_entry.place(x=250, y=200, anchor=CENTER)
        # --- enter password ---
        password_entry = Entry(self.root, font="Helvetica 11", width=17, fg="gray")
        password_entry.insert(0, "password")
        password_entry.select_range(0, END)
        # passwordEntry.focus_set()
        password_entry.place(x=250, y=230, anchor=CENTER)

        submit = Button(self.root, text='submit', command=submit_info)
        submit.place(x=250, y=260, anchor=CENTER)
        # --- end of name section ---

    def account_screen(self):
        self.choose_bc = None
        self.choose_b = None
        # print(self.attributes)

        def destroy_main():
            # --- clear screen ---
            garage_b.destroy()
            shop_b.destroy()
            levels_b.destroy()
            log_out_b.destroy()
            switch_acc_b.destroy()
            kills_label.destroy()
            money_label.destroy()

        # --- game sections ---
        def choose_level():
            destroy_main()

            def destroy_level():
                if self.getattr("kills", True) > 100:
                    if self.getattr("kills", True) < 1000:
                        self.update_file("level", self.getattr("kills", True) // 100, True)
                    else:
                        self.update_file("level", 9, True)
                if self.choose_bc:
                    self.choose_bc.destroy()
                if self.unlock_l:
                    self.unlock_l.destroy()
                if self.right_bc:
                    self.right_bc.destroy()
                if self.left_bc:
                    self.left_bc.destroy()
                bg_img.destroy()
                home_b.destroy()
                play_b.destroy()
                self.account_screen()

            def call_game():
                self.num = self.attributes["current_ship"]
                self.update_player_information(False)
                #print(self.num)
                Game(self.attributes, self.current_ship)

            def change():
                self.attributes["current_level"] = self.num
                self.choose_bc.destroy()
                self.choose_bc = None

            def move_l():
                self.num -= 1
                bg_img.configure(image=self.bg_path[self.num - 1])
                if self.num == self.attributes["current_level"]:
                    if self.choose_bc:
                        self.choose_bc.destroy()
                        self.choose_bc = None
                    else:
                        self.unlock_l.destroy()
                        self.unlock_l = None
                elif self.unlock_l:
                    if self.getattr("kills", True) < self.num * 100:
                        self.unlock_l.configure(text=f"requires {self.num * 100} kills")
                    else:
                        self.unlock_l.destroy()
                        self.unlock_l = None
                        self.choose_bc = Button(self.root, text="choose", command=change, width=8, height=2)
                        self.choose_bc.place(x=250, y=450, anchor=CENTER)
                elif not self.choose_bc:
                    self.choose_bc = Button(self.root, text="choose", command=change, width=8, height=2)
                    self.choose_bc.place(x=250, y=450, anchor=CENTER)

                if self.num == 1:
                    self.left_bc.destroy()
                elif self.num == 8:
                    self.right_bc = Button(self.root, text=">", command=move_r, width=4, height=2)
                    self.right_bc.place(x=460, y=250, anchor=CENTER)

            def move_r():
                self.num += 1
                bg_img.configure(image=self.bg_path[self.num - 1])
                if self.num == self.attributes["current_level"]:
                    self.choose_bc.destroy()
                    self.choose_bc = None
                elif self.choose_bc:
                    if self.getattr("kills", True) < self.num * 100:
                        self.choose_bc.destroy()
                        self.choose_bc = None
                        self.unlock_l = Label(self.root, text=f"requires {self.num * 100} kills", width=15, height=2)
                        self.unlock_l.place(x=250, y=250, anchor=CENTER)
                elif self.unlock_l:
                    self.unlock_l.configure(text=f"requires {self.num * 100} kills")
                else:
                    if self.getattr("kills", True) < self.num * 100:
                        self.unlock_l = Label(self.root, text=f"requires {self.num * 100} kills", width=15, height=2)
                        self.unlock_l.place(x=250, y=250, anchor=CENTER)
                    else:
                        self.choose_bc = Button(self.root, text="choose", command=change, width=8, height=2)
                        self.choose_bc.place(x=250, y=450, anchor=CENTER)

                if self.num == 9:
                    self.right_bc.destroy()
                elif self.num == 2:
                    self.left_bc = Button(self.root, text="<", command=move_l, width=4, height=2)
                    self.left_bc.place(x=40, y=250, anchor=CENTER)

            self.info_label.configure(text="Levels")
            home_b = Button(self.root, text="Home", command=destroy_level, width=8, height=2)
            home_b.place(x=50, y=30, anchor=CENTER)
            play_b = Button(self.root, text="Play", command=call_game, width=8, height=2)
            play_b.place(x=450, y=30, anchor=CENTER)
            self.num = self.attributes["current_level"]
            if self.num > 1:
                self.left_bc = Button(self.root, text="<", command=move_l, width=4, height=2)
                self.left_bc.place(x=40, y=250, anchor=CENTER)
            if self.num < 9:
                self.right_bc = Button(self.root, text=">", command=move_r, width=4, height=2)
                self.right_bc.place(x=460, y=250, anchor=CENTER)
            path = self.bg_path[self.num - 1]
            bg_img = Label(self.root, image=path)
            bg_img.place(x=250, y=250, anchor=CENTER)

        def shop():
            destroy_main()

            def destroy_shop():
                home_b.destroy()
                self.account_screen()
                spaceShipImg.destroy()
                imgPlace.destroy()
                money_label.destroy()
                if self.speed_label:
                    self.speed_label.destroy()
                    self.shield_label.destroy()
                    self.guns_label.destroy()
                    self.loading_label.destroy()
                    self.magazine_label.destroy()
                    self.speed_up.destroy()
                    self.shield_up.destroy()
                    self.guns_up.destroy()
                    self.loading_up.destroy()
                    self.magazine_up.destroy()
                else:
                    self.lock_b.destoy()
                if self.right_b:
                    self.right_b.destroy()
                if self.left_b:
                    self.left_b.destroy()

            def configure():
                spaceShipImg.configure(image=self.ship_shop_path[self.num - 1])
                if self.getattr('unlock', False):
                    if self.getattr("ship", True) >= self.num:
                        if self.getattr('speed', False) < 30:
                            self.speed_label.configure(text=f"speed : {self.getattr('speed', False)}")
                            self.speed_up.configure(text=f"upgrade for {self.getattr('speed', False) * 20} $", state=NORMAL)
                        else:
                            self.speed_label.configure(text=f"speed : {self.getattr('speed', False)}")
                            self.speed_up.configure(text="max", state=DISABLED)
                        if self.getattr('shield', False) < 50:
                            self.shield_label.configure(text=f"shield : {self.getattr('shield', False)}")
                            self.shield_up.configure(text=f"upgrade for {self.getattr('shield', False) * 20} $", state=NORMAL)
                        else:
                            self.shield_label.configure(text=f"shield : {self.getattr('shield', False)}")
                            self.shield_up.configure(text="max", state=DISABLED)
                        if self.getattr('guns', False) < 3:
                            #print(self.getattr("guns", False), 3)
                            self.guns_label.configure(text=f"guns : {self.getattr('guns', False)}")
                            self.guns_up.configure(text=f"upgrade for {self.getattr('guns', False) * 1000} $", state=NORMAL)
                        else:
                            self.guns_up.configure(text="max", state=DISABLED)
                            self.guns_label.configure(text=f"guns : {self.getattr('guns', False)}")
                        if self.getattr('loading', False) > 3:
                            self.loading_label.configure(text=f"reloading magazine time : {self.getattr('loading', False)}")
                            self.loading_up.configure(text=f"upgrade for {self.getattr('loading', False) * 20} $", state=NORMAL)
                        else:
                            self.loading_up.configure(text="max", state=DISABLED)
                            self.loading_label.configure(text=f"reloading magazine time : {self.getattr('loading', False)}")
                        if self.getattr('magazine', False) < 100:
                            self.magazine_label.configure(text=f"magazine capacity : {self.getattr('magazine', False)}")
                            self.magazine_up.configure(text=f"upgrade for {self.getattr('magazine', False) * 20} $", state=NORMAL)
                        else:
                            self.magazine_up.configure(text="max", state=DISABLED)
                            self.magazine_label.configure(text=f"magazine capacity : {self.getattr('magazine', False)}")
                    else:
                        self.speed_label = Label(self.root, text=f"speed : {self.getattr('speed', False)}", width=25)
                        self.shield_label = Label(self.root, text=f"shield : {self.getattr('shield', False)}", width=25)
                        self.guns_label = Label(self.root, text=f"guns : {self.getattr('guns', False)}", width=25)
                        self.loading_label = Label(self.root, text=f"reloading magazine time : {self.getattr('loading', False)}", width=25)
                        self.magazine_label = Label(self.root, text=f"magazine capacity : {self.getattr('magazine', False)}", width=25)
                        self.speed_label.place(x=150, y=200, anchor=CENTER)
                        self.shield_label.place(x=150, y=250, anchor=CENTER)
                        self.guns_label.place(x=150, y=300, anchor=CENTER)
                        self.loading_label.place(x=150, y=350, anchor=CENTER)
                        self.magazine_label.place(x=150, y=400, anchor=CENTER)
                        self.speed_up = Button(self.root, text=f"upgrade for {self.getattr('speed', False) * 20} $", command=upgrade_speed, width=18)
                        self.shield_up = Button(self.root, text=f"upgrade for {self.getattr('shield', False) * 20} $", command=upgrade_shield, width=18)
                        self.guns_up = Button(self.root, text=f"upgrade for {self.getattr('guns', False) * 1000} $", command=upgrade_guns, width=18)
                        self.loading_up = Button(self.root, text=f"upgrade for {self.getattr('loading', False) * 20} $", command=upgrade_loading, width=18)
                        self.magazine_up = Button(self.root, text=f"upgrade for {self.getattr('magazine', False) * 20} $", command=upgrade_magazine, width=18)
                        self.speed_up.place(x=400, y=200, anchor=CENTER)
                        self.shield_up.place(x=400, y=250, anchor=CENTER)
                        self.guns_up.place(x=400, y=300, anchor=CENTER)
                        self.loading_up.place(x=400, y=350, anchor=CENTER)
                        self.magazine_up.place(x=400, y=400, anchor=CENTER)
                else:
                    self.speed_label.destroy()
                    self.speed_label = None
                    self.shield_label.destroy()
                    self.guns_label.destroy()
                    self.loading_label.destroy()
                    self.magazine_label.destroy()
                    self.speed_up.destroy()
                    self.shield_up.destroy()
                    self.guns_up.destroy()
                    self.loading_up.destroy()
                    self.magazine_up.destroy()

            def move_l():
                self.num -= 1
                configure()
                if self.num == 1:
                    self.left_b.destroy()
                if self.num == self.getattr("ship", True) - 1:
                    self.right_b = Button(self.root, text=">", command=move_r, width=2, height=1)
                    self.right_b.place(x=330, y=100, anchor=CENTER)

            def move_r():
                self.num += 1
                configure()
                if self.num == self.getattr("ship", True):
                    self.right_b.destroy()
                if self.num == 2:
                    self.left_b = Button(self.root, text="<", command=move_l, width=2, height=1)
                    self.left_b.place(x=170, y=100, anchor=CENTER)

            self.info_label.configure(text="Shop")
            home_b = Button(self.root, text="Home", command=destroy_shop, width=8, height=2)
            home_b.place(x=50, y=30, anchor=CENTER)
            money_label = Label(self.root, text=f"{self.getattr('coins', True)} $", width=8, height=2)
            money_label.place(x=450, y=30, anchor=CENTER)
            self.num = self.attributes["current_ship"]
            if self.num > 1:
                self.left_b = Button(self.root, text="<", command=move_l, width=2, height=1)
                self.left_b.place(x=170, y=100, anchor=CENTER)
            if self.num < self.getattr("ship", True):
                self.right_b = Button(self.root, text=">", command=move_r, width=2, height=1)
                self.right_b.place(x=330, y=100, anchor=CENTER)
            imgplace = tkinter.PhotoImage(file=f"vektor/hotove/ships/shop/imgPlace.png")
            imgPlace = Label(self.root, image=imgplace)
            imgPlace.place(x=250, y=100, anchor=CENTER)
            path = self.ship_shop_path[self.num - 1]
            spaceShipImg = Label(self.root, image=path)
            spaceShipImg.place(x=250, y=100, anchor=CENTER)

            # --- upgrade section ---
            def upgrade(item, costs):
                if self.attributes["coins"] >= costs:
                    if item == "unlock":
                        self.update_file(item, True, False)
                    elif item == "loading":
                        self.update_file(item, self.getattr(item, False) - 1, False)
                    else:
                        self.update_file(item, self.getattr(item, False) + 1, False)
                    self.update_file("coins", self.attributes["coins"] - costs, True)
                    money_label.configure(text=f"{self.getattr('coins', True)} $")
                    self.update_player_information(True)
                    self.update_player_information(False)

            self.speed_label = Label(self.root, text=f"speed : {self.getattr('speed', False)}", width=25)
            self.shield_label = Label(self.root, text=f"shield : {self.getattr('shield', False)}", width=25)
            self.guns_label = Label(self.root, text=f"guns : {self.getattr('guns', False)}", width=25)
            self.loading_label = Label(self.root, text=f"reloading magazine time : {self.getattr('loading', False)}", width=25)
            self.magazine_label = Label(self.root, text=f"magazine capacity : {self.getattr('magazine', False)}", width=25)
            self.speed_label.place(x=150, y=200, anchor=CENTER)
            self.shield_label.place(x=150, y=250, anchor=CENTER)
            self.guns_label.place(x=150, y=300, anchor=CENTER)
            self.loading_label.place(x=150, y=350, anchor=CENTER)
            self.magazine_label.place(x=150, y=400, anchor=CENTER)

            def upgrade_speed():
                upgrade("speed", self.getattr('speed', False) * 20)
                self.speed_label.configure(text=f"speed : {self.getattr('speed', False)}")
                if self.getattr('speed', False) < 30:
                    self.speed_up.configure(text=f"upgrade for {self.getattr('speed', False) * 20} $")
                else:
                    self.speed_up.configure(text="max", state=DISABLED)

            def upgrade_shield():
                upgrade("shield", self.getattr('shield', False) * 20)
                self.shield_label.configure(text=f"shield : {self.getattr('shield', False)}")
                if self.getattr('shield', False) < 50:
                    self.shield_up.configure(text=f"upgrade for {self.getattr('shield', False) * 20} $")
                else:
                    self.shield_up.configure(text="max", state=DISABLED)

            def upgrade_guns():
                upgrade("guns", self.getattr('guns', False) * 1000)
                self.guns_label.configure(text=f"guns : {self.getattr('guns', False)}")
                if self.getattr('guns', False) < 3:
                    self.guns_up.configure(text=f"upgrade for {self.getattr('guns', False) * 1000} $")
                else:
                    self.guns_up.configure(text="max", state=DISABLED)

            def upgrade_loading():
                upgrade("loading", self.getattr('loading', False) * 20)
                self.loading_label.configure(text=f"reloading magazine time : {self.getattr('loading', False)}")
                if self.getattr('loading', False) > 3:
                    self.loading_up.configure(text=f"upgrade for {self.getattr('loading', False) * 20} $")
                else:
                    self.loading_up.configure(text="max", state=DISABLED)

            def upgrade_magazine():
                upgrade("magazine", self.getattr('magazine', False) * 20)
                self.magazine_label.configure(text=f"magazine capacity : {self.getattr('magazine', False)}")
                if self.getattr('magazine', False) < 100:
                    self.magazine_up.configure(text=f"upgrade for {self.getattr('magazine', False) * 20} $")
                else:
                    self.magazine_up.configure(text="max", state=DISABLED)

            self.speed_up = Button(self.root, text=f"upgrade for {self.getattr('speed', False) * 20} $", command=upgrade_speed, width=18)
            if self.getattr("speed", False) >= 30:
                self.speed_up.configure(text="max", state=DISABLED)
            self.shield_up = Button(self.root, text=f"upgrade for {self.getattr('shield', False) * 20} $", command=upgrade_shield, width=18)
            if self.getattr("shield", False) >= 50:
                self.shield_up.configure(text="max", state=DISABLED)
            self.guns_up = Button(self.root, text=f"upgrade for {self.getattr('guns', False) * 1000} $", command=upgrade_guns, width=18)
            if self.getattr("guns", False) >= 3:
                self.guns_up.configure(text="max", state=DISABLED)
            self.loading_up = Button(self.root, text=f"upgrade for {self.getattr('loading', False) * 20} $", command=upgrade_loading, width=18)
            if self.getattr("loading", False) <= 3:
                self.loading_up.configure(text="max", state=DISABLED)
            self.magazine_up = Button(self.root, text=f"upgrade for {self.getattr('magazine', False) * 20} $", command=upgrade_magazine, width=18)
            if self.getattr("magazine", False) >= 100:
                self.magazine_up.configure(text="max", state=DISABLED)
            self.speed_up.place(x=400, y=200, anchor=CENTER)
            self.shield_up.place(x=400, y=250, anchor=CENTER)
            self.guns_up.place(x=400, y=300, anchor=CENTER)
            self.loading_up.place(x=400, y=350, anchor=CENTER)
            self.magazine_up.place(x=400, y=400, anchor=CENTER)
            # --- end of upgrade section ---

        def garage():
            destroy_main()

            def destroy_garage():
                if self.choose_b:
                    self.choose_b.destroy()
                if self.unlock_b:
                    self.unlock_b.destroy()
                if self.right_b:
                    self.right_b.destroy()
                if self.left_b:
                    self.left_b.destroy()
                img_place.destroy()
                spaceShipImg.destroy()
                home_b.destroy()
                play_b.destroy()
                self.account_screen()

            def call_game():
                self.update_player_information(False)
                # print('g', self.num)
                Game(self.attributes, self.current_ship)

            def change():
                self.attributes["current_ship"] = self.num
                self.choose_b.destroy()
                self.choose_b = None

            def buy_new_ship():
                if self.getattr("coins", True) >= self.num * 1000:
                    self.update_file("coins", self.getattr("coins", True) - self.num * 1000, True)
                    self.update_file("ship", self.getattr("ship", True) + 1, True)
                    self.update_file("unlock", True, False)
                    self.update_player_information(True)
                    self.unlock_b.destroy()
                else:
                    self.info_label.configure(text="Not enough money!")

            def move_l():
                self.num -= 1
                spaceShipImg.configure(image=self.ship_path[self.num - 1])
                self.info_label.configure(text="Garage")

                if self.num == self.attributes["current_ship"]:
                    if self.choose_b:
                        self.choose_b.destroy()
                        self.choose_b = None
                    else:
                        self.unlock_b.destroy()
                        self.unlock_b = None
                elif self.unlock_b:
                    if not self.getattr("unlock", False):
                        self.unlock_b.configure(text=f"buy for {self.num * 1000} $")
                    else:
                        self.unlock_b.destroy()
                        self.unlock_b = None
                        self.choose_b = Button(self.root, text="choose", command=change, width=8, height=2)
                        self.choose_b.place(x=250, y=450, anchor=CENTER)
                elif not self.choose_b:
                    self.choose_b = Button(self.root, text="choose", command=change, width=8, height=2)
                    self.choose_b.place(x=250, y=450, anchor=CENTER)

                if self.num == 1:
                    self.left_b.destroy()
                elif self.num == 3:
                    self.right_b = Button(self.root, text=">", command=move_r, width=4, height=2)
                    self.right_b.place(x=460, y=250, anchor=CENTER)

            def move_r():
                self.num += 1
                spaceShipImg.configure(image=self.ship_path[self.num - 1])
                self.info_label.configure(text="Garage")

                if self.num == self.attributes["current_ship"]:
                    self.choose_b.destroy()
                    self.choose_b = None
                elif self.choose_b:
                    if not self.getattr("unlock", False):
                        self.choose_b.destroy()
                        self.choose_b = None
                        self.unlock_b = Button(self.root, text=f"buy for {self.num * 1000} $", command=buy_new_ship, width=15, height=2)
                        self.unlock_b.place(x=250, y=250, anchor=CENTER)
                elif self.unlock_b:
                    self.unlock_b.configure(text=f"buy for {self.num * 1000} $")
                else:
                    if not self.getattr("unlock", False):
                        self.unlock_b = Button(self.root, text=f"buy for {self.num * 1000} $", command=buy_new_ship, width=15, height=2)
                        self.unlock_b.place(x=250, y=250, anchor=CENTER)
                    else:
                        self.choose_b = Button(self.root, text="choose", command=change, width=8, height=2)
                        self.choose_b.place(x=250, y=450, anchor=CENTER)

                if self.num == 4:
                    self.right_b.destroy()
                elif self.num == 2:
                    self.left_b = Button(self.root, text="<", command=move_l, width=4, height=2)
                    self.left_b.place(x=40, y=250, anchor=CENTER)

            self.info_label.configure(text="Garage")
            home_b = Button(self.root, text="Home", command=destroy_garage, width=8, height=2)
            home_b.place(x=50, y=30, anchor=CENTER)
            play_b = Button(self.root, text="Play", command=call_game, width=8, height=2)
            play_b.place(x=450, y=30, anchor=CENTER)
            self.num = self.attributes["current_ship"]
            if self.num > 1:
                self.left_b = Button(self.root, text="<", command=move_l, width=4, height=2)
                self.left_b.place(x=40, y=250, anchor=CENTER)
            if self.num < 4:
                self.right_b = Button(self.root, text=">", command=move_r, width=4, height=2)
                self.right_b.place(x=460, y=250, anchor=CENTER)
            imgplace = tkinter.PhotoImage(file=f"vektor/hotove/ships/garage/imgPlace.png")
            img_place = Label(self.root, image=imgplace)
            img_place.place(x=250, y=250, anchor=CENTER)
            path = self.ship_path[self.num - 1]
            spaceShipImg = Label(self.root, image=path)
            spaceShipImg.place(x=250, y=250, anchor=CENTER)

        # --- settings ---
        def log_out():
            destroy_main()
            self.info_label.destroy()
            return self.main_screen()

        def switch_acc():
            destroy_main()
            return self.sign_in()

        self.info_label.configure(text=f"Signed as: {self.name_info}")

        money_label = Label(self.root, text=f"{self.getattr('coins', True)} $", width=10, fg="black")
        money_label.place(x=300, y=60, anchor=CENTER)
        kills_label = Label(self.root, text=f"{self.getattr('kills', True)} kills", width=10, fg="black")
        kills_label.place(x=200, y=60, anchor=CENTER)
        switch_acc_b = Button(self.root, text="switch\naccount", command=switch_acc, width=8, height=3)
        log_out_b = Button(self.root, text="log out", command=log_out, width=8, height=2)
        garage_b = Button(self.root, text="Garage", command=garage, width=13)
        shop_b = Button(self.root, text="Shop", command=shop, width=13)
        levels_b = Button(self.root, text="Levels", command=choose_level, width=13)

        switch_acc_b.place(x=450, y=30, anchor=CENTER)
        log_out_b.place(x=450, y=80, anchor=CENTER)
        garage_b.place(x=125, y=250, anchor=CENTER)
        shop_b.place(x=250, y=250, anchor=CENTER)
        levels_b.place(x=375, y=250, anchor=CENTER)


if __name__ == "__main__":
    Main()
