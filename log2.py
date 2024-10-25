from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox
import subprocess
import Globalvariable


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x900")
        root.resizable(False, False)
        self.connection = sqlite3.connect("customer.db")
        self.connection.commit()
        
        self.sidebar = Frame(self.root, bg='black')
        self.sidebar.place(x=5,y=5, width=380, height=600)

        image_path1 = r"C:\Users\home\Pictures\Saved Pictures\login"
        image1= Image.open(image_path1)
        image1 = image1.resize((150,150))
        self.photo1 = ImageTk. PhotoImage(image1)

        self.background_label1 = Label(self.sidebar, image=self.photo1, bg='black')
        self.background_label1.image = self.photo1
        self.background_label1.place(x=120, y=90)

        image_path2 = r"C:\Users\home\Pictures\Saved Pictures\taxi_booking.png"
        image2= Image.open(image_path2)
        image2 = image2.resize((550,550))
        self.photo2 = ImageTk. PhotoImage(image2)

        self.background_label2 = Label(image=self.photo2)
        self.background_label2.image = self.photo2
        self.background_label2.place(x=420, y=50)

        self.heading =Label(self.sidebar, text='Login Page', bg='Black', font=("", 16, "bold"), bd=1, fg='White')
        self.heading.place(x=160, y=10)
  
        label_username = tk.Label(self.root, text="Username:", font=("Courier New",15, "bold"), fg='white', bg='Black')
        label_username.place(x=10, y=350)
        self.entry_username = tk.Entry(self.root, font=("Arial",15, "bold"))
        self.entry_username.place(x=150, y=350)

        label_password = tk.Label(self.root, text="Password:", font=("Courier New",15, "bold"),fg='white', bg='Black')
        label_password.place(x=10, y=400)
        self.entry_password = tk.Entry(self.root, font=("Arial",15, "bold"),show='*')
        self.entry_password.place(x=150, y=400)
        self.check_button = Checkbutton( root, text="show password", bg='black', fg='white', command= self.show_password, cursor='hand2')
        self.check_button.place(x= 150, y=430)
            
        login_button = tk.Button(self.root, text="Login",width=10, command=self.login,font=("Courier New",15, "bold" ), bg="gray")
        login_button.place(x=110, y=480)

        register_button1 = tk.Button(self.root, text="Register as customer?",width=20, command=self.open_register_page,font=("Courier New",11, "bold"),fg='white', bg="Black",  bd=0, cursor ='hand2')
        register_button1.place(x=90, y=540)
        
        registertwo_button = tk.Button(self.root, text="Register as Driver?",width=20, command=self.register ,font=("Courier New",11, "bold"), bg="Black", fg='White',  bd=0, cursor='hand2')
        registertwo_button.place(x=90, y=560) 

    def show_password(self):
        if self.entry_password.cget('show') == '*':
            self.entry_password.config(show='')
        else:
            self.entry_password.config(show='*')

    def check_credentials(self, username , password):
        username = self.entry_username.get()
        password = self.entry_password.get()
        connection = sqlite3.connect("customer.db")
        cursor= connection.cursor()
        cursor.execute("SELECT username and password FROM tblregister WHERE username=? AND password=?", (username, password))        
        result = cursor.fetchone()
        connection. close   
        return result is not None   
    
    def login(self):
        if  self.entry_username.get() == "" or self.entry_password.get() == "":
            messagebox.showwarning('Error', 'No username or password')

        elif self.entry_username.get() == "Admin123" and self.entry_password.get() == "password":
             self.new1()
    
        username = self.entry_username.get()
        password = self.entry_password.get()
        connection = sqlite3.connect("customer.db")
        cursor= connection.cursor()
        cursor2= connection.cursor()       
        cursor.execute("SELECT * FROM tblregister WHERE username=? AND password=?", (username, password))
        customer = cursor.fetchone()    
        
        cursor2.execute("SELECT * FROM Drivers WHERE username=? AND password=?", (username, password))
        user1 = cursor2.fetchone()
        
        if customer is not None:
            Globalvariable.Customer_information= customer
            messagebox.showinfo("Success", "Login Successful")
            self.clear_entries()
                
            self.root.destroy()
            from customer import Customer 
            root = Tk()
            Customer(root)
        elif user1 is not None:
            Globalvariable.Driver_information=user1
            messagebox.showinfo("Success", "Driver Login Successful")
            self.clear_entries()
            self.root.destroy()
            from Driver import Dashboard 
            root = Tk()
            Dashboard(root)
        else:
            messagebox.showwarning('Error', 'Invalid username or password')
        
    def clear_entries(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def open_register_page(self):
        self.root.destroy()
        subprocess.run(['python','register1.py'])

    def new1(self):
        self.root.destroy()
        subprocess.run(['python','Admin.py'])

    def new(self):
        subprocess.run(['python','customer.py'])
        self.root.destroy()

    def register(self):
        self.root.destroy()
        subprocess.run(['python','resgidriver.py'])

    def dashboard(self): 
        self.root.destroy()
        from customer import Customer
        root= Tk()
        Customer(root, Customer_information)
        
    
        
if __name__ == "__main__":
    root = tk.Tk()  
    app = Login(root)
    root.mainloop()


