import random
import pandas as pd 
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#----------------------------------------------------------------#
data = pd.read_csv("data/french_words.csv")
# df_dict = {row.French: row.English for (index, row) in data.iterrows()}
df_dict = data.to_dict(orient='records')
def next_card():
    current_card = random.choice(df_dict)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french_word)


#-----------------------UI SETUP------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#CANVAS
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = PhotoImage(file="images/card_front.png")
card_front = canvas.create_image(400,263,image=card_image)
card_title = canvas.create_text(400,150,font=("Ariel", 40, "italic"), fill='black')
card_word = canvas.create_text(400,263,font=("Ariel", 60, "bold"), fill='black')
canvas.grid(column=0, row=0, columnspan=2)



wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")


#BUTTONS
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
right_button = Button(image=right_image,highlightbackground=BACKGROUND_COLOR,command=next_card)

wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)




next_card()

window.mainloop()