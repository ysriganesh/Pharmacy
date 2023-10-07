from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox


class PharmacyManagementSystem:
    def __init__(self, root):

        self.root = root
        self.root.title('Pharmacy Management System')
        self.root.geometry("1550x800+0+0")


        self.addmed_var=StringVar()
        self.refmed_var=StringVar()

        self.ref_var= StringVar()
        self.cmpName_var = StringVar()
        self.typeMed_var = StringVar()
        self.medName_var = StringVar()
        self.lot_var = StringVar()
        self.issuedate_var = StringVar()
        self.expdate_var = StringVar()
        self.uses_var = StringVar()
        self.sideEffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.product_var = StringVar()



        lbltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE, bg='lightblue',
                         fg="darkblue", font=("Bookman Old Style", 50, "bold"), padx=2, pady=4)

        lbltitle.pack(side=TOP, fill=X)

        img1 = Image.open("C:/Users/sriga/Downloads/360_F_42047733_qUCTmFgDt1XahmRAnFtIOLe5EuEvBoGs.jpg")
        img1 = img1.resize((80, 80))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=50, y=20)
        # ++++++++++++++++++++++ Data Frame+++++++++++++++++++#

        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1530, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Information", fg="blue",
                                   font=("Bookman Old Style", 14, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        # =====================buttonFrame=================#

        ButtonDataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonDataFrame.place(x=0, y=520, width=1530, height=65)

        # ================== Main Button==================#

        btnAddData = Button(ButtonDataFrame, text="Medicine Add", font=("arial", 12, "bold"), width=12, bg="darkblue",
                            fg="lightblue",command=self.add_data)
        btnAddData.grid(row=0, column=0)

        btnUpdateMed = Button(ButtonDataFrame, text="Update", font=("arial", 12, "bold"), width=12, bg="darkblue",
                              fg="lightblue",command=self.Update)
        btnUpdateMed.grid(row=0, column=1)

        btnDeleteMed = Button(ButtonDataFrame, text="Delete", font=("arial", 12, "bold"), width=12, bg="darkred",
                              fg="lightblue",command=self.delete)
        btnDeleteMed.grid(row=0, column=2)

        btnRestMed = Button(ButtonDataFrame, text="Reset", font=("arial", 12, "bold"), width=12, bg="darkblue",
                            fg="lightblue",command=self.reset)
        btnRestMed.grid(row=0, column=3)

        btnExitMed = Button(ButtonDataFrame, text="EXIT", font=("arial", 12, "bold"), width=12, bg="darkblue",
                            fg="lightblue")
        btnExitMed.grid(row=0, column=4)

        # ==============Search By===============#
        lblSearch = Label(ButtonDataFrame, font=("arial", 17, "bold"), text="Search By", padx=2, width=12, bg="red",
                          fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)

        self.search_var = StringVar()
        serch_combo = ttk.Combobox(ButtonDataFrame,textvariable=self.search_var, width=12, font=("arial", 17, "bold"), state="readonly")
        serch_combo["values"] = ("Ref_no", "MedName", "LotNo")
        serch_combo.grid(row=0, column=6)
        serch_combo.current(0)

        self.serchTxt_var = StringVar()
        txtSerch = Entry(ButtonDataFrame, textvariable=self.serchTxt_var,bd=3, relief=RIDGE, width=12, font=("arial", 13, "bold"))
        txtSerch.grid(row=0, column=7)

        searchBtn = Button(ButtonDataFrame, text="SEARCH", font=("arial", 12, "bold"), width=14, bg="darkblue",
                           fg="lightblue",command=self.search_data)
        searchBtn.grid(row=0, column=8)

        showAll = Button(ButtonDataFrame, text="SHOW ALL", font=("arial", 12, "bold"), width=14, bg="darkblue",
                         fg="lightblue",command=self.fatch_data)
        showAll.grid(row=0, column=9)

        lblrefno = Label(DataFrameLeft, font=("arial", 13, "bold"), text="Reference No", padx=2, width=12, )
        lblrefno.grid(row=0, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="ganesh", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()


        ref_combo = ttk.Combobox(DataFrameLeft, textvariable=self.ref_var,width=27, font=("arial", 11, "bold"), state="readonly")
        ref_combo["values"] = row
        ref_combo.grid(row=0, column=1)
        ref_combo.current(0)

        lblcompname = Label(DataFrameLeft, font=("arial", 13, "bold"), text="Company Name", padx=2, width=12, )
        lblcompname.grid(row=1, column=0, sticky=W)
        txtcompname = Entry(DataFrameLeft, textvariable=self.cmpName_var,font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtcompname.grid(row=1, column=1, sticky=W)

        lblTypeMedicine = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Type of Medicine", padx=2, pady=4)
        lblTypeMedicine.grid(row=2, column=0, sticky=W)


        comTypeMedicine = ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var, state="readonly", font=("arial", 12, "bold"), width=24)

        comTypeMedicine['value'] = ("Tablet", "Liquid", "Capsules", "Topical Medicine", "Drops", "Inhale", "Injection")
        comTypeMedicine.current(0)
        comTypeMedicine.grid(row=2, column=1)

        lblMedicineName = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Medicine Name", padx=2, pady=4)
        lblMedicineName.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="ganesh", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med = my_cursor.fetchall()

        comMedicineName = ttk.Combobox(DataFrameLeft, textvariable=self.medName_var,state="readonly", font=("arial", 12, "bold"), width=24)

        comMedicineName['value'] = med
        comMedicineName.current(0)
        comMedicineName.grid(row=3, column=1)

        lblLotNo = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Lot No:", padx=2, pady=6)
        lblLotNo.grid(row=4, column=0, sticky=W)
        txtLotNo = Entry(DataFrameLeft,textvariable=self.lot_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtLotNo.grid(row=4, column=1, sticky=W)

        lblIssueDate = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataFrameLeft,textvariable=self.issuedate_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtIssueDate.grid(row=5, column=1, sticky=W)

        lblExDate = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExDate.grid(row=6, column=0, sticky=W)
        txtExDate = Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtExDate.grid(row=6, column=1)

        lblUses = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Uses:", padx=2, pady=6)
        lblUses.grid(row=7, column=0, sticky=W)
        txtUses = Entry(DataFrameLeft,textvariable=self.uses_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtUses.grid(row=7, column=1)

        lblSideEffect = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft,textvariable=self.sideEffect_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtSideEffect.grid(row=8, column=1)

        lblPrecWarning = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Prec Warning:", padx=2, pady=6)
        lblPrecWarning.grid(row=0, column=3, sticky=W)
        txtPresWarning = Entry(DataFrameLeft,textvariable=self.warning_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPresWarning.grid(row=0, column=4)

        lblDosage = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Dosage:", padx=2, pady=6)
        lblDosage.grid(row=1, column=3, sticky=W)
        txtDosage = Entry(DataFrameLeft,textvariable=self.dosage_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtDosage.grid(row=1, column=4)

        lblPrice = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Tabelets Prices:", padx=2, pady=6)
        lblPrice.grid(row=2, column=3, sticky=W)
        txtPrice = Entry(DataFrameLeft,textvariable=self.price_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPrice.grid(row=2, column=4)

        lblProducttQt = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Product QT:", padx=2, pady=6)
        lblProducttQt.grid(row=3, column=3, sticky=W)
        txtProducttQt = Entry(DataFrameLeft,textvariable=self.product_var, font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtProducttQt.grid(row=3, column=4, sticky=W)

        lblhome = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Stay Home Stay Safe  ", padx=2, pady=6,
                        bg="white", fg="red", width=37)
        lblhome.place(x=475, y=140)

        img2 = Image.open("C:/Users/sriga/Downloads/360_F_221757417_2iKw8n5r8JV6VgrM0IGz32rGzlN7fHmX.jpg")
        img2 = img2.resize((150, 135))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.root, image=self.photoimg2, borderwidth=0)
        b1.place(x=770, y=330)

        img3 = Image.open("C:/Users/sriga/Downloads/logo-health-care-clinic-cross-260nw-338808005.webp")
        img3 = img3.resize((150, 135))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.photoimg3, borderwidth=0)
        b1.place(x=620, y=330)

        img4 = Image.open("C:/Users/sriga/Downloads/images.jpeg")
        img4 = img4.resize((150, 135))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root, image=self.photoimg4, borderwidth=0)
        b1.place(x=475, y=330)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department", fg="blue",
                                    font=("Bookman Old Style", 14, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        img5 = Image.open("C:/Users/sriga/Downloads/360_F_221757417_2iKw8n5r8JV6VgrM0IGz32rGzlN7fHmX.jpg")
        img5 = img5.resize((130, 75))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root, image=self.photoimg5, borderwidth=0)
        b1.place(x=960, y=170)

        img6 = Image.open("C:/Users/sriga/Downloads/360_F_221757417_2iKw8n5r8JV6VgrM0IGz32rGzlN7fHmX.jpg")
        img6 = img6.resize((130, 75))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(self.root, image=self.photoimg6, borderwidth=0)
        b1.place(x=1060, y=170)

        img7 = Image.open("C:/Users/sriga/Downloads/360_F_221757417_2iKw8n5r8JV6VgrM0IGz32rGzlN7fHmX.jpg")
        img7 = img7.resize((130, 75))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(self.root, image=self.photoimg7, borderwidth=0)
        b1.place(x=1160, y=170)

        img8 = Image.open("C:/Users/sriga/Downloads/360_F_221757417_2iKw8n5r8JV6VgrM0IGz32rGzlN7fHmX.jpg")
        img8 = img8.resize((130, 75))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(self.root, image=self.photoimg8, borderwidth=0)
        b1.place(x=1260, y=170)

        lblrefno = Label(DataFrameRight, font=("arial", 11, "bold"), text="Reference Number  :", padx=0, pady=6)
        lblrefno.place(x=0, y=90)
        txtrefno = Entry(DataFrameRight, textvariable=self.refmed_var,font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=19)
        txtrefno.place(x=135, y=100)

        lblmedName = Label(DataFrameRight, font=("arial", 11, "bold"), text="Medicine Name:", padx=2, pady=6)
        lblmedName.place(x=0, y=130)
        txtmedName = Entry(DataFrameRight ,textvariable=self.addmed_var,font=("arial", 11, "bold"), bg="white", bd=2, relief=RIDGE, width=19)
        txtmedName.place(x=135, y=135)

        side_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=0, y=160, width=290, height=160)

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table = ttk.Treeview(side_frame, column=("ref", "medname"), xscrollcommand=sc_x.set,
                                           yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="REF")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"] = "headings"

        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=70)
        self.medicine_table.column("medname", width=70)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        down_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="darkgreen")
        down_frame.place(x=300, y=160, width=135, height=160)

        btnAddmed = Button(down_frame, text="ADD", font=("arial", 12, "bold"), bg="lime", width=12, fg="white", pady=2,command=self.AddMed)
        btnAddmed.grid(row=0, column=0)

        btnUpdatemed = Button(down_frame, text="UPDATE", font=("arial", 12, "bold"), bg="blue", width=12, fg="white",
                              pady=2,command=self.UpdateMed)
        btnUpdatemed.grid(row=1, column=0)

        btnDeletemed = Button(down_frame, text="DELETE", font=("arial", 12, "bold"), bg="red", width=12, fg="white",
                              pady=2,command=self.DeleteMed)
        btnDeletemed.grid(row=2, column=0)

        btnClearmed = Button(down_frame, text="CLEAR", font=("arial", 12, "bold"), bg="violet", width=12, fg="white",
                             pady=2,command=self.ClearMed)
        btnClearmed.grid(row=3, column=0)

        Framedetails = Frame(self.root, bd=15, relief=RIDGE)
        Framedetails.place(x=0, y=580, width=1530, height=210)

        Table_frame = Frame(self.root, bd=15, relief=RIDGE)
        Table_frame.place(x=0, y=595, width=1520, height=180)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table = ttk.Treeview(Table_frame, columns=(
        "reg", "companyname", "type","tabletname","lotno", "issuedate", "expdate","uses", "sideeffect", "warning",
        "dosage", "price", "productqt")
         ,xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("reg", text="Reference No")
        self.pharmacy_table.heading("reg", text="Reference No")
        self.pharmacy_table.heading("companyname", text="Company No")
        self.pharmacy_table.heading("type", text="Type of Medicine")
        self.pharmacy_table.heading("tabletname", text="Tablet Name")
        self.pharmacy_table.heading("lotno", text="Lot No")
        self.pharmacy_table.heading("issuedate", text="Issue Date")
        self.pharmacy_table.heading("expdate", text="Exp Date")
        self.pharmacy_table.heading("uses", text="Uses")
        self.pharmacy_table.heading("sideeffect", text="Side Effect")
        self.pharmacy_table.heading("warning", text="Warning")
        self.pharmacy_table.heading("dosage", text="Dosage")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("productqt", text="Product Qts ")
        self.pharmacy_table.pack(fill=BOTH, expand=1)

        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname", width=100)
        self.pharmacy_table.column("type", width=100)
        self.pharmacy_table.column("tabletname", width=100)
        self.pharmacy_table.column("lotno", width=100)
        self.pharmacy_table.column("issuedate", width=100)
        self.pharmacy_table.column("expdate", width=100)
        self.pharmacy_table.column("uses", width=100)
        self.pharmacy_table.column("sideeffect", width=100)
        self.pharmacy_table.column("warning", width=100)
        self.pharmacy_table.column("dosage", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.column("productqt", width=100)
        self.fetch_dataMed()
        self.fatch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)


    def AddMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="ganesh", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("INSERT INTO pharma(Ref, MedName) VALUES (%s, %s)",
                          (self.refmed_var.get(), self.addmed_var.get()))
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success", "Medicine Added")

    def fetch_dataMed(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="ganesh", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from pharma")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.medicine_table.delete(*self.medicine_table.get_children())
                for i in rows:
                    self.medicine_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    def Medget_cursor(self,event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row=content.get("values",())
        if row:
            self.refmed_var.set(row[0])
            self.addmed_var.set(row[1])
    def UpdateMed(self):
        if self.refmed_var.get() == "" or self.addmed_var.get() ==" ":
            messagebox.showerror("Error","All Fileds are requried")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="ganesh", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                                                                                      self.addmed_var.get(),
                                                                                      self.refmed_var.get(),
            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success","Medicine has beem Updated")

    def DeleteMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="ganesh", database="mydata")
        my_cursor = conn.cursor()

        sql="delete from pharma where Ref=%s"
        val=(self.refmed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()

    def ClearMed(self):
        self.refmed_var.set("")
        self.addmed_var.set("")

    def add_data(self):

            if (
                    self.ref_var.get() == ""
                    or self.cmpName_var.get() == ""
                    or self.typeMed_var.get() == ""
                    or self.medName_var.get() == ""
                    or self.lot_var.get() == ""
                    or self.issuedate_var.get() == ""
                    or self.expdate_var.get() == ""
                    or self.uses_var.get() == ""
                    or self.sideEffect_var.get() == ""
                    or self.warning_var.get() == ""
                    or self.dosage_var.get() == ""
                    or self.price_var.get() == ""
                    or self.product_var.get() == ""
            ):
                messagebox.showerror("Error", "All Fields are required")
            else:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="ganesh",
                    database="mydata",
                )
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "INSERT INTO pharmacyy (Ref_no, CmpName, TypeMed, MedName,LotNo, IssueDate, ExpDate, Uses, Sideeffect, "
                    "warning, dosage, Price, product) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)",
                    (
                        self.ref_var.get(),
                        self.cmpName_var.get(),
                        self.typeMed_var.get(),
                        self.medName_var.get(),
                        self.lot_var.get(),
                        self.issuedate_var.get(),
                        self.expdate_var.get(),
                        self.uses_var.get(),
                        self.sideEffect_var.get(),
                        self.warning_var.get(),
                        self.dosage_var.get(),
                        self.price_var.get(),
                        self.product_var.get(),
                    ),
                )
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "Data has been inserted")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="ganesh", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharmacyy")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,ev=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row = content["values"]

        self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11])
        self.product_var.set(row[12])

    def Update(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="ganesh", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "UPDATE pharmacyy SET CmpName=%s, TypeMed=%s, MedName=%s, LotNo=%s, IssueDate=%s, ExpDate=%s, Uses=%s, "
                "Sideeffect=%s, warning=%s, dosage=%s, Price=%s, product=%s WHERE Ref_no=%s",
                (
                    self.cmpName_var.get(),
                    self.typeMed_var.get(),
                    self.medName_var.get(),
                    self.lot_var.get(),
                    self.issuedate_var.get(),
                    self.expdate_var.get(),
                    self.uses_var.get(),
                    self.sideEffect_var.get(),
                    self.warning_var.get(),
                    self.dosage_var.get(),
                    self.price_var.get(),
                    self.product_var.get(),
                    self.ref_var.get(),
                )
            )

            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success", "Medicine has been Updated")

    def delete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="ganesh", database="mydata")
        my_cursor = conn.cursor()

        sql = "delete from pharmacyy where Ref_no=%s"
        val = (self.ref_var.get(),)
        my_cursor.execute(sql, val)

        conn.commit()
        self.fatch_data()
        conn.close()

    def reset(self):
        self.cmpName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(r""),
        self.price_var.set(r""),
        self.price_var.set(r"")

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="ganesh", database="mydata")
        my_cursor = conn.cursor()

        # Use placeholders in the query to prevent SQL injection
        query = "SELECT * FROM pharmacyy WHERE {} LIKE %s".format(self.search_var.get())
        search_value = self.serchTxt_var.get()  # Assuming serchTxt_var holds the search value

        my_cursor.execute(query, (search_value,))

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
