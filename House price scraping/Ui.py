from tkinter import *


class Ui:
    def __init__(self):
        self.window = Tk()
        self.window.eval('tk::PlaceWindow %s center' % self.window.winfo_pathname(self.window.winfo_id()))
        self.window.title("Info")

        self.label = Label(text='Proszę wybrać filtry, następnie wcisnąć "Wynik" i pozostawić bota.')
        self.label.grid(row=0, column=0)

        self.button = Button(text="ok", command=self.window.destroy)
        self.button.grid(row=1, column=0)

        self.window.mainloop()

