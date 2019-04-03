# --- toto je hlavna cast programu ---
# --- import ---
import random
import json
import tkinter
from tkinter import *


# --- main class ---
class Jadro:

    def __init__(self):
        # --- CANVAS ---
        self.root = Tk()
        self.root.title("Name of the game")
        self.root.geometry("500x500+1000+200")
        background_image=tkinter.PhotoImage(file="pic/nebula/stars.png")
        background = Label(self.root, image=background_image).pack()
        # --- start ---
        self.back_b = None
        self.main_screen()
        # --- finish ---
        self.root.mainloop()

    def main_screen(self):
        self.infoLabel = None
        self.nameInfo = None
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
            ...

        if self.back_b:
            self.back_b.destroy()
        # --- main label ---
        self.infoLabel = Label(self.root, text=f'Welcome to SPACE WAR', width=30, fg="red")
        self.infoLabel.place(x=250, y=30, anchor=CENTER)
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

    def sign_in(self):

        with open("playersInfo.json", "r") as f:
            data = json.load(f)

        def back():
            # --- clear screen and call mainscreen ---
            nameEntry.destroy()
            passwordEntry.destroy()
            submit.destroy()
            self.main_screen()

        def submit_info():

            def checkData(password):
                for info in data["players"]:
                    if self.nameInfo == info["name"]:
                        return password == info["password"]
                return False

            self.nameInfo = nameEntry.get()
            passwordInfo = passwordEntry.get()
            if checkData(passwordInfo):
                nameEntry.destroy()
                passwordEntry.destroy()
                submit.destroy()
                self.infoLabel.configure(text=f'Welcome back, {self.nameInfo}!')
                self.back_b.destroy()
                self.account_screen()
            else:
                self.infoLabel.configure(text=f'Wrong name or password!')

        # --- vyrob back button ---
        self.back_b = Button(self.root, text="Back", command=back, width=8, height=2)
        self.back_b.place(x=50, y=30, anchor=CENTER)
        # --- info label ---
        self.infoLabel.configure(text="Sign in")
        # --- enter name ---
        nameEntry = Entry(self.root, font="Helvetica  11", width=17, fg="grey")
        nameEntry.insert(0, "name")
        nameEntry.select_range(0, END)
        nameEntry.focus_set()
        nameEntry.place(x=250, y=200, anchor=CENTER)
        # --- enter password ---
        passwordEntry = Entry(self.root, font="Helvetica 11", width=17, fg="gray")
        passwordEntry.insert(0, "password")
        passwordEntry.select_range(0, END)
        #passwordEntry.focus_set()
        passwordEntry.place(x=250, y=230, anchor=CENTER)
        # --- submit button ---
        submit = Button(self.root, text='Log in', command=submit_info)
        submit.place(x=250, y=260, anchor=CENTER)

        # --- new player section ---
    def register(self):

        def back():
            # --- clear screen and call main_screen ---
            nameEntry.destroy()
            passwordEntry.destroy()
            submit.destroy()
            self.main_screen()

        def submit_info():

            def zapis(password):
                value = {}
                value["name"] = f"{self.nameInfo}"
                value["password"] = f"{password}"
                value["level"] = f"0"

                # --- nacita JSON subor do premennej data ---
                with open("playersInfo.json", "r") as file:
                    data = json.load(file)
                # --- pridam value do data ---
                data["players"].append(value)
                # --- vlozim data naspat do suboru
                with open("playersInfo.json", "w") as file:
                    json.dump(data, file, indent=2)

            def checkData(password):
                if password != "password" and password != "":
                    return True
                return False

            self.nameInfo = nameEntry.get()
            passwordInfo = passwordEntry.get()
            if checkData(passwordInfo):
                nameEntry.destroy()
                passwordEntry.destroy()
                submit.destroy()
                zapis(passwordInfo)
                self.infoLabel.configure(text=f'Welcome {self.nameInfo}!')
                self.back_b.destroy()
                self.account_screen()
            else:
                self.infoLabel.configure(text=f'Password missing!')

        # --- vyrob back button ---
        self.back_b = Button(self.root, text="Back", command=back, width=8, height=2)
        self.back_b.place(x=50, y=30, anchor=CENTER)
        # --- info label ---
        self.infoLabel.configure(text="Register")
        # --- zadaj meno ---
        nameEntry = Entry(self.root, font="Helvetica  11", width=17, fg="grey")
        nameEntry.insert(0, "please, enter your name")
        nameEntry.select_range(0, END)
        nameEntry.focus_set()
        nameEntry.place(x=250, y=200, anchor=CENTER)
        # --- zadaj heslo ---
        passwordEntry = Entry(self.root, font="Helvetica 11", width=17, fg="gray")
        passwordEntry.insert(0, "password")
        passwordEntry.select_range(0, END)
        #passwordEntry.focus_set()
        passwordEntry.place(x=250, y=230, anchor=CENTER)

        submit = Button(self.root, text='submit', command=submit_info)
        submit.place(x=250, y=260, anchor=CENTER)
        # --- koniec sekcie mena ---

    def account_screen(self):

        def destroy():
            # --- clear screen ---
            self.garage_b.destroy()
            self.shop_b.destroy()
            self.levels_b.destroy()
            self.log_out_b.destroy()
            self.switch_acc_b.destroy()
            # --- vyrob home button ---
            self.home_b = Button(self.root, text="Home", command=self.account_screen, width=8, height=2)
            self.home_b.place(x=50, y=30, anchor=CENTER)

        # --- game sections ---
        def choose_level():
            destroy()
            self.infoLabel.configure(text="Levels")
            scroll = Scrollbar(self.root, bg="red")
            scroll.place(fill=Y, side=RIGHT)
            level_box = Listbox(self.root, yscrollcommand=scroll.set)
            for i in range(1, 11):
                button = Button(self.root, text=f"level {i}.")
            level_box.place(side=LEFT)
            scroll.config(command=level_box.yview)

        def shop():
            destroy()
            self.infoLabel.configure(text="Shop")

        def garage():
            destroy()
            self.infoLabel.configure(text="Garage")

        # --- settings ---
        def log_out():
            destroy()
            self.home_b.destroy()
            self.infoLabel.destroy()
            return self.main_screen()

        def switch_acc():
            destroy()
            self.home_b.destroy()
            self.sign_in()
            ...

        if self.home_b:
            self.home_b.destroy()
            self.infoLabel.configure(text=f"Signed as: {self.nameInfo}")
        self.switch_acc_b = Button(self.root, text="switch\naccount", command=switch_acc, width=8, height=3)
        self.log_out_b = Button(self.root, text="log out", command=log_out, width=8, height=2)
        self.garage_b = Button(self.root, text="Garage", command=garage, width=13)
        self.shop_b = Button(self.root, text="Shop", command=shop, width=13)
        self.levels_b = Button(self.root, text="Levels", command=choose_level, width=13)
        self.switch_acc_b.place(x=450, y=30, anchor=CENTER)
        self.log_out_b.place(x=450, y=80, anchor=CENTER)
        self.garage_b.place(x=125, y=250, anchor=CENTER)
        self.shop_b.place(x=250, y=250, anchor=CENTER)
        self.levels_b.place(x=375, y=250, anchor=CENTER)










if __name__ == "__main__":
    Jadro()
