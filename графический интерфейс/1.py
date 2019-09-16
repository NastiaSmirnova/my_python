import tkinter
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.my_button = tkinter.Button(self.bottom_frame,text='Показать информацию',command=self.do_something)
        self.my_button.pack(side='left')
        
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                command=self.main_window.destroy)
        self.quit_button.pack(side='left')
        
        self.label = tkinter.Label(self.top_frame,
                                   text='',justify='left')
        self.label.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

    def do_something(self):
        self.label.config(text='Стивен Маркус \n 247 Бейли \n Северная Каролина 27999')
my_gui=MyGUI()
