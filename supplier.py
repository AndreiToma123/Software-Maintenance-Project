from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+320+220")
        self.root.config(bg="white")
        self.root.resizable(False,False)
        self.root.focus_force()

        #------------ all variables --------------
        self.var_search_field = StringVar()
        self.var_search_querry = StringVar()
        self.var_invoice_number = StringVar()
        self.var_supplier_name = StringVar()
        self.var_contact_number = StringVar()
        
        
        #---------- Search Frame -------------
        search_by_label = Label(self.root,text="Invoice No.",bg="white",font=("goudy old style",15))
        search_by_label.place(x = 700,y = 80)

        search_by_text = Entry(self.root,textvariable = self.var_search_querry,font=("goudy old style",15),bg="lightyellow").place(x = 850,y = 80,width = 160)
        search_button = Button(self.root,command = self.search,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x = 980,y = 79,width = 100,height = 28)

        #-------------- title ---------------
        title = Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x = 50,y = 10,width = 1000,height = 40)

        #-------------- content ---------------
        #---------- row 1 ----------------
        label_supplier_invoice = Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x = 50,y = 80)
        text_supplier_invoice = Entry(self.root,textvariable = self.var_invoice_number,font=("goudy old style",15),bg="lightyellow").place(x = 180,y = 80,width = 180)
        
        #---------- row 2 ----------------
        label_name = Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x = 50,y = 120)
        text_name = Entry(self.root,textvariable = self.var_supplier_name,font=("goudy old style",15),bg="lightyellow").place(x = 180,y = 120,width = 180)
        
        #---------- row 3 ----------------
        label_contact = Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x = 50,y = 160)
        text_contact = Entry(self.root,textvariable = self.var_contact_number,font=("goudy old style",15),bg="lightyellow").place(x = 180,y = 160,width = 180)
        
        #---------- row 4 ----------------
        label_description = Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x = 50,y = 200)
        self.text_description = Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.text_description.place(x = 180,y = 200,width = 470,height = 120)
        
        #-------------- buttons -----------------
        button_add = Button(self.root,text="Save",command = self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x = 180,y = 370,width = 110,height = 35)
        button_update = Button(self.root,text="Update",command = self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x = 300,y = 370,width = 110,height = 35)
        button_delete = Button(self.root,text="Delete",command = self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x = 420,y = 370,width = 110,height = 35)
        button_clear = Button(self.root,text="Clear",command = self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x = 540,y = 370,width = 110,height = 35)

        #------------ supplier details -------------
        supplier_frame = Frame(self.root,bd = 3,relief = RIDGE)
        supplier_frame.place(x = 700,y = 120,width = 380,height = 350)

        scrolly = Scrollbar(supplier_frame,orient = VERTICAL)
        scrollx = Scrollbar(supplier_frame,orient = HORIZONTAL)\
        
        self.SupplierTable = ttk.Treeview(supplier_frame,columns=("invoice","name","contact","desc"),yscrollcommand = scrolly.set,xscrollcommand = scrollx.set)
        scrollx.pack(side = BOTTOM,fill = X)
        scrolly.pack(side = RIGHT,fill = Y)
        scrollx.config(command = self.SupplierTable.xview)
        scrolly.config(command = self.SupplierTable.yview)
        self.SupplierTable.heading("invoice",text="Invoice")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("desc",text="Description")
        self.SupplierTable["show"]="headings"
        self.SupplierTable.column("invoice",width = 90)
        self.SupplierTable.column("name",width = 100)
        self.SupplierTable.column("contact",width = 100)
        self.SupplierTable.column("desc",width = 100)
        
        self.SupplierTable.pack(fill = BOTH,expand = 1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#-----------------------------------------------------------------------------------------------------
    def add(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_invoice_number.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent = self.root)
            else:
                db_cursor.execute("Select * from supplier where invoice=?",(self.var_invoice_number.get(),))
                row = db_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error","Invoice no. is already assigned",parent = self.root)
                else:
                    db_cursor.execute("insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",(
                        self.var_invoice_number.get(),
                        self.var_supplier_name.get(),
                        self.var_contact_number.get(),
                        self.text_description.get('1.0',END),
                    ))
                    db_connection.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent = self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def show(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            db_cursor.execute("select * from supplier")
            rows = db_cursor.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):
        focused_item = self.SupplierTable.focus()
        content=(self.SupplierTable.item(focused_item))
        row = content['values']
        self.var_invoice_number.set(row[0])
        self.var_supplier_name.set(row[1])
        self.var_contact_number.set(row[2])
        self.text_description.delete('1.0',END)
        self.text_description.insert(END,row[3])

    def update(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_invoice_number.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent = self.root)
            else:
                db_cursor.execute("Select * from supplier where invoice=?",(self.var_invoice_number.get(),))
                row = db_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent = self.root)
                else:
                    db_cursor.execute("update supplier set name=?,contact=?,desc=? where invoice=?",(
                        self.var_supplier_name.get(),
                        self.var_contact_number.get(),
                        self.text_description.get('1.0',END),
                        self.var_invoice_number.get(),
                    ))
                    db_connection.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def delete(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_invoice_number.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent = self.root)
            else:
                db_cursor.execute("Select * from supplier where invoice=?",(self.var_invoice_number.get(),))
                row = db_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent = self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete?",parent = self.root)
                    if op == True:
                        db_cursor.execute("delete from supplier where invoice=?",(self.var_invoice_number.get(),))
                        db_connection.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent = self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def clear(self):
        self.var_invoice_number.set("")
        self.var_supplier_name.set("")
        self.var_contact_number.set("")
        self.text_description.delete('1.0',END)
        self.var_search_querry.set("")
        self.show()

    def search(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_search_querry.get()=="":
                messagebox.showerror("Error","Invoice No. should be required",parent = self.root)
            else:
                db_cursor.execute("select * from supplier where invoice=?",(self.var_search_querry.get(),))
                row = db_cursor.fetchone()
                if row != None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values = row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


if __name__=="__main__":
    root = Tk()
    object_supplier = supplierClass(root)
    root.mainloop()