from tkinter import *

# Window creation, root of the interface
window = Tk()

# Creation of a label (text line) that says Hello World ! and with as first parameter the previous window
label_field = Label(window,text="Hello World !")

# Display of the label
label_field.pack()

# Running of the Tkinter loop that ends when we close the windw
window.mainloop()
