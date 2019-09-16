import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.mid_frame = tkinter.Frame()

        
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
 
    
        self.radio_var = tkinter.IntVar()
 
        
        self.radio_var.set(1)

       
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Дневное время (6:00-17:59)',
                                       variable=self.radio_var,
                                       value=10)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Вечернее время (18:00-23:59)',
                                       variable=self.radio_var,
                                       value=12)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Непиковый период (00:00-5:59)',
                                       variable=self.radio_var,
                                       value=5)

       
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
       

        self.descr_label = tkinter.Label(self.mid_frame,
                    text='Введите количество минут:')
        self.min_label = tkinter.Entry(self.mid_frame,
                                        width=10)
        self.descr_label.pack(side='left')
        self.min_label.pack(side='left')

        
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='Показать время',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                command=self.main_window.destroy)

       
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

       
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
 
        tkinter.mainloop()

   
    def show_choice(self):
           tkinter.messagebox.showinfo('Общая стоимость', 'Ваши затраты =$' +
                                    str(int(self.radio_var.get())*int(self.min_label.get())/100))

my_gui = MyGUI()
