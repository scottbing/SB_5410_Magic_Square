# BSSD 5410 Final - Question #1
# Scott Bing
# Stenography

from tkinter import *
from make_square import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageTk, ImageOps, ImageEnhance, ImageFont
from pandas import *  # use pandas DataFrame
import os


class Application(Frame):
    """ GUI application that displays the image processing
        selections"""

    def __init__(self, master):
        """ Initialize Frame - application constructor"""
        super(Application, self).__init__(master)

        Frame.__init__(self, master)
        self.master = master

        # set filename as global
        self.fileName = None

        self.grid()
        # open the application frame
        self.create_widgets()
        # self.create_initial_screen()
    # end application constructor

    def openFile(self):
        """Process the Open File Menu"""
        # reset the screen
        self.resetScreen()

        self.fileName = askopenfilename(parent=self,
                                        initialdir=os.getcwd(),
                                        filetypes=[("PNG files", ".png .PNG")],
                                        title='Choose an image.')
        #print("fileName = ", self.fileName)
    # end def openFile(self):

    def resetScreen(self):
        """Clears the screen. Sets the screen
        back to its defaults"""
        # clear the message
        self.msg2show.set('')
        self.msg_ent.delete(0, 'end')

        # reset radio buttons
        self.encode.deselect()
        self.decode.deselect()
        self.encode.select()

    # end def clearScreen(self):

    def create_widgets(self):
        """ Create and place screen widgets in the
        main application frame"""
        self.lblFont = font.Font(weight="bold")
        self.lblFont = font.Font(size=20)

        Label(self,
              text="The Magic Square",
              wraplength=300,
              font=self.lblFont
              ).grid(row=0, column=0, columnspan=3, sticky=NSEW)

        animFont = font.Font(weight="bold")
        animFont = font.Font(size=21)

        Label(self,
              text="Height and Width of Square:",
              ).grid(row=1, column=0, padx=5, sticky=W)

        self.dimensions = IntVar()
        self.dimensions.set(5)
        self.dim = Spinbox(self,
                                   from_=1,
                                   to=8,
                                   width=3,
                                   textvariable=self.dimensions
                                   ).grid(row=1, column=0, padx=187, sticky=W)

        Label(self,
              text="Stop the Count At:",
              ).grid(row=2, column=0, padx=5, sticky=W)

        self.stopat = IntVar()
        self.stopat.set(15)
        self.stopat_count = Spinbox(self,
                           from_=1,
                           to=20,
                           width=3,
                           textvariable=self.stopat
                           ).grid(row=2, column=0, padx=187, sticky=W)

        Label(self,
              text="Select Starting Point of Square"
              ).grid(row=3, column=0, columnspan=2, padx=5, sticky=W)

        self.orientValue = tk.StringVar()
        self.top_left = tk.Radiobutton(self, text='Top Left',
                                     variable=self.orientValue, value='TL')
        self.top_left.select()
        self.top_right = tk.Radiobutton(self, text='Top Right',
                                     variable=self.orientValue, value='TR')

        self.bottom_left = tk.Radiobutton(self, text='Bottom Left',
                                          variable=self.orientValue, value='BL')
        self.top_left.select()
        self.bottom_right = tk.Radiobutton(self, text='Bottom Right',
                                           variable=self.orientValue, value='BR')

        self.top_left.grid(column=0, row=4, padx=8, sticky=W)
        self.top_right.grid(column=0, row=5, padx=8, sticky=W)
        self.bottom_left.grid(column=0, row=6, padx=8, sticky=W)
        self.bottom_right.grid(column=0, row=7, padx=8, sticky=W)

        # create a the generate button
        self.generate_btn = Button(self,
                                   text="Run",
                                   command=self.processSelections,
                                   highlightbackground='#3E4149'
                                   # font=btnFont
                                   ).grid(row=8, column=0, sticky=W, pady=10, padx=5)

        # create a the clear screen button
        self.clear_btn = Button(self,
                                text="Clear",
                                command=self.resetScreen,
                                highlightbackground='#2E4149'
                                # font=btnFont
                                ).grid(row=8, column=0, sticky=W, pady=10, padx=45)

        ttk.Separator(self,
                      orient=HORIZONTAL
                      ).grid(row=9, column=0, columnspan=3, sticky=NSEW, pady=5, padx=5)



        self.msg2show = StringVar()
        Label(self,
              textvariable=self.msg2show,
              wraplength=500
              ).grid(row=14, column=0, columnspan=2, sticky=W, pady=4)

        self.errFont = font.Font(weight="bold")
        self.errFont = font.Font(size=20)
        self.err2show = StringVar()
        Label(self,
              textvariable=self.err2show,
              foreground="red",
              font=self.errFont,
              wraplength=200
              ).grid(row=15, column=0, sticky=NSEW, pady=4)
    # end def create_widgets(self):

    # process user selections
    def processSelections(self):
        """Processes user screen selections"""
        size = self.dimensions.get()
        stopat = self.stopat.get()
        type = self.orientValue.get()
        square = make_square(size, stopat, type)
    # end def processSelections(self):


# main
def main():
    """Application Entry Point - the main
    driver code for the BSSD5410 Final Question #2"""
    root = Tk()
    root.resizable(height=None, width=None)
    root.title("BSSD 5410 Final Question #2")
    root.iconbitmap('William_Shakespeare.ico')
    root.geometry("450x425")
    app = Application(root)
    root.mainloop()


if __name__ == "__main__":
    main()
