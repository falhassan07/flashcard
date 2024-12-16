import random
import pandas as pd 
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

#----------------------------------------------------------------#
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card, image=front_card_image)
    canvas.itemconfig(card_title, text="French",fill="black")
    french_word = current_card["French"]
    canvas.itemconfig(card_word, text=french_word,fill="black")
    flip_timer = window.after(3000, flip_card)




def flip_card():
    canvas.itemconfig(card, image=back_card_image)
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



#-----------------------UI SETUP------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, flip_card)

#CANVAS
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400,263,image=front_card_image)
card_title = canvas.create_text(400,150,font=("Ariel", 40, "italic"), fill='black')
card_word = canvas.create_text(400,263,font=("Ariel", 60, "bold"), fill='black')
canvas.grid(column=0, row=0, columnspan=2)



wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")


#BUTTONS
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
right_button = Button(image=right_image,highlightbackground=BACKGROUND_COLOR,command=is_known)

wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

#----------------------------------------------------------------#







next_card()

window.mainloop()