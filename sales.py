from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

# ------------------ BASE PATH SETUP ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
BILL_DIR = os.path.join(BASE_DIR, "bill")

os.makedirs(BILL_DIR, exist_ok = True)
# ---------------------------------------------------

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+320+220")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        self.root.focus_force()

        self.bill_list = []
        self.var_invoice_number = StringVar()

        # --------------- title ---------------------
        label_title = Label(
            self.root,
            text="View Customer Bills",
            font=("goudy old style", 30),
            bg="#184a45",
            fg="white",
            bd = 3,
            relief = RIDGE
        ).pack(side = TOP, fill = X, padx = 10, pady = 20)

        label_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 15), bg="white")
        label_invoice.place(x = 50, y = 100)

        text_invoice = Entry(self.root, textvariable = self.var_invoice_number, font=("times new roman", 15), bg="lightyellow")
        text_invoice.place(x = 160, y = 100, width = 180, height = 28)

        button_search = Button(
            self.root, text="Search", command = self.search,
            font=("times new roman", 15, "bold"),
            bg="#2196f3", fg="white", cursor="hand2"
        ).place(x = 360, y = 100, width = 120, height = 28)

        button_clear = Button(
            self.root, text="Clear", command = self.clear,
            font=("times new roman", 15, "bold"),
            bg="lightgray", cursor="hand2"
        ).place(x = 490, y = 100, width = 120, height = 28)

        # ----------------- bill list -------------------
        sales_Frame = Frame(self.root, bd = 3, relief = RIDGE)
        sales_Frame.place(x = 50, y = 140, width = 200, height = 330)

        scrolly = Scrollbar(sales_Frame, orient = VERTICAL)
        self.sales_List = Listbox(
            sales_Frame, font=("goudy old style", 15),
            bg="white", yscrollcommand = scrolly.set
        )
        scrolly.pack(side = RIGHT, fill = Y)
        scrolly.config(command = self.sales_List.yview)
        self.sales_List.pack(fill = BOTH, expand = 1)
        self.sales_List.bind("<ButtonRelease-1>", self.get_data)

        # --------------- bill area ----------------------
        bill_Frame = Frame(self.root, bd = 3, relief = RIDGE)
        bill_Frame.place(x = 280, y = 140, width = 410, height = 330)

        label_title_2 = Label(
            bill_Frame, text="Customer Bill Area",
            font=("goudy old style", 20), bg="orange"
        ).pack(side = TOP, fill = X)

        scrolly2 = Scrollbar(bill_Frame, orient = VERTICAL)
        self.bill_area = Text(bill_Frame, bg="lightyellow", yscrollcommand = scrolly2.set)
        scrolly2.pack(side = RIGHT, fill = Y)
        scrolly2.config(command = self.bill_area.yview)
        self.bill_area.pack(fill = BOTH, expand = 1)

        # ------------- image -----------------
        image_path = os.path.join(IMAGE_DIR, "cat2.jpg")
        self.bill_photo = Image.open(image_path)
        self.bill_photo = self.bill_photo.resize((450, 300))
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

        label_image = Label(self.root, image = self.bill_photo, bd = 0)
        label_image.place(x = 700, y = 110)

        self.show()

    # -------------------------------------------------------
    def show(self):
        del self.bill_list[:]
        self.sales_List.delete(0, END)

        for i in os.listdir(BILL_DIR):
            if i.split('.')[-1] == 'txt':
                self.sales_List.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        index = self.sales_List.curselection()
        if not index:
            return

        file_name = self.sales_List.get(index)
        self.bill_area.delete('1.0', END)

        file_path = os.path.join(BILL_DIR, file_name)
        with open(file_path, 'r') as fp:
            for i in fp:
                self.bill_area.insert(END, i)

    def search(self):
        if self.var_invoice_number.get() == "":
            messagebox.showerror("Error", "Invoice no. should be required", parent = self.root)
        else:
            if self.var_invoice_number.get() in self.bill_list:
                file_path = os.path.join(BILL_DIR, f"{self.var_invoice_number.get()}.txt")
                self.bill_area.delete('1.0', END)

                with open(file_path, 'r') as fp:
                    for i in fp:
                        self.bill_area.insert(END, i)
            else:
                messagebox.showerror("Error", "Invalid Invoice No.", parent = self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)


if __name__ == "__main__":
    root = Tk()
    object_sales = salesClass(root)
    root.mainloop()
