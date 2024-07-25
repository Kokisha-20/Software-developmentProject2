import tkinter as tk
from tkinter import messagebox,simpledialog
import json
import os
class ContactManagementSystem:
    def __init__(self,master):
        self.master = master
        master.title("CONTACT MANAGEMENT SYSTEM")
        self.contacts = {}
        self.load_contacts()
        self.name_label = tk.Label(master,text="Name:")
        self.name_label.grid(row=0,column=0)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0,column=1)
        self.phone_label = tk.Label(master,text="Phone:")
        self.phone_label.grid(row=1,column=0)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1,column=1)
        self.email_label = tk.Label(master,text="Email:")
        self.email_label.grid(row=2,column=0)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2,column=1)
        self.add_button = tk.Button(master,text="Add Contact",command=self.add_contact)
        self.add_button.grid(row=3,column=0,columnspan=2)
        self.view_button = tk.Button(master,text="View Contacts",command=self.view_contacts)
        self.view_button.grid(row=4,column=0,columnspan=2)
        self.edit_button = tk.Button(master,text="Edit Contact",command=self.edit_contact)
        self.edit_button.grid(row=5,column=0,columnspan=2)
        self.delete_button = tk.Button(master,text="Delete Contact",command=self.delete_contact)
        self.delete_button.grid(row=6,column=0,columnspan=2)
    def load_contacts(self):
        if os.path.exists("Contacts.json"):
            with open("contacts.json","r")as file:
                self.contacts = json.load(file)
    def save_contacts(self):
        with open("contacts.json","w")as file:
            json.dump(self.contacts,file)
    def add_contact(self):
        name=self.name_entry.get()
        phone=self.phone_entry.get()
        email=self.email_entry.get()
        if name and phone and email:
            self.contacts[name] = {"phone":phone,"email":email}
            self.save_contacts()
            messagebox.showinfo("Success","Contact added successfully!")
            self.clear_entities()
        else:
            messagebox.showwarning("Input Error","Please fill all fields")
    def view_contacts(self):
        contacts_str = "\n".join([f"Name:{name},Phone:{details['phone']},Email:{details['email']}"for name,details in self.contacts.items()])
        messagebox.showinfo("Contact List",contacts_str or "No contacts available")
    def edit_contact(self):
        name=simpledialog.askstring("Edit Contact","Enter the name of the contact to edit:")
        if name in self.contacts:
            phone = simpledialog.askstring("Edit Contact","Enter the new phone number:")
            email = simpledialog.askstring("Edit Contact","Enter the new email address:")
            if phone and email:
                self.contacts[name] = {"phone":phone,"email":email}
                self.save_contacts()
                messagebox.showinfo("Success","Contact updated successfully!")
            else:
                messagebox.showwarning("Input Error","Please fill all fields")
        else:
            messagebox.showwarning("Error","Contact not found")
    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact","Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            messagebox.showinfo("Success","Contact deleted successfully!")
        else:
            messagebox.showwarning("Error","Contact not found")
    def clear_entities(self):
        self.name_entry.delete(0,tk.END)
        self.phone_entry.delete(0,tk.END)
        self.email_entry.delete(0,tk.END)
root = tk.Tk()
contact_management_system = ContactManagementSystem(root)
root.mainloop()