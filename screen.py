from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# colors
color_1 = 'orange'
color_2 = 'gray'
color_3 = 'white'
color_4 = 'black'

root = Tk()

root.title("title test!!")
root.geometry('750x350')
root.configure(background=color_1)
root.resizable( width=FALSE, height=FALSE )

style = ttk.Style( root )

style.theme_use("clam")

# frames
frame_header = Frame( root, width='750', height='50', bg=color_3, relief="flat")
frame_header.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frame_menu = Frame( root, width='150', height='265', bg=color_2, relief="solid")
frame_menu.grid( row=1, column=0, sticky=NSEW )

frame_right = Frame( root, width='600', height='265', bg=color_3, relief="raised")
frame_right.grid( row=1, column=1, sticky=NSEW )

# logo header
logo ='icons8-book-40.png'
# logo_header = logo_header.resize( ( 40, 40 ) )
logo_img = ImageTk.PhotoImage( Image.open( logo ) )

logo_header = Label( frame_header, image=logo_img, width=1000, padx=5, anchor=NW, bg=color_3, fg=color_4)
logo_header.place( x=5, y=0 )

header_title = Label( frame_header, text="title", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=color_3, fg=color_4 )
header_title.place( x=50, y=7 )

root.mainloop()
