from tkinter import *
from tkinter import ttk

# colors
color_1 = 'orange'
color_2 = 'gray'
color_3 = 'white'

root = Tk()

root.title("title test!!")
root.geometry('750x350')
root.configure(background=color_1)
root.resizable( width=FALSE, height=FALSE )

style = ttk.Style( root )

style.theme_use("clam")

# frames
frame_header = Frame( root, width='750', height='50', bg=color_1, relief="flat")
frame_header.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frame_menu = Frame( root, width='150', height='265', bg=color_2, relief="solid")
frame_menu.grid( row=1, column=0, sticky=NSEW )

frame_right = Frame( root, width='650', height='265', bg=color_3, relief="raised")
frame_right.grid( row=1, column=1, sticky=NSEW )

root.mainloop()
