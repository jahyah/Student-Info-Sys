import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.ttk as ttk
import csv
import os 

class Student:
    
    def __init__ (self,root):
        self.root = root
        blank_space = ""
        self.root.title(200 * blank_space + "Student Information System")
        self.root.geometry("1350x600+0+0")
        self.root.resizable(False,False)
        self.data = dict()
        self.temp = dict()
        self.filename = "SIS.csv"
        
        Stud_First_Name = StringVar()
        Stud_Middle_Name = StringVar()
        Stud_Last_Name = StringVar()
        Stud_IDNumber = StringVar()
        Stud_YearLevel = StringVar()
        Stud_Gender = StringVar()
        Stud_Course = StringVar()
        searchbar = StringVar()
        
        if not os.path.exists('SIS.csv'):
            with open('SIS.csv', mode='w') as csv_file:
                fieldnames = ["Student ID Number", "Last Name", "First Name", "Middle Name","Gender", "Year Level", "Course"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
        
        else:
            with open('SIS.csv', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["Student ID Number"]] = {'Last Name': row["Last Name"], 'First Name': row["First Name"], 'Middle Name': row["Middle Name"], 'Gender': row["Gender"],'Year Level': row["Year Level"], 'Course': row["Course"]}
            self.temp = self.data.copy()
        
        
         
        #=============================================================FUNCTIONS================================================================#
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Information System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
            
        def addStudent():
            with open('SIS.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if Stud_IDNumber.get()=="" or Stud_First_Name.get()=="" or Stud_Middle_Name.get()=="" or Stud_Last_Name.get()=="" or Stud_YearLevel.get()=="":
                    tkinter.messagebox.showinfo("SIS","Please fill in the box.")
                else:
                    studentID = Stud_IDNumber.get()
                    studentID_list = []
                    for i in studentID:
                        studentID_list.append(i)
                    if "-" in studentID_list:
                        x=studentID.split("-")
                        y=x[0]
                        n=x[1]
                        if y.isdigit()==False or n.isdigit()==False:
                            tkinter.messagebox.showerror("SIS","Invalid Student ID")
                        else:
                            if studentID in self.data:
                                tkinter.messagebox.showinfo("SIS", "Student already existed")
                            else:
                                self.data[Stud_IDNumber.get()] = {'Last Name': Stud_Last_Name.get(), 'First Name': Stud_First_Name.get(), 'Middle Name': Stud_Middle_Name.get(), 'Gender': Stud_Gender.get(),'Year Level': Stud_YearLevel.get(), 'Course': Stud_Course.get()}
                                self.saveData()
                                tkinter.messagebox.showinfo("SIS", "Recorded Successfully!")
                                Clear()
                    else:
                        tkinter.messagebox.showerror("SIS","Invaild ID")
                displayData()
                    
        
        def Clear():
            Stud_IDNumber.set("")
            Stud_First_Name.set("")
            Stud_Middle_Name.set("")
            Stud_Last_Name.set("")
            Stud_YearLevel.set("")
            Stud_Gender.set("")
            Stud_Course.set("")
        
        
        
        def displayData():
            tree.delete(*tree.get_children())
            with open('SIS.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    IDNumber=row['Student ID Number']
                    LastName=row['Last Name']
                    FirstName=row['First Name']
                    MiddleName=row['Middle Name']
                    YearLevel=row['Year Level']
                    Course=row['Course']
                    Gender=row['Gender']
                    tree.insert("",0, values=(IDNumber, LastName, FirstName, MiddleName, Gender, YearLevel, Course))
                    
      
        
        def deleteData():
            if tree.focus()=="":
                tkinter.messagebox.showerror("Student Information System","Please select a student record from the table")
                return
            id_no = tree.item(tree.focus(),"values")[0]
            
            self.data.pop(id_no, None)
            self.saveData()
            tree.delete(tree.focus())
            tkinter.messagebox.showinfo("Student Information System","Student Record Deleted Successfully")
            
        
        
        def searchData():
            if self.searchbar.get() in self.data:
                vals = list(self.data[self.searchbar.get()].values())
                tree.delete(*tree.get_children())
                tree.insert("",0, values=(self.searchbar.get(), vals[0],vals[1],vals[2],vals[3],vals[4],vals[5]))
            elif self.searchbar.get() == "":
                displayData()
            else:
                tkinter.messagebox.showerror("Student Information System","Student not found")
                return
            
        
        
        
        def editData():
            if tree.focus() == "":
                tkinter.messagebox.showerror("Student Information System", "Please select a student record from the table")
                return
            values = tree.item(tree.focus(), "values")
            Stud_IDNumber.set(values[0])
            Stud_Last_Name.set(values[1])
            Stud_First_Name.set(values[2])
            Stud_Middle_Name.set(values[3])
            Stud_Gender.set(values[4])
            Stud_YearLevel.set(values[5])
            Stud_Course.set(values[6])
       
    
       
        def updateData():
            with open('SIS.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if Stud_IDNumber.get()=="" or Stud_First_Name.get()=="" or Stud_Middle_Name.get()=="" or Stud_Last_Name.get()=="" or Stud_YearLevel.get()=="":
                    tkinter.messagebox.showinfo("SIS","Please select a student record from the table")
                else:
                    self.data[Stud_IDNumber.get()] = {'Last Name': Stud_Last_Name.get(), 'First Name': Stud_First_Name.get(), 'Middle Name': Stud_Middle_Name.get(), 'Gender': Stud_Gender.get(),'Year Level': Stud_YearLevel.get(), 'Course': Stud_Course.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("SIS", "Updated")
                Clear()
                displayData()     

        #============================================================FRAMES====================================================#
        
        MainFrame = Frame(self.root, bd=7, width=1350, height=800, relief=RIDGE, bg="gray")
        MainFrame.grid()
        
        TopFrame1 = Frame(MainFrame,  width=1330, height=130, relief=RIDGE,bg="gray")
        TopFrame1.grid(row=2, column=0)
        
        TitleFrame = Frame(MainFrame, bd=5, width=1340, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        
        TopFrame2 = Frame(MainFrame, bd=5, width=1340, height=450, relief=RIDGE)
        TopFrame2.grid(row=1, column=0)
        
        SearchFrame = Frame(MainFrame, width = 1340, height = 100, relief = RIDGE)
        SearchFrame.grid(row =3, column =0)
        
        LeftFrame = Frame(TopFrame2, bd=5, width=1350, height=400, padx=2, bg="white", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=400, padx=2, pady=4, relief=RIDGE)
        LeftFrame1.pack(side=TOP, padx=0, pady=0)
        
        RightFrame1 = Frame(TopFrame2, bd=5, width=600, height=400, padx=2, bg="white", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        

        
        #=============================================TITLE===========================================#
        
        self.lblTitle = Label(TitleFrame, font=('arial',56,'bold'), text="Student Management System", bd=7)
        self.lblTitle.grid(row=0, column=0, padx=132)
        
        #===========================================================================LABELS & ENTRy WIDGETS=======================================================#
        
        
        self.lblStudentID1 = Label(LeftFrame1, font=('arial', 12, 'bold', 'italic'), text="( YYYY-NNNN )", bd=7)
        self.lblStudentID1.grid(row=0,column=2)
        self.lblStudentID = Label(LeftFrame1, font=('arial',12,'bold'), text="Student ID", bd=7 , anchor=W)
        self.lblStudentID.grid(row=0, column=0, sticky=W, padx=5)
        self.txtStudentID = Entry(LeftFrame1, font=('arial',12,'bold'), width=40, justify='left', textvariable = Stud_IDNumber)
        self.txtStudentID.grid(row=0, column=1)
        
        self.lblLastName = Label(LeftFrame1, font=('arial',12,'bold'), text="Last Name", bd=7, anchor=W)
        self.lblLastName.grid(row=1, column=0, sticky=W, padx=5)
        self.txtLastName = Entry(LeftFrame1, font=('arial',12,'bold'), width=40, justify='left', textvariable = Stud_Last_Name)
        self.txtLastName.grid(row=1, column=1)
        
        self.lblFirstName = Label(LeftFrame1, font=('arial',12,'bold'), text="First Name", bd=7, anchor=W)
        self.lblFirstName.grid(row=2, column=0, sticky=W, padx=5)
        self.txtFirstName = Entry(LeftFrame1, font=('arial',12,'bold'), width=40, justify='left', textvariable = Stud_First_Name)
        self.txtFirstName.grid(row=2, column=1)
        
        self.lblMiddleName = Label(LeftFrame1, font=('arial',12,'bold'), text="Middle Name", bd=7, anchor=W)
        self.lblMiddleName.grid(row=3, column=0, sticky=W, padx=5)
        self.txtMiddleName = Entry(LeftFrame1, font=('arial',12,'bold'), width=40, justify='left', textvariable = Stud_Middle_Name)
        self.txtMiddleName.grid(row=3, column=1)
        
        self.lblCourse = Label(LeftFrame1, font=('arial',12,'bold'), text="Course", bd=7, anchor=W)
        self.lblCourse.grid(row=4, column=0, sticky=W, padx=5)
        self.txtCourse = Entry(LeftFrame1, font=('arial',12,'bold'), width=40, justify='left', textvariable = Stud_Course)
        self.txtCourse.grid(row=4, column=1)
        
        self.lblGender = Label(LeftFrame1, font=('arial',12,'bold'), text="Gender", bd=7, anchor=W)
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5)
        
        self.cboGender = ttk.Combobox(LeftFrame1, font=('arial',12,'bold'), state='readonly', width=39, textvariable = Stud_Gender)
        self.cboGender['values'] = ('Female', 'Male')
        self.cboGender.grid(row=5, column=1)
        
        self.lblYearLevel = Label(LeftFrame1, font=('arial',12,'bold'), text="Year Level", bd=7, anchor=W)
        self.lblYearLevel.grid(row=6, column=0, sticky=W, padx=5)
        
        self.cboYearLevel = ttk.Combobox(LeftFrame1, font=('arial',12,'bold'), state='readonly', width=39, textvariable = Stud_YearLevel)
        self.cboYearLevel['values'] = ('1st Year', '2nd Year', '3rd Year', '4th Year')
        self.cboYearLevel.grid(row=6, column=1)
        
        self.searchbar = Entry(self.root, font=('arial',12,'bold'), textvariable = searchbar, width = 29 )
        self.searchbar.place(x=850,y=490)
        self.searchbar.insert(0,'Search here')
        
        
        #=========================================================BUTTONS================================================#
        
        self.btnAddNew=Button(self.root, pady=1,bd=4,font=('arial',16,'bold'), padx=24, width=10, text='Add New Student', command=addStudent)
        self.btnAddNew.place(x=130,y=480)
        
        self.btnClear=Button(self.root, pady=1,bd=4,font=('arial',16,'bold'), padx=24, width=8, text='Clear', command=Clear)
        self.btnClear.place(x=145,y=540)
        
        self.btnUpdate=Button(self.root, pady=1,bd=4,font=('arial',16,'bold'), padx=24, width=8, text='Update', command=updateData)
        self.btnUpdate.place(x=380,y=540)

        self.btnEdit=Button(self.root, pady=1,bd=4,font=('arial',16,'bold'), padx=24, width=8, text='Edit Student', command = editData)
        self.btnEdit.place(x=380,y=480)

        self.btnDelete=Button(self.root, pady=1,bd=4,font=('arial',16,'bold'), padx=24, width=8, text='Delete',command = deleteData)
        self.btnDelete.place(x=910,y=540)

        self.btnExit=Button(self.root, pady=1,bd=4,font=('arial',16,'bold'), padx=2, width=8, text='Exit',command = iExit)
        self.btnExit.place(x=1150,y=540)

        self.btnSearch=Button(self.root, pady=1,bd=4,font=('arial',16,'bold'), padx=2, width=8, text='Search', command = searchData)
        self.btnSearch.place(x=1150,y=480)

        
        
        #==============================================================================TREEVIEW=========================================================================#
        
        scroll_y=Scrollbar(RightFrame1, orient=VERTICAL)
        
        tree = ttk.Treeview(RightFrame1, height=15, columns=("Student ID Number", "Last Name", "First Name", "Middle Name", "Gender", "Year Level", "Course"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        tree.heading("Student ID Number", text="Student ID Number")
        tree.heading("Last Name", text="Last Name")
        tree.heading("First Name", text="First Name")
        tree.heading("Middle Name", text="Middle Name")
        tree.heading("Gender", text="Gender")
        tree.heading("Year Level", text="Year Level")
        tree.heading("Course", text="Course")
        tree['show'] = 'headings'

        tree.column("Student ID Number", width=120)
        tree.column("Last Name", width=100)
        tree.column("First Name", width=100)
        tree.column("Middle Name", width=100)
        tree.column("Gender", width=70)
        tree.column("Year Level", width=70)
        tree.column("Course", width=80)
        tree.pack(fill=BOTH,expand=1)
        
        displayData()
        #===========================================================================================================================================================#
    def saveData(self):
        temps = []
        with open('SIS.csv', "w", newline ='') as update:
            fieldnames = ["Student ID Number","Last Name","First Name","Middle Name","Gender","Year Level","Course"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp ={"Student ID Number": id}
                for key, value in val.items():
                    temp[key] = value
                temps.append(temp)
            writer.writerows(temps)
            

if __name__ =='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
