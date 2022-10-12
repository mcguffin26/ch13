import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('400x200')
        self.main_window.title('Pizza Menu')

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3= tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()

        #frame 1 - customer name
        self.customer_name = tkinter.Label(self.frame1, text='Customer Name:')
        self.name_entry = tkinter.Entry(self.frame1, width=10)

        self.customer_name.pack(side='left')
        self.name_entry.pack(side='left')
        
        #frame 2 - crust type
        self.crust_var = tkinter.IntVar()

        self.label2 = tkinter.Label(self.frame2, text='Select Crust Type:')
        self.crust1 = tkinter.Radiobutton(self.frame2, text='Regular', variable = self.crust_var, value = 2)
        self.crust2 = tkinter.Radiobutton(self.frame2, text='Thin', variable = self.crust_var, value = 4)
        self.crust3 = tkinter.Radiobutton(self.frame2, text='Deep Dish', variable = self.crust_var, value = 4)
        
        self.label2.pack(side='left')
        self.crust1.pack(side='left')
        self.crust2.pack(side='left')
        self.crust3.pack(side='left')

        #pepperoni, sausage, ham, beef, grilled chicken, mushrooms, bell peppers, pineapple
        #frame 4 & 5 - toppings

        #define toppings variables
        self.t1_var = tkinter.IntVar()
        self.t2_var = tkinter.IntVar()
        self.t3_var = tkinter.IntVar()
        self.t4_var = tkinter.IntVar()
        self.t5_var = tkinter.IntVar()
        self.t6_var = tkinter.IntVar()
        self.t7_var = tkinter.IntVar()
        self.t8_var = tkinter.IntVar()

        self.t1 = tkinter.Checkbutton(self.frame4, text='Pepperoni', variable = self.t1_var, value = 1.20)
        self.t2 = tkinter.Checkbutton(self.frame4, text='Sausage', variable = self.t2_var, value = 1.20)
        self.t3 = tkinter.Checkbutton(self.frame4, text='Ham', variable = self.t3_var, value = 1.20)
        self.t4 = tkinter.Checkbutton(self.frame4, text='Beef', variable = self.t4_var, value = 1.20)
        self.t5 = tkinter.Checkbutton(self.frame5, text='Grilled Chicken', variable = self.t5_var, value = 1.20)
        self.t6 = tkinter.Checkbutton(self.frame5, text='Mushrooms', variable = self.t6_var, value = .75)
        self.t7 = tkinter.Checkbutton(self.frame5, text='Bell Peppers', variable = self.t7_var, value = .75)
        self.t8 = tkinter.Checkbutton(self.frame5, text='Pineapple', variable = self.t8_var, value = .75)

        self.t1.pack(side='left')
        self.t2.pack(side='left')
        self.t3.pack(side='left')
        self.t4.pack(side='left')
        self.t5.pack(side='left')
        self.t6.pack(side='left')
        self.t7.pack(side='left')
        self.t8.pack(side='left')


        #pack buttons in frame6
        self.orderbutton = tkinter.Button(self.frame6, text='Order', command=self.calculate)
        self.quitbutton = tkinter.Button(self.frame6, text='Quit', command=self.main_window.destroy)

        self.orderbutton.pack(side='left')
        self.quitbutton.pack(side='right')

        tkinter.mainloop()

    def calculate(self):


        tkinter.messagebox.showinfo('Response', 'Thanks for clicking me!')


my_gui = myGUI()

print('I am done!')