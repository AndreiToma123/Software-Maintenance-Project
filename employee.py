from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+320+220")

        self.root.config(bg="white")
        self.root.resizable(False,False)
        self.root.focus_force()

        #------------ all variables --------------
        self.var_search_field = StringVar()
        self.var_search_querry = StringVar()
        self.var_employee_id = StringVar()
        self.var_employee_gender = StringVar()
        self.var_employee_contact = StringVar()
        self.var_employee_name = StringVar()
        self.var_employee_dob = StringVar()
        self.var_employee_doj = StringVar()
        self.var_employee_email = StringVar()
        self.var_employee_pass = StringVar()
        self.var_user_type = StringVar()
        self.var_employee_salary = StringVar()

        #---------- Search Frame -------------
        SearchFrame = LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd = 2,relief = RIDGE,bg="white")
        SearchFrame.place(x = 250,y = 20,width = 600,height = 70)

        #------------ options ----------------
        cmb_search = ttk.Combobox(SearchFrame,textvariable = self.var_search_field,values=("Select","Email","Name","Contact"),state='readonly',justify = CENTER,font=("goudy old style",15))
        cmb_search.place(x = 10,y = 10,width = 180)
        cmb_search.current(0)

        text_search = Entry(SearchFrame,textvariable = self.var_search_querry,font=("goudy old style",15),bg="lightyellow").place(x = 200,y = 10)
        button_search = Button(SearchFrame,command = self.search,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x = 410,y = 9,width = 150,height = 30)

        #-------------- title ---------------
        title = Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x = 50,y = 100,width = 1000)

        #-------------- content ---------------
        #---------- row 1 ----------------
        label_employee_id = Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x = 50,y = 150)
        label_employee_gender = Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x = 350,y = 150)
        label_employee_contact = Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x = 750,y = 150)

        text_employee_id = Entry(self.root,textvariable = self.var_employee_id,font=("goudy old style",15),bg="lightyellow").place(x = 150,y = 150,width = 180)
        cmb_employee_gender = ttk.Combobox(self.root,textvariable = self.var_employee_gender,values=("Select","Male","Female","Other"),state='readonly',justify = CENTER,font=("goudy old style",15))
        cmb_employee_gender.place(x = 500,y = 150,width = 180)
        cmb_employee_gender.current(0)
        text_employee_contact = Entry(self.root,textvariable = self.var_employee_contact,font=("goudy old style",15),bg="lightyellow").place(x = 850,y = 150,width = 180)

        #---------- row 2 ----------------
        label_employee_name = Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x = 50,y = 190)
        label_employee_dob = Label(self.root,text="D.O.B.",font=("goudy old style",15),bg="white").place(x = 350,y = 190)
        label_employee_doj = Label(self.root,text="D.O.J.",font=("goudy old style",15),bg="white").place(x = 750,y = 190)

        text_employee_name = Entry(self.root,textvariable = self.var_employee_name,font=("goudy old style",15),bg="lightyellow").place(x = 150,y = 190,width = 180)
        text_employee_dob = Entry(self.root,textvariable = self.var_employee_dob,font=("goudy old style",15),bg="lightyellow").place(x = 500,y = 190,width = 180)
        text_employee_doj = Entry(self.root,textvariable = self.var_employee_doj,font=("goudy old style",15),bg="lightyellow").place(x = 850,y = 190,width = 180)

        #---------- row 3 ----------------
        label_employee_email = Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x = 50,y = 230)
        label_employee_password = Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x = 350,y = 230)
        label_user_type = Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x = 750,y = 230)

        text_employee_email = Entry(self.root,textvariable = self.var_employee_email,font=("goudy old style",15),bg="lightyellow").place(x = 150,y = 230,width = 180)
        text_employee_password = Entry(self.root,textvariable = self.var_employee_pass,font=("goudy old style",15),bg="lightyellow").place(x = 500,y = 230,width = 180)
        cmb_user_type = ttk.Combobox(self.root,textvariable = self.var_user_type,values=("Admin","Employee"),state='readonly',justify = CENTER,font=("goudy old style",15))
        cmb_user_type.place(x = 850,y = 230,width = 180)
        cmb_user_type.current(0)
        
        #---------- row 4 ----------------
        label_employee_address = Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x = 50,y = 270)
        label_employee_salary = Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x = 500,y = 270)

        self.text_employee_address = Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.text_employee_address.place(x = 150,y = 270,width = 300,height = 60)
        text_employee_salary = Entry(self.root,textvariable = self.var_employee_salary,font=("goudy old style",15),bg="lightyellow").place(x = 600,y = 270,width = 180)
        
        #-------------- buttons -----------------
        betton_add = Button(self.root,text="Save",command = self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x = 500,y = 305,width = 110,height = 28)
        button_update = Button(self.root,text="Update",command = self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x = 620,y = 305,width = 110,height = 28)
        button_delete = Button(self.root,text="Delete",command = self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x = 740,y = 305,width = 110,height = 28)
        button_clear = Button(self.root,text="Clear",command = self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x = 860,y = 305,width = 110,height = 28)

        #------------ employee details -------------
        employee_frame = Frame(self.root,bd = 3,relief = RIDGE)
        employee_frame.place(x = 0,y = 350,relwidth = 1,height = 150)

        scrolly = Scrollbar(employee_frame,orient = VERTICAL)
        scrollx = Scrollbar(employee_frame,orient = HORIZONTAL)\
        
        self.EmployeeTable = ttk.Treeview(employee_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand = scrolly.set,xscrollcommand = scrollx.set)
        scrollx.pack(side = BOTTOM,fill = X)
        scrolly.pack(side = RIGHT,fill = Y)
        scrollx.config(command = self.EmployeeTable.xview)
        scrolly.config(command = self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        self.EmployeeTable["show"]="headings"
        self.EmployeeTable.column("eid",width = 90)
        self.EmployeeTable.column("name",width = 100)
        self.EmployeeTable.column("email",width = 100)
        self.EmployeeTable.column("gender",width = 100)
        self.EmployeeTable.column("contact",width = 100)
        self.EmployeeTable.column("dob",width = 100)
        self.EmployeeTable.column("doj",width = 100)
        self.EmployeeTable.column("pass",width = 100)
        self.EmployeeTable.column("utype",width = 100)
        self.EmployeeTable.column("address",width = 100)
        self.EmployeeTable.column("salary",width = 100)
        
        self.EmployeeTable.pack(fill = BOTH,expand = 1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#-----------------------------------------------------------------------------------------------------
    def add(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent = self.root)
            else:
                db_cursor.execute("Select * from employee where eid=?",(self.var_employee_id.get(),))
                row = db_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error","This Employee ID is already assigned",parent = self.root)
                else:
                    db_cursor.execute("insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_employee_id.get(),
                        self.var_employee_name.get(),
                        self.var_employee_email.get(),
                        self.var_employee_gender.get(),
                        self.var_employee_contact.get(),
                        self.var_employee_dob.get(),
                        self.var_employee_doj.get(),
                        self.var_employee_pass.get(),
                        self.var_user_type.get(),
                        self.text_employee_address.get('1.0',END),
                        self.var_employee_salary.get(),
                    ))
                    db_connection.commit()
                    messagebox.showinfo("Success","Employee Added Successfully",parent = self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def show(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            db_cursor.execute("select * from employee")
            rows = db_cursor.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):
        focused_item = self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(focused_item))
        row = content['values']
        self.var_employee_id.set(row[0])
        self.var_employee_name.set(row[1])
        self.var_employee_email.set(row[2])
        self.var_employee_gender.set(row[3])
        self.var_employee_contact.set(row[4])
        self.var_employee_dob.set(row[5])
        self.var_employee_doj.set(row[6])
        self.var_employee_pass.set(row[7])
        self.var_user_type.set(row[8])
        self.text_employee_address.delete('1.0',END)
        self.text_employee_address.insert(END,row[9])
        self.var_employee_salary.set(row[10])

    def update(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent = self.root)
            else:
                db_cursor.execute("Select * from employee where eid=?",(self.var_employee_id.get(),))
                row = db_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Employee ID",parent = self.root)
                else:
                    db_cursor.execute("update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                        self.var_employee_name.get(),
                        self.var_employee_email.get(),
                        self.var_employee_gender.get(),
                        self.var_employee_contact.get(),
                        self.var_employee_dob.get(),
                        self.var_employee_doj.get(),
                        self.var_employee_pass.get(),
                        self.var_user_type.get(),
                        self.text_employee_address.get('1.0',END),
                        self.var_employee_salary.get(),
                        self.var_employee_id.get(),
                    ))
                    db_connection.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def delete(self):
        db_connection = sqlite3.connect(database = r'ims.db')
        db_cursor = db_connection.cursor()
        try:
            if self.var_employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent = self.root)
            else:
                db_cursor.execute("Select * from employee where eid=?",(self.var_employee_id.get(),))
                row = db_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Employee ID",parent = self.root)
                else:
                    confirmation = messagebox.askyesno("Confirm","Do you really want to delete?",parent = self.root)
                    if confirmation == True:
                        db_cursor.execute("delete from employee where eid=?",(self.var_employee_id.get(),))
                        db_connection.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent = self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def clear(self):
        self.var_employee_id.set("")
        self.var_employee_name.set("")
        self.var_employee_email.set("")
        self.var_employee_gender.set("Select")
        self.var_employee_contact.set("")
        self.var_employee_dob.set("")
        self.var_employee_doj.set("")
        self.var_employee_pass.set("")
        self.var_user_type.set("Admin")
        self.text_employee_address.delete('1.0',END)
        self.var_employee_salary.set("")
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
                db_cursor.execute("select * from employee where "+self.var_search_field.get()+" LIKE '%"+self.var_search_querry.get()+"%'")
                rows = db_cursor.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values = row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


if __name__=="__main__":
    root = Tk()
    object_employee = employeeClass(root)
    root.mainloop()