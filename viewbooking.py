
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class ViewBooking():

    def __init__(self, root):
        self.root = root
        self.root.title("View Booking")
        self.root.geometry("1200x600+80+50")
        root.resizable(False, False)

        columns = ("ID","Pickup Address","Drop off Address","Pickup Time","Pickup Date",'Payment'," Driver Id")
        self.treeview = ttk.Treeview(self.root, columns=columns, show="headings", height=10)
        self.treeview.bind('<<TreeviewSelect>>', self.getting_data)

        for col in columns:
            self.treeview.heading(col, text=col, anchor="center")
            self.treeview.column(col, anchor = "center", width=110)
            
        self.treeview.pack(pady=20)
        self.getting_data()

        try:
                self.conn = sqlite3.connect('customer.db')
                # self.conn.connect("customer.db")
                self.curs = self.conn.cursor()
                self.curs.execute('''SELECT booking_ID, PickupAddress, DropoffAddress, PickupTime ,PickupDate, Payment, driver_id from Customers''')
                records = self.curs.fetchall()
                for record in records:
                    self.treeview.insert("", 'end', values = record)
                    # self.curs.commit()
                self.conn.commit()
                self.conn.close()

                

        except Exception as e:
                print("f{e}")

        #All the entry boxes 
        label_pickup_address = Label(self.root, text="Pickup Address:", font=("Courier New", 15, "bold"), fg='Black')
        label_pickup_address.place(x=300, y=300)
        self.entry_pickup_address = Entry(self.root, font=("Arial", 15, "bold"), bd=2)
        self.entry_pickup_address.place(x=600, y=300)

        label_dropoff_address = Label(self.root, text="Dropoff Address:", font=("Courier New", 15, "bold"), fg='Black')
        label_dropoff_address.place(x=300, y=350)
        self.entry_dropoff_address = Entry(self.root, font=("Arial", 15, "bold"), bd=2)
        self.entry_dropoff_address.place(x=600, y=350)

        label_date = Label(self.root, text="Pickup Date:", font=("Courier New", 15, "bold"), fg='Black')
        label_date.place(x=300, y=400)
        self.entry_date = Entry(self.root, font=("Arial", 15, "bold"), bd=2)
        self.entry_date.place(x=600, y=400)
         
        label_time = Label(self.root, text="Pickup Time:", font=("Courier New", 15, "bold"), fg='Black')
        label_time.place(x=300, y=450)
        self.entry_time = Entry(self.root, font=("Arial", 15, "bold"), bd=2)
        self.entry_time.place(x=600, y=450)
      
        label_payment = Label(self.root, text="Payment:", font=("Courier New", 15, "bold"), fg='Black')
        label_payment.place(x=300, y=500)
        self.entry_payment = Entry(self.root, font=("Arial", 15, "bold"), bd=2)
        self.entry_payment.place(x=600, y=500)

        label_contact= Label(self.root, text="Driver ID:", font=("Courier New", 15, "bold"), fg='Black')
        label_contact.place(x=300, y=250)
        self.entry_driver = Entry(self.root, font=("Arial", 15, "bold"), bd=2)
        self.entry_driver.place(x=600, y=250)


        self.Assign_text=Button(self.root, text='Assign',bg= 'lightblue',font=("", 13, "bold"), bd=1, fg='Black', cursor='hand2', activebackground='lightblue', command=self.assign_booking)
        self.Assign_text.place(x=900, y=500)

    def getting_data(self,event=""):
  
            selected_item = self.treeview.selection()

            if selected_item:
               
                values = self.treeview.item(selected_item)['values']

              
                self.entry_pickup_address.delete(0, END)
                self.entry_dropoff_address.delete(0, END)
                self.entry_date.delete(0, END)
                self.entry_time.delete(0, END)
                self.entry_payment.delete(0, END)

                self.entry_pickup_address.insert(0, values[1])  
                self.entry_dropoff_address.insert(0, values[2]) 
                self.entry_date.insert(0, values[4]) 
                self.entry_time.insert(0, values[3]) 
                self.entry_payment.insert(0, values[5])
                
    def assign_booking(self):

        Driverid = self.entry_driver.get()

        if not Driverid:
            messagebox.showerror("Error", "Please fill in all fields")  
            return
        try:
            # Fetch DriverID based on the selected driver name
            conn = sqlite3.connect('customer.db')
            curs = conn.cursor()
            curs.execute("SELECT Driverid FROM Drivers WHERE Driverid = ?", (Driverid))
            driver_id = curs.fetchone()

            if driver_id:  
                driverid = self.entry_driver.get()
                selected_item = self.treeview.selection()
                booking_id = self.treeview.item(selected_item, "values")[0]
                

                # Update the Booking table with the selected driver
                curs.execute("UPDATE customers SET driver_id = ? WHERE Booking_ID = ?", (driverid, booking_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Booking assigned to driver successfully")
                self.root.destroy()
                # new_root = Tk()
                # ViewBooking(new_root)
                # new_root.getting_data()
            else:
                messagebox.showerror("Error", "Selected driver not found")

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
         
            print(f"Error: {e}")
        finally:
            conn.close()  
          
                
if __name__ == "__main__":
    root = Tk()
    ViewBooking(root)
    root.mainloop()
    