import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


root = tk.Tk()
root.title("Word Predictor")

canvas = tk.Canvas(root, width=600, height=500, background='#FFDE59')
canvas.grid(columnspan=3, rowspan=7)

#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, background='#FFDE59')
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Type the required text to predict the next word..", font="Helvetica", background='#FFDE59')
instructions.grid(columnspan=3, column=0, row=1)

#textbox
usrinp=tk.Entry(root)
usrinp.grid(columnspan=5, row=2, rowspan=1)

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Predict")
browse_btn.grid(column=1, row=3)

#label
# output = tk.Label(root, "Checking")
# output.grid

#titlebar ico
ico = Image.open('ico.png')
ico = ImageTk.PhotoImage(ico)
root.iconphoto(False, ico)

root.resizable(False, False)
root.mainloop()
