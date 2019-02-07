from tkinter import *

#GUI setup
class Questionnaire(Frame):
    def __init__(self, master ):
        Frame.__init__(self,master)
        self.grid()
        self.creatProgSelect()
        self.creatTeamExpQuest()
        self.creatProblems()

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

    def creatTeamExpQuest(self):
        lblProg = Label(self, text='Team Experience:', font=('MS', 8, 'bold'))
        lblProg.grid(row=4, column=0, columnspan=2, sticky=NE)

        lblProg = Label(self, text='1. Our Team worked together effectively', font=('MS', 8, 'bold'))
        lblProg.grid(row=5, column=0, columnspan=2, sticky=NE)

        self.varQ1 = IntVar()

        R1Q1 = Radiobutton(self, variable=self.varQ1, value = 4)
        R1Q1.grid(row=5, column=4)

        R2Q1 = Radiobutton(self, variable=self.varQ1, value =3)
        R2Q1.grid(row=5, column=5)

        R3Q1 = Radiobutton(self, variable=self.varQ1, value =2)
        R3Q1.grid(row=5, column=6)

        R4Q1 = Radiobutton(self, variable=self.varQ1, value =1)
        R4Q1.grid(row=5, column=7)

        lblProg = Label(self, text='2. Our team produced good quality products', font=('MS', 8, 'bold'))
        lblProg.grid(row=6, column=0, columnspan=2, sticky=NE)

        self.varQ2 = IntVar()

        R1Q2 = Radiobutton(self, variable=self.varQ2, value = 4)
        R1Q2.grid(row=6, column=4)

        R2Q2 = Radiobutton(self, variable=self.varQ2, value = 2)
        R2Q2.grid(row=6, column=5)

        R3Q2 = Radiobutton(self, variable=self.varQ2, value = 3)
        R3Q2.grid(row=6, column=6)

        R4Q2 = Radiobutton(self, variable=self.varQ2, value = 1)
        R4Q2.grid(row=6, column=7)

        lblProg = Label(self, text='3. I enjoyed working in our team', font=('MS', 8, 'bold'))
        lblProg.grid(row=7, column=0, columnspan=2, sticky=NE)

        self.varQ3 = IntVar()

        R1Q3 = Radiobutton(self, variable=self.varQ3, value = 4)
        R1Q3.grid(row=7, column=4)

        R2Q3 = Radiobutton(self, variable=self.varQ3, value = 3)
        R2Q3.grid(row=7, column=5)

        R3Q3 = Radiobutton(self, variable=self.varQ3, value = 2)
        R3Q3.grid(row=7, column=6)

        R4Q3 = Radiobutton(self, variable=self.varQ3, value = 1)
        R4Q3.grid(row=7, column=7)

        lblStrAgr = Label(self,text = 'Strongly \n Agree', font=('MS','8','bold'))
        lblStrAgr.grid(row=3, column =4, rowspan =2)

        lblStrAgr = Label(self,text = 'Partly \n Agree', font=('MS','8','bold'))
        lblStrAgr.grid(row=3, column =5, rowspan =2)

        lblStrAgr = Label(self,text = 'Partly \n Disagree', font=('MS','8','bold'))
        lblStrAgr.grid(row=3, column =6, rowspan =2)

        lblStrAgr = Label(self,text = 'Strongly \n Disagree', font=('MS','8','bold'))
        lblStrAgr.grid(row=3, column =7, rowspan =2)

    def creatProblems(self):
        lblProb1 = Label(self, text='Problems:', font=('MS', 8, 'bold'))
        lblProb1.grid(row=8, column = 0)

        lblProb2 = Label(self, text='Our team often experienced the following problems (Choose all that apply):')
        lblProb2.grid(row=8, column=1, columnspan=6, sticky=W)




#Main
root = Tk()
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()
