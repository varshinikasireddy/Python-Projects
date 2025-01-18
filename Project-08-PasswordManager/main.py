from tkinter import *
from tkinter import messagebox#predefined pop ups
from random import choice, randint, shuffle
import pyperclip #enables to copy to clipboard automatically
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'
     , 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    p_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = w_entry.get()
    email = e_entry.get()
    password = p_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Reading old data
        except FileNotFoundError:
            # If the file doesn't exist, initialize it with the new data
            data = {}
        except json.JSONDecodeError:
            # If the file exists but is empty or contains invalid JSON, reinitialize
            data = {}
        
        data.update(new_data)  # Updating with new data

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)  # Saving updated data

        w_entry.delete(0, END)  # Clears the text
        p_entry.delete(0, END)


def find_password():
    website = w_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

w_label=Label(text="Website")
w_label.grid(row=1,column=0)
e_lable=Label(text="Email/Username")
e_lable.grid(row=2,column=0)
p_lable=Label(text="Password")
p_lable.grid(row=3,column=0)

w_entry=Entry(width=33)
w_entry.focus()#focus() is to keep cursor default
w_entry.grid(row=1,column=1)#columnspan is to spread the column(in this case it occupies 2 colmns)
e_entry=Entry(width=53)
e_entry.grid(row=2,column=1,columnspan=2)
e_entry.insert(0,"varshinikasireddy29@gamil.com")#allows to display the text default at starting index
p_entry=Entry(width=33)
p_entry.grid(row=3,column=1,padx=0)

search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(row=1, column=2)
p_button=Button(text="Generate Password",width=16,command=generate_password)
p_button.grid(row=3,column=2,padx=0)
add_button=Button(text="Add",width=45,command=save)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
