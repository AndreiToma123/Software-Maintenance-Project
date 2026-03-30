from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import sqlite3
import os


from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass

# ------------------ BASE PATH SETUP ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
BILL_DIR = os.path.join(BASE_DIR, "bill")

os.makedirs(BILL_DIR, exist_ok = True)
# ---------------------------------------------------

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+110+80")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        # ------------- title --------------
        self.icon_title = PhotoImage(file = os.path.join(IMAGE_DIR, "logo1.png"))
        title = Label(
            self.root,
            text="Inventory Management System",
            image = self.icon_title,
            compound = LEFT,
            font=("times new roman", 40, "bold"),
            bg="#010c48",
            fg="white",
            anchor="w",
            padx = 20
        ).place(x = 0, y = 0, relwidth = 1, height = 70)

        # ------------ logout button -----------
        button_logout = Button(
            self.root, text="Logout",
            font=("times new roman", 15, "bold"),
            bg="yellow", cursor="hand2"
        ).place(x = 1150, y = 10, height = 50, width = 150)

        # ------------ clock -----------------
        self.label_clock = Label(
            self.root,
            text="Welcome to Inventory Management System\t\t Date: DD:MM:YYYY\t\t Time: HH:MM:SS",
            font=("times new roman", 15),
            bg="#4d636d", fg="white"
        )
        self.label_clock.place(x = 0, y = 70, relwidth = 1, height = 30)

        # ---------------- left menu ---------------
        self.menu_logo = Image.open(os.path.join(IMAGE_DIR, "menu_im.png"))
        self.menu_logo = self.menu_logo.resize((200, 200))
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)

        menu_left = Frame(self.root, bd = 2, relief = RIDGE, bg="white")
        menu_left.place(x = 0, y = 102, width = 200, height = 565)

        label_menu_logo = Label(menu_left, image = self.menu_logo)
        label_menu_logo.pack(side = TOP, fill = X)

        label_menu = Label(
            menu_left, text="Menu",
            font=("times new roman", 20),
            bg="#009688"
        ).pack(side = TOP, fill = X)

        self.icon_side = PhotoImage(file = os.path.join(IMAGE_DIR, "side.png"))

        button_employee = Button(
            menu_left, text="Employee", command = self.employee,
            image = self.icon_side, compound = LEFT,
            padx = 5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd = 3, cursor="hand2"
        ).pack(side = TOP, fill = X)

        button_supplier = Button(
            menu_left, text="Supplier", command = self.supplier,
            image = self.icon_side, compound = LEFT,
            padx = 5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd = 3, cursor="hand2"
        ).pack(side = TOP, fill = X)

        button_category = Button(
            menu_left, text="Category", command = self.category,
            image = self.icon_side, compound = LEFT,
            padx = 5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd = 3, cursor="hand2"
        ).pack(side = TOP, fill = X)

        button_product = Button(
            menu_left, text="Products", command = self.product,
            image = self.icon_side, compound = LEFT,
            padx = 5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd = 3, cursor="hand2"
        ).pack(side = TOP, fill = X)

        button_sales = Button(
            menu_left, text="Sales", command = self.sales,
            image = self.icon_side, compound = LEFT,
            padx = 5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd = 3, cursor="hand2"
        ).pack(side = TOP, fill = X)

        button_exit = Button(
            menu_left, text="Exit",
            image = self.icon_side, compound = LEFT,
            padx = 5, anchor="w",
            font=("times new roman", 20, "bold"),
            bg="white", bd = 3, cursor="hand2",
            command = self.root.destroy
        ).pack(side = TOP, fill = X)

        # ----------- content ----------------
        self.label_employee = Label(
            self.root, text="Total Employee\n{ 0 }",
            bd = 5, relief = RIDGE, bg="#33bbf9",
            fg="white", font=("goudy old style", 20, "bold")
        )
        self.label_employee.place(x = 300, y = 120, height = 150, width = 300)

        self.label_supplier = Label(
            self.root, text="Total Supplier\n{ 0 }",
            bd = 5, relief = RIDGE, bg="#ff5722",
            fg="white", font=("goudy old style", 20, "bold")
        )
        self.label_supplier.place(x = 650, y = 120, height = 150, width = 300)

        self.label_category = Label(
            self.root, text="Total Category\n{ 0 }",
            bd = 5, relief = RIDGE, bg="#009688",
            fg="white", font=("goudy old style", 20, "bold")
        )
        self.label_category.place(x = 1000, y = 120, height = 150, width = 300)

        self.label_product = Label(
            self.root, text="Total Product\n{ 0 }",
            bd = 5, relief = RIDGE, bg="#607d8b",
            fg="white", font=("goudy old style", 20, "bold")
        )
        self.label_product.place(x = 300, y = 300, height = 150, width = 300)

        self.label_sales = Label(
            self.root, text="Total Sales\n{ 0 }",
            bd = 5, relief = RIDGE, bg="#ffc107",
            fg="white", font=("goudy old style", 20, "bold")
        )
        self.label_sales.place(x = 650, y = 300, height = 150, width = 300)

        # ------------ footer -----------------
        label_footer = Label(
            self.root,
            text="IMS-Inventory Management System",
            font=("times new roman", 12),
            bg="#4d636d", fg="white"
        ).pack(side = BOTTOM, fill = X)

        self.update_content()

    # -------------- functions ----------------
    def employee(self):
        self.new_window = Toplevel(self.root)
        self.new_object = employeeClass(self.new_window)

    def supplier(self):
        self.new_window = Toplevel(self.root)
        self.new_object = supplierClass(self.new_window)

    def category(self):
        self.new_window = Toplevel(self.root)
        self.new_object = categoryClass(self.new_window)

    def product(self):
        self.new_window = Toplevel(self.root)
        self.new_object = productClass(self.new_window)

    def sales(self):
        self.new_window = Toplevel(self.root)
        self.new_object = salesClass(self.new_window)

    def update_content(self):
        db_connection = sqlite3.connect(database = os.path.join(BASE_DIR, 'ims.db'))
        db_cursor = db_connection.cursor()

        try:
            db_cursor.execute("select * from product")
            product = db_cursor.fetchall()
            self.label_product.config(text = f"Total Product\n[ {len(product)} ]")

            db_cursor.execute("select * from category")
            category = db_cursor.fetchall()
            self.label_category.config(text = f"Total Category\n[ {len(category)} ]")

            db_cursor.execute("select * from employee")
            employee = db_cursor.fetchall()
            self.label_employee.config(text = f"Total Employee\n[ {len(employee)} ]")

            db_cursor.execute("select * from supplier")
            supplier = db_cursor.fetchall()
            self.label_supplier.config(text = f"Total Supplier\n[ {len(supplier)} ]")

            bill = len(os.listdir(BILL_DIR))
            self.label_sales.config(text = f"Total Sales\n[ {bill} ]")

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.label_clock.config(
                text = f"Welcome to Inventory Management System\t\t Date: {date_}\t\t Time: {time_}"
            )

            self.label_clock.after(200, self.update_content)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)


if __name__ == "__main__":
    root = Tk()
    object_IMS = IMS(root)
    root.mainloop()
