from tkinter import *

class Questionnaire(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()

root = Tk()
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()
