from tkinter import *

#GUI setup
class Questionnaire(Frame):
    def __init__(self, master ):
        Frame.__init__(self,master)
        self.grid()
        self.creatProgSelect()

    def creatProgSelect(self):
        lblProg = Label(self, text='Degree Programme:', font=('MS', 8, 'bold'))
        lblProg.grid(row=0, column=0, columnspan=2, sticky=NE)

        self.listProg = Listbox(self, height =3)
        scroll = Scrollbar(self, command =self.listProg.yview)
        self.listProg.configure(yscrollcommand = scroll.set)

        self.listProg.grid(row=0, column=2, columnspan=2, sticky=NE)
        scroll.grid(row=0, column=4, sticky=W)

        for item in ["CS", "CS with", "BIS", "SE", "Joints", ""]:
            self.listProg.insert(END, item)

        self.listProg.selection_set(END)


#Main
root = Tk()
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()
