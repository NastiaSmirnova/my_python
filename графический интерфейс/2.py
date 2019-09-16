import tkinter
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.my_button = tkinter.Button(self.bottom_frame,text='sinister',command=self.do_something)
        self.my_button.pack(side='left')
        
        self.my_button = tkinter.Button(self.bottom_frame,text='dexter',command=self.do_something1)
        self.my_button.pack(side='left')
        
        self.my_button = tkinter.Button(self.bottom_frame,text='medium',command=self.do_something2)
        self.my_button.pack(side='left')
        
        self.label = tkinter.Label(self.top_frame,
                                   text='',justify='left')
        self.label.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

    def do_something(self):
        self.label.config(text='левый')
    def do_something1(self):
        self.label.config(text='центр')
    def do_something2(self):
        self.label.config(text='правый') 
    
my_gui=MyGUI()

