from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox
from datetime import*

from tkinter import Tk,Label
import Globalvariable
from log2 import Login 

class Customer:
    def __init__(self, window):
        self.window = window
        self.window.title('Taxi Booking System')
        self.window.geometry("1366x768")
        # self.window.state('zoomed')
        self.window.resizable(False, False)

        self.conn = sqlite3.connect("customer.db")
        self.cursor = self.conn.cursor()

        # Create table if not exists
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Customers
                            (booking_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            PickupAddress TEXT,DropoffAddress TEXT,PickupTime INTEGER,PickupDate INTEGER, Payment Method TEXT, Fare TEXT, Status TEXT, customer_id INTEGER,
                driver_id INTEGER, FOREIGN KEY (customer_id) REFERENCES tblregister(customer_id), FOREIGN KEY (driver_id) REFERENCES Drivers(driver_id))''')
        self.conn.commit()

        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=2, y=1, width=2000, height=130)
        
        #side bar
        self.sidebar = Frame(self.window, bg='light blue')
        self.sidebar.place(x=0,y=0, width=205, height=7500)  
          
        #side text
        self.heading =Label(self.sidebar, text='Home', bg='lightblue', font=("", 14 , "bold"), bd=1, fg='Black')
        self.heading.place(x=60, y=210)
       
        self.logout_text = Button(self.window, text='Log out', bg='#32cf8e', font=("", 13, "bold"), bd=1, fg='white', cursor='hand2', activebackground='#32cf8e',command= self.log)
        self.logout_text.place(x=1250, y=10) 

        self.heading =Label(self.window, text='Taxi Booking System', bg='#009df4', font=("", 26, "bold"), bd=1, fg='Black')
        self.heading.place(x=410, y=30)
        
        self.booking_text = Button(self.window, text='Make a booking', bg='lightblue', font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command= self.booking)
        self.booking_text.place(x=40, y=270)
             
        self.profile=Button(self.window, text='Password' ,bg='lightblue', font = ("", 13, "bold"), bd=1, fg='Black',cursor='hand2', activebackground='lightblue', command= self.manage_profile)
        self.profile.place(x=40, y=330)

        self.exit_text=Button(self.window, text='exit',bg= 'lightblue',command=self.exit, font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue')
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

        image_path6 = r"C:\Users\home\Pictures\Saved Pictures\profile.jpg"
        image6= Image.open(image_path6)
        image6 = image6.resize((26,26))
        self.photo6 = ImageTk. PhotoImage(image6)

        self.background_label6 = Label(self.sidebar, image=self.photo6, bg='lightblue')
        self.background_label6.image = self.photo6
        self.background_label6.place(x=5, y=330)
        self.photo6 = ImageTk. PhotoImage(image6)

        image_path7 = r"C:\Users\home\Pictures\Saved Pictures\exit.png"
        image7= Image.open(image_path7)
        image7 = image7.resize((25,25))
        self.photo7 = ImageTk. PhotoImage(image7)

        self.background_label7 = Label(self.sidebar, image=self.photo7, bg='lightblue')
        self.background_label7.image = self.photo7
        self.background_label7.place(x=5, y=600)
    
    def booking(self):
        self.bodyframe = Frame(self.window)
        self.bodyframe.place(x=205, y=130, width=1200, height=1300)

        label_pickup_address = Label(self.window, text="Pickup Address:", font=("Courier New", 15, "bold"), fg='Black')
        label_pickup_address.place(x=220, y=200)
        self.entry_pickup_address = Entry(self.window, font=("Arial", 15, "bold"), bd=2)
        self.entry_pickup_address.place(x=420, y=200)
        
        label_dropoff_address = Label(self.window, text="Dropoff Address:", font=("Courier New", 15, "bold"), fg='Black')
        label_dropoff_address.place(x=220, y=250)
        self.entry_dropoff_address = Entry(self.window, font=("Arial", 15, "bold"), bd=2)
        self.entry_dropoff_address.place(x=420, y=250)

        label_pickup_date = Label(self.window, text="Pickup Date:", font=("Courier New", 15, "bold"), fg='Black')
        label_pickup_date.place(x=800, y=200)
        self.entry_pickup_date = Entry(self.window, font=("Arial", 15, "bold"), bd=2)
        self.entry_pickup_date.place(x=970, y=200)

        label_pickup_time = Label(self.window, text="Pickup Time:", font=("Courier New", 15, "bold"), fg='Black')
        label_pickup_time.place(x=800, y=250)
        self.entry_pickup_time = Entry(self.window, font=("Arial", 15, "bold"), bd=2,)
        self.entry_pickup_time.place(x=970, y=250)

        label_payment= Label(self.window, text ='Payment Method:', font=('Courier New', 15, "bold"), fg='Black')
        label_payment.place(x=420, y=330)    
        self.payment_combobox=Entry(self.window, font=("Arial", 15, "bold"), bd=2)
        self.payment_combobox.place(x=600, y=330)

        self.book_text=Button(self.window, text='BOOK',bg= 'lightblue', font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command = self.book)
        self.book_text.place(x=1200, y=390)            
        self.cancel_text=Button(self.window, text='Cancel Booking',bg= 'lightblue', font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command = self.Cancel)
        self.cancel_text.place(x=1200, y=450)
        self.update_booking_text=Button(self.window, text='Update booking',bg= 'lightblue', font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command=self.update_Dashboard)
        self.update_booking_text.place(x=1200, y=500)

        self.tree = ttk.Treeview(self.window, columns=('ID','Pickup Address','Dropoff Address','Pickup Time','Pickup Date','Payment'), height=10)
        self.tree.heading("ID", text="Booking ID")
        self.tree.heading("Pickup Address", text="Pickup Address")
        self.tree.heading("Dropoff Address", text="Dropoff Address")
        self.tree.heading("Pickup Time", text="Pickup Time")
        self.tree.heading("Pickup Date", text="Pickup Date")        
        self.tree.heading("Payment", text= "Payment")

        self.tree.column("ID", width=100)
        self.tree.column("Pickup Address", width=150)
        self.tree.column("Dropoff Address", width=150)
        self.tree.column("Pickup Time", width=100)
        self.tree.column("Pickup Date", width=100)
        self.tree.column("Payment", width=150)
        self.conn.commit()
        self.tree.place(x=220, y=450)
        self.tree.bind("<<TreeviewSelect>>", self.selectedRow)
        self.read_Dashboard()
 
    def Cancel(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to cancel.")
            return

        selected_id = self.tree.item(selected_item,"values")[0]

        self.cursor.execute('''DELETE FROM Customers WHERE booking_ID=?''', (selected_id,))
        # self.conn.commit()
        self.conn.commit()
        self.conn.close()

        messagebox.showinfo("Success", "Booking cancelled successfully!")
        self.window.destroy()
        new_root = Tk()
        Customer(new_root)
        new_root.mainloop()

    def selectedRow(self, event):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")

        if values:
            self.entry_pickup_address.delete(0, "end")
            self.entry_pickup_address.insert(0, values[1])

            self.entry_dropoff_address.delete(0, "end")
            self.entry_dropoff_address.insert(0, values[2])

            self.entry_pickup_time.delete(0, "end")
            self.entry_pickup_time.insert(0, values[3])

            self.entry_pickup_date.delete(0, "end")
            self.entry_pickup_date.insert(0, values[4])

            self.payment_combobox.delete(0, "end")
            self.payment_combobox.insert(0, values[5])

    def update_Dashboard(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showerror("Error", "Please select a record to update.")
            return
     
        selected_id = self.tree.item(selected_item, "values")[0]
        pickup_address = self.entry_pickup_address.get()
        dropoff_address = self.entry_dropoff_address.get()
        Pickup_Date = self.entry_pickup_date.get()
        Pickup_Time = self.entry_pickup_time.get()
        Payment = self.payment_combobox.get()


        self.cursor.execute(('''UPDATE Customers SET PickupAddress=?, DropoffAddress=?, PickupDate=? , PickupTime=?, Payment=? WHERE booking_ID=?'''),
                            (pickup_address, dropoff_address, Pickup_Date, Pickup_Time, Payment ,selected_id))
        self.conn.commit()
        messagebox.showinfo("Success","Booking updated successfully!")
        self.window.destroy()
        new_root = Tk()
        Customer(new_root)
        new_root.mainloop()

    def book(self):

            PickupAddress = self.entry_pickup_address.get()
            DropoffAddress = self.entry_dropoff_address.get()
            PickupDate = self.entry_pickup_date.get()
            PickupTime = self.entry_pickup_time.get()
            Payment = self.payment_combobox.get()
            cus_id = Globalvariable.Customer_information[0]
            status = "Pending"
            # Check if all fields are filled
            if PickupAddress and DropoffAddress and PickupDate and PickupTime and cus_id :

                # Insert the record into the database
                self.cursor.execute('''INSERT INTO Customers (customer_id, PickupAddress, DropoffAddress, PickupDate, PickupTime, Payment,Status) 
                                    VALUES (?,?,?,?,?,?,?)''',
                                    (cus_id, PickupAddress, DropoffAddress, PickupDate, PickupTime, Payment,status))
                self.conn.commit()
                self.conn.close() 

                messagebox.showinfo("Success", "Record created successfully!")
                self.window.destroy()
                new_root = Tk()
                Customer(new_root)
                new_root.mainloop()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")                     
           
    def insert_tree_record(self, Dashboard):
        self.tree.insert('', 'end', values= (Dashboard[0], Dashboard[1], Dashboard[2], Dashboard[3]))
        self.cursor.execute('''INSERT INTO Customers (PickupAddress, DropoffAddress, PickupDate, PickupTime, Payment) VALUES (?, ?, ?, ?, ?)''', Dashboard)
        self.conn.commit()
          
    def read_Dashboard(self):
        self.tree.delete(*self.tree.get_children())

        self.cursor.execute('''SELECT * FROM Customers where customer_id=?''', (Globalvariable.Customer_information[0], ))
        self.conn.commit()
        records = self.cursor.fetchall()

        if records:
            for record in records:
                    self.tree.insert("", "end", values=record[0:])
    def clear_entries(self):
        self.entry_pickup_address.delete(0, tk.END)
        self.entry_dropoff_address.delete(0, tk.END)
        self.entry_pickup_date.delete(0, tk.END)
        self.entry_pickup_time.delete(0, tk.END)
        self.payment_combobox.delete(0, tk.END)

    def manage_profile(self):
        self.bodyframe = Frame(self.window)
        self.bodyframe.place(x=205, y=130, width=1250, height=1300)

        self.heading = Label(self.bodyframe, text='Want to change password = ?', font=('', 14, 'bold'), bd=4)
        self.heading.place(x=300,y=50)

        label_Username = Label(self.window, text="Username:", font=("Courier New", 15, "bold"), fg='Black')
        label_Username.place(x=300, y=350)
        self.entry_Username = Entry(self.window, font=("Arial", 15, "bold"), bd=2, fg='lightblue')
        self.entry_Username.place(x=600, y=350)

        label_old_password= Label(self.window, text="old Password:", font=("Courier New", 15, "bold"), fg='Black')
        label_old_password.place(x=300, y=400)
        self.entry_old_password= Entry(self.window, font=("Arial", 15, "bold"), bd=2, fg='lightblue')
        self.entry_old_password.place(x=600, y=400)
       
        label_new_password= Label(self.window, text="Password:", font=("Courier New", 15, "bold"), fg='Black')
        label_new_password.place(x=300, y=450)
        self.entry_new_password= Entry(self.window, font=("Arial", 15, "bold"), bd=2, fg='lightblue')
        self.entry_new_password.place(x=600, y=450)

        self.change= Button(self.window, text="Update the password",font=("Arial",15, "bold" ) ,bg="Lightblue", fg="black", cursor= "hand2",command= self.button_password)
        self.change.place(x=400,y= 570 )
        
    def button_password(self):
        username = self.entry_Username.get()
        old_password = self.entry_old_password.get()
        new_password = self.entry_new_password.get()

        if username == "" or old_password == "" or new_password == "":
            messagebox.showinfo("Error", "Please fill in all fields.")
        else:
            self.change_password(username, old_password, new_password)

    def change_password(self, username, old_password, new_password):
        try:
            conn = sqlite3.connect('customer.db')
            curs = conn.cursor()

            # Check if the old password matches the one stored in the database for the given username
            curs.execute('''
                SELECT Password FROM tblregister
                WHERE Username = ?
            ''', (username,))
            stored_password = curs.fetchone()

            if stored_password and stored_password[0] == old_password:
                # Update the password for the specified username
                curs.execute('''
                    UPDATE tblregister
                    SET Password = ?
                    WHERE Username = ?
                ''', (new_password, username))

                conn.commit()
                curs.close()
                conn.close()
                messagebox.showinfo("Success", "Password changed successfully.")

        except Exception as e:
            print(f"Error: {e}")
    def log(self):
        self.window.destroy()
        log2_root = Tk()
        log2 = Login(log2_root)
        log2_root.mainloop()

    def exit(self):
        self.window.destroy()
if __name__ == "__main__":
    window = Tk()
    Customer(window)
    window.mainloop()

 
