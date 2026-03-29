from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+320+220")
        self.root.config(bg="white")
        self.root.resizable(False,False)
        self.root.focus_force()
        #---------------------------------------
        #----------- variables -------------
        self.var_category = StringVar()
        self.category_list=[]
        self.supplier_list=[]
        self.fetch_category_and_supplier()
        self.var_product_id = StringVar()
        self.var_supplier = StringVar()
        self.var_product_name = StringVar()
        self.var_product_price = StringVar()
        self.var_product_quantity = StringVar()
        self.var_product_status = StringVar()
        self.var_search_field = StringVar()
        self.var_search_querry = StringVar()

        product_Frame = Frame(self.root,bd = 2,relief = RIDGE,bg="white")
        product_Frame.place(x = 10,y = 10,width = 450,height = 480)

        #------------ title --------------
        title = Label(product_Frame,text="Manage Product Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side = TOP,fill = X)

        label_category = Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x = 30,y = 60)
        label_supplier = Label(product_Frame,text="Supplier",font=("goudy old style",18),bg="white").place(x = 30,y = 110)
        label_product_name = Label(product_Frame,text="Name",font=("goudy old style",18),bg="white").place(x = 30,y = 160)
        label_price = Label(product_Frame,text="Price",font=("goudy old style",18),bg="white").place(x = 30,y = 210)
        label_quantity = Label(product_Frame,text="Quantity",font=("goudy old style",18),bg="white").place(x = 30,y = 260)
        label_status = Label(product_Frame,text="Status",font=("goudy old style",18),bg="white").place(x = 30,y = 310)

        cmb_category = ttk.Combobox(product_Frame,textvariable = self.var_category,values = self.category_list,state='readonly',justify = CENTER,font=("goudy old style",15))
        cmb_category.place(x = 150,y = 60,width = 200)
        cmb_category.current(0)

        cmb_supplier = ttk.Combobox(product_Frame,textvariable = self.var_supplier,values = self.supplier_list,state='readonly',justify = CENTER,font=("goudy old style",15))
        cmb_supplier.place(x = 150,y = 110,width = 200)
        cmb_supplier.current(0)

        text_product_name = Entry(product_Frame,textvariable = self.var_product_name,font=("goudy old style",15),bg="lightyellow").place(x = 150,y = 160,width = 200)
        text_product_price = Entry(product_Frame,textvariable = self.var_product_price,font=("goudy old style",15),bg="lightyellow").place(x = 150,y = 210,width = 200)
        text_product_quantity = Entry(product_Frame,textvariable = self.var_product_quantity,font=("goudy old style",15),bg="lightyellow").place(x = 150,y = 260,width = 200)

        cmb_product_status = ttk.Combobox(product_Frame,textvariable = self.var_product_status,values=("Active","Inactive"),state='readonly',justify = CENTER,font=("goudy old style",15))
        cmb_product_status.place(x = 150,y = 310,width = 200)
        cmb_product_status.current(0)

        #-------------- buttons -----------------
        button_add = Button(product_Frame,text="Save",command = self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x = 10,y = 400,width = 100,height = 40)
        button_update = Button(product_Frame,text="Update",command = self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x = 120,y = 400,width = 100,height = 40)
        button_delete = Button(product_Frame,text="Delete",command = self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x = 230,y = 400,width = 100,height = 40)
        button_clear = Button(product_Frame,text="Clear",command = self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x = 340,y = 400,width = 100,height = 40)

        #---------- Search Frame -------------
        SearchFrame = LabelFrame(self.root,text="Search Product",font=("goudy old style",12,"bold"),bd = 2,relief = RIDGE,bg="white")
        SearchFrame.place(x = 480,y = 10,width = 600,height = 80)

        #------------ options ----------------
        cmb_search = ttk.Combobox(SearchFrame,textvariable = self.var_search_field,values=("Select","Category","Supplier","Name"),state='readonly',justify = CENTER,font=("goudy old style",15))
        cmb_search.place(x = 10,y = 10,width = 180)
        cmb_search.current(0)

        text_search = Entry(SearchFrame,textvariable = self.var_search_querry,font=("goudy old style",15),bg="lightyellow").place(x = 200,y = 10)
        btn_search = Button(SearchFrame,text="Search",command = self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x = 410,y = 9,width = 150,height = 30)

        #------------ product details -------------
        product_frame = Frame(self.root,bd = 3,relief = RIDGE)
        product_frame.place(x = 480,y = 100,width = 600,height = 390)

        scrolly = Scrollbar(product_frame,orient = VERTICAL)
        scrollx = Scrollbar(product_frame,orient = HORIZONTAL)\
        
        self.ProductTable = ttk.Treeview(product_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand = scrolly.set,xscrollcommand = scrollx.set)
        scrollx.pack(side = BOTTOM,fill = X)
        scrolly.pack(side = RIGHT,fill = Y)
        scrollx.config(command = self.ProductTable.xview)
        scrolly.config(command = self.ProductTable.yview)
        self.ProductTable.heading("pid",text="P ID")
        self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("Supplier",text="Suppler")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="Quantity")
        self.ProductTable.heading("status",text="Status")
        self.ProductTable["show"]="headings"
        self.ProductTable.column("pid",width = 90)
        self.ProductTable.column("Category",width = 100)
        self.ProductTable.column("Supplier",width = 100)
        self.ProductTable.column("name",width = 100)
        self.ProductTable.column("price",width = 100)
        self.ProductTable.column("qty",width = 100)
        self.ProductTable.column("status",width = 100)
        
        self.ProductTable.pack(fill = BOTH,expand = 1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_category_and_supplier()
#-----------------------------------------------------------------------------------------------------
    def fetch_category_and_supplier(self):
        self.category_list.append("Empty")
        self.supplier_list.append("Empty")
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            db_cursor.execute("select name from category")
            category = db_cursor.fetchall()
            if len(category)>0:
                del self.category_list[:]
                self.category_list.append("Select")
                for i in category:
                    self.category_list.append(i[0])
            db_cursor.execute("select name from supplier")
            supplier = db_cursor.fetchall()
            if len(supplier)>0:
                del self.supplier_list[:]
                self.supplier_list.append("Select")
                for i in supplier:
                    self.supplier_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    
    
    def add(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_category.get()=="Select" or self.var_category.get()=="Empty" or self.var_supplier=="Select" or self.var_supplier=="Empty":
                messagebox.showerror("Error","All fields are required",parent = self.root)
            else:
                db_cursor.execute("Select * from product where name=?",(self.var_product_name.get(),))
                row = db_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error","Product already present",parent = self.root)
                else:
                    db_cursor.execute("insert into product(Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_product_name.get(),
                        self.var_product_price.get(),
                        self.var_product_quantity.get(),
                        self.var_product_status.get(),
                    ))
                    db_connection.commit()
                    messagebox.showinfo("Success","Product Added Successfully",parent = self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def show(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            db_cursor.execute("select * from product")
            rows = db_cursor.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):
        focused_item = self.ProductTable.focus()
        content=(self.ProductTable.item(focused_item))
        row = content['values']
        self.var_product_id.set(row[0])
        self.var_category.set(row[1])
        self.var_supplier.set(row[2])
        self.var_product_name.set(row[3])
        self.var_product_price.set(row[4])
        self.var_product_quantity.set(row[5])
        self.var_product_status.set(row[6])

    def update(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_product_id.get()=="":
                messagebox.showerror("Error","Please select product from list",parent = self.root)
            else:
                db_cursor.execute("Select * from product where pid=?",(self.var_product_id.get(),))
                row = db_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product",parent = self.root)
                else:
                    db_cursor.execute("update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_product_name.get(),
                        self.var_product_price.get(),
                        self.var_product_quantity.get(),
                        self.var_product_status.get(),
                        self.var_product_id.get(),
                    ))
                    db_connection.commit()
                    messagebox.showinfo("Success","Product Updated Successfully",parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def delete(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_product_id.get()=="":
                messagebox.showerror("Error","Select Product from the list",parent = self.root)
            else:
                db_cursor.execute("Select * from product where pid=?",(self.var_product_id.get(),))
                row = db_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Product",parent = self.root)
                else:
                    confirmation = messagebox.askyesno("Confirm","Do you really want to delete?",parent = self.root)
                    if confirmation == True:
                        db_cursor.execute("delete from product where pid=?",(self.var_product_id.get(),))
                        db_connection.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent = self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def clear(self):
        self.var_category.set("Select")
        self.var_supplier.set("Select")
        self.var_product_name.set("")
        self.var_product_price.set("")
        self.var_product_quantity.set("")
        self.var_product_status.set("Active")
        self.var_product_id.set("")
        self.var_search_field.set("Select")
        self.var_search_querry.set("")
        self.show()

    
    def search(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_search_field.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent = self.root)
            elif self.var_search_querry.get()=="":
                messagebox.showerror("Error","Search input should be required",parent = self.root)
            else:
                db_cursor.execute("select * from product where "+self.var_search_field.get()+" LIKE '%"+self.var_search_querry.get()+"%'")
                rows = db_cursor.fetchall()
                if len(rows) != 0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values = row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

if __name__=="__main__":
    root = Tk()
    object_product = productClass(root)
    root.mainloop()