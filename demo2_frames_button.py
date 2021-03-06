import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='John')
        self.label2 = tkinter.Label(self.top_frame, text='Jill')
        self.label3 = tkinter.Label(self.top_frame, text='James')

        self.label1.pack(side = 'left')
        self.label2.pack(side = 'left')
        self.label3.pack(side = 'left')

        self.label4 = tkinter.Label(self.bottom_frame, text='Jack')
        self.label5 = tkinter.Label(self.bottom_frame, text='Jim')
        self.label6 = tkinter.Label(self.bottom_frame, text='Jerry')

        self.label4.pack(side = 'left')
        self.label5.pack(side = 'left')
        self.label6.pack(side = 'left')

        self.mybutton = tkinter.Button(self.main_window,
                                         text = "Click Me!",
                                         command = self.do_something)

        self.quit_button = tkinter.Button(self.main_window,
                                            text = 'Quit',
                                            command = self.main_window.destroy)

        self.mybutton.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')
        
        tkinter.mainloop()
    
    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')
       

my_gui = MyGUI()

print("moving on.....")