from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox  
import tkinter as tk    
import sqlite3
import subprocess
root=Tk
class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x900")
        root.resizable(False, False)
        self.root.configure(bg='#fff')
        self.widgets()

        # self.connection = sqlite3.connect("customer.db")
        # self.connection.commit()
        
        self.conn = sqlite3.connect("customer.db")
        self.cursor = self.conn.cursor()

        # Create table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tblregister
                            (customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Username TEXT, Email TEXT, Address Text, Phone integer,Password TEXT)''')
        self.conn.commit()
 
    def Signin(self):
        Username = self.entry_Username.get()
        Email_ID = self.entry_Email_Id.get()
        Address = self.entry_Address.get()
        Phone_No = self.entry_Phone_No.get()
        Create_Password= self.entry_Create_Password.get()

        if Username and Email_ID and Address and Phone_No and Create_Password:
            self.cursor.execute('''INSERT INTO tblregister(Username, Email, Address, Phone, Password) VALUES ( ? , ? , ? , ? , ?)''', (Username, Email_ID,Address,Phone_No, Create_Password))                                                                                                                                                            
            self.conn.commit()
            messagebox.showinfo("Success!!!", "Record created successfully!")
            self.open_register_page()
            # self.clear_entries()
            # self.read_records()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    def open_register_page(self):
        subprocess.run(['python', 'log2.py'])
    

    def widgets(self):
        self.frame = Frame(self.root, bg='black') 
        self.frame.place(x=5, y=5, width=350, height=600)

        self.root.title("Registration Page")

        self.heading =Label( text='Register Page', bg='Black', font=("Courier New", 16, "bold"), bd=1, fg='White')
        self.heading.place(x=100, y=70)

        label_First_Name = tk.Label(self.root, text="First Name:", font=("Segoe Print",12, "bold"), bg='black', fg='white')
        label_First_Name.place(x=30, y=120)
        self.entry_First_label_First_Name = tk.Entry(self.root, font=("Arial",12, "bold"))
        self.entry_First_label_First_Name.place(x=160, y=130)
        
        label_Username = tk.Label(self.root, text="Username:", font=("Segoe Print",12, "bold"), bg='black', fg='white')
        label_Username.place(x=30, y=170)
        self.entry_Username = tk.Entry(self.root, font=("Arial",12, "bold"))
        self.entry_Username.place(x=160, y=180)

        label_Email_Id = tk.Label(self.root, text="Email ID:", font=("Segoe Print",12, "bold"),  bg='black', fg='white')
        label_Email_Id.place(x=30, y=230)
        self.entry_Email_Id = tk.Entry(self.root, font=("Arial",12, "bold"))
        self.entry_Email_Id.place(x=160, y=230)

        label_Address = tk.Label(self.root, text="Address:", font=("Segoe Print",12, "bold"), bg='black', fg='white')
        label_Address.place(x=30, y=280)
        self.entry_Address = tk.Entry(self.root, font=("Arial",12, "bold"))
        self.entry_Address.place(x=160, y=280)
        
        label_Phone_No = tk.Label(self.root, text="Phone No:", font=("Segoe Print",12, "bold"),  bg='black', fg='white')
        label_Phone_No.place(x=30, y=330)
        self.entry_Phone_No = tk.Entry(self.root, font=("Arial",12, "bold"))
        self.entry_Phone_No.place(x=160, y=330)
 
        label_Create_Password= tk.Label(self.root, text="Create Password:", font=("Segoe Print",12, "bold"), bg='black', fg='white')
        label_Create_Password.place(x=20, y=380)
        self.entry_Create_Password= tk.Entry(self.root, font=("Arial",11, "bold"))
        self.entry_Create_Password.place(x=180, y=380)

    
        Signin_button = tk.Button(self.root, text="Signin",width=10, command=self.Signin,font=("Courier New",12, "bold" ), bg="gray")
        Signin_button.place(x=150, y=450)

        Go_back_to_login_button = tk.Button(self.root, text="Login Page ",command= self.login, width=10, font=("Courier New",12, "bold" ), bg="gray")
        Go_back_to_login_button.place(x=50, y=550)

        image_path2 = r"C:\Users\home\Pictures\Saved Pictures\taxi_booking.png"
        image2= Image.open(image_path2)
        image2 = image2.resize((550,550))
        self.photo2 = ImageTk. PhotoImage(image2)

        self.background_label2 = Label(image=self.photo2, bg='#ffffff')
        self.background_label2.image = self.photo2
        self.background_label2.place(x=420, y=50)
        
    def open_register_page(self):        
        self.root.destroy()
        subprocess.run(['python', 'log2.py'])

    def login(self):
        self.root.destroy()

    
    
# def clear_entries(self):
#         self.entry_First_Name.delete(0, END)
#         self.entry_Last_Name.delete(0, END)
#         self.entry_Email_Id.delete(0, END)
#         self.entry_Address.delete(0, END)
#         self.entry_Phone_No.delete(0, END)
#         self.entry_Password.delete(0, END)
#         self.entry_entry_Confirm_password.delete(0, END)
#         self.entry_Country.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    register_app = Register(root)
    root.mainloop()






