
import tkinter

class KiloConverterGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        
        self.top_frame = tkinter.Frame()
        self.top2_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        
        self.prompt_label = tkinter.Label(self.top_frame,
                    text='Введите количество галлонов:')
        self.galo_entry = tkinter.Entry(self.top_frame,
                                        width=10)
        self.prompt1_label = tkinter.Label(self.top2_frame,
                    text='Введите количество миль:')
        self.mil_entry = tkinter.Entry(self.top2_frame,
                                        width=10)
        

        
        self.prompt_label.pack(side='left')
        self.galo_entry.pack(side='left')
        self.prompt1_label.pack(side='left')
        self.mil_entry.pack(side='left')
        

        
        self.descr_label = tkinter.Label(self.mid_frame,
                   text='Мили на галлон(MPG)=')

        
        self.value = tkinter.StringVar()

        
        self.miles_label = tkinter.Label(self.mid_frame,
                   textvariable=self.value)

        
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

       
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Вычислить MPG',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                   command=self.main_window.destroy)

        
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

       
        self.top_frame.pack()
        self.top2_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        
        tkinter.mainloop()


    def convert(self):
        
        galo = float(self.galo_entry.get())
        mil=float(self.mil_entry.get())

       
        miles = mil/galo

        
        self.value.set(miles)


kilo_conv = KiloConverterGUI()

