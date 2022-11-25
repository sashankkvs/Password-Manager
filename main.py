# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox

from random import randint,shuffle,choice
import pyperclip
import json
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]

    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    entry_3.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    input_1 = entry_1.get()
    input_2 = entry_2.get()
    input_3 = entry_3.get()
    new_data = {input_1:{
        "Email" : input_2,
        "Password" : input_3
    }}

    if len(input_1) == 0 or len(input_3) == 0:
        messagebox.showwarning(message="Please dont leave any fields empty")
    else :
        is_ok = messagebox.askokcancel(title=input_1,
                                       message=f"These are the details entered \nEmail : {input_2} \nPassword : {input_3} \nIs it ok to save?")
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data,data_file, indent=4)
        finally:

            entry_1.delete(0, END)
            entry_3.delete(0, END)

def search_website():
    website = entry_1.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="Data file doesnt exist")
    except KeyError:
        messagebox.showwarning(message="Data not found")
    else:

        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website,message=f"Email : {email} \nPassword : {password}")
        elif len(website)==0:
            messagebox.showinfo(message="Please dont leave any fields empty")
        else:
            messagebox.showinfo(message=f"Data for {website} doesnt exist ")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50, bg=GREEN)


canvas = Canvas(width=200, height=200,highlightthickness=0,bg=GREEN)
my_pass = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = my_pass)
canvas.grid(column=1,row=0)

web_label = Label(text="Website:", font=("Arial", 10, "normal"),highlightthickness=0,bg=GREEN)
web_label.grid(column=0,row=1)

email_label = Label(text="Email/Username:", font=("Arial", 10, "normal"),highlightthickness=0,bg=GREEN)
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:", font=("Arial", 10, "normal"),highlightthickness=0,bg=GREEN)
pass_label.grid(column=0, row=3)

entry_1 = Entry(width=21)
entry_1.grid(row=1,column=1,columnspan=1, sticky="EW")
entry_1.focus()

entry_2  = Entry(width = 35)
entry_2.grid(row=2,column=1,columnspan=2,sticky="EW")
entry_2.insert(0, "sashankkvs99@gmail.com")

entry_3 = Entry(width=21)
entry_3.grid(column=1,row=3,sticky="EW")


generate_button = Button(text = "Generate Password", command=password_gen)
generate_button.grid(column=2,row=3,sticky="EW")

add_button =Button(text="Add", width=36, command = save)
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")

search_button = Button(text="Search", width=15,command=search_website, activebackground=YELLOW)
search_button.grid(row=1,column=2)




window.mainloop()
