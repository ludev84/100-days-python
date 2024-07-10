from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    password = []
    num_letters = random.randint(8, 10)
    num_numbers = random.randint(2, 4)
    num_symbols = random.randint(2, 4)

    password += [random.choice(LETTERS) for _ in range(num_letters)]
    password += [random.choice(SYMBOLS) for _ in range(num_symbols)]
    password += [random.choice(NUMBERS) for _ in range(num_numbers)]

    random.shuffle(password)
    generated_password = ''.join(password)
    pyperclip.copy(generated_password)
    password_input.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Pleas make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\nEmail: {email} "
                                                      f"\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            try:
                with open("vault.json", "r") as data_file:
                    # Read old data
                    json_data = json.load(data_file)
            except FileNotFoundError:
                with open("vault.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Update old data with new data
                json_data.update(new_data)
                with open("vault.json", "w") as data_file:
                    # Save updated data
                    json.dump(json_data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

# ------------------------- SEARCH WEBSITE ---------------------------- #

def find_password():
    website = website_input.get().lower()
    try:
        with open("vault.json", "r") as data_file:
            json_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        new_data = {item.lower():key for (item, key) in json_data.items()}
        if website in new_data:
            website_data = new_data[website]
            messagebox.showinfo(title=website.title(), message=f"Email: {website_data["email"]}\n "
                                f"\nPassword: {website_data["password"]}")
        else:
            messagebox.showinfo(title="Error", message="Website Not Found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, sticky='EW')
website_input.focus()

website_search_btn = Button(text="Search", command=find_password)
website_search_btn.grid(column=2, row=1, sticky='EW')

email_lbl = Label(text="Email/Username:")
email_lbl.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.insert(0, "luis@email.com")
email_input.grid(column=1, row=2, columnspan=2, sticky='EW')

password_lbl = Label(text="Password:")
password_lbl.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky='EW')

generate_pwd_btn = Button(text="Generate Password", command=generate_password)
generate_pwd_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky='EW')

window.mainloop()
