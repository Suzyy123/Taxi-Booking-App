from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox
from datetime import*
from viewbooking import ViewBooking
from log2 import Login 

window=Tk

class Admin: 
    def __init__(self, window):
        self.window = window
        self.window.title('Taxi Booking System')
        self.window.geometry("1300x768")
        self.window.state('zoomed')
        self.window.resizable(False, False)

        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=2, y=1, width=2000, height=130)

        self.logout_text = Button(self.window, text='Log out', bg='#32cf8e', font=("", 13, "bold"), bd=1, fg='white', cursor='hand2', activebackground='#32cf8e', command= self.log)
        self.logout_text.place(x=1250, y=10)
        
        #side bar
        self.sidebar = Frame(self.window, bg='light blue')
        self.sidebar.place(x=0,y=0, width=205, height=7500)
        #body frame       

        #side text
        self.heading =Label(self.sidebar, text='Home', bg='lightblue', font=("", 14, "bold"), bd=1, fg='Black')
        self.heading.place(x=60, y=210)
        
        self.heading =Label(self.window, text='Taxi Booking System', bg='#009df4', font=("", 24, "bold"), bd=1, fg='Black')
        self.heading.place(x=410, y=30)
        
        self.booking_text = Button(self.window, text='Assign Booking', bg='lightblue', font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command = self.open_treeview)
        self.booking_text.place(x=40, y=270)

        self.Drivers_text = Button(self.window, text='Drivers', bg='lightblue', font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command = self.theDrivers)
        self.Drivers_text.place(x=40, y=330)

        self.customer=Button(self.window, text='View customers',bg='lightblue', font = ("", 13, "bold"), bd=1, fg='Black',cursor='hand2', activebackground='lightblue', command= self.customers)
        self.customer.place(x=40, y=390)

        self.exit_text=Button(self.window, text='exit',bg= 'lightblue', font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command= self.exit)
        self.exit_text.place(x=40, y=600)        
              
        self.image_path1 = r"C:\Users\home\Pictures\Saved Pictures\final.jpg"
        self.image1 = Image.open(self.image_path1)
        self.image1 = self.image1.resize((1000, 550))
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.background_label1 = Label( image=self.photo1, bg='white')
        self.background_label1.image = self.photo1
        self.background_label1.place(x=280, y=170)

        image_path2 = r"C:\Users\home\Pictures\Saved Pictures\images.jpg"
        image2 = Image.open(image_path2)
        image2 = image2.resize((180, 180))
        self.photo2 = ImageTk.PhotoImage(image2)

        self.background_label2 = Label(self.sidebar, image=self.photo2, bg='black')
        self.background_label2.image = self.photo2
        self.background_label2.place(x=15, y=20)        

        image_path3 = r"C:\Users\home\Pictures\Saved Pictures\25694.png"
        image3= Image.open(image_path3)
        image3 = image3.resize((25,25))
        self.photo3 = ImageTk. PhotoImage(image3)

        self.background_label3 = Label(self.sidebar, image=self.photo3, bg='lightblue')
        self.background_label3.image = self.photo3
        self.background_label3.place(x=10, y=210)


        image_path4 = r"C:\Users\home\Pictures\Saved Pictures\5361032.png"
        image4= Image.open(image_path4)
        image4 = image4.resize((25,25))
        self.photo4 = ImageTk. PhotoImage(image4)

        self.background_label4 = Label(self.sidebar, image=self.photo4, bg='lightblue')
        self.background_label4.image = self.photo4
        self.background_label4.place(x=5, y=270)

        image_path4 = r"C:\Users\home\Pictures\Saved Pictures\drivers.png"
        image4= Image.open(image_path4)
        image4 = image4.resize((25,25))
        self.photo4 = ImageTk. PhotoImage(image4)

        self.background_label4 = Label(self.sidebar, image=self.photo4, bg='lightblue')
        self.background_label4.image = self.photo4
        self.background_label4.place(x=5, y=330)

        image_path5 = r"C:\Users\home\Pictures\Saved Pictures\profile.jpg"
        image5= Image.open(image_path5)
        image5 = image5.resize((25,25))
        self.photo5 = ImageTk. PhotoImage(image5)

        self.background_label5 = Label(self.sidebar, image=self.photo5, bg='lightblue')
        self.background_label5.image = self.photo5
        self.background_label5.place(x=5, y=390)
        self.photo5 = ImageTk. PhotoImage(image5)

        self.background_label5 = Label(self.sidebar, image=self.photo5, bg='lightblue')
        self.background_label5.image = self.photo5
        self.background_label5.place(x=5, y=390)
        
        image_path6 = r"C:\Users\home\Pictures\Saved Pictures\exit.png"
        image6= Image.open(image_path6)
        image6 = image6.resize((25,25))
        self.photo6 = ImageTk. PhotoImage(image6)

        self.background_label6 = Label(self.sidebar, image=self.photo6, bg='lightblue')
        self.background_label6.image = self.photo6
        self.background_label6.place(x=5, y=600)

    def open_treeview(self):
        treeview_bodyframe = Tk()
        ViewBooking(treeview_bodyframe)

    def theDrivers(self):
        self.bodyframe = Frame(self.window)
        self.bodyframe.place(x=205, y=130, width=1200, height=1300)
        self.label =Label(self.window, text='Driver Details',  font=("", 18, "bold"), bd=1, fg='Black')
        self.label.place(x=300, y=190)
        
        columns = ("Driver ID", "FullName", "Username", "License no", "Email", "Address", "Phone")
        self.treeview = ttk.Treeview(self.window, columns=columns, show="headings", height=15)

        for col in columns:
            self.treeview.heading(col, text=col, anchor="center")
            self.treeview.column(col, anchor="center", width=120)
        self.treeview.place(x=400, y=250)

        try:
            self.conn = sqlite3.connect('customer.db')
            self.curs = self.conn.cursor()
            self.curs.execute('''SELECT * from Drivers''')
            records = self.curs.fetchall()
            for record in records:
                self.treeview.insert("", 'end', values=record)
            self.curs.commit()   
            self.conn.close()
        except Exception as e:
            print(f"{e}")

    def customers(self):
        self.bodyframe = Frame(self.window)
        self.bodyframe.place(x=205, y=130, width=1200, height=1300)
        
        self.label =Label(self.window, text='Customer Details',  font=("", 18, "bold"), bd=1, fg='Black')
        self.label.place(x=300, y=190)
        
        columns = ("Customer ID", "UserName", "Email Id", "Address", "Contact No")
        self.treeview = ttk.Treeview(self.window, columns=columns, show="headings", height=15)

        for col in columns:
            self.treeview.heading(col, text=col, anchor="center")
            self.treeview.column(col, anchor="center", width=120)
        self.treeview.place(x=470, y=250)

        try:
            self.conn = sqlite3.connect('customer.db')
            self.curs = self.conn.cursor()
            self.curs.execute('''SELECT * from tblregister''')
            records = self.curs.fetchall()
            for record in records:
                self.treeview.insert("", 'end', values=record)
            self.curs.commit()   
            self.conn.close()
        except Exception as e:
            print(f"{e}")

    def log(self):
        self.window.destroy()

        # Create a new Tkinter window for the Log2 Page
        log2_root = Tk()
        log2 = Login(log2_root)
        log2_root.mainloop()

    def exit(self):
        self.window.destroy()  

window = Tk()
dashboard = Admin(window)
window.mainloop()


 
