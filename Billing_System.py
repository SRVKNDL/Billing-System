
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#                            __    __     _______     _______               ____                            ____
#                           |  |  |  |   |       |   |       |    |\   |   |        |   |   O    |\    |   |
#                           |  |__|  |   |       |   |       |    | \  |   |____    |___|   |    | \   |   |____    
#                           |        |   |       |   |       |    |  \ |       |    |   |   |    |  \  |   |
#                           |        |   |_______|   |_______|    |   \|   ____|    |   |   |    |   \ |   |____
#
#                                     _____     _______                       _____      ____
#                                    |     |   |       |    |      |    |       |       |    |   |    |
#                                    |_____|   |       |    |      |    |       |       |____|   |____|    
#                                    |         |       |    |      |    |       |       | \           |
#                                    |         |_______|    |______|    |___    |       |  \      ____|
#
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================
#===============================================================================================================================================




#
#
#
#
#
from tkinter import *
import random
import os
import sys
import tempfile
from tkinter import ttk
import time;
import datetime
from tkinter import font
import tkinter
from tkinter.font import Font
from tkinter import messagebox 
import tkinter as tk

class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#708090", height=431, width=626)  # this is the background
        main_frame.pack(fill="both", expand="true")

        self.geometry("626x431")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "blue",
                       "foreground": "#E1FFFF"}

        frame_login = tk.Frame(main_frame, bg="blue", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        label_title = tk.Label(frame_login, title_styles, text="Login Page")
        label_title.grid(row=0, column=1, columnspan=1)

        label_user = tk.Label(frame_login, text_styles, text="Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(frame_login, text_styles, text="Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(frame_login, text="Login", command=lambda: getlogin())
        button.place(rely=0.70, relx=0.28)

        signup_btn = ttk.Button(frame_login, text="Register", command=lambda: get_signup())
        signup_btn.place(rely=0.70, relx=0.53)

        close_btn = ttk.Button(frame_login, text="Exit", command=lambda: get_close())
        close_btn.place(rely=0.70, relx=0.78)


        def get_close():
                top.destroy()
                sys.exit()
        def get_signup():
            SignupPage()

        def getlogin():
            username = entry_user.get()
            password = entry_pw.get()
            # if your want to run the script as it is set validation = True
            validation = validate(username, password)
            if validation:
                tk.messagebox.showinfo("Login Successful",
                                       "Welcome {}".format(username))
                top.destroy()
            else:
                tk.messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")

        def validate(username, password):
            # Checks the text file for a username\password combination.
            try:
                with open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/credentials.txt", "r") as credentials:
                    for line in credentials:
                        line = line.split(",")
                        if line[1] == username and line[3] == password:
                            return True
                    return False
            except FileNotFoundError:
                return False


class SignupPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#3F6BAA", height=400, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("250x150")
        self.resizable(0, 0)

        self.title("Registration")

        text_styles = {"font": ("Verdana", 10),
                       "background": "#3F6BAA",
                       "foreground": "#E1FFFF"}

        label_user = tk.Label(main_frame, text_styles, text="Admin Username:")
        label_user.grid(row=0, column=0)
        
        label_user = tk.Label(main_frame, text_styles, text="Admin Password:")
        label_user.grid(row=1, column=0)

        label_user = tk.Label(main_frame, text_styles, text="New Username:")
        label_user.grid(row=2, column=0)

        label_pw = tk.Label(main_frame, text_styles, text="New Password:")
        label_pw.grid(row=3, column=0)

        entry_adminuser = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_adminuser.grid(row=0, column=1)

        entry_adminpw = ttk.Entry(main_frame, width=20, cursor="xterm",show="*")
        entry_adminpw.grid(row=1, column=1)

        entry_user = ttk.Entry(main_frame, width=20, cursor="xterm" ,)
        entry_user.grid(row=2, column=1)

        entry_pw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        entry_pw.grid(row=3, column=1)

        button = ttk.Button(main_frame, text="Create Account", command=lambda: signup())
        button.grid(row=4, column=1)

        def signup():
            # Creates a text file with the Username and password
            adminuser=entry_adminuser.get()
            adminpw=entry_adminpw.get()
            user = entry_user.get()
            pw = entry_pw.get()
            validation = validate_user(user)
            if adminuser=="moonshine-admin" and adminpw=="9815440039":
                    if not validation:
                        tk.messagebox.showerror("Information", "That Username already exists")
                    else:
                        if len(pw) > 6:
                                credentials = open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/credentials.txt", "a")
                                credentials.write(f"Username,{user},Password,{pw},\n")
                                credentials.close()
                                tk.messagebox.showinfo("Information", "Your account details have been stored.")
                                SignupPage.destroy(self)

                        else:
                                tk.messagebox.showerror("Information", "Your password needs to be longer than 6 values.")
            else:
                    messagebox.showerror("Information","Wrong Admin Username Or Password")


        def validate_user(username):
            # Checks the text file for a username\password combination.
            try:
                with open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/credentials.txt", "r") as credentials:
                    for line in credentials:
                        line = line.split(",")
                        if line[1] == username:
                            return False
                return True
            except FileNotFoundError:
                return True


class Poultry_app():
        
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x800+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("MOONSHINE POULTRY PVT. LTD.")
        #===========================================================variables=======================================================================================
        idate = StringVar()
        idate.set(time.strftime("%d-%m-20%y"))

        name= StringVar()
        contact= StringVar()
        Address= StringVar()
        bill_no= StringVar()
        provider=StringVar()
        large_eggs= IntVar()
        medium_eggs= IntVar()
        small_eggs= IntVar()
        cracked_eggs= IntVar()
        chicken= IntVar()
        litter=IntVar()
        total=IntVar()
        large_rate=IntVar()
        medium_rate=IntVar()
        small_rate=IntVar()
        chicken_rate=IntVar()
        litter_rate=IntVar()
        large_ttl=IntVar()
        medium_ttl=IntVar()
        small_ttl=IntVar()
        chicken_ttl=IntVar()
        litter_ttl=IntVar()
        discount=IntVar()
        self.for_save=StringVar()
        ttl_date=StringVar()
        daily_sum=IntVar()
        date_bs=StringVar()

#=====================================================================WINDOWS===================================================================
        
        def date1():
                q1=idate.get()
                file1=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/date/current.txt","w")
                file1.write(q1)

        date1()

        def date2():
                file1=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/date/current.txt","r")
                q1=file1.read()
                q2=idate.get()

                if q1!=q2:
                        p=messagebox.askokcancel("Change Date")
                        if p>0:
                                file=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/date/current.txt","w")
                                file.write(idate.get())
                                date3()
                        elif p<0:
                                pass
                else:
                        pass
        date2()

        def date4():
                file1=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/date/last_bs.txt", "r")
                q1=file1.read()
                date_bs.set(q1)
        
        date4()

        def date5():
                file1=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/date/last_bs.txt", "w")
                q=date_bs.get()
                file1.write(q)
         
        def date3():
                date_frame=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
                date_frame.place(x=400,y=350,width=375,height=110)


                lblrates=Label(date_frame, font=('arial',16,'bold'),text="Date in BS", bd=7,height=1)
                lblrates.grid(row=0,column=0 ,sticky=W)

                txtlarge=Entry(date_frame, font=('arial',13,'bold'), textvariable=date_bs ,bd=7,insertwidth=2)
                txtlarge.grid(row=1,column=0)

                btndone=Button(date_frame,bd=7,font=('arial',16,'bold'),width=10,text="Done",command=lambda:done()).grid(row=1, column=1,padx=0)
                def done():
                        date_frame.destroy()
                        date5()

                


        
        ttl_date.set(date_bs.get())
        

        def bill_fetch():   
                file0=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/bill no.txt", "r")
                r_bill_no=file0.read()
                last_bill_no=int(r_bill_no)
                bill_no.set(last_bill_no)
                file0.close()


        def bill_set():
                file0=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/bill no.txt", "r")
                r_bill_no=file0.read()
                last_bill_no=int(r_bill_no)
                now_bill_no=last_bill_no+1
                q4=str(now_bill_no)
                file1=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/bill no.txt", "w")
                file1.write(q4)
                file1.close()
        
        bill_fetch()


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Rate Set++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        def rate_set():

                file1=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/rates/large.txt","r")
                q1=file1.read()
                q1=int(q1)
                large_rate.set(q1)
                file1.close()  

                file2=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/rates/medium.txt","r")
                q2=file2.read()
                q2=int(q2)
                medium_rate.set(q2)
                file3=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/rates/small.txt","r")
                q3=file3.read()
                q3=int(q3)
                small_rate.set(q3)
                file3.close()

                file4=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/rates/chicken.txt","r")
                q4=file4.read()
                q4=int(q4)
                chicken_rate.set(q4)
                file4.close()

                file5=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/rates/litter.txt","r")
                q5=file5.read()
                q5=int(q5)
                litter_rate.set(q5)
                file5.close()


        rate_set()



#==================================================================Frames========================================================================

        Mainframe=Frame(self.root)
        Mainframe.grid()

        Tops=Frame(Mainframe, bd=10 , relief=RIDGE)  #bd=border
        Tops.pack(side=TOP)

        self.lbltitle=Label(Tops, width=30, font=('arial',39,'bold'),text="Billing System",bg="#FF0000",bd=12,relief=RIDGE,fg="white",justify=CENTER)
        self.lbltitle.pack(fill=X)

        Bill_frame= LabelFrame(Mainframe, bd=10,bg="#9932CC",width=1000,height=50,font=('arial',12,'bold'),text='',relief=RIDGE)
        Bill_frame.pack(padx=38,side=TOP)

        MembersName_F= LabelFrame(Mainframe, bd=10,bg="#008000",fg="white",width=1300,height=400,font=('arial',12,'bold'),text='Customer Details',relief=RIDGE)
        MembersName_F.pack(padx=38, side=TOP )

        Products_frame= LabelFrame(Mainframe, bd=10,bg="#9932CC",width=1300,height=600,font=('arial',12,'bold'),text='Products',relief=RIDGE)
        Products_frame.pack(padx=38,side=TOP)

        Button_frame=Frame(self.root,bd=10,relief=RIDGE,bg="#E5B4F3")
        Button_frame.place(x=900,y=475,width=400,height=170)

        Disc_ttl=Frame(self.root,bd=10,relief=RIDGE,bg="#E5B4F3")
        Disc_ttl.place(x=470,y=475,width=425,height=200)

        self.lbldisc=Label(Disc_ttl, font=('arial',16,'bold'),text="Discount", bd=7)
        self.lbldisc.grid(row=0,column=0 ,sticky=W)
        self.lbldisc=Entry(Disc_ttl, font=('arial',13,'bold'), textvariable=discount ,bd=7,insertwidth=2)
        self.lbldisc.grid(row=0,column=1)

        self.lblttl=Label(Disc_ttl, font=('arial',16,'bold'),text="Total      ", bd=7)
        self.lblttl.grid(row=2,column=0 ,sticky=W)
        self.lblttl=Entry(Disc_ttl, font=('arial',13,'bold'), textvariable=total ,bd=7,insertwidth=2,state=DISABLED)
        self.lblttl.grid(row=2,column=1)

        
        #===========================================================Widget bill no. and Date===============================================================

        self.lblbill=Label(Bill_frame, font=('arial',16,'bold'),text="Bill.No.", bd=7)
        self.lblbill.grid(row=0,column=0 ,sticky=W)
        self.txtbill=Entry(Bill_frame, font=('arial',13,'bold'), textvariable=bill_no ,bd=7,insertwidth=2,state=DISABLED)
        self.txtbill.grid(row=0,column=1)


        self.lbldate=Label(Bill_frame, font=('arial',16,'bold'),text="Date", bd=7)
        self.lbldate.grid(row=0,column=2 ,sticky=W)
        self.txtdate=Entry(Bill_frame, font=('arial',13,'bold'), textvariable=date_bs ,bd=7,insertwidth=2,state=DISABLED)
        self.txtdate.grid(row=0,column=3)



        #=========================================================Widgets Customer Details=================================================================

        self.lblname=Label(MembersName_F, font=('arial',16,'bold'),text="Name", bd=7)
        self.lblname.grid(row=0,column=0 ,sticky=W)
        self.txtname=Entry(MembersName_F, font=('arial',13,'bold'), textvariable=name ,bd=7,insertwidth=2,)
        self.txtname.grid(row=0,column=1)

        self.lblAddress=Label(MembersName_F, font=('arial',16,'bold'),text="Address", bd=7)
        self.lblAddress.grid(row=0,column=3 ,sticky=W)
        self.txtAddress=Entry(MembersName_F, font=('arial',13,'bold'), textvariable=Address ,bd=7,insertwidth=2,)
        self.txtAddress.grid(row=0,column=4)

        self.lblcontact=Label(MembersName_F, font=('arial',16,'bold'),text="Contact", bd=7)
        self.lblcontact.grid(row=0,column=5 ,sticky=W)
        self.txtcontact=Entry(MembersName_F, font=('arial',13,'bold'), textvariable=contact ,bd=7,insertwidth=2,)
        self.txtcontact.grid(row=0,column=6)

        self.lblAddress=Label(MembersName_F, font=('arial',16,'bold'),text="Provider", bd=7)
        self.lblAddress.grid(row=0,column=7 ,sticky=W)
        self.txtAddress=Entry(MembersName_F, font=('arial',13,'bold'), textvariable=provider ,bd=7,insertwidth=2,)
        self.txtAddress.grid(row=0,column=8)
#===============================================================Widget product egg===============================================================

        self.lbleggs=Label(Products_frame, font=('arial',16,'bold'),text="Eggs", bd=7)
        self.lbleggs.grid(row=0,column=0 ,sticky=W)

        self.lbllarge=Label(Products_frame, font=('arial',16,'bold'),text="Large\t", bd=7)
        self.lbllarge.grid(row=1,column=0 ,sticky=W)
        self.txtlarge=Entry(Products_frame, font=('arial',13,'bold'), textvariable=large_eggs ,bd=7,insertwidth=2,)
        self.txtlarge.grid(row=1,column=1)

        self.lblmedium=Label(Products_frame, font=('arial',16,'bold'),text="Medium\t", bd=7)
        self.lblmedium.grid(row=2,column=0 ,sticky=W)
        self.txtmedium=Entry(Products_frame, font=('arial',13,'bold'), textvariable=medium_eggs ,bd=7,insertwidth=2,)
        self.txtmedium.grid(row=2,column=1)

        self.lblsmall=Label(Products_frame, font=('arial',16,'bold'),text="Small\t", bd=7)
        self.lblsmall.grid(row=3,column=0 ,sticky=W)
        self.txtsmall=Entry(Products_frame, font=('arial',13,'bold'), textvariable=small_eggs ,bd=7,insertwidth=2,)
        self.txtsmall.grid(row=3,column=1)

        self.lblcracked=Label(Products_frame, font=('arial',16,'bold'),text="Cracked\t", bd=7)
        self.lblcracked.grid(row=4,column=0 ,sticky=W)
        self.txtcracked=Entry(Products_frame, font=('arial',13,'bold'), textvariable=cracked_eggs ,bd=7,insertwidth=2,)
        self.txtcracked.grid(row=4,column=1)

#=========================================================Widgets product Chicken=====================================================================

        self.lblchicken=Label(Products_frame, font=('arial',16,'bold'),text="Chickens", bd=7)
        self.lblchicken.grid(row=0,column=2 ,sticky=W)
        
        self.lbllayer=Label(Products_frame, font=('arial',16,'bold'),text="Chicken(Layers)", bd=7)
        self.lbllayer.grid(row=1,column=2 ,sticky=W)
        self.txtlayer=Entry(Products_frame, font=('arial',13,'bold'), textvariable=chicken ,bd=7,insertwidth=2,)
        self.txtlayer.grid(row=1,column=3)

#===========================================================Widget product litter================================================================

        self.lbllitter=Label(Products_frame, font=('arial',16,'bold'),text="Litter", bd=7)
        self.lbllitter.grid(row=0,column=4 ,sticky=W)


        self.lblsacks=Label(Products_frame, font=('arial',16,'bold'),text="    Litter(Sacks)    ", bd=7)
        self.lblsacks.grid(row=1,column=4 ,sticky=W)
        self.txtsacks=Entry(Products_frame, font=('arial',13,'bold'), textvariable=litter ,bd=7,insertwidth=2,)
        self.txtsacks.grid(row=1,column=5)

#=================================================================print frame=====================================================================

        Print_frame=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        Print_frame.place(x=40,y=475,width=425,height=225)

        lblprint=Label(Print_frame,text="Bill",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)
        scrol_y=Scrollbar(Print_frame,orient=VERTICAL)
        self.lblprint=Text(Print_frame,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.lblprint.yview)
        self.lblprint.pack(fill=BOTH,expand=1)

        Save_frame=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        Save_frame.place(x=470,y=577,width=1,height=1)

        lblsave=Label(Save_frame,text="Save",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)
        scrol_x=Scrollbar(Save_frame,orient=HORIZONTAL)
        self.lblsave=Text(Save_frame,yscrollcommand=scrol_x.set)
        scrol_x.pack(side=RIGHT,fill=X)
        scrol_x.config(command=self.lblsave.xview)
        self.lblsave.pack(fill=BOTH,expand=1)

        self.btntotal_bill=Button(Button_frame,bd=7,font=('arial',16,'bold'),width=13,text="Total Bill",command=lambda:ttl_bill()).grid(row=0, column=0,pady=0)
        self.btnsave=Button(Button_frame,bd=7,font=('arial',16,'bold'),width=13,text="Save",command=lambda:save()).grid(row=0, column=1,pady=0,)
        self.btnprint=Button(Button_frame,bd=7,font=('arial',16,'bold'),width=13,text="Print",command=lambda:print()).grid(row=1, column=0,pady=0,)
        self.btnclear=Button(Button_frame,bd=7,font=('arial',16,'bold'),width=13,text="Clear",command=lambda:clear()).grid(row=1, column=1,pady=0)
        self.btnexit=Button(Button_frame,bd=7,font=('arial',16,'bold'),width=13,text="Exit",command=lambda:exit1()).grid(row=2, column=0,padx=0)
        self.btnsetting=Button(Button_frame,bd=7,font=('arial',16,'bold'),width=13,text="Rates",command=lambda:rates()).grid(row=2, column=1,padx=0)
        btndate=Button(Bill_frame,bd=7,font=('arial',16,'bold'),width=6,text="Change",command=lambda:date3()).grid(row=0, column=5,padx=0)

        Print_frame2=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        Print_frame2.place(x=0,y=0,width=1,height=1)

        lblprint2=Label(Print_frame2,text="",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)
        scrol_z=Scrollbar(Print_frame2,orient=VERTICAL)
        self.lblprint2=Text(Print_frame2,yscrollcommand=scrol_z.set)
        scrol_z.pack(side=RIGHT,fill=Y)
        scrol_z.config(command=self.lblprint2.yview)
        self.lblprint2.pack(fill=BOTH,expand=1)
        

#===========================================================================fuctions=============================================================
        
#===================================================================Daily total==================================================================
        
        self.lbld_ttl=Label(Disc_ttl, font=('arial',16,'bold'),text="Total Of  ", bd=7)
        self.lbld_ttl.grid(row=3,column=0 ,sticky=W)
        self.lbld_ttl=Entry(Disc_ttl, font=('arial',13,'bold'), textvariable=ttl_date,bd=7,insertwidth=2)
        self.lbld_ttl.grid(row=3,column=1)

        self.btntotal_bill=Button(Disc_ttl,bd=7,font=('arial',16,'bold'),width=7,text="Get Total",command=lambda:daily_total2()).grid(row=4, column=0,pady=0)
        self.lbld_ttl=Entry(Disc_ttl, font=('arial',13,'bold'), textvariable=daily_sum,bd=7,insertwidth=2,state=DISABLED)
        self.lbld_ttl.grid(row=4,column=1) 

        def a():
                file= open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/daily_total/" + date_bs.get() + "-total" + ".txt" , "a")
                q=total.get()
                q=str(q)
                file.write(f"{q}\n")
                
                       
                                
        def c():
                total=0
                with open('C:/Users/saura/Desktop/Billing/Donot_Touch_Files/daily_total/' + date_bs.get() + '-total' + '.txt') as infile:
                        for line in infile:
                                try:
                                        num = int(line)
                                        total += num
                                        daily_sum.set(total)
                                except ValueError:
                                        pass
                

                        
        def daily_total():
                a()
                c()

        def daily_total2():
                c()


        def clear():
                k=messagebox.askyesnocancel("Change Bill")
                if k==True:
                        bill_set()
                        bill_fetch()
                        self.lblprint.delete(1.0,END)
                        self.lblsave.delete(1.0,END)
                        large_eggs.set(0)
                        medium_eggs.set(0)
                        small_eggs.set(0)
                        cracked_eggs.set(0)
                        chicken.set(0)
                        litter.set(0)

                        name.set("")
                        contact.set("")
                        Address.set("")
                        provider.set("")
                        discount.set(0)
                        total.set(0)
                elif k==False:
                        self.lblprint.delete(1.0,END)
                        self.lblsave.delete(1.0,END)
                        large_eggs.set(0)
                        medium_eggs.set(0)
                        small_eggs.set(0)
                        cracked_eggs.set(0)
                        chicken.set(0)
                        litter.set(0)

                        name.set("")
                        contact.set("")
                        Address.set("")
                        provider.set("")
                        discount.set(0)
                        total.set(0)
                elif k==None:
                        pass




                Print_frame=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
                Print_frame.place(x=40,y=475,width=425,height=225)

                lblprint=Label(Print_frame,text="Bill",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)
                scrol_y=Scrollbar(Print_frame,orient=VERTICAL)
                self.lblprint=Text(Print_frame,yscrollcommand=scrol_y.set)
                scrol_y.pack(side=RIGHT,fill=Y)
                scrol_y.config(command=self.lblprint.yview)
                self.lblprint.pack(fill=BOTH,expand=1)

                
        def exit1():
                k1=messagebox.askyesnocancel("Change Bill")
                if(k1==True):
                        bill_set()
                        self.root.destroy()
                elif(k1==False):
                        self.root.destroy()
                elif(k1==None):
                        pass
        
        

        def ttl_bill():
                large_ttl.set(large_eggs.get()*large_rate.get())
                medium_ttl.set(medium_eggs.get()*medium_rate.get())
                small_ttl.set(small_eggs.get()*small_rate.get())
                chicken_ttl.set(chicken.get()*chicken_rate.get())
                litter_ttl.set(litter.get()*litter_rate.get())
                total.set(large_ttl.get()+medium_ttl.get()+small_ttl.get()+cracked_eggs.get()+chicken_ttl.get()+litter_ttl.get()-discount.get())
                self.lblprint.insert(END,"\t    MoonShine Poultry PVT. LTD.\n    \t\tContact: 9855061005\n\nBill.No.: " + bill_no.get() +"\nDate: "+  date_bs.get()+"\n")

                if name.get()!="":
                        self.lblprint.insert(END,"\nCustomer Name: " + name.get())
                if Address.get()!="":
                        self.lblprint.insert(END,"\nAddress: " + Address.get())
                if contact.get()!="":
                        self.lblprint.insert(END,"\nContact: " + contact.get())
                if provider.get()!="":
                        self.lblprint.insert(END,"\nProvider: " + provider.get())
                
                self.lblprint.insert(END,"\n________________________________________________\nProduct\t       Quantity\tRate\t\tTotal")

                if large_eggs.get()!=0:
                        self.lblprint.insert(END,f"\nLarge Eggs\t\t {large_eggs.get()}\t {large_rate.get()}\t{large_ttl.get()}")
                if medium_eggs.get()!=0:
                        self.lblprint.insert(END,f"\nMedium Eggs\t\t {medium_eggs.get()}\t {medium_rate.get()}\t{medium_ttl.get()}")
                if small_eggs.get()!=0:
                        self.lblprint.insert(END,f"\nSmall Eggs\t\t {small_eggs.get()}\t {small_rate.get()}\t{small_ttl.get()}")
                if cracked_eggs.get()!=0:
                        self.lblprint.insert(END,f"\nCracked Eggs\t\t\t\t{cracked_eggs.get()}" )

                if chicken.get()!=0:
                        self.lblprint.insert(END,f"\nChicken\t\t {chicken.get()}\t {chicken_rate.get()}\t{chicken_ttl.get()}")
    
                if litter.get()!=0:
                        self.lblprint.insert(END,f"\nLitter\t\t {litter.get()} \t {litter_rate.get()}\t{litter_ttl.get()}")
                
                if discount.get()!=0:
                        self.lblprint.insert(END,f"\nDiscount\t\t\t\t{discount.get()}" )
                if large_eggs.get() or medium_eggs.get() or small_eggs.get() or cracked_eggs.get() or chicken.get() or litter.get()!=0:
                        self.lblprint.insert(END,f"\n________________________________________________\n\t\t\t Total: {total.get()}\n================================================" )


        def print():
                self.lblprint2.delete(1.0, END)
                self.lblprint2.insert(END,"\tMoonShine Poultry PVT. LTD.\n\t    Contact: 9855061005\n\nBill.No.: " + bill_no.get() +"\nDate: "+  date_bs.get()+ "\n")

                if name.get()!="":
                        self.lblprint2.insert(END,"\nCustomer Name: " + name.get())
                if Address.get()!="":
                        self.lblprint2.insert(END,"\nAddress: " + Address.get())
                if contact.get()!="":
                        self.lblprint2.insert(END,"\nContact: " + contact.get())
                if provider.get()!="":
                        self.lblprint2.insert(END,"\nProvider: " + provider.get())

                self.lblprint2.insert(END,"\n_____________________________________\nProduct\t\tQty\tRate\tTotal")

                if large_eggs.get()!=0:
                        self.lblprint2.insert(END,f"\nLarge Eggs\t{large_eggs.get()}\t{large_rate.get()}\t{large_ttl.get()}")

                if medium_eggs.get()!=0:
                        self.lblprint2.insert(END,f"\nMedium Eggs\t{medium_eggs.get()}\t{medium_rate.get()}\t{medium_ttl.get()}")

                if small_eggs.get()!=0:
                        self.lblprint2.insert(END,f"\nSmall Eggs\t{small_eggs.get()}\t{small_rate.get()}\t{small_ttl.get()}")

                if cracked_eggs.get()!=0:
                        self.lblprint2.insert(END,f"\nCracked Eggs\t\t\t{cracked_eggs.get()}" )

                if chicken.get()!=0:
                        self.lblprint2.insert(END,f"\nChicken\t\t{chicken.get()}\t{chicken_rate.get()}\t{chicken_ttl.get()}")
    
                if litter.get()!=0:
                        self.lblprint2.insert(END,f"\nLitter\t\t{litter.get()}\t{litter_rate.get()}\t{litter_ttl.get()}")
                
                if discount.get()!=0:
                        self.lblprint2.insert(END,f"\nDiscount\t\t\t{discount.get()}" )
                self.lblprint2.insert(END,"\n_____________________________________")
                if large_eggs.get() or medium_eggs.get() or small_eggs.get() or cracked_eggs.get() or chicken.get() or litter.get()!=0:
                        self.lblprint2.insert(END,f"\n\t\t\tTotal: {total.get()}" )
                self.lblprint2.insert(END,"\n=====================================")
                q=self.lblprint2.get("1.0", "end-1c")
                filename=tempfile.mktemp(".txt")
                open(filename, "w").write(q)

                p=messagebox.askokcancel("Do you want to print the bill")
                if(p>0):
                        os.startfile(filename, "print")
                elif(p<0):
                       pass

                
        def save():
                self.lblsave.insert(END, "\n============================================================================================================================\n")
                self.lblsave.insert(END, ">>Bill.No.: " + bill_no.get())
                self.lblsave.insert(END, "\n>>Date: " + date_bs.get())
                if name.get()!="":
                        self.lblsave.insert(END,"\n>>Customer Name: " + name.get())
                if Address.get()!="":
                        self.lblsave.insert(END,"\n>>Address: " + Address.get())
                if contact.get()!="":
                        self.lblsave.insert(END,"\n>>Contact: " + contact.get())
                if provider.get()!="":
                        self.lblsave.insert(END,"\n>>Provider: " + provider.get())

                if large_eggs.get()!=0:
                        self.lblsave.insert(END,f"\n>>Large Eggs: {large_ttl.get()}")

                if medium_eggs.get()!=0:
                        self.lblsave.insert(END,f"\n>>Medium Eggs: {medium_ttl.get()}")

                if small_eggs.get()!=0:
                        self.lblsave.insert(END,f"\n>>Small Eggs: {small_ttl.get()}")

                if cracked_eggs.get()!=0:
                        self.lblsave.insert(END,f"\n>>Cracked Eggs: {cracked_eggs.get()}" )

                if chicken.get()!=0:
                        self.lblsave.insert(END,f"\n>>Chicken: {chicken_ttl.get()}")
    
                if litter.get()!=0:
                        self.lblsave.insert(END,f"\n>>Litter: {litter_ttl.get()}")
                
                if discount.get()!=0:
                        self.lblsave.insert(END,f"\n>>Discount: {discount.get()}" )
                self.lblsave.insert(END,f"\n>>Total: {total.get()}" )
                j=self.lblsave.get("1.0", "end-1c")
                file= open("C:/Users/saura/Desktop/Billing/Daily_Files/" + date_bs.get() + ".txt" , "a")
                p=messagebox.askokcancel("Do you want to save it in a file")
                if(p>0):
                        file.write(j)
                        daily_total()
                elif(p<0):
                        pass
                        
        def rates():

                Rates_frame=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
                Rates_frame.place(x=40,y=400,width=425,height=300)


                lblrates=Label(Rates_frame, font=('arial',16,'bold'),text="Rates", bd=7,height=1)
                lblrates.grid(row=0,column=0 ,sticky=W)

                lbllarge=Label(Rates_frame, font=('arial',16,'bold'),text="Large Eggs", bd=7)
                lbllarge.grid(row=1,column=0 ,sticky=W)
                txtlarge=Entry(Rates_frame, font=('arial',13,'bold'), textvariable=large_rate ,bd=7,insertwidth=2)
                txtlarge.grid(row=1,column=1)

                lblmedium=Label(Rates_frame, font=('arial',16,'bold'),text="Medium Eggs", bd=7)
                lblmedium.grid(row=2,column=0 ,sticky=W)
                txtmedium=Entry(Rates_frame, font=('arial',13,'bold'), textvariable=medium_rate ,bd=7,insertwidth=2)
                txtmedium.grid(row=2,column=1)

                lblsmall=Label(Rates_frame, font=('arial',16,'bold'),text="Small Eggs", bd=7)
                lblsmall.grid(row=3,column=0 ,sticky=W)
                txtsmall=Entry(Rates_frame, font=('arial',13,'bold'), textvariable=small_rate ,bd=7,insertwidth=2)
                txtsmall.grid(row=3,column=1)

                lblchicken=Label(Rates_frame, font=('arial',16,'bold'),text="Chicken", bd=7)
                lblchicken.grid(row=4,column=0 ,sticky=W)
                txtchicken=Entry(Rates_frame, font=('arial',13,'bold'), textvariable=chicken_rate ,bd=7,insertwidth=2)
                txtchicken.grid(row=4,column=1)

                lbllitter=Label(Rates_frame, font=('arial',16,'bold'),text="Litter", bd=7)
                lbllitter.grid(row=5,column=0 ,sticky=W)
                txtlitter=Entry(Rates_frame, font=('arial',13,'bold'), textvariable=litter_rate ,bd=7,insertwidth=2)
                txtlitter.grid(row=5,column=1)

                btn_set=Button(Rates_frame,bd=7,font=('arial',16,'bold'),width=5,text="Set",command=lambda:set_value()).grid(row=6, column=1,pady=0,)

                def set_value():
                        if large_rate.get()>0:
                                q1=large_rate.get()
                                q1=str(q1)
                                file1=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/rates/large.txt","w")
                                file1.write(q1)
                                file1.close()
                        
                        if medium_rate.get()>0:
                                q2=medium_rate.get()
                                q2=str(q2)
                                file2=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/rates/medium.txt","w")
                                file2.write(q2)
                                file2.close()

                        if small_rate.get()>0:
                                q3=small_rate.get()
                                q3=str(q3)
                                file3=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/rates/small.txt","w")
                                file3.write(q3)
                                file3.close()

                        if chicken_rate.get()>0:
                                q4=chicken_rate.get()
                                q4=str(q4)
                                file4=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/rates/chicken.txt","w")
                                file4.write(q4)
                                file4.close()

                        if litter_rate.get()>0:
                                q5=litter_rate.get()
                                q5=str(q5)
                                file5=open("C:/Users/saura/Desktop/Billing/Donot_Touch_Files/rates/litter.txt","w")
                                file5.write(q5)
                                file5.close()


                Button_frame2=Frame(self.root,bd=10,relief=RIDGE,bg="#E5B4F3")
                Button_frame2.place(x=900,y=475,width=400,height=170)
                self.btnsetting=Button(Button_frame2,bd=7,font=('arial',16,'bold'),width=13,text="Done",command=lambda:done()).grid(row=2, column=1,padx=0)

                def done():
                        Rates_frame.destroy()
                        Button_frame2.destroy()


       
top = LoginPage()
top.title("Moonshine Billing-Login Page")
top.overrideredirect(1)
top.mainloop()


root = Tk()
application =  Poultry_app(root)
root.mainloop()
