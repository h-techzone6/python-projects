import tkinter
from tkinter import ttk
from tkinter import messagebox
# import tkinter.messagebox
import os
import openpyxl


def enter_data():

    accepted=accept_var.get()

    if accepted == "Accepted":


        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age=age_spinbox.get()
            nationality=nationality_combox.get()

            # Course Info
            registration_status=reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print("First name :",firstname, "Last name: ",lastname)
            print("Title:",title,"Age:",age,"Nationality:",nationality)
            print("Courses :",numcourses,"Semesters: ",numsemesters)
            print("Registration status",registration_status)

            # Add your filepath
            filepath = "F:\Source Codes\Python\dataentry_project\dataentry.xlsx"

            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading=["First Name","Last Name","Title","Age","Nationality","Courses","Semesters","Registeration Status"]
                sheet.append(heading)
                workbook.save(filepath)
            workbook=openpyxl.load_workbook(filepath)
            sheet=workbook.active
            sheet.append([firstname,lastname,title,age,nationality,numcourses,numsemesters,registration_status])
            workbook.save(filepath)

        else:
            tkinter.messagebox.showwarning(title="Error",message="First name and last name are required")
        

    else:
        # print("Error")
        tkinter.messagebox.showwarning(title="Error",message="You have not accepted terms")


window =tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

#Saving user info
user_info_frame = tkinter.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0,column=0,padx=20,pady=20)

first_name_label = tkinter.Label(user_info_frame,text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label = tkinter.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label = tkinter.Label(user_info_frame,text="Title")
title_combobox = ttk.Combobox(user_info_frame,values=["","Mr","Ms","Engr"])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label = tkinter.Label(user_info_frame,text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame,from_=18,to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label = tkinter.Label(user_info_frame,text="Nationality")
nationality_combox = ttk.Combobox(user_info_frame,values=["Myanmar","India","Thailand","Singapore"])
nationality_label.grid(row=2,column=1)
nationality_combox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

# Saving Course Info
course_frame = tkinter.LabelFrame(frame)
course_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)

registered_label =tkinter.Label(course_frame,text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")

registered_check = tkinter.Checkbutton(course_frame,text="Currently Registered",variable=reg_status_var,onvalue="Registered",offvalue="Not Registered") 
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_label = tkinter.Label(course_frame,text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(course_frame,from_=0,to='infinity')
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_label = tkinter.Label(course_frame,text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(course_frame,from_=0,to='infinity')
numsemesters_label.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

# Accpet terms
terms_frame = tkinter.LabelFrame(frame,text="Terms and Conditions")
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=20)

accept_var = tkinter.StringVar(value="Not accepted")
terms_check = tkinter.Checkbutton(terms_frame,text="I accept the terms and conditions",variable=accept_var,onvalue="Accepted",offvalue="Not accepted")
terms_check.grid(row=0,column=0)

#Button
button = tkinter.Button(frame,text="Enter data",command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=20)

window.mainloop()