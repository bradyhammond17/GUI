import tkinter
import tkinter.messagebox

class AverageGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)               
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)

        self.test1_label = tkinter.Label(self.frame1,
                                        text = 'Enter the score for test 1:')
        self.test1_entry = tkinter.Entry(self.frame1, width=10)
       
        self.test2_label = tkinter.Label(self.frame2,
                                        text = 'Enter the score for test 2:')
        self.test2_entry = tkinter.Entry(self.frame2, width=10)
        
        self.test3_label = tkinter.Label(self.frame3,
                                        text = 'Enter the score for test 3:')
        self.test3_entry = tkinter.Entry(self.frame3, width=10)
        
        self.desc_label = tkinter.Label(self.frame4, text = 'Average')
        
        self.average_var = tkinter.StringVar()

        self.average_label = tkinter.Label(self.frame4, textvariable= self.average_var)
        
        self.desc_label.pack()    
        self.average_label.pack()

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.test1_label.pack(side='left')
        self.test1_entry.pack(side = 'left')
        
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side = 'left')

        self.test3_label.pack(side='left')
        self.test3_entry.pack(side = 'left')

        self.calcbutton = tkinter.Button(self.main_window,
                                            text = 'Average',
                                            command = self.average)
        self.calcbutton.pack()
        tkinter.mainloop()
    def average(self):
        test1 = float(self.test1_entry.get())
        test2 = float(self.test2_entry.get())
        test3 = float(self.test3_entry.get())
        
        average = round(((test1 + test2 + test3) / 3), 2)
        self.average_var.set(average)
avg_gui = AverageGUI()