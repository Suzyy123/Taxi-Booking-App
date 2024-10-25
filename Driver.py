from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox
from datetime import*
import Globalvariable
from log2 import Login 
# window=Tk

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title('Taxi Booking System')
        self.window.geometry("1366x768")
        self.window.state('zoomed')  
        self.window.resizable(False, False)      

        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=2, y=1, width=2000, height=130)
        
        #side bar
        self.sidebar = Frame(self.window, bg='light blue')
        self.sidebar.place(x=0,y=0, width=205, height=7500)
        #body frame
    
        #side text
        self.heading =Label(self.sidebar, text='Home', bg='lightblue', font=("", 14, "bold"), bd=1, fg='Black')
        self.heading.place(x=60, y=210)
        
        self.heading =Label(self.window, text='Taxi Booking System', bg='#009df4', font=("", 26, "bold"), bd=1, fg='Black')
        self.heading.place(x=410, y=30)
        
        self.booking_text = Button(self.window, text='View customer', bg='lightblue', font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command= self.view_booking)
        self.booking_text.place(x=40, y=270)
  
        self.Manage_profile=Button(self.window, text='Password' ,bg='lightblue', font = ("", 13, "bold"), bd=1, fg='Black',cursor='hand2', activebackground='lightblue', command= self.manage_profile)
        self.Manage_profile.place(x=40, y=330)

        self.exit_text=Button(self.window, text='exit',bg= 'lightblue', font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command= self.exit)
        self.exit_text.place(x=40, y=600)
        
        self.logout_text = Button(self.window, text='Log out', bg='#32cf8e', font=("", 13, "bold"), bd=1, fg='white', cursor='hand2', activebackground='#32cf8e', command= self.log)
        self.logout_text.place(x=1250, y=10)
        # Images here
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

        image_path4 = r"C:\Users\home\Pictures\Saved Pictures\pending.png"
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
        
    def view_booking(self):
        self.bodyframe = Frame(self.window)
        self.bodyframe.place(x=205, y=130, width=1200, height=1300)
        
        columns = ("ID","Pickup Address","Drop off Address","Pickup Time","Pickup Date",'Payment')
        self.treeview = ttk.Treeview(self.bodyframe, columns=columns, show="headings", height=15)

        for col in columns:
            self.treeview.heading(col, text=col, anchor="center")
            self.treeview.column(col, anchor = "center", width=150)
        self.treeview.place(x=30, y=250)
        
        self.treeview.bind("<<TreeviewSelect>>", self.getting_data)
        self.getting_data()
        try:
                self.conn = sqlite3.connect('customer.db')
                self.curs = self.conn.cursor()
                self.curs.execute(f"SELECT * from Customers WHERE driver_id={Globalvariable.Driver_information[0]} and Status='Pending'")
                records = self.curs.fetchall()
                for record in records:
                    self.treeview.insert("", 'end', values = record)
                self.curs.commit()

        except Exception as e:
                print("f{e}")

        self.Complete=Button(self.window, text='Complete' ,bg='lightblue', font = ("", 13, "bold"), bd=1, fg='Black',cursor='hand2', activebackground='lightblue',command = self.Accept_request)
        self.Complete.place(x=1200, y=300)

        label_time = Label(self.window, text="Pickup Time:", font=('Arial', 15, 'bold'), fg= 'Black')
        label_time.place(x=220, y=200)
        self.pickup_time_entry= Entry(self.window, font=('Arial', 15, 'bold'), bd=2, fg='Black')
        self.pickup_time_entry.place(x=400, y=200)

        label_pickup_address = Label(self.window, text="Pickup Address", font=('Arial', 15, 'bold'), fg= 'Black')
        label_pickup_address.place(x=220, y=250)
        self.entry_pickup_addres= Entry(self.window, font=('Arial', 15, 'bold'), bd=2, fg='Black')
        self.entry_pickup_addres.place(x=400, y=250)

        label_pickup_date = Label(self.window,text="Pickup Date", font=('Arial', 15, 'bold'), fg= 'Black')
        label_pickup_date.place(x=800, y=250)
        self.entry_pickup_date= Entry(self.window, font=('Arial', 15, 'bold'), bd=2, fg='Black')
        self.entry_pickup_date.place(x=970, y=250)

        label_dropoff_address = Label(self.window,text="Dropoff Address", font=('Arial', 15, 'bold'), fg= 'Black')
        label_dropoff_address.place(x=800, y=200)
        self.entry_dropoff_address= Entry(self.window, font=('Arial', 15, 'bold'), bd=2, fg='Black')
        self.entry_dropoff_address.place(x=970, y=200)
        
        label_payment = Label(self.window,text="Payment Method", font=('Arial', 15, 'bold'), fg= 'Black')
        label_payment.place(x=420, y=330)
        self.entry_payment= Entry(self.window, font=('Arial', 15, 'bold'), bd=2, fg='Black')
        self.entry_payment.place(x=600, y=330)

    def manage_profile(self):
        self.bodyframe = Frame(self.window)
        self.bodyframe.place(x=205, y=130, width=1200, height=1300)

        self.heading = Label(self.bodyframe, text='Your Profile', fg='Black',font=('', 20, 'bold'), bd=1)
        self.heading.place(x=150,y=50)

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
                SELECT Password FROM Drivers
                WHERE Username = ?
            ''', (username,))
            stored_password = curs.fetchone()

            if stored_password and stored_password[0] == old_password:
                # Update the password for the specified username
                curs.execute('''
                    UPDATE Drivers
                    SET Password = ?
                    WHERE Username = ?
                ''', (new_password, username))

                conn.commit()
                curs.close()
                conn.close()
                messagebox.showinfo("Success", "Password changed successfully.")
            # else:
            #     messagebox.showerror("Error", "Invalid username or old password.")

        except Exception as e:
            print(f"Error: {e}")

    def log(self):
        self.window.destroy()

        # Create a new Tkinter window for the Log2 Page
        log2_root = Tk()
        log2 = Login(log2_root)
        log2_root.mainloop()



    def exit(self):
        self.window.destroy()
        
    def Accept_request(self):
        selected_item = self.treeview.selection()

        selected_id = self.treeview.item(selected_item, "values")[0]
        conn = sqlite3.connect('customer.db')
        curs = conn.cursor()
        # Update the status to "Accepted"
        curs.execute('''
            UPDATE Customers
            SET Status = 'Completed'
            WHERE booking_ID = ?
        ''', (selected_id,))
        conn.commit()
        curs.close()
        conn.close()

        messagebox.showinfo("Success", "Booking completed successfully!")
        self.window.destroy()
        new_root = Tk()
        Dashboard(new_root)
        new_root.mainloop()
       

    def getting_data(self,event=""):  
        selected_item = self.treeview.selection()

        if selected_item:               
            values = self.treeview.item(selected_item)['values']
              
            self.pickup_time_entry.delete(0, END)
            self.entry_dropoff_address.delete(0, END)
            self.entry_pickup_addres.delete(0, END)
            self.entry_pickup_date.delete(0, END)
            self.entry_payment.delete(0, END)

            self.pickup_time_entry.insert(0, values[3])  
            self.entry_dropoff_address.insert(0, values[2]) 
            self.entry_payment.insert(0, values[5])
            self.entry_pickup_addres.insert(0, values[1])
            self.entry_pickup_date.insert(0, values[4])
                
 
   
window = Tk()
dashboard = Dashboard(window)  
window.mainloop()

