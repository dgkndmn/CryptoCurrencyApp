import tkinter.ttk
from tkinter import *
from tkinter import messagebox

import requests
from PIL import Image, ImageTk

# where did i get the data from: https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json
#UI
window = Tk()
window.geometry("350x300")
window.title("Crypto List")
window.resizable(width=False,height=False)
image_path = "bitcoinicon.png"
new_width = 200
new_height = 100

def resize_image(image_path, new_width, new_height):
    img_pil = Image.open(image_path)
    img_resized = img_pil.resize((new_width, new_height), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_resized)
    return img_tk

resized_image = resize_image(image_path, new_width, new_height)
label = Label(image=resized_image)
label.pack(anchor="center")
font=["Ariel",12,"normal"]

combobox = tkinter.ttk.Combobox(window, font=font)
combobox.config(width=13)
combobox.place(x=20,y=125)
combobox.set("Select a currency")

entry = Entry(width=16,font=font)
entry.insert(0,"Price: ")
entry.config(state="readonly")
entry.place(y=123,x=177)


#functionality and buttons
response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
def get_data():
    return response.json()

crypto = get_data()
currencies = []
for currency in crypto:
    combobox['values'] = (*combobox['values'], currency["currency"])
    currencies.append(currency["currency"])

def search_button():
    selected_currency = combobox.get()
    if(selected_currency not in currencies):
        messagebox.showwarning(title="Error!",message="Sorry, there is no such a currency in the list.")
        clear_button()
    else:
        for currency in crypto:
            if currency["currency"] == selected_currency:
                entry_var.set(f"Price: {currency['price']}")

def clear_button():
    entry_var.set("Price: ")
    entry.config(state="readonly")
    combobox.set("")

entry_var = StringVar()
entry = Entry(width=16, font=font, textvariable=entry_var)
entry.insert(0, "Price: ")
entry.config(state="readonly")
entry.place(y=123, x=177)

button1 = Button(text="Search",font=font,width=8,height=1,command=search_button)
button1.place(x=125,y=165)

button2 = Button(text="Clear",font=font,width=8,height=1,command=clear_button)
button2.place(x=125,y=200)

window.mainloop()
