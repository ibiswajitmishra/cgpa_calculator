from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import Menu
from tkinter import Image
window=Tk()
window.geometry('1400x600')
window.title("CGPA Calculator")
window.configure(background="#000")
def base():
       f=Frame(window, width='1000', height='1000', background="black")
       f.place(x=0, y=0) #Login Page Black Background 
base()
#LOGIN -------------------------------------------------------------------
def page(event):
       f2=Frame(window, width='1000', height='1000', background="black")
       f2.place(x=200, y=0) #Login Page Black Background Frame
       icon=PhotoImage(file="usericon.gif") #Login Page Icon
       iconlabel=Label(f2,image=icon)
       iconlabel.image=icon
       iconlabel.place(x=458, y=130, width=90,height=90)
       label1=Label(window, text=" CGPA Calculator ",fg="white",bg='#000',font=("Arial Bold",15))
       label1.place(x=0, y=50)
       #Progress Bars Function
       def fill(event):
              a=username.get()
              b=password.get()
              f2.after(3000,fill,"<1>")
              if((a=="")and(b=="")):
                     style = ttk.Style() 
                     style.theme_use('clam')
                     style.configure("bar1.Horizontal.TProgressbar",
                       troughcolor='black', background='red')
                     bar1=Progressbar(f2,length=20, value=100, style="bar1.Horizontal.TProgressbar")
                     bar1.place(x=600, y=255)
                     bar2=Progressbar(f2,length=20, value=100, style="bar1.Horizontal.TProgressbar")
                     bar2.place(x=600, y=290)
              elif((a=="")and(not(b==""))):
                     style = ttk.Style() 
                     style.theme_use('clam')
                     style.configure("bar1.Horizontal.TProgressbar",
                       troughcolor='black', background='#00AA00')
                     style.configure("bar2.Horizontal.TProgressbar",
                       troughcolor='black', background='red')
                     bar1=Progressbar(f2,length=20, value=100, style="bar2.Horizontal.TProgressbar")
                     bar1.place(x=600, y=255)
                     bar2=Progressbar(f2,length=20, value=100, style="bar1.Horizontal.TProgressbar")
                     bar2.place(x=600, y=290)
              elif((b=="")and(not(a==""))):
                     style = ttk.Style() 
                     style.theme_use('clam')
                     style.configure("bar1.Horizontal.TProgressbar",
                       troughcolor='black', background='red')
                     style.configure("bar2.Horizontal.TProgressbar",
                       troughcolor='black', background='#00AA00')
                     bar1=Progressbar(f2,length=20, value=100, style="bar2.Horizontal.TProgressbar")
                     bar1.place(x=600, y=255)
                     bar2=Progressbar(f2,length=20, value=100, style="bar1.Horizontal.TProgressbar")
                     bar2.place(x=600, y=290)
              elif((not(a==""))and(not(b==""))):
                     style = ttk.Style() 
                     style.theme_use('clam')
                     style.configure("bar1.Horizontal.TProgressbar",
                       troughcolor='black', background='#00AA00')
                     style.configure("bar2.Horizontal.TProgressbar",
                       troughcolor='black', background='#00AA00')
                     bar1=Progressbar(f2,length=20, value=100, style="bar2.Horizontal.TProgressbar")
                     bar1.place(x=600, y=255)
                     bar2=Progressbar(f2,length=20, value=100, style="bar1.Horizontal.TProgressbar")
                     bar2.place(x=600, y=290)
       #Username Label
       label3=Label(f2, text=" Username ",font=("calibri Bold",14), bg="black", fg="white")
       label3.place(x=305, y=250)
       #Username Input Box
       username=Entry(f2, width=23, bd=3, bg="#101010", fg="red",justify="left",
              font=("arial Bold",12),selectbackground="red", selectforeground="white",insertbackground='white')
       username.bind("<1>",fill)
       username.place(x=410, y=250)
       #Password Label
       label4=Label(f2, text=" Password  ",font=("calibri Bold",14), bg="black", fg="white")
       label4.place(x=305, y=285)
       #Password Input Box
       password=Entry(f2, width=23, bd=3, bg="#101010",show="x", fg="red", justify="left",
              font=("arial Bold",12),selectbackground="red", selectforeground="white",insertbackground='white')
       password.bind("<1>",fill)
       password.place(x=410, y=285)
       def log():
              a=username.get()     #username extracted
              b=password.get()     #password extracted
              if((a=="123456789")and(b=="123456789")):
                     messagebox.showinfo("Message", "Successfull Login")
                     f2.destroy()
                     calculator("<1>")
              elif((a=="")or(b=="")):
                     messagebox.showwarning("Warning", "Please fill all Details")
              else:
                     messagebox.showerror("Error", "Invalid Login")
       #Login BUTTON
       button=Button(f2, width=10, text="Login", bd=2, font=("arial Bold",9),
              command=log)
       button.place(x=470, y=325)
       #Forgot Passowrd
       def req(event):
              messagebox.showinfo("Forgot Password", "Go to Official Site and Request for new password")
       lbl6=Label(f2, text=" Forgot Password ? ",font=("Arial Bold",9), bg="black", fg="red")
       lbl6.place(x=420,y=360)
       lbl8=Label(f2, text="_________ ",font=("Arial Bold",9), bg="black", fg="white")
       lbl8.bind("<1>",req)
       lbl8.place(x=541,y=365)
       lbl7=Label(f2, text=" Click here ",font=("Arial Bold",9), bg="black", fg="white")
       lbl7.bind("<1>",req)
       lbl7.place(x=540,y=360)
       #temporary Button
       def temp():
              f2.destroy()
              calculator("<1>")
page("<1>")
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#CGPA Calculator Frame Function
def calculator(event):
       def destroy3(event):
              f3.destroy()
              calculator("<1>")
       def destroy2(event):
              f3.destroy()
              avg("<1>")
       def destroy1(event):
              a=messagebox.askyesno("Logout","Are you sure you want to logout")
              if(a==True):
                     f3.destroy()
                     page("<1>")
       #Black Background for CGPA Calculator Frame 
       window.configure(background='black')
       f3=Frame(window, width='1500', height='1000', background="black")
       f3.place(x=0, y=0)      
       #LABEL CGPA Calculator (ACTIVE TAB)
       lbl1=Label(f3, text=" CGPA Calculator ",font=("arial Bold",11), bg="#FFA07A",
                  width=18)
       lbl1.place(x=150,y=20)
       lbl1.bind("<1>",destroy3)
       #Label LOG OUT
       lbl3=Label(f3, text=" Logout ",font=("arial Bold",11),bg="#E9967A", width=15)
       lbl3.place(x=1150,y=20)
       lbl3.bind("<1>",destroy1)
       def semester1():
              #Semester 1 Heading LABEL
              heading=Label(f3, text="SEMESTER 1\t\t\t\t            Marks     \t\t               Credits\t\t\tGrade\t             TGPA =\t\t",
                     font=("arial Bold",11), bg="#E9967A")
              heading.place(x=200,y=80)
              valueTGPA=Label(f3, text="0.00", font=("arial Bold",11), bg="#E9967A",
                         justify="left", width="4", fg="black")
              valueTGPA.place(x=1145,y=80)
              #SUBJECT 1 (Semester 1)
              def subcheck1(event):
                     try:
                            a=sub1.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)              
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck1(event):          
                     try:                                          
                            a=credit1.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)      
              def markcheck1(event):
                     try:
                            a=mark1.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)           
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)
              def gradecheck1():
                     m1=markcheck1("<1>")
                     if(m1==0):
                            grade1['text']="F"
                            gmeaning1['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=107)
                     if(m1==4):
                            grade1['text']="D"
                            gmeaning1['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=107)
                     if(m1==5):
                            grade1['text']="C"
                            gmeaning1['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=107)
                     if(m1==6):
                            grade1['text']="B"
                            gmeaning1['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=107)
                     if(m1==7):
                            grade1['text']="B+"
                            gmeaning1['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=107)
                     if(m1==8):
                            grade1['text']="A"
                            gmeaning1['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=107)
                     if(m1==9):
                            grade1['text']="A+"
                            gmeaning1['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=107)
                     if(m1==10):
                            grade1['text']="O"
                            gmeaning1['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=107)
              id1=Label(f3, text="1.", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="5")
              id1.place(x=230,y=107)
              sub1=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="left")
              sub1.place(x=310, y=107)
              sub1.insert(1," Subject 1")
              mark1=Entry(f3, width=18, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              mark1.place(x=510, y=107)
              mark1.insert(1," 00 ")
              credit1=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              credit1.place(x=710, y=107)
              credit1.insert(1," 01 ")
              grade1=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              grade1.place(x=930,y=107)
              gmeaning1=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              gmeaning1.place(x=1070,y=107)
              #SUBJECT 2 (Semester 1)
              def subcheck2(event):
                     try:
                            a=sub2.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)  
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck2(event):          
                     try:
                            a=credit2.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)      
              def markcheck2(event):
                     try:
                            a=mark2.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)           
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)
              def gradecheck2():
                     m2=markcheck2("<1>")
                     if(m2==0):
                            grade2['text']="F"
                            gmeaning2['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=130)
                     if(m2==4):
                            grade2['text']="D"
                            gmeaning2['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=130)
                     if(m2==5):
                            grade2['text']="C"
                            gmeaning2['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=130)
                     if(m2==6):
                            grade2['text']="B"
                            gmeaning2['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=130)
                     if(m2==7):
                            grade2['text']="B+"
                            gmeaning2['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=130)
                     if(m2==8):
                            grade2['text']="A"
                            gmeaning2['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=130)
                     if(m2==9):
                            grade2['text']="A+"
                            gmeaning2['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=130)
                     if(m2==10):
                            grade2['text']="O"
                            gmeaning2['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=130)
              id2=Label(f3, text="2.", font=("arial Bold",10), bg="white",
                         justify="left", width="5")
              id2.place(x=230,y=130)
              sub2=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="left")
              sub2.place(x=310, y=130)
              sub2.insert(1," Subject 2")
              mark2=Entry(f3, width=18, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              mark2.place(x=510, y=130)
              mark2.insert(1," 00 ")
              credit2=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              credit2.place(x=710, y=130)
              credit2.insert(1," 01 ")
              grade2=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              grade2.place(x=930,y=130)
              gmeaning2=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              gmeaning2.place(x=1070,y=130)                                 
              #SUBJECT 3 (Semester 1)
              def subcheck3(event):
                     try:
                            a=sub3.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)           
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck3(event):          
                     try:                
                            a=credit3.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)      
              def markcheck3(event):
                     try:
                            a=mark3.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)           
                            else:
                                   return(-1)            
                     except ValueError:
                            return(-1)
              def gradecheck3():
                     m3=markcheck3("<1>")
                     if(m3==0):
                            grade3['text']="F"
                            gmeaning3['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=153)
                     if(m3==4):
                            grade3['text']="D"
                            gmeaning3['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=153)
                     if(m3==5):
                            grade3['text']="C"
                            gmeaning3['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=153)
                     if(m3==6):
                            grade3['text']="B"
                            gmeaning3['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=153)
                     if(m3==7):
                            grade3['text']="B+"
                            gmeaning3['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=153)
                     if(m3==8):
                            grade3['text']="A"
                            gmeaning3['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=153)
                     if(m3==9):
                            grade3['text']="A+"
                            gmeaning3['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=153)
                     if(m3==10):
                            grade3['text']="O"
                            gmeaning3['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=153)
              id3=Label(f3, text="3.", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="5")
              id3.place(x=230,y=153)
              sub3=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="left")
              sub3.place(x=310, y=153)
              sub3.insert(1," Subject 3")
              mark3=Entry(f3, width=18, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              mark3.place(x=510, y=153)
              mark3.insert(1," 00 ")
              credit3=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              credit3.place(x=710, y=153)
              credit3.insert(1," 01 ")
              grade3=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              grade3.place(x=930,y=153)
              gmeaning3=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              gmeaning3.place(x=1070,y=153) 
              #SUBJECT 4 (Semester 1)
              def subcheck4(event):
                     try:
                            a=sub4.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)           
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck4(event):          
                     try:               
                            a=credit4.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:                                   
                                   return(-1)        
                     except ValueError:
                            return(-1)      
              def markcheck4(event):
                     try:
                            a=mark4.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)
                            else:
                                   return(-1)                                           
                     except ValueError:
                            return(-1)
              def gradecheck4():
                     m4=markcheck4("<1>")
                     if(m4==0):
                            grade4['text']="F"
                            gmeaning4['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=176)
                     if(m4==4):
                            grade4['text']="D"
                            gmeaning4['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=176)
                     if(m4==5):
                            grade4['text']="C"
                            gmeaning4['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=176)   
                     if(m4==6):
                            grade4['text']="B"
                            gmeaning4['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=176)
                     if(m4==7):
                            grade4['text']="B+"
                            gmeaning4['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=176)
                     if(m4==8):
                            grade4['text']="A"
                            gmeaning4['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=176)
                     if(m4==9):
                            grade4['text']="A+"
                            gmeaning4['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=176)
                     if(m4==10):
                            grade4['text']="O"
                            gmeaning4['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=176)
              id4=Label(f3, text="4.", font=("arial Bold",10), bg="white",
                         justify="left", width="5")
              id4.place(x=230,y=176)
              sub4=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="left")
              sub4.place(x=310, y=176)
              sub4.insert(1," Subject 4")
              mark4=Entry(f3, width=18, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              mark4.place(x=510, y=176)
              mark4.insert(1," 00 ")
              credit4=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              credit4.place(x=710, y=176)
              credit4.insert(1," 01 ")
              grade4=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              grade4.place(x=930,y=176)
              gmeaning4=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              gmeaning4.place(x=1070,y=176)
              #SUBJECT 5 (Semester 1)
              def subcheck5(event):
                     try:             
                            a=sub5.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)                 
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck5(event):          
                     try:               
                            a=credit5.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)      
              def markcheck5(event):
                     try:
                            a=mark5.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)                       
                            else:
                                   return(-1)                                           
                     except ValueError:
                            return(-1)
              def gradecheck5():
                     m5=markcheck5("<1>")
                     if(m5==0):
                            grade5['text']="F"
                            gmeaning5['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=199)
                     if(m5==4):
                            grade5['text']="D"
                            gmeaning5['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=199)
                     if(m5==5):
                            grade5['text']="C"
                            gmeaning5['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=199)
                     if(m5==6):
                            grade5['text']="B"
                            gmeaning5['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=199)
                     if(m5==7):
                            grade5['text']="B+"
                            gmeaning5['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=199) 
                     if(m5==8):
                            grade5['text']="A"
                            gmeaning5['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=199)
                     if(m5==9):
                            grade5['text']="A+"
                            gmeaning5['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=199)
                     if(m5==10):
                            grade5['text']="O"
                            gmeaning5['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=199)
              id5=Label(f3, text="5.", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="5")
              id5.place(x=230,y=199)
              sub5=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="left")
              sub5.place(x=310, y=199)
              sub5.insert(1," Subject 5")
              mark5=Entry(f3, width=18, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              mark5.place(x=510, y=199)
              mark5.insert(1," 00 ")
              credit5=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              credit5.place(x=710, y=199)
              credit5.insert(1," 01 ")
              grade5=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              grade5.place(x=930,y=199)
              gmeaning5=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              gmeaning5.place(x=1070,y=199)
              #SUBJECT 6 (Semester 1)
              def subcheck6(event):
                     try:               
                            a=sub6.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)                
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck6(event):          
                     try:           
                            a=credit6.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)      
              def markcheck6(event):
                     try:
                            a=mark6.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)           
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)
              def gradecheck6():
                     m6=markcheck6("<1>")
                     if(m6==0):
                            grade6['text']="F"
                            gmeaning6['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=222)
                     if(m6==4):
                            grade6['text']="D"
                            gmeaning6['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=222)
                     if(m6==5):
                            grade6['text']="C"
                            gmeaning6['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=222)
                     if(m6==6):
                            grade6['text']="B"
                            gmeaning6['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=222)
                     if(m6==7):
                            grade6['text']="B+"
                            gmeaning6['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=222)
                     if(m6==8):
                            grade6['text']="A"
                            gmeaning6['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=222)
                     if(m6==9):
                            grade6['text']="A+"
                            gmeaning6['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=222)
                     if(m6==10):
                            grade6['text']="O"
                            gmeaning6['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=222)
              id6=Label(f3, text="6.", font=("arial Bold",10), bg="white",
                         justify="left", width="5")
              id6.place(x=230,y=222)
              sub6=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="left")
              sub6.place(x=310, y=222)
              sub6.insert(1," Subject 6")
              mark6=Entry(f3, width=18, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              mark6.place(x=510, y=222)
              mark6.insert(1," 00 ")
              credit6=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              credit6.place(x=710, y=222)
              credit6.insert(1," 01 ")
              grade6=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              grade6.place(x=930,y=222)
              gmeaning6=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              gmeaning6.place(x=1070,y=222)
              #SEMESTER 1 COMPLETED ///////////////////////////////////////////////
              #Semester 2 Heading LABEL
              heading_2=Label(f3, text="SEMESTER 2\t\t\t\t            Marks    \t\t               Credits\t\t\tGrade\t             TGPA =\t\t",
                     font=("arial Bold",11), bg="#E9967A")
              heading_2.place(x=200,y=290)
              valueTGPA_2=Label(f3, text="0.00", font=("arial Bold",11), bg="#E9967A",
                         justify="left", width="4")
              valueTGPA_2.place(x=1145,y=290)
              #SUBJECT 1 (Semester 2)
              def subcheck_1(event):
                     try:               
                            a=sub_1.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)          
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck_1(event):          
                     try:              
                            a=credit_1.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)     
              def markcheck_1(event):
                     try:
                            a=mark_1.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)           
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)
              def gradecheck_1():
                     m_1=markcheck_1("<1>")
                     if(m_1==0):
                            grade_1['text']="F"
                            gmeaning_1['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=317)
                     if(m_1==4):
                            grade_1['text']="D"
                            gmeaning_1['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=317)
                     if(m_1==5):
                            grade_1['text']="C"
                            gmeaning_1['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=317)
                     if(m_1==6):
                            grade_1['text']="B"
                            gmeaning_1['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=317)
                     if(m_1==7):
                            grade_1['text']="B+"
                            gmeaning_1['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=317)
                     if(m_1==8):
                            grade_1['text']="A"
                            gmeaning_1['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=317)
                     if(m_1==9):
                            grade_1['text']="A+"
                            gmeaning_1['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=317) 
                     if(m_1==10):
                            grade_1['text']="O"
                            gmeaning_1['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=317)
              id_1=Label(f3, text="1.", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="5")
              id_1.place(x=230,y=317)
              sub_1=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="left")
              sub_1.place(x=310, y=317)
              sub_1.insert(1," Subject 1")
              mark_1=Entry(f3, width=18, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              mark_1.place(x=510, y=317)
              mark_1.insert(1," 00 ")
              credit_1=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              credit_1.place(x=710, y=317)
              credit_1.insert(1," 01 ")
              grade_1=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              grade_1.place(x=930,y=317)
              gmeaning_1=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              gmeaning_1.place(x=1070,y=317)
              #SUBJECT 2 (Semester 2)
              def subcheck_2(event):
                     try:
                            a=sub_2.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)                    
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck_2(event):          
                     try:               
                            a=credit_2.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)     
              def markcheck_2(event):
                     try:
                            a=mark_2.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)                      
                            else:
                                   return(-1)                                                       
                     except ValueError:
                            return(-1)
              def gradecheck_2():
                     m_2=markcheck_2("<1>")
                     if(m_2==0):
                            grade_2['text']="F"
                            gmeaning_2['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=340)
                     if(m_2==4):
                            grade_2['text']="D"
                            gmeaning_2['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=340)
                     if(m_2==5):
                            grade_2['text']="C"
                            gmeaning_2['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=340)
                     if(m_2==6):
                            grade_2['text']="B"
                            gmeaning_2['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=340)
                     if(m_2==7):
                            grade_2['text']="B+"
                            gmeaning_2['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=340)
                     if(m_2==8):
                            grade_2['text']="A"
                            gmeaning_2['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=340)
                     if(m_2==9):
                            grade_2['text']="A+"
                            gmeaning_2['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=340)
                     if(m_2==10):
                            grade_2['text']="O"
                            gmeaning_2['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=340)              
              id_2=Label(f3, text="2.", font=("arial Bold",10), bg="white",
                         justify="left", width="5")
              id_2.place(x=230,y=340)
              sub_2=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="left")
              sub_2.place(x=310, y=340)
              sub_2.insert(1," Subject 2")
              mark_2=Entry(f3, width=18, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              mark_2.place(x=510, y=340)
              mark_2.insert(1," 00 ")
              credit_2=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              credit_2.place(x=710, y=340)
              credit_2.insert(1," 01 ")
              grade_2=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              grade_2.place(x=930,y=340)
              gmeaning_2=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              gmeaning_2.place(x=1070,y=340)
              #SUBJECT 3 (Semester 2)
              def subcheck_3(event):
                     try:             
                            a=sub_3.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)                
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck_3(event):          
                     try:              
                            a=credit_3.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)     
              def markcheck_3(event):
                     try:
                            a=mark_3.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)                       
                            else:
                                   return(-1)                                           
                     except ValueError:
                            return(-1)
              def gradecheck_3():
                     m_3=markcheck_3("<1>")
                     if(m_3==0):
                            grade_3['text']="F"
                            gmeaning_3['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=363)
                     if(m_3==4):
                            grade_3['text']="D"
                            gmeaning_3['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=363)
                     if(m_3==5):
                            grade_3['text']="C"
                            gmeaning_3['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=363)
                     if(m_3==6):
                            grade_3['text']="B"
                            gmeaning_3['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=363)
                     if(m_3==7):
                            grade_3['text']="B+"
                            gmeaning_3['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=363)
                     if(m_3==8):
                            grade_3['text']="A"
                            gmeaning_3['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=363)
                     if(m_3==9):
                            grade_3['text']="A+"
                            gmeaning_3['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=363)
                     if(m_3==10):
                            grade_3['text']="O"
                            gmeaning_3['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=363)
              id_3=Label(f3, text="3.", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="5")
              id_3.place(x=230,y=363)
              sub_3=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="left")
              sub_3.place(x=310, y=363)
              sub_3.insert(1," Subject 3")
              mark_3=Entry(f3, width=18, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              mark_3.place(x=510, y=363)
              mark_3.insert(1," 00 ")
              credit_3=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              credit_3.place(x=710, y=363)
              credit_3.insert(1," 01 ")
              grade_3=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              grade_3.place(x=930,y=363)
              gmeaning_3=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              gmeaning_3.place(x=1070,y=363)
              #SUBJECT 4 (Semester 2)
              def subcheck_4(event):
                     try:               
                            a=sub_4.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)                   
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck_4(event):          
                     try:               
                            a=credit_4.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:                                   
                                   return(-1)        
                     except ValueError:
                            return(-1)     
              def markcheck_4(event):
                     try:
                            a=mark_4.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)           
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)
              def gradecheck_4():
                     m_4=markcheck_4("<1>")
                     if(m_4==0):
                            grade_4['text']="F"
                            gmeaning_4['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=386)
                     if(m_4==4):
                            grade_4['text']="D"
                            gmeaning_4['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=386)
                     if(m_4==5):
                            grade_4['text']="C"
                            gmeaning_4['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=386)  
                     if(m_4==6):
                            grade_4['text']="B"
                            gmeaning_4['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=386)
                     if(m_4==7):
                            grade_4['text']="B+"
                            gmeaning_4['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=386)
                     if(m_4==8):
                            grade_4['text']="A"
                            gmeaning_4['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=386)
                     if(m_4==9):
                            grade_4['text']="A+"
                            gmeaning_4['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=386)
                     if(m_4==10):
                            grade_4['text']="O"
                            gmeaning_4['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=386)
              id_4=Label(f3, text="4.", font=("arial Bold",10), bg="white",
                         justify="left", width="5")
              id_4.place(x=230,y=386)
              sub_4=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="left")
              sub_4.place(x=310, y=386)
              sub_4.insert(1," Subject 4")
              mark_4=Entry(f3, width=18, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              mark_4.place(x=510, y=386)
              mark_4.insert(1," 00 ")
              credit_4=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              credit_4.place(x=710, y=386)
              credit_4.insert(1," 01 ")
              grade_4=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              grade_4.place(x=930,y=386)
              gmeaning_4=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              gmeaning_4.place(x=1070,y=386)
              #SUBJECT 5 (Semester 2)
              def subcheck_5(event):
                     try:              
                            a=sub_5.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)          
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck_5(event):          
                     try:
                            a=credit_5.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)     
              def markcheck_5(event):
                     try:
                            a=mark_5.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)                      
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)
              def gradecheck_5():
                     m_5=markcheck_5("<1>")
                     if(m_5==0):
                            grade_5['text']="F"
                            gmeaning_5['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=409)
                     if(m_5==4):
                            grade_5['text']="D"
                            gmeaning_5['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=409)
                     if(m_5==5):
                            grade_5['text']="C"
                            gmeaning_5['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=409)
                     if(m_5==6):
                            grade_5['text']="B"
                            gmeaning_5['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=409)
                     if(m_5==7):
                            grade_5['text']="B+"
                            gmeaning_5['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=409)
                     if(m_5==8):
                            grade5['text']="A"
                            gmeaning5['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=409)
                     if(m_5==9):
                            grade_5['text']="A+"
                            gmeaning_5['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=409)
                     if(m_5==10):
                            grade_5['text']="O"
                            gmeaning_5['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=409)
              id_5=Label(f3, text="5.", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="5")
              id_5.place(x=230,y=409)
              sub_5=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="left")
              sub_5.place(x=310, y=409)
              sub_5.insert(1," Subject 5")
              mark_5=Entry(f3, width=18, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              mark_5.place(x=510, y=409)
              mark_5.insert(1," 00 ")
              credit_5=Entry(f3, width=20, bg="#D3D3D3",font=("arial Bold",12), bd=0,
                              justify="center")
              credit_5.place(x=710, y=409)
              credit_5.insert(1," 01 ")
              grade_5=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              grade_5.place(x=930,y=409)
              gmeaning_5=Label(f3, text="--", font=("arial Bold",10), bg="#D3D3D3",
                         justify="left", width="15")
              gmeaning_5.place(x=1070,y=409)
              #SUBJECT 6 (Semester 2)
              def subcheck_6(event):
                     try:
                            a=sub_6.get()
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)          
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
              def intcheck_6(event):          
                     try:
                            a=credit_6.get()
                            b=int(a)
                            if(b>=0):
                                   return(b)
                            else:
                                   return(-1)        
                     except ValueError:
                            return(-1)     
              def markcheck_6(event):
                     try:
                            a=mark_6.get()
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)           
                            else:
                                   return(-1)                       
                     except ValueError:
                            return(-1)
              def gradecheck_6():
                     m_6=markcheck_6("<1>")
                     if(m_6==0):
                            grade_6['text']="F"
                            gmeaning_6['text']="Fail"
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=432)
                     if(m_6==4):
                            grade_6['text']="D"
                            gmeaning_6['text']="Pass"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=432)
                     if(m_6==5):
                            grade_6['text']="C"
                            gmeaning_6['text']="Average"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=432)
                     if(m_6==6):
                            grade_6['text']="B"
                            gmeaning_6['text']="Fair"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=432)
                     if(m_6==7):
                            grade_6['text']="B+"
                            gmeaning_6['text']="Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=432)
                     if(m_6==8):
                            grade_6['text']="A"
                            gmeaning_6['text']="Very Good"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=432)
                     if(m_6==9):
                            grade_6['text']="A+"
                            gmeaning_6['text']="Excellent"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=432)
                     if(m_6==10):
                            grade_6['text']="O"
                            gmeaning_6['text']="Outstanding"
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=432)
              id_6=Label(f3, text="6.", font=("arial Bold",10), bg="white",
                         justify="left", width="5")
              id_6.place(x=230,y=432)
              sub_6=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="left")
              sub_6.place(x=310, y=432)
              sub_6.insert(1," Subject 6")
              mark_6=Entry(f3, width=18, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              mark_6.place(x=510, y=432)
              mark_6.insert(1," 00 ")
              credit_6=Entry(f3, width=20, bg="white",font=("arial Bold",12), bd=0,
                              justify="center")
              credit_6.place(x=710, y=432)
              credit_6.insert(1," 01 ")
              grade_6=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              grade_6.place(x=930,y=432)
              gmeaning_6=Label(f3, text="--", font=("arial Bold",10), bg="white",
                         justify="left", width="15")
              gmeaning_6.place(x=1070,y=432)
              #RESULT ---------------------------------------------
              heading3=Label(f3, text=" OVERALL  RESULT\t\t\t\t\t\t\t\t\t\t\t            CGPA = \t\t",
                     font=("arial Bold",11), bg="darkred", fg="white")#E9967A
              heading3.place(x=200,y=500)
              valueCGPA=Label(f3, text="0.00", font=("arial Bold",11), bg="darkred",
                         justify="left", width="4", fg="white")
              valueCGPA.place(x=1145,y=500)
              missing=Label(f3, bg="orange", width=3, font=("Arial Bold",11))
              missing.place(x=230, y=528)
              missingtext=Label(f3, bg="white",  font=("Arial Bold",11),
                                text=" INVALID FIELD \t\t")
              missingtext.place(x=267, y=528)
              fail=Label(f3, bg="red", width=3, font=("Arial Bold",11))
              fail.place(x=230, y=553)
              failtext=Label(f3, bg="#D6D6D6", font=("Arial Bold",11),
                                text=" FAILED\t\t                ")
              failtext.place(x=267, y=553)
              sem1=Label(f3, bg="royalblue", width=3, font=("Arial Bold",11))
              sem1.place(x=230, y=578)
              sem1text=Label(f3, bg="white", font=("Arial Bold",11),
                                text=" SEMESTER 1\t                ")
              sem1text.place(x=267, y=578)
              sem2=Label(f3, bg="lime", width=3, font=("Arial Bold",11))
              sem2.place(x=230, y=603)
              sem2text=Label(f3, bg="#D6D6D6", font=("Arial Bold",11),
                                text=" SEMESTER 2\t                ")
              sem2text.place(x=267, y=603)
              sem1colo=Label(f3, bg="royalblue", width=3, font=("Arial Bold",11))
              sem1colo.place(x=490, y=528) 
              # PERCENTAGE SEMESTER 1
              per1label=Label(f3, bg="white",  font=("Arial Bold",11),
                                text=" PERCENTAGE %  ")
              per1label.place(x=527, y=528)
              pervalue=Label(f3, bg="white", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ",width=5)
              pervalue.place(x=665, y=528)
              tgpa1colo=Label(f3, bg="royalblue", width=3, font=("Arial Bold",11))
              tgpa1colo.place(x=490, y=553)
              tgpa1=Label(f3, bg="#D6D6D6",  font=("Arial Bold",11),
                                text=" TGPA\t\t ")
              tgpa1.place(x=527, y=553)
              tgpavalue1=Label(f3, bg="#D6D6D6", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ",width=5)
              tgpavalue1.place(x=665, y=553)
              sem2colo=Label(f3, bg="lime", width=3, font=("Arial Bold",11))
              sem2colo.place(x=745, y=528)
              per2label=Label(f3, bg="white",  font=("Arial Bold",11),
                                text=" PERCENTAGE %  ")
              per2label.place(x=782, y=528)
              pervalue2=Label(f3, bg="white", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ",width=5)
              pervalue2.place(x=920, y=528)
              tgpa2colo=Label(f3, bg="lime", width=3, font=("Arial Bold",11))
              tgpa2colo.place(x=745, y=553)
              tgpa2=Label(f3, bg="#D6D6D6",  font=("Arial Bold",11),
                                text=" TGPA\t\t ")
              tgpa2.place(x=782, y=553)
              tgpavalue2=Label(f3, bg="#D6D6D6", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ",width=5)
              tgpavalue2.place(x=920, y=553)
              overallP=Label(f3, bg="#E9967A",  font=("Arial Bold",11),
                                text=" PERCENTAGE %   ")
              overallP.place(x=1000, y=528)
              overallPvalue=Label(f3, bg="#E9967A", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ", width=5)
              overallPvalue.place(x=1140, y=528)
              overallCGPA=Label(f3, bg="#E9967A",  font=("Arial Bold",11),
                                text=" CGPA\t\t  ")
              overallCGPA.place(x=1000, y=553)
              overallCvalue=Label(f3, bg="#E9967A", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ",width=5)
              overallCvalue.place(x=1140, y=553)
              def gg():
                     v1=intcheck1("<1>")#--------------
                     if(v1==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=107)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=107)
                     v2=intcheck2("<1>")#-------------
                     if(v2==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=130)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=130)
                     v3=intcheck3("<1>")#------------
                     if(v3==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=153)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=153)
                     v4=intcheck4("<1>")#------------
                     if(v4==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=176)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=176)            
                     v5=intcheck5("<1>")#------------
                     if(v5==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=199)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=199)
                     v6=intcheck6("<1>")#------------
                     if(v6==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=222)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=222)     
                     m1=markcheck1("<1>")
                     m2=markcheck2("<1>")
                     m3=markcheck3("<1>")
                     m4=markcheck4("<1>")
                     m5=markcheck5("<1>")
                     m6=markcheck6("<1>")
                     s1=subcheck1("<1>")                     
                     s2=subcheck2("<1>")
                     s3=subcheck3("<1>")
                     s4=subcheck4("<1>")
                     s5=subcheck5("<1>")
                     s6=subcheck6("<1>")
                     if(s1==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=107)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=107)
                     if(s2==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=130)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=130)
                     if(s3==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=153)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=153)
                     if(s4==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=176)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=176)
                     if(s5==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=199)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=199)
                     if(s6==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=222)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=222)
                     if(m1==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=107)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=107)
                     if(m2==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=130)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=130)
                     if(m3==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=153)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=153)
                     if(m4==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=176)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=176)
                     if(m5==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=199)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=199)
                     if(m6==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=222)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=222)
                     v_1=intcheck_1("<1>")
                     v_2=intcheck_2("<1>")
                     v_3=intcheck_3("<1>")
                     v_4=intcheck_4("<1>")
                     v_5=intcheck_5("<1>")
                     v_6=intcheck_6("<1>")
                     m_1=markcheck_1("<1>")
                     m_2=markcheck_2("<1>")
                     m_3=markcheck_3("<1>")
                     m_4=markcheck_4("<1>")
                     m_5=markcheck_5("<1>")
                     m_6=markcheck_6("<1>")
                     s_1=subcheck_1("<1>")
                     s_2=subcheck_2("<1>")
                     s_3=subcheck_3("<1>")
                     s_4=subcheck_4("<1>")
                     s_5=subcheck_5("<1>")
                     s_6=subcheck_6("<1>")
                     if(s_1==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=317)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=317)
                     if(s_2==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=340)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=340)
                     if(s_3==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=363)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=363)
                     if(s_4==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=386)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=386)
                     if(s_5==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=409)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=409)
                     if(s_6==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=432)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=432)
                     if(v_1==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=317)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=317)
                     if(v_2==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=340)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=340)
                     if(v_3==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=363)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=363)
                     if(v_4==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=386)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=386)
                     if(v_5==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=409)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=409)
                     if(v_6==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=432)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=432)
                     if(m_1==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=317)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=317)
                     if(m_2==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=340)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=340)
                     if(m_3==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=363)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=363)
                     if(m_4==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=386)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=386)
                     if(m_5==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=409)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=409)
                     if(m_6==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=432)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=432)
                     tcredit=v1+v2+v3+v4+v5+v6
                     tproduct=(m1*v1)+(m2*v2)+(m3*v3)+(m4*v4)+(m5*v5)+(m6*v6)
                     t_credit=v_1+v_2+v_3+v_4+v_5+v_6
                     t_product=(m_1*v_1)+(m_2*v_2)+(m_3*v_3)+(m_4*v_4)+(m_5*v_5)+(m_6*v_6)
                     if((v1==-1)or(v2==-1)or(v3==-1)or(v4==-1)or(v5==-1)or(v6==-1)or
                        (v_1==-1)or(v_2==-1)or(v_3==-1)or(v_4==-1)or(v_5==-1)or(v_6==-1)):                               
                            messagebox.showwarning("Warning","Please Enter Valid Credits")
                     elif((m1==-1)or(m2==-1)or(m3==-1)or(m4==-1)or(m5==-1)or(m6==-1)or
                         (m_1==-1)or(m_2==-1)or(m_3==-1)or(m_4==-1)or(m_5==-1)or(m_6==-1) ):
                            messagebox.showwarning("Warning","Please Enter Valid Marks")
                     elif((s1==-1)or(s2==-1)or(s3==-1)or(s4==-1)or(s5==-1)or(s6==-1)or
                         (s_1==-1)or(s_2==-1)or(s_3==-1)or(s_4==-1)or(s_5==-1)or(s_6==-1) ):
                            messagebox.showwarning("Subject Name","Please Enter Subject Name")
                     else:                                                     
                            gradecheck1()
                            gradecheck2()
                            gradecheck3()
                            gradecheck4()
                            gradecheck5()
                            gradecheck6()
                            gradecheck_1()
                            gradecheck_2()
                            gradecheck_3()
                            gradecheck_4()
                            gradecheck_5()
                            gradecheck_6()
                            if(tproduct==0):
                                   tgpa="0.00"
                                   valueTGPA['text']=tgpa
                                   valueTGPA['fg']="white"
                                   valueTGPA['bg']="darkred"
                                   valueTGPA['font']=("arial bold",11)                                           
                            else:
                                   tgpa=round((tproduct/tcredit),2)
                                   valueTGPA['text']=tgpa
                                   valueTGPA['fg']="white"
                                   valueTGPA['bg']="darkred"
                                   valueTGPA['font']=("arial bold",11)
                            if(t_product==0):
                                   tgpa_2="0.00"
                                   valueTGPA_2['text']=tgpa_2
                                   valueTGPA_2['fg']="white"
                                   valueTGPA_2['bg']="darkred"
                                   valueTGPA_2['font']=("arial bold",11)
                            else:
                                   tgpa_2=round((t_product/t_credit),2)
                                   valueTGPA_2['text']=tgpa_2
                                   valueTGPA_2['fg']="white"
                                   valueTGPA_2['bg']="darkred"
                                   valueTGPA_2['font']=("arial bold",11)
                            tgpa=round((tproduct/tcredit),2)
                            tgpa_2=round((t_product/t_credit),2)
                            cgpa=round(((tgpa+tgpa_2)/2),2)
                            valueCGPA['text']=cgpa
                            valueCGPA['fg']="black"
                            valueCGPA['bg']="#E9967A"
                            valueCGPA['font']=("arial bold",11)
                            percent1=round((tgpa*10),2)
                            pervalue['text']=percent1
                            tgpavalue1['text']=round(tgpa,2)
                            percent2=round((tgpa_2*10),2)
                            pervalue2['text']=percent2
                            tgpavalue2['text']=round(tgpa_2,2)
                            overallCvalue['text']=cgpa
                            overallCvalue['bg']="#D6D6D6"
                            overallCvalue['fg']="black"
                            overallPvalue['text']=round((cgpa*10),2)
                            overallPvalue['bg']="white"
                            overallPvalue['fg']="black"                          
                            generated=Label(f3, font=("calibri bold",13), width=20, bg="orange")
                            generated.place(x=1003,y=610)
                            generated['text']=" Generated "
              btn=Button(f3, text="Generate", command=gg, font=("arial bold",11),
                         width=10, bd=0)
              btn.place(x=1095, y=580)
              btn2=Button(f3, text="Reset", font=("arial bold",11),
                         width=10, bg="white", bd=0)
              btn2.place(x=1000, y=580)
              btn2.bind("<1>",destroy3)
       semester1()
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# About Frame Function
def avg(event):      # Destroys Previous Frames while Changing Tabs
       def destroy3(event):
              f3.destroy()
              calculator("<1>")
       def destroy2(event):
              f3.destroy()
              avg("<1>")
       def destroy1(event):
              a=messagebox.askyesno("Logout","Are you sure you want to logout")
              if(a==True):
                     f3.destroy()
                     page("<1>")
       # Black Wallpaper for AVG Calculator
       f3=Frame(window, width='1500', height='1000', background="black")
       f3.place(x=150, y=0)
       #Label CGPA Calculator
       lbl1=Label(f3, text=" CGPA Calculator ",font=("arial Bold",11),
                  width=18)
       lbl1.place(x=0,y=20)
       lbl1.bind("<1>",destroy3)
       #Label LOG OUT
       lbl3=Label(f3, text=" Logout ",font=("arial Bold",11), width=15)
       lbl3.place(x=330,y=20)
       lbl3.bind("<1>",destroy1)
       window.mainloop()
