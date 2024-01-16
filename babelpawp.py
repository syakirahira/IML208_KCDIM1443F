import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import mysql.connector
from datetime import datetime, date
import random, string, re

class KpopPurchasingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("K-pop Purchasing System")
        self.master.geometry("760x305")
        self.master.configure(bg='mistyrose')  

        # GUI for main menu
        self.master_frame = tk.Frame(master,bd=5,relief='groove')
        self.master_frame.pack()

        self.master_label = tk.Label(self.master_frame, text="BABELPAWP ENTERTAINMENT", font=('Terminal', 20, 'bold'),bg='indian red2', fg= 'lemon chiffon') 
        self.master_label.pack(ipadx=760, ipady=15)

        #notes area
        notes_text = tk.Text(self.master, height=7, width=800, font=('terminal', 11),bg='mistyrose',fg= 'palevioletred3')
        notes_text.pack()
        notes_text.insert(tk.END, "\nWelcome to Babelpawp Entertainment page!\n\nThere are few features presented in this page\n\n")
        notes_text.insert(tk.END, "If you need any help, you can press the button 'HELP' at the bottom of each window :)")
        notes_text.configure(state='disabled')
        notes_text.tag_configure('center', justify='center')
        notes_text.tag_add('center', 1.0, tk.END)
        
        # Create buttons for each GUI
        self.masterframe = tk.Frame(master,bd=5,relief='groove',bg='mistyrose')
        self.masterframe.pack(ipadx=760,pady=2)

        # Membershipbutton
        self.registration_btn = tk.Button(self.masterframe, text="Membership", font=('terminal', 15), bg='powderblue', fg='steelblue',bd=10,relief= 'groove', command=self.open_registration_gui)
        self.registration_btn.grid(ipadx=30,pady=5,padx=30,row=0,column=0)
        notestext=tk.Text(self.masterframe,width=25,height=5,font=('terminal', 9),bg='mistyrose',fg= 'palevioletred3')
        notestext.grid(row=1,column=0,pady=5)
        notestext.insert(tk.END, "\nThis button will take\nyou to the membership\nregistration window")
        notestext.configure(state='disabled')
        notestext.tag_configure('center', justify='center')
        notestext.tag_add('center', 1.0, tk.END)

        # Ticketingbutton
        self.ticketing_btn = tk.Button(self.masterframe, text="Ticketing", font=('terminal', 15), bg='pink', fg='palevioletred3', bd=10, relief='groove', command=self.open_ticketing_gui)
        self.ticketing_btn.grid(ipadx=30,pady=5,padx=30,row=0,column=1)
        notestext2=tk.Text(self.masterframe,width=25,height=5,font=('terminal', 9),bg='mistyrose',fg= 'palevioletred3')
        notestext2.grid(row=1,column=1,pady=5)
        notestext2.insert(tk.END, "\nThis button will take \nyou to the ticket \npurchasing window")
        notestext2.configure(state='disabled')
        notestext2.tag_configure('center', justify='center')
        notestext2.tag_add('center', 1.0, tk.END)

        # Fanmeeting
        self.schedule_btn = tk.Button(self.masterframe, text="Fanmeeting", font=('terminal', 15),bg='plum1', fg='orchid3',bd=10, relief='groove', command=self.open_fanmeeting_gui)
        self.schedule_btn.grid(ipadx=30,pady=5,padx=30,row=0,column=2)
        notestext3=tk.Text(self.masterframe,width=25,height=5,font=('terminal', 9),bg='mistyrose',fg= 'palevioletred3')
        notestext3.grid(row=1,column=2,pady=5)
        notestext3.insert(tk.END, "\nThis button will take \nyou to the fanmeeting\npurchasing window")
        notestext3.configure(state='disabled')
        notestext3.tag_configure('center', justify='center')
        notestext3.tag_add('center', 1.0, tk.END)

    def show_help_mem(self):
        # Help text button for membership registration window
        help_text_mem = """
        How to register for BABELPAWP's membership?

        Fill in the following information:
        - Name: Your full name.
        - Date of Birth (YYYY-MM-DD): Your date of birth
          in the specified format.
        - Email (xxx@xxx.xxx): Your email address.
        - Phone number (+60 only): Your phone number, which 
          must start with '60', as this membership is only valid for 
          Malaysians.

        After filling in the details, click the 'Register' button to 
        complete the registration.

        If you encounter any issues, reach out to our support 
        team on either of these contacts below.
        
        Phone number: +601133228274
        e-mail: babelpawp@gmail.com

        Thank you for supporting BABELPAWP!
        """

        messagebox.showinfo("Help", help_text_mem)

    def open_registration_gui(self):
        registration_window = tk.Toplevel(self.master)
        registration_window.title("Membership Registration")
        registration_window.geometry("400x600")

        # Heading label
        self.label_reg = tk.Label(registration_window, text='BABELPAWP MEMBERSHIP', font=('Georgia Font', 20, 'italic'), bg='light sky blue', fg='dark blue', bd=10, relief='groove')
        self.label_reg.pack(ipadx=470)
        
        # Name frama and entry grid
        name_frame=tk.LabelFrame(registration_window,text="Name:", font=("Arial", 15), bg='#e6ffff', fg= 'dark blue',bd=5,relief= 'groove')
        name_frame.pack(ipadx=470)
        self.name_entry = tk.Entry(name_frame, font=("Arial", 12))
        self.name_entry.grid(ipadx=101)

        # Email frame and entry grid
        email_frame=tk.LabelFrame(registration_window, text="Email (xxx@xxx.xxx):", font=("Arial", 15), bg='#e6ffff', fg= 'dark blue',bd=5,relief= 'groove')
        email_frame.pack(ipadx=470)
        self.email_entry = tk.Entry(email_frame, font=("Arial", 12))
        self.email_entry.grid(ipadx=101)

        # DOB frame and entry grid
        dob_frame=tk.LabelFrame(registration_window, text="Date of Birth (YYYY-MM-DD):", font=("Arial", 15), bg='#e6ffff', fg= 'dark blue',bd=5,relief= 'groove')
        dob_frame.pack(ipadx=470)
        self.dob_entry = tk.Entry(dob_frame, font=("Arial", 12))
        self.dob_entry.grid(ipadx=101)

        # Phone frame and entry grid
        phone_frame=tk.LabelFrame(registration_window, text="Phone number (+60 only):", font=("Arial", 15), bg='#e6ffff', fg= 'dark blue',bd=5,relief= 'groove')
        phone_frame.pack(ipadx=470)
        self.phone_entry = tk.Entry(phone_frame, font=("Arial", 12))
        self.phone_entry.grid(ipadx=101)

        # Register, Update and Delete frame
        RUD_frame=tk.LabelFrame(registration_window, bg='#e6ffff', bd=5, relief='groove')
        RUD_frame.pack(ipadx=470)

        # Register, Update and Deletebutton and grid
        registermem_button = tk.Button(RUD_frame, text="Register", command=self.register_member, font=("Times New Roman", 14), bg="#84e0b3", fg="black")
        registermem_button.grid(row=5, column=1, pady=10, padx=30, sticky="ew")
        updmem_button = tk.Button(RUD_frame, text="Update", command=self.update_member_gui, font=("Times New Roman", 14), bg="#5bc0de", fg="black")
        updmem_button.grid(row=5, column=2, pady=10, padx=30, sticky="ew")
        deletemem_button = tk.Button(RUD_frame, text="Delete", command=self.delete_member_gui, font=("Times New Roman", 14), bg="#d9534f", fg="white")
        deletemem_button.grid(row=5, column=3, pady=10, padx=30, sticky="ew")

        # Data display frame
        memdisplay_frame = tk.LabelFrame(registration_window, bg='#e6ffff', bd=5, relief='groove')
        memdisplay_frame.pack(ipadx=470)

        self.data_display_box = tk.Text(memdisplay_frame, height=10, width=50)
        self.data_display_box.pack(pady=10)

        # Disable the data display box
        self.data_display_box.config(state='disabled')

        # Help, register, and quit button frame
        button_frame=tk.LabelFrame(registration_window, bg='#e6ffff', bd=5, relief='groove')
        button_frame.pack(ipadx=470)

        # Help and quit button with grid
        help_button = tk.Button(button_frame, text="Help", command=self.show_help_mem, font=("Times New Roman", 14), bg="#5bc0de", fg="black")
        help_button.grid(row=5, column=0, pady=10, padx=100, sticky="e")
        quit_button = tk.Button(button_frame, text="Back", command=registration_window.destroy, font=("Times New Roman", 14), bg="#d9534f", fg="white")
        quit_button.grid(row=5, column=1, pady=10, padx=1, sticky="w")

    def register_member(self):
        # Get user information
        name_mem = self.name_entry.get()
        email_mem = self.email_entry.get()
        dob_mem = self.dob_entry.get()
        phone_mem = self.phone_entry.get()

        # Validate input
        if not name_mem or not dob_mem or not email_mem or not phone_mem:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        # Check if name contains only alphabetic characters
        if not name_mem.replace(" ", "").isalpha():
            messagebox.showerror("Invalid", "Name must contain only alphabetic characters.")
            return

        elif not phone_mem.startswith("60") or not phone_mem[3:].isdigit():
            messagebox.showerror("Invalid", "Phone number must start with '+60' and contain only numeric values.")
            return

        # Check email format using a regular expression
        email_pattern = re.compile(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
        if not email_pattern.match(email_mem):
            messagebox.showerror("Invalid", "Invalid email format. Please use the format xxx@xxx.xxx.")
            return

        # Convert dob to date and calculate age
        try:
            dob_date = datetime.strptime(dob_mem, "%Y-%m-%d").date()
            age = (date.today() - dob_date).days // 365
        except ValueError:
            messagebox.showerror("Error", "Invalid Date of Birth format.")
            return

        # Generate a random alphanumeric Member ID
        member_ID = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

        # Display registration information in a message box
        registration_success_message = f"Registration Successful!\n\nMember ID: {member_ID}\nName: {name_mem}\nAge: {age}\nEmail: {email_mem}\nPhone: {phone_mem}"
        messagebox.showinfo("Registration Successful", registration_success_message)

        # Update the data display box in the GUI
        self.data_display_box.config(state='normal')
        self.data_display_box.insert(tk.END, registration_success_message + '\n\n')
        self.data_display_box.config(state='disabled')

        # Insert the data into the database
        self.insert_into_database_mem(member_ID, name_mem, dob_mem, age, email_mem, phone_mem)

    def insert_into_database_mem(self, member_ID, name_mem, dob_mem, age, email_mem, phone_mem):
        try:
            # Establish a connection to the MySQL server
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kpop_site"
            )

            # Create a cursor object to interact with the database
            cursor = mydb.cursor()

            # Inserting data into a table
            sql = "INSERT INTO `memship_details` (member_ID, user_name, user_dob, user_age, user_email, user_phone) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (member_ID, name_mem, dob_mem, age, email_mem, phone_mem)

            cursor.execute(sql, val)
            mydb.commit()
            print("Data inserted successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()

        finally:
            cursor.close()
            mydb.close()

    def update_member(self, member_ID):
        new_name = self.name_entry.get()
        new_email = self.email_entry.get()
        new_dob = self.dob_entry.get()
        new_phone = self.phone_entry.get()

        # Validate input
        if not member_ID or not new_name or not new_dob or not new_email or not new_phone:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        # Check if name contains only alphabetic characters
        if not new_name.replace(" ", "").isalpha():
            messagebox.showerror("Invalid", "Name must contain only alphabetic characters.")
            return

        elif not new_phone.startswith("60") or not new_phone[3:].isdigit():
            messagebox.showerror("Invalid", "Phone number must start with '+60' and contain only numeric values.")
            return

        # Check email format using a regular expression
        email_pattern = re.compile(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
        if not email_pattern.match(new_email):
            messagebox.showerror("Invalid", "Invalid email format. Please use the format xxx@xxx.xxx.")
            return

        # Convert dob to date and calculate age
        try:
            new_dob_date = datetime.strptime(new_dob, "%Y-%m-%d").date()
            new_age = (date.today() - new_dob_date).days // 365
        except ValueError:
            messagebox.showerror("Error", "Invalid Date of Birth format.")
            return

        # Establish a connection to the MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kpop_site"
        )

        # Create a cursor object to interact with the database
        cursor = mydb.cursor()

        # Fetch the updated data from the database
        cursor.execute("SELECT * FROM `memship_details` WHERE member_id=%s", (member_ID,))
        updated_member_info = cursor.fetchone()

        # Updating data in the table
        sql = "UPDATE `memship_details` SET user_name=%s, user_dob=%s, user_age=%s, user_email=%s, user_phone=%s WHERE member_id=%s"
        val = (new_name, new_dob, new_age, new_email, new_phone, member_ID)

        try:
            cursor.execute(sql, val)
            mydb.commit()
            print("Data updated successfully!")

            # Fetch the updated data from the database
            cursor.execute("SELECT * FROM `memship_details` WHERE member_id=%s", (member_ID,))
            updated_member_info = cursor.fetchone()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()

        finally:
            # Close cursor and database connection
            cursor.close()
            mydb.close()

        messagebox.showinfo("Update Successful", "Member information updated successfully.")

        # Return the updated member information
        return updated_member_info

    def update_member_gui(self):
        # Prompt the user for Member ID
        member_id_to_update = simpledialog.askstring("Update Member", "Enter Member ID to update:")

        if member_id_to_update:
            # Call the update_member method
            updated_member_info = self.update_member(member_id_to_update)

            if updated_member_info:
                # Clear existing content in data display box
                self.data_display_box.config(state='normal')
                self.data_display_box.delete(1.0, tk.END)

                # Display updated member information in the data display box
                updated_info_mem_str = (
                    f"Updated Member Information:\n\n"
                    f"Member ID: {updated_member_info[0]}\n"
                    f"Name: {updated_member_info[1]}\n"
                    f"Age: {updated_member_info[3]}\n"
                    f"Email: {updated_member_info[4]}\n"
                    f"Phone: {updated_member_info[5]}"
                )
                self.data_display_box.insert(tk.END, updated_info_mem_str)
                self.data_display_box.config(state='disabled')

    def delete_member(self, member_ID):
        # Validate input
        if not member_ID:
            messagebox.showerror("Error", "Please fill in the Member ID.")
            return

        # Establish a connection to the MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kpop_site"
        )

        # Create a cursor object to interact with the database
        cursor = mydb.cursor()

        # Deleting data from the table
        sql = "DELETE FROM `memship_details` WHERE member_ID=%s"
        val = (member_ID,)

        try:
            cursor.execute(sql, val)
            mydb.commit()
            print("Data deleted successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()

        cursor.close()
        mydb.close()

        messagebox.showinfo("Delete Successful", "Member information deleted successfully.")

    def delete_member_gui(self):
        # Prompt the user for Member ID
        member_id_to_delete = simpledialog.askstring("Delete Member", "Enter Member ID to delete:")

        if member_id_to_delete:
            # Call the delete_member method
            self.delete_member(member_id_to_delete)

            # Clear existing content in data display box
            self.data_display_box.config(state='normal')
            self.data_display_box.delete(1.0, tk.END)
            self.data_display_box.config(state='disabled')

    def quit_application(self):
        self.master.quit()

    def show_help_ticket(self):
        # Help text button for ticketing window
        help_text_tic = """
        How to register for BABELPAWP's ticketing?

        Fill in the following information:
        - Name: Your full name.
        - Email (xxx@xxx.xxx): Your email address.
        - Phone number (+60 only): Your phone number, which 
          must start with '60', as this membership is only valid for 
          Malaysians.
        - Membership ID : Only insert the membership ID that 
          has been registered in the Membership Registration 
          section.
        - RM 50 per ticket
        - DISCOUNT 10% IS APPLIED WHEN CUSTOMER 
          PURCHASED MORE THAN 3 TICKETS

        After filling in the details, click the 'Enter' button to 
        complete the registration.

        If you encounter any issues, reach out to our support 
        team on either of these contacts below.
        
        Phone number: +601133228274
        e-mail: babelpawp@gmail.com

        Thank you for supporting BABELPAWP!
        """

        messagebox.showinfo("Help", help_text_tic)

    def open_ticketing_gui(self):
        ticket_window = tk.Toplevel(self.master)
        ticket_window.title("Ticket purchase")
        ticket_window.geometry("680x420")

        # Create a title label
        title_label = tk.Label(ticket_window, text='TICKETING SYSTEM', font=("constantia", 16, "bold"), fg='black', bg='lightcoral')
        title_label.grid(row=0, column=0,columnspan=5, ipadx=240)

        self.ticket_price = 50.0
        self.total_cost = 0.0
        self.discount_percentage = 0.0

        # Create labels and entry widgets for personal details
        labels = ["NAME", "EMAIL", "PHONE NO", "MEMBERSHIP ID", "TOTAL TICKETS"]
        for i, label_text in enumerate(labels):
            tk.Label(ticket_window, text=f"{label_text}:", font=("Times", 10, "bold"), fg='gray9', bg='mistyrose').grid(row=i+2, column=0, padx=5, pady=5,sticky="e")

        self.entry_name = tk.Entry(ticket_window)
        self.entry_email = tk.Entry(ticket_window)
        self.entry_phone = tk.Entry(ticket_window)
        self.entry_membershipid = tk.Entry(ticket_window)
        self.entry_num_tickets = tk.Entry(ticket_window)

        entries = [self.entry_name, self.entry_email, self.entry_phone, self.entry_membershipid, self.entry_num_tickets]
        for i, entry_widget in enumerate(entries):
            entry_widget.grid(row=i+2, column=1, padx=10, pady=5, sticky="ew")

        # Create button to calculate total cost
        calculate_button = tk.Button(ticket_window, text="ENTER", font=("Times", 10, "bold"), fg='black', bg='lightpink1', padx=40, pady=20, command=self.calculate_total_ticket)
        calculate_button.grid(row=8, column=0, rowspan=2, pady=5,sticky='e')

        # Create button to update data in the table
        update_button = tk.Button(ticket_window, text="UPDATE", font=("Times", 10, "bold"), fg='black', bg='lightpink2', padx=40, pady=20, command=self.update_ticket)
        update_button.grid(row=8, column=1,rowspan=2, pady=5,padx=10,sticky="sw")

        # Create button to delete data from the table
        delete_button = tk.Button(ticket_window, text="DELETE", font=("Times", 10, "bold"), fg='black', bg='lightpink3', padx=40, pady=20, command=self.delete_ticket)
        delete_button.grid(row=10, column=0,columnspan=2,rowspan=2, pady=5)

        # Help and quit button with grid
        help_button = tk.Button(ticket_window, text="Help", command=self.show_help_ticket, font=("Times New Roman", 10), bg="lightpink4", fg="white",padx=11,pady=2)
        help_button.grid(row=10,column=2,pady=2)
        quit_button = tk.Button(ticket_window, text="Back", command=ticket_window.destroy, font=("Times New Roman", 10), bg="lightpink4", fg="white",padx=10,pady=2)
        quit_button.grid(row=11, column=2, pady=2)

        # Create billing area
        bill_frame = tk.Frame(ticket_window, bd=8, relief='groove')
        bill_frame.grid(row=1, column=2, ipadx=8, ipady=14, padx=15, pady=10, rowspan=9)
        bill_area_label = tk.Label(bill_frame, text='RECEIPTS', font=('Times New Roman', 13, 'bold'), fg='brown')
        bill_area_label.grid(row=0, column=0, pady=(0, 5))
        self.text_area = tk.Text(bill_frame, width=24, height=13)
        self.text_area.grid(row=1, column=0, sticky='ew')

    def calculate_total_ticket(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kpop_site"
        )

        # Create a cursor object to interact with the database
        cursor = mydb.cursor()

        # User input
        name_ticket = self.entry_name.get()
        email_ticket = self.entry_email.get()
        phone_ticket = self.entry_phone.get()
        memid_ticket = self.entry_membershipid.get()
        numtic_ticket = self.entry_num_tickets.get()

        # Validate input
        if not name_ticket or not email_ticket or not phone_ticket or not memid_ticket or not numtic_ticket:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        # Check if name contains only alphabetic characters
        if not name_ticket.replace(" ", "").isalpha():
            messagebox.showerror("Invalid", "Name must contain only alphabetic characters.")
            return

        elif not phone_ticket.startswith("60") or not phone_ticket[3:].isdigit():
            messagebox.showerror("Invalid", "Phone number must start with '+60' and contain only numeric values.")
            return

        # Check email format using a regular expression
        email_pattern = re.compile(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
        if not email_pattern.match(email_ticket):
            messagebox.showerror("Invalid", "Invalid email format. Please use the format xxx@xxx.xxx.")
            return
        
        try:
            num_tickets_str = self.entry_num_tickets.get()

            if not num_tickets_str.isdigit():
                messagebox.showerror("Error", "Please enter a valid number of tickets.")
                return

            num_tickets = int(num_tickets_str)

            if num_tickets > 0 and num_tickets <= 10:
                self.total_cost = self.ticket_price * num_tickets
                self.discount_percentage = self.calculate_discount_ticket(num_tickets)
                discounted_amount = (self.discount_percentage / 100) * self.total_cost
                discounted_cost = self.total_cost - discounted_amount

                details_text = f"Name: {self.entry_name.get()}\nEmail: {self.entry_email.get()}\n"
                details_text += f"Phone: {self.entry_phone.get()}\nMembership ID: {self.entry_membershipid.get()}\n"
                details_text += f"Total Tickets: {num_tickets}\n"
                details_text += f"Cost: RM{self.total_cost:.2f}\nDiscount: {self.discount_percentage}%\n"
                details_text += f"TOTAL: RM{discounted_cost:.2f}"
                bill_text = details_text
                self.text_area.insert(tk.END, bill_text)
                self.text_area.configure(state='disabled')

                # Inserting data into a table
                sql = "INSERT INTO `cust_details` (cust_name, cust_email, cust_phone, membership_id, total_ticket, TOTAL) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (self.entry_name.get(), self.entry_email.get(), self.entry_phone.get(), self.entry_membershipid.get(), self.entry_num_tickets.get(), discounted_cost)

                try:
                    cursor.execute(sql, val)
                    mydb.commit()
                    print("Data inserted successfully!")
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    mydb.rollback()
            else:
                messagebox.showerror("Error", "Please enter a valid number of tickets (greater than 0 and less than or equal to 10).")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")
    
        finally:
        # Close the cursor and the connection after finishing all database operations
            cursor.close()
            mydb.close()

    def calculate_discount_ticket(self, num_tickets):
        if num_tickets >= 3:
            return 10  # 10% discount for 3 or more tickets
        else:
            return 0   # No discount for fewer than 3 tickets

    def update_ticket(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kpop_site"
        )

        # Create a cursor object to interact with the database
        cursor = mydb.cursor()

        try:
            new_name = self.entry_name.get()
            new_email = self.entry_email.get()
            new_phone = self.entry_phone.get()

            # Updating data in the table
            sql = "UPDATE `cust_details` SET cust_name=%s, cust_email=%s WHERE cust_phone=%s"
            val = (new_name, new_email, new_phone)

            cursor.execute(sql, val)
            mydb.commit()
            print("Data updated successfully!")

            # Fetch the updated data from the database
            select_sql = "SELECT * FROM `cust_details` WHERE cust_phone=%s"
            select_val = (new_phone,)

            cursor.execute(select_sql, select_val)
            updated_data = cursor.fetchone()

            if updated_data:
                # Update the billing area with the updated data
                details_text = f"Name: {updated_data[1]}\nEmail: {updated_data[2]}\n"
                details_text += f"Phone: {updated_data[3]}\nMembership ID: {updated_data[4]}\n"
                details_text += f"Total Tickets: {updated_data[5]}\n"
                details_text += f"Cost: RM{updated_data[6]:.2f}\nDiscount: {self.discount_percentage}%\n"
                details_text += f"TOTAL: RM{updated_data[7]:.2f}"

                # Clear the existing content in the billing area and insert the updated data
                self.text_area.configure(state='normal')
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, details_text)
                self.text_area.configure(state='disabled')

                # Optional: Display a message to the user indicating a successful update
                messagebox.showinfo("Success", "Data updated successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()
            # Optional: Display an error message to the user
            messagebox.showerror("Error", f"Error updating data: {err}")

        finally:
            # Close the cursor and the connection when the application is closed
            cursor.close()
            mydb.close()

    def delete_ticket(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kpop_site"
        )

        # Create a cursor object to interact with the database
        cursor = mydb.cursor()

        try:

            # Deleting data from the table
            sql = "DELETE FROM `cust_details` WHERE cust_name=%s"
            val = (self.entry_name.get(),)

            cursor.execute(sql, val)
            mydb.commit()
            print("Data deleted successfully!")

            # Optional: Display a message to the user indicating a successful delete
            messagebox.showinfo("Success", "Data deleted successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()
            # Optional: Display an error message to the user
            messagebox.showerror("Error", f"Error deleting data: {err}")

        # Close the cursor and the connection when the application is closed
        cursor.close()
        mydb.close()

    def show_help_fan(self):
        # Help text button for fanmeeting registration window
        help_text_fan = """
        How to register for PAWPAWP FANMEETING?

        Fill in the following information:
        - Name: Your full name.
        - ID number: Your identification number.
        - Email (xxx@xxx.xxx): Your email address.
        - Membership ID: Your Babelpawp Membership ID.
        - Fanmeetings are available for members only.
          If you don't have a Membership ID, please press
          the back button and proceed to register as a
          member first. 
        - Choose the number of ticket you want to buy 
          (limited to 5 ticket per purchase)
        - 1 ticket = RM150

        After filling in the details, click the 'Enter' button to 
        complete the purchasing.

        If you encounter any issues, reach out to our support 
        team on either of these contacts below.
        
        Phone number: +601133228274
        e-mail: babelpawp@gmail.com

        Thank you for supporting BABELPAWP!
        """

        messagebox.showinfo("Help", help_text_fan)
        
    def open_fanmeeting_gui(self):
        # GUI
        fanmeeting_window = tk.Toplevel(self.master)
        fanmeeting_window.title("Fanmeet booking")
        fanmeeting_window.geometry("485x520")

        # GUI label
        label= tk.Label(fanmeeting_window, text='PAWPAWP FANMEETING',font=('Georgia Font', 20, 'italic'),bg='magenta4',fg='mistyrose',bd=10, relief='groove')
        label.pack(ipadx=480) 

        # Customer details frame
        customer_details_frame=tk.LabelFrame(fanmeeting_window,text='Customer Details',font=('Times New Roman',10,'bold'),bg='thistle2',fg= 'purple4',bd=5,relief= 'groove')
        customer_details_frame.pack(ipadx=470)

        # Name 
        self.nameLabel=tk.Label(customer_details_frame,text='Name',font=('Times New Roman',10,'bold'),bg='thistle2',fg= 'magenta4')
        self.nameLabel.grid (row=0,column=0,ipadx=5,ipady=5)
        self.nameEntry=tk.Entry(customer_details_frame,font=('Times New Roman', 10),bd=3)
        self.nameEntry.grid (row=0,column=1,ipadx=17)

        # Email
        self.emailLabel=tk.Label(customer_details_frame,text='Email',font=('Times New Roman',10,'bold'),bg='thistle2',fg= 'magenta4')
        self.emailLabel.grid(row=1,column=0,ipadx=5,ipady=5)
        self.emailEntry=tk.Entry(customer_details_frame,font=('Times New Roman', 10),bd=3)
        self.emailEntry.grid (row=1,column=1,ipadx=17)

        # Membership ID 
        self.membershipLabel=tk.Label(customer_details_frame,text='Member ID',font=('Times New Roman',10,'bold'),bg='thistle2',fg= 'magenta4')
        self.membershipLabel.grid(row=0,column=2,ipadx=3,ipady=5)
        self.membershipEntry=tk.Entry(customer_details_frame,font=('Times New Roman', 10),bd=3)
        self.membershipEntry.grid (row=0,column=3,ipadx=20)

        # Ticket number
        self.ticketLabel=tk.Label(customer_details_frame,text='Ticket amount',font=('Times New Roman',10,'bold'),bg='thistle2',fg= 'magenta4')
        self.ticketLabel.grid(row=1,column=2,ipadx=3,ipady=5)
        self.ticket_spinbox = ttk.Spinbox(customer_details_frame, values=["1", "2", "3","4","5"])
        self.ticket_spinbox.grid(row=1,column=3,ipadx=15)

        # Ticket bill frame
        self.ticketframe=tk.LabelFrame(fanmeeting_window,text='Ticket bill',font=('Times New Roman',10,'bold'),bg='thistle2',fg= 'purple4',bd=5,relief= 'groove')
        self.ticketframe.pack(ipadx=470)

        # Enter frame
        self.enterbuttonFrame=tk.Frame(self.ticketframe,bd=8,relief='groove')
        self.enterbuttonFrame.grid(row=2,column=0,padx=5,pady=20)
        self.enterButton=tk.Button(self.ticketframe,text='ENTER',font=('Times New Roman',10,'bold'),bd=5,bg='thistle2',fg= 'magenta4',padx=50,pady=10,command=self.register_fan)
        self.enterButton.grid(row=2,column=0,pady=20, padx=5, columnspan=2)
        
        # Update frame
        self.updatebuttonFrame=tk.Frame(self.ticketframe,bd=8,relief='groove')
        self.updatebuttonFrame.grid(row=3,column=0,padx=5,pady=20)
        self.updatebutton=tk.Button(self.ticketframe, text="UPDATE", font=('Times New Roman',10,'bold'),bd=5,bg='thistle2',fg= 'magenta4',padx=50,pady=10, command=self.update_fan_gui)
        self.updatebutton.grid(row=3,column=0,pady=20,padx=5,columnspan=2)

        # Delete Frame
        self.deletebuttonFrame=tk.Frame(self.ticketframe,bd=8,relief='groove')
        self.deletebuttonFrame.grid(row=4,column=0,padx=5,pady=20)
        self.deleteButton=tk.Button(self.ticketframe,text='DELETE',font=('Times New Roman',10,'bold'),bd=5,bg='thistle2',fg= 'magenta4',padx=50,pady=10,command=self.delete_fan_gui)
        self.deleteButton.grid(row=4,column=0,pady=20, padx=5, columnspan=2)

        # Bill frame
        self.billframe=tk.Frame(self.ticketframe,bd=8,bg='thistle1',relief='groove')
        self.billframe.grid(row=0,column=2,ipadx=5,pady=5,padx=10,rowspan=20)
        self.billareaLabel=tk.Label(self.billframe,text='TOTAL',font=('Times New Roman',10,'bold'),bg='thistle1',fg= 'magenta4')
        self.billareaLabel.pack()
        self.scrollbar=tk.Scrollbar(self.billframe,orient='vertical')
        self.scrollbar.pack(side='right', fill='y')
        self.textareafan=tk.Text(self.billframe,width=30,height=15)
        self.textareafan.pack(ipady=5)
        self.scrollbar.config(command=self.textareafan.yview)

        # Disable the text area
        self.textareafan.config(state='disabled')

        # Help, register, and quit button frame
        button_frame=tk.LabelFrame(fanmeeting_window, bg='thistle1', bd=8, relief='groove')
        button_frame.pack(ipadx=470)

        # Help and quit button with grid
        help_button = tk.Button(button_frame, text="Help", command=self.show_help_fan, font=("Times New Roman", 12), bg="magenta4", fg="white")
        help_button.grid(row=0, column=0, pady=5, padx=80, ipadx=30, sticky="ew")
        quit_button = tk.Button(button_frame, text="Back", command=fanmeeting_window.destroy, font=("Times New Roman", 12), bg="magenta4", fg="white")
        quit_button.grid(row=0, column=1, pady=5, padx=1, ipadx=30, sticky="ew")

    # Calculation
    def register_fan(self):
        name_fan = self.nameEntry.get()
        email_fan = self.emailEntry.get()
        numtic_fan = self.ticket_spinbox.get()
        memid_fan = self.membershipEntry.get()

        if not name_fan or not email_fan or not numtic_fan or not memid_fan:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Check if name contains only alphabetic characters
        if not name_fan.replace(" ", "").isalpha():
            messagebox.showerror("Invalid", "Name must contain only alphabetic characters.")
            return

        # Check email format using a regular expression
        email_pattern = re.compile(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
        if not email_pattern.match(email_fan):
            messagebox.showerror("Invalid", "Invalid email format. Please use the format xxx@xxx.xxx.")
            return
        
        try:
            ticket_price = 150
            num_tickets = int(self.ticket_spinbox.get())
            total_cost = num_tickets * ticket_price
            

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of tickets.")
            return
        
        # Generate a random alphanumeric Ticket ID
        fantic_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Display registration information in a message box
        fan_success_message = f"Purchase Successful!\n\nTicket ID: {fantic_id}\nName: {name_fan}\nEmail: {email_fan}\nMembership ID: {memid_fan}\nNumber of tickets: {numtic_fan}\nTotal cost: {total_cost}"
        messagebox.showinfo("Purchase Successful", fan_success_message)

        self.textareafan.config(state='normal')
        self.textareafan.insert(tk.END, fan_success_message + '\n\n')
        self.textareafan.config(state='disabled')

        self.insert_into_database_fan(fantic_id, name_fan, email_fan, memid_fan, numtic_fan, total_cost)

    def insert_into_database_fan(self, fantic_id, name_fan, email_fan, memid_fan, numtic_fan, total_cost):
    # Establish a connection to the MySQL server
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kpop_site"
            )

            # Create a cursor object to interact with the database
            cursor = mydb.cursor()

            # Inserting data into a table
            sql = "INSERT INTO `fm_details` (Ticket_ID, Name, Email, Membership_ID, Number_of_Tickets, Total_Cost) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (fantic_id, name_fan, email_fan, memid_fan, numtic_fan, total_cost)

            cursor.execute(sql, val)
            mydb.commit()
            print("Data inserted successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()
            cursor.close()
            mydb.close()
            return

        finally:
            cursor.close()
            mydb.close()

    def update_fan(self, fantic_id):
        # User input new entry
        newname_fan = self.nameEntry.get()
        newmemid_fan = self.membershipEntry.get()
        newemail_fan = self.emailEntry.get()
        newnumtic_fan = self.ticket_spinbox.get()

        if not fantic_id or not newname_fan or not newmemid_fan or not newemail_fan or not newnumtic_fan:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Check if name contains only alphabetic characters
        if not newname_fan.replace(" ", "").isalpha():
            messagebox.showerror("Invalid", "Name must contain only alphabetic characters.")
            return

        # Check email format using a regular expression
        email_pattern = re.compile(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
        if not email_pattern.match(newemail_fan):
            messagebox.showerror("Invalid", "Invalid email format. Please use the format xxx@xxx.xxx.")
            return
        
        try:
            ticket_price = 150
            newnumtic_fan = int(self.ticket_spinbox.get())
            total_cost = newnumtic_fan * ticket_price
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of tickets.")
            return
        
        # Establish a connection to the MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kpop_site"
        )

        # Create a cursor object to interact with the database
        cursor = mydb.cursor()
        
        # Fetch the updated data from the database
        cursor.execute("SELECT * FROM `fm_details` WHERE Ticket_ID=%s", (fantic_id,))
        updated_fan_info = cursor.fetchone()
        
        # UPDATE SQL statement
        sql = "UPDATE `fm_details` SET `Name`= %s, `Email`= %s, `Membership_ID`= %s, `Number_of_Tickets`= %s, `Total_Cost`= %s WHERE Ticket_ID=%s"
        val = (newname_fan, newemail_fan, newmemid_fan, newnumtic_fan, total_cost, fantic_id)

        try:
            cursor.execute(sql, val)
            mydb.commit()
            print("Data updated successfully!")

            # Fetch the updated data from the database
            cursor.execute("SELECT * FROM `fm_details` WHERE Ticket_ID=%s", (fantic_id,))
            updated_fan_info = cursor.fetchone()
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()

        finally:
            # Close the cursor and the connection when the application is closed
            cursor.close()
            mydb.close()

        # Display a message to the user indicating a successful update
        messagebox.showinfo("Update Successful", "Data updated successfully!")

        # Return the updated member information
        return updated_fan_info

    def update_fan_gui(self):
        # Prompt the user for Ticket ID to update
        fantic_id_to_update = simpledialog.askstring("Update Fan", "Enter Ticket ID to update:")

        if fantic_id_to_update is not None:
            # Call the update_fan method
            updated_fan_info = self.update_fan(fantic_id_to_update)

            if updated_fan_info:
                # Clear existing content in data display box
                self.textareafan.config(state='normal')
                self.textareafan.delete(1.0, tk.END)

                # Display updated member information in the bill area
                updated_fan_info_str = (
                    f"Updated Member Information:\n\n"
                    f"Ticket ID: {updated_fan_info[0]}\n"
                    f"Name: {updated_fan_info[1]}\n"
                    f"Email: {updated_fan_info[2]}\n"
                    f"Member ID: {updated_fan_info[3]}\n"
                    f"Number of Tickets: {updated_fan_info[4]}\n"
                    f"Total Cost: {updated_fan_info[5]}"
                )

                self.textareafan.insert(tk.END, updated_fan_info_str)
                self.textareafan.config(state='disabled')

    def delete_fan(self, fantic_id):
        # Validate input
        if not fantic_id:
            messagebox.showerror("Error", "Please fill in the Ticket ID.")
            return

        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kpop_site"
        )

        # Create a cursor object to interact with the database
        cursor = mydb.cursor()

        
        try:
            # Deleting data from the table based on Ticket ID
            sql = "DELETE FROM fm_details WHERE Ticket_ID=%s"
            val = (fantic_id,)

            cursor.execute(sql, val)
            mydb.commit()
            print("Data deleted successfully!")

            # Display a message to the user indicating a successful delete
            messagebox.showinfo("Success", "Data deleted successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()

            # Optional: Display an error message to the user
            messagebox.showerror("Error", f"Error deleting data: {err}")

        finally:
            # Close the cursor and the connection when the application is closed
            cursor.close()
            mydb.close()


    def delete_fan_gui(self):
        # Prompt the user for Membership ID to delete
        fantic_id_to_delete = simpledialog.askstring("Delete Fan", "Enter Ticket ID to delete:")

        if fantic_id_to_delete:
            # Call the delete_fan method
            self.delete_fan(fantic_id_to_delete)

            # Clear existing content in data display box
            self.textareafan.config(state='normal')
            self.textareafan.delete(1.0, tk.END)
            self.textareafan.config(state='disabled')

    def quit_application(self):
        self.master.quit()


def main():
    root = tk.Tk()
    app: KpopPurchasingSystem = KpopPurchasingSystem(root)
    app.master.mainloop()

if __name__ == "__main__":
    main()
