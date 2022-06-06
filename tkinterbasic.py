# import the tkinter module
# create the main application window.
# add the widgets like labels, buttons,frames, etc. to the window.
# call  the main event loop so that the actions can take place on the user's computer.

# from tkinter import *
# import tkinter
# top = Tk()
# top.title("my window")
# top.geometry("500x600")
# # top.min()
# # Entering the event main loop
# top.mainloop()

# ------------------------------------------------------------------

# Tkinter canvas script 1
"""import tkinter

top = tkinter.Tk()

c = tkinter.Canvas(top,bg="blue",height=250,width=300)

coord = 1,5,240,210

arc = c.create_arc(coord,start=0,extent=200,fill="red")

# rectangle = c.create_rectangle(coord,fill="red")
c.pack()
top.mainloop()"""

"""from tkinter import *
import tkinter

top = tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()
top.mainloop()"""