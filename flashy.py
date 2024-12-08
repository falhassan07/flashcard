from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#-----------------------UI SETUP------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#CANVAS
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = PhotoImage(file="images/card_front.png")
card_front = canvas.create_image(400,263,image=card_image)
canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"), fill='black')
canvas.create_text(400,263, text="Word", font=("Ariel", 60, "bold"), fill='black')
canvas.grid(column=0, row=0, columnspan=2)



#BUTTON IMAGES
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")


#BUTTONS
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR)
right_button = Button(image=right_image,highlightbackground=BACKGROUND_COLOR)

wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)










window.mainloop()