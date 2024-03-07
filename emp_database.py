from tkinter import *
from tkinter import ttk

win=Tk()

win.title("Employee Data Entry Form")



emp_dict={'111':['Raj','M', 'raj@gmail.com','IT','Bangalore'],
          '121':['Shyam','M', 'shyam@gmail.com','Training','Pune'],
          '131':['Krishna','M','krishna@gmail.com','HR','Allahabad'],
          '141':['Riya','F','riya@gmail.com','Accounts','Chandigarh'],
          '151':['Siya','F','siya@gmail.com','IT','Raipur']
          }

def search():
    
    global emp_dict
    value= emp_id_entry.get()
    label5.config(text=' ')

    if value in emp_dict.keys():
        
        details=emp_dict[value]
        emp_id_detail_entry.insert(0,value)
        emp_name_entry.insert(0,details[0])
        gender_detail.insert(0,details[1])
        email_id_entry.insert(0,details[2])
        department_detail.insert(0,details[3])
        address_detail.insert(1.0,details[4])
                

def save():
    
    value3=emp_id_detail_entry.get()

    if value3 not in emp_dict.keys():
        emp_dict[value3]=[emp_name_entry.get(),gender_detail.get(),email_id_entry.get(),department_detail.get(),address_detail.get(1.0,END)
]
    label5.config(text='The details have been saved successfully.')
    emp_id_entry.delete(0,END)
    emp_id_detail_entry.delete(0,END)
    emp_name_entry.delete(0,END)
    gender_detail.delete(0,END)
    email_id_entry.delete(0,END)
    department_detail.delete(0,END)
    address_detail.delete(1.0,END)
    

def modify():
    global emp_dict
    label5.config(text=' ')
    value1=emp_id_entry.get()
    
    if value1 in emp_dict.keys():
        details1=emp_dict[value1]
        
        emp_dict[value1][0]=emp_name_entry.get()

        emp_dict[value1][1]=gender_detail.get()

        emp_dict[value1][2]=email_id_entry.get()

        emp_dict[value1][3]=department_detail.get()

        emp_dict[value1][4]=address_detail.get(1.0,END)  
        
        # clear the screen
        emp_id_entry.delete(0,END)
        emp_id_detail_entry.delete(0,END)
        emp_name_entry.delete(0,END)
        gender_detail.delete(0,END)
        email_id_entry.delete(0,END)
        department_detail.delete(0,END)
        address_detail.delete(1.0,END)
        
        
    
def delete():
    global emp_dict
    label5.config(text=' ')
    value2=emp_id_entry.get()
    
    if value2 in emp_dict.keys():
        del emp_dict[value2]
        
    emp_id_entry.delete(0,END)
    emp_id_detail_entry.delete(0,END)
    emp_name_entry.delete(0,END)
    gender_detail.delete(0,END)
    email_id_entry.delete(0,END)
    department_detail.delete(0,END)
    address_detail.delete(1.0,END)
    


def clear():
    label5.config(text=' ')
    
    emp_id_detail_entry.delete(0,END)
    emp_name_entry.delete(0,END)
    gender_detail.delete(0,END)
    email_id_entry.delete(0,END)
    department_detail.delete(0,END)
    address_detail.delete(1.0,END)
    emp_id_entry.delete(0,END)


heading=Label(win,text="EMPLOYEE DATA ENTRY FORM",font=("Arial Bold",20),fg='dark blue')
heading.place(x=220,y=20)

emp_id=Label(win, text= 'Emp Id',width=30,justify='left',height=1,fg='black',bg='pink',font=("Arial",15))
emp_id.place(x=20,y=150)

emp_id_entry=Entry(win,width=30,font=("Arial",15))
emp_id_entry.place(x=400,y=150)

search_btn=Button(win,text='SEARCH',command=search,width=10,font=("Arial",15),fg='black',bg='pink')
search_btn.place(x=800,y=150)

seperate_line=Label(win,text=' ___________________________________________________________________________________________________________________________________________________________________________________________________',bg='white',fg='black')
seperate_line.place(x=20,y=200)

emp_id_detail=Label(win, text= 'Employee Id',width=30,justify='left',height=1,fg='black',bg='pink',font=("Arial",15))
emp_id_detail.place(x=20,y=250)

emp_id_detail_entry=Entry(win,width=30,font=("Arial",15))
emp_id_detail_entry.place(x=400,y=250)

emp_name=Label(win,text='Employee Name', width=30,justify='left',height=1,fg='black',bg='pink',font=("Arial",15))
emp_name.place(x=20,y=300)

emp_name_entry=Entry(win,width=30,font=("Arial",15))
emp_name_entry.place(x=400,y=300)

gender=Label(win,text='Gender', width=30,justify='left',height=1,fg='black',bg='pink',font=("Arial",15))
gender.place(x=20,y=350)

i=StringVar()
gender_detail=ttk.Combobox(win, width=30,textvariable=i)
gender_detail['values']=('Male','Female')
gender_detail.place(x=400,y=350)

email_id=Label(win,text="Email ID",width=30,justify='left',height=1,fg='black',bg='pink',font=("Arial",15))
email_id.place(x=20,y=400)

email_id_entry=Entry(win,width=30,font=("Arial",15))
email_id_entry.place(x=400,y=400)


department= Label(win,text='Department',width=30,justify='left',height=1,fg='black',bg='pink',font=("Arial",15))
department.place(x=20,y=450)

n=StringVar()
department_detail=ttk.Combobox(win, width=30,textvariable=n)
department_detail['values']=('Accounts','IT','HR','Training')
department_detail.place(x=400,y=450)

address=Label(win,text="Address",width=30,justify='left',height=1,fg='black',bg='pink',font=("Arial",15))
address.place(x=20,y=500)

address_detail=Text(win,width=30,relief=RAISED,height=5,font=("Arial",15),fg='black')
address_detail.place(x=400,y=500)

save_btn=Button(win,text='SAVE',width=10,font=("Arial",15),command=save,fg='black',bg='pink')
save_btn.place(x=400,y=650)

modify_btn=Button(win,text='MODIFY',command=modify,width=10,font=("Arial",15),fg='black',bg='pink')
modify_btn.place(x=550,y=650)

delete_btn=Button(win,text='DELETE',width=10,command=delete,font=("Arial",15),fg='black',bg='pink')
delete_btn.place(x=700,y=650)

clear_btn=Button(win,text='CLEAR',width=10,command=clear,font=("Arial",15),fg='black',bg='pink')
clear_btn.place(x=850,y=650)

label5=Label(win,text='',font=("Arial",15),fg='pink')
label5.place(x=850,y=500)


win.mainloop()
