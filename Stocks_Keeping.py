
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
from io import StringIO
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
import pyautogui

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
                with open("C:/Users/saura/Desktop/stocks/Donot_Touch_Files/credentials.txt", "r") as credentials:
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
                                credentials = open("C:/Users/saura/Desktop/stocks/Donot_Touch_Files/credentials.txt", "a")
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
                with open("C:/Users/saura/Desktop/stocks/Donot_Touch_Files/credentials.txt", "r") as credentials:
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
        self.root.geometry("1000x650+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("MOONSHINE POULTRY PVT. LTD.")
        #===========================================================variables=======================================================================================
        idate = StringVar()
        idate.set(time.strftime("%d-%m-20%y"))
        opening_stock1=IntVar()
        production1=IntVar()
        sales1=IntVar()
        closing_stock1=IntVar()
        opening_stock2=IntVar()
        purchase2=IntVar()
        consumption2=IntVar()
        closing_stock2=IntVar()
        opening_stock2_=IntVar()
        purchase2_=IntVar()
        consumption2_=IntVar()
        closing_stock2_=IntVar()
        opening_stock2__=IntVar()
        purchase2__=IntVar()
        consumption2__=IntVar()
        closing_stock2__=IntVar()
        date_bs=StringVar()
        opening_stock1_=IntVar()
        production1_=IntVar()
        sales1_=IntVar()
        closing_stock1_=IntVar()
        opening_stock1__=IntVar()
        production1__=IntVar()
        sales1__=IntVar()
        closing_stock1__=IntVar()
        send_date=StringVar()
#=====================================================================WINDOWS===================================================================
        
        def date1():
                q1=idate.get()
                file1=open("C:/Users/saura/Desktop/Stocks/Donot_Touch_Files/date/current.txt","w")
                file1.write(q1)

        date1()

        def date2():
                file1=open("C:/Users/saura/Desktop/stocks/Donot_Touch_Files/date/current.txt","r")
                q1=file1.read()
                q2=idate.get()

                if q1!=q2:
                        p=messagebox.askokcancel("Change Date")
                        if p>0:
                                file=open("C:/Users/saura/Desktop/stocks/Donot_Touch_Files/date/current.txt","w")
                                file.write(idate.get())
                                date3()
                        elif p<0:
                                pass
                else:
                        pass
        date2()

        def date4():
                file1=open("C:/Users/saura/Desktop/stocks/Donot_Touch_Files/date/last_bs.txt", "r")
                q1=file1.read()
                date_bs.set(q1)
        
        date4()

        def date5():
                file1=open("C:/Users/saura/Desktop/stocks/Donot_Touch_Files/date/last_bs.txt", "w")
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

        send_date.set(date_bs.get())

#==================================================================Frames========================================================================
        Mainframe=Frame(self.root)
        Mainframe.grid()

        Tops=Frame(Mainframe, bd=10 , relief=RIDGE)  #bd=border
        Tops.pack(side=TOP)

        self.lbltitle=Label(Tops, width=30, font=('arial',39,'bold'),text="Billing System",bg="#FF0000",bd=12,relief=RIDGE,fg="white",justify=CENTER)
        self.lbltitle.pack(fill=X)

        Bill_frame= LabelFrame(Mainframe, bd=10,bg="#9932CC",width=1000,height=50,font=('arial',12,'bold'),text='',relief=RIDGE)
        Bill_frame.pack(padx=38,side=TOP)


        Select_frame= LabelFrame(Mainframe, bd=10,bg="#9932CC",width=1300,height=600,font=('arial',12,'bold'),text='Goto',relief=RIDGE)
        Select_frame.pack(padx=38,side=TOP)

        Feed_frame= LabelFrame(Mainframe, bd=10,bg="#9932CC",width=1300,height=600,font=('arial',12,'bold'),text='Products',relief=RIDGE)
        Feed_frame.pack(padx=38,side=TOP)
        
#===========================================================Widget bill no. and Date===============================================================

        self.lbldate=Label(Bill_frame, font=('arial',16,'bold'),text="Date", bd=7)
        self.lbldate.grid(row=0,column=2 ,sticky=W)
        self.txtdate=Entry(Bill_frame, font=('arial',13,'bold'), textvariable=date_bs ,bd=7,insertwidth=2,state=DISABLED)
        self.txtdate.grid(row=0,column=3)

        Save_frame=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        Save_frame.place(x=470,y=577,width=1,height=1)

        lblsave=Label(Save_frame,text="Save",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)
        scrol_x=Scrollbar(Save_frame,orient=HORIZONTAL)
        self.lblsave=Text(Save_frame,yscrollcommand=scrol_x.set)
        scrol_x.pack(side=RIGHT,fill=X)
        scrol_x.config(command=self.lblsave.xview)
        self.lblsave.pack(fill=BOTH,expand=1)

#===============================================================Widget product egg===============================================================
        
        self.lblbtneggs=Button(Select_frame,bd=7,font=('arial',16,'bold'),width=26,text="Eggs",command=lambda:eggs()).grid(row=0, column=0,pady=0,)
       


        self.lbleggs=Label(Feed_frame, font=('arial',16,'bold'),text="FEED", bd=7)
        self.lbleggs.grid(row=0,column=0 ,sticky=W)

        self.lbleggs=Label(Feed_frame, font=('arial',16,'bold'),text="L1", bd=7)
        self.lbleggs.grid(row=0,column=1 ,sticky=W)


        self.lbllarge=Label(Feed_frame, font=('arial',16,'bold'),text="Opening Stock", bd=7)
        self.lbllarge.grid(row=1,column=0 ,sticky=W)
        self.txtlarge=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=opening_stock2 ,bd=7,insertwidth=2,width=3)
        self.txtlarge.grid(row=1,column=1)
                

        self.lblmedium=Label(Feed_frame, font=('arial',16,'bold'),text="Purchase", bd=7)
        self.lblmedium.grid(row=2,column=0 ,sticky=W)
        self.txtmedium=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=purchase2 ,bd=7,insertwidth=2,width=3)
        self.txtmedium.grid(row=2,column=1)

        self.lblsmall=Label(Feed_frame, font=('arial',16,'bold'),text="Consumption", bd=7)
        self.lblsmall.grid(row=3,column=0 ,sticky=W)
        self.txtsmall=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=consumption2 ,bd=7,insertwidth=2,width=3)
        self.txtsmall.grid(row=3,column=1)

        self.lblcracked=Label(Feed_frame, font=('arial',16,'bold'),text="Closing Stock", bd=7)
        self.lblcracked.grid(row=4,column=0 ,sticky=W)
        self.txtcracked=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=closing_stock2 ,bd=7,insertwidth=2,width=3)
        self.txtcracked.grid(row=4,column=1)

        self.lbleggs=Label(Feed_frame, font=('arial',16,'bold'),text="L2", bd=7)
        self.lbleggs.grid(row=0,column=2 ,sticky=W)

        self.txtlarge=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=opening_stock2_ ,bd=7,insertwidth=2,width=3)
        self.txtlarge.grid(row=1,column=2)
        self.txtmedium=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=purchase2_ ,bd=7,insertwidth=2,width=3)
        self.txtmedium.grid(row=2,column=2)
        self.txtsmall=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=consumption2_ ,bd=7,insertwidth=2,width=3)
        self.txtsmall.grid(row=3,column=2)
        self.txtcracked=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=closing_stock2_ ,bd=7,insertwidth=2,width=3)
        self.txtcracked.grid(row=4,column=2)

        self.lbleggs=Label(Feed_frame, font=('arial',16,'bold'),text="L3", bd=7)
        self.lbleggs.grid(row=0,column=3 ,sticky=W)

        self.txtlarge=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=opening_stock2__ ,bd=7,insertwidth=2,width=3)
        self.txtlarge.grid(row=1,column=3)
        self.txtmedium=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=purchase2__ ,bd=7,insertwidth=2,width=3)
        self.txtmedium.grid(row=2,column=3)
        self.txtsmall=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=consumption2__ ,bd=7,insertwidth=2,width=3)
        self.txtsmall.grid(row=3,column=3)
        self.txtcracked=Entry(Feed_frame, font=('arial',13,'bold'), textvariable=closing_stock2__ ,bd=7,insertwidth=2,width=3)
        self.txtcracked.grid(row=4,column=3)

        btnget=Button(Feed_frame,bd=7,font=('arial',16,'bold'),width=8,text="Calculate",command=lambda:feed_calc()).grid(row=5, column=0,padx=0)






        def convert():
                o1=opening_stock1_.get()
                o2=opening_stock1.get()
                o3=opening_stock1__.get()

                while o3>=30:
                        o3=o3-30
                        o1=o1+1
                
                while o1>=7:
                        o1=o1-7
                        o2=o2+1
                opening_stock1_.set(o1)
                opening_stock1.set(o2)
                opening_stock1__.set(o3)

                p1=production1_.get()
                p2=production1.get()
                p3=production1__.get()

                while p3>=30:
                        p3=p3-30
                        p1=p1+1

                while p1>=7:
                        p1=p1-7
                        p2=p2+1
                production1_.set(p1)
                production1.set(p2)
                production1__.set(p3)

                s1=sales1_.get()
                s2=sales1.get()
                s3=sales1__.get()
                while s3>=30:
                        s3=s3-30
                        s1=s1+1

                while s1>=7:
                        s1=s1-7
                        s2=s2+1
                sales1_.set(s1)
                sales1.set(s2)
                sales1__.set(s3)

                c1=closing_stock1_.get()
                c2=closing_stock1.get()
                c3=closing_stock1__.get()
                while c3>=30:
                        c3=c3-30
                        c1=c1+1

                while c1>=7:
                        c1=c1-7
                        c2=c2+1
                closing_stock1_.set(c1)
                closing_stock1.set(c2)
                closing_stock1__.set(c3)

        def eggs():
                Chicken_frame=Frame(self.root,bd=10,relief=RIDGE,bg="#E5B4F3")
                Chicken_frame.place(x=300,y=250,width=800,height=300)

                self.lbleggs=Label(Chicken_frame, font=('arial',16,'bold'),text="Eggs", bd=7)
                self.lbleggs.grid(row=0,column=0 ,sticky=W)

        #====



                self.lbleggs=Label(Chicken_frame, font=('arial',16,'bold'),text="Pack", bd=7)
                self.lbleggs.grid(row=1,column=1 ,sticky=W)

                self.lbleggs=Label(Chicken_frame, font=('arial',16,'bold'),text="Crate", bd=7)
                self.lbleggs.grid(row=1,column=2 ,sticky=W)

                self.lbllarge=Label(Chicken_frame, font=('arial',16,'bold'),text="Opening Stock", bd=7)
                self.lbllarge.grid(row=2,column=0 ,sticky=W)
                self.txtlarge=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=opening_stock1 ,bd=7,insertwidth=2,width=4)
                self.txtlarge.grid(row=2,column=1)
                self.txtlarge=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=opening_stock1_ ,bd=7,insertwidth=2,width=4)
                self.txtlarge.grid(row=2,column=2)
                        
                self.lblmedium=Label(Chicken_frame, font=('arial',16,'bold'),text="Production", bd=7)
                self.lblmedium.grid(row=3,column=0 ,sticky=W)
                self.txtmedium=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=production1 ,bd=7,insertwidth=2,width=4)
                self.txtmedium.grid(row=3,column=1)
                self.txtmedium=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=production1_ ,bd=7,insertwidth=2,width=4)
                self.txtmedium.grid(row=3,column=2)

                self.lblsmall=Label(Chicken_frame, font=('arial',16,'bold'),text="Sales", bd=7)
                self.lblsmall.grid(row=4,column=0 ,sticky=W)
                self.txtsmall=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=sales1 ,bd=7,insertwidth=2,width=4)
                self.txtsmall.grid(row=4,column=1)
                self.txtsmall=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=sales1_ ,bd=7,insertwidth=2,width=4)
                self.txtsmall.grid(row=4,column=2)

                self.lblcracked=Label(Chicken_frame, font=('arial',16,'bold'),text="Closing Stock", bd=7,)
                self.lblcracked.grid(row=5,column=0 ,sticky=W)
                self.txtcracked=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=closing_stock1 ,bd=7,insertwidth=2,width=4)
                self.txtcracked.grid(row=5,column=1)
                self.txtcracked=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=closing_stock1_ ,bd=7,insertwidth=2,width=4)
                self.txtcracked.grid(row=5,column=2)

#==============================

                self.lbleggs=Label(Chicken_frame, font=('arial',16,'bold'),text="Pack", bd=7)
                self.lbleggs.grid(row=1,column=3 ,sticky=W)

                self.lbleggs=Label(Chicken_frame, font=('arial',16,'bold'),text="Crate", bd=7)
                self.lbleggs.grid(row=1,column=4 ,sticky=W)

                self.txtlarge=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=opening_stock1 ,bd=7,insertwidth=2,width=4)
                self.txtlarge.grid(row=2,column=1)
                self.txtlarge=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=opening_stock1_ ,bd=7,insertwidth=2,width=4)
                self.txtlarge.grid(row=2,column=2)
                        
                self.txtmedium=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=production1 ,bd=7,insertwidth=2,width=4)
                self.txtmedium.grid(row=3,column=3)
                self.txtmedium=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=production1_ ,bd=7,insertwidth=2,width=4)
                self.txtmedium.grid(row=3,column=4)

                self.txtsmall=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=sales1 ,bd=7,insertwidth=2,width=4)
                self.txtsmall.grid(row=4,column=5)
                self.txtsmall=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=sales1_ ,bd=7,insertwidth=2,width=4)
                self.txtsmall.grid(row=4,column=6)

                self.txtcracked=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=closing_stock1 ,bd=7,insertwidth=2,width=4)
                self.txtcracked.grid(row=5,column=1)
                self.txtcracked=Entry(Chicken_frame, font=('arial',13,'bold'), textvariable=closing_stock1_ ,bd=7,insertwidth=2,width=4)
                self.txtcracked.grid(row=5,column=2)


                btnget=Button(Chicken_frame,bd=7,font=('arial',16,'bold'),width=8,text="Calculate",command=lambda:eggs_calc()).grid(row=6, column=0,padx=0)


                def feed():
                        Chicken_frame.destroy()
                        fbtn_frame.destroy()
                        Button_frame2.destroy()
                
                Save_frame2=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
                Save_frame2.place(x=470,y=577,width=1,height=1)

                lblsave2=Label(Save_frame2,text="Save",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)

                scrol_x=Scrollbar(Save_frame2,orient=HORIZONTAL)
                self.lblsave2=Text(Save_frame2,yscrollcommand=scrol_x.set)
                scrol_x.pack(side=RIGHT,fill=X)
                scrol_x.config(command=self.lblsave2.xview)
                self.lblsave2.pack(fill=BOTH,expand=1)

                def save1():
                        self.lblsave2.insert(END, "Eggs Stocks" )
                        self.lblsave2.insert(END, "\n>>Date: " + date_bs.get())
                        self.lblsave2.insert(END,f"\n>>Opening Stock: {opening_stock1.get()} pack {opening_stock1_.get()} crate {opening_stock1__.get()} piece")
                        self.lblsave2.insert(END,f"\n>>Production {production1.get()} pack {production1_.get()} crate {production1__.get()} piece")
                        self.lblsave2.insert(END,f"\n>>Sales: {sales1.get()} pack {sales1_.get()} crate {sales1__.get()} piece")
                        self.lblsave2.insert(END,f"\n>>Closing Stock: {closing_stock1.get()} pack {closing_stock1_.get()} crate {closing_stock1__.get()} piece" )

                        j=self.lblsave2.get("1.0", "end-1c")
                        file= open("C:/Users/saura/Desktop/stocks/Daily_Files/Eggs/" + date_bs.get() +".txt" , "a")
                        p=messagebox.askokcancel("Do you want to save it in a file")
                        if(p>0):
                                file.write(j)
                        elif(p<0):
                                pass


                fbtn_frame= LabelFrame(self.root, bd=10,bg="#9932CC",font=('arial',12,'bold'),text='Goto',relief=RIDGE)
                fbtn_frame.place(x=312,y=168,width=380,height=85)


                self.lblbtnfeed=Button(fbtn_frame,bd=7,font=('arial',16,'bold'),width=26,text="Feed",command=lambda:feed()).grid(row=0, column=1,pady=0,)
                


                Button_frame2= LabelFrame(self.root, bd=10,bg="#9932CC",font=('arial',12,'bold'),text='Buttons',relief=RIDGE)
                Button_frame2.place(x=750,y=300,width=225,height=250)

                self.btnsave=Button(Button_frame2,bd=7,font=('arial',16,'bold'),width=13,text="Save",command=lambda:save1()).grid(row=0, column=0,pady=0,)
                self.btnclear=Button(Button_frame2,bd=7,font=('arial',16,'bold'),width=13,text="Clear",command=lambda:clear2()).grid(row=1, column=0,pady=0)
                self.btnexit=Button(Button_frame2,bd=7,font=('arial',16,'bold'),width=13,text="Exit",command=lambda:exit1()).grid(row=2, column=0,padx=0)
                self.btnmsg=Button(Button_frame2,bd=7,font=('arial',16,'bold'),width=13,text="Message",command=lambda:messenger()).grid(row=3, column=0,padx=0)

#=================================================================button frame=====================================================================
        Button_frame= LabelFrame(self.root, bd=10,bg="#9932CC",font=('arial',12,'bold'),text='Buttons',relief=RIDGE)
        Button_frame.place(x=750,y=300,width=225,height=250)

        self.btnsave=Button(Button_frame,bd=7,font=('arial',16,'bold'),width=13,text="Save",command=lambda:save2()).grid(row=0, column=0,pady=0,)
        self.btnclear=Button(Button_frame,bd=7,font=('arial',16,'bold'),width=13,text="Clear",command=lambda:clear()).grid(row=1, column=0,pady=0)
        self.btnexit=Button(Button_frame,bd=7,font=('arial',16,'bold'),width=13,text="Exit",command=lambda:exit1()).grid(row=2, column=0,padx=0)
        self.btnmsg=Button(Button_frame,bd=7,font=('arial',16,'bold'),width=13,text="Message",command=lambda:messenger()).grid(row=3, column=0,padx=0)

        btndate=Button(Bill_frame,bd=7,font=('arial',16,'bold'),width=6,text="Change",command=lambda:date3()).grid(row=0, column=4,padx=0)

#===========================================================================fuctions==================================-===========================
        
        Save_frame3=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        Save_frame3.place(x=470,y=577,width=1,height=1)

        lblsave3=Label(Save_frame3,text="Save",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)

        scrol_x=Scrollbar(Save_frame3,orient=HORIZONTAL)
        self.lblsave3=Text(Save_frame3,yscrollcommand=scrol_x.set)
        scrol_x.pack(side=RIGHT,fill=X)
        scrol_x.config(command=self.lblsave3.xview)
        self.lblsave3.pack(fill=BOTH,expand=1)


        
        def messenger():
                Send_frame=Frame(self.root,bd=10,relief=RIDGE,bg="#E5B4F3")
                Send_frame.place(x=300,y=250,width=400,height=300)
                self.btneggs=Button(Send_frame,bd=7,font=('arial',16,'bold'),width=13,text="Eggs",command=lambda:eggs_msg()).grid(row=2, column=0,pady=0,)
                self.btnfeed=Button(Send_frame,bd=7,font=('arial',16,'bold'),width=13,text="Feed",command=lambda:feed_msg()).grid(row=3, column=0,pady=0)
                self.btnboth=Button(Send_frame,bd=7,font=('arial',16,'bold'),width=13,text="Both",command=lambda:both_msg()).grid(row=4, column=0,padx=0)


        def eggs_calc():
                convert()
                k1=opening_stock1.get()
                k2=production1.get()
                k3=sales1.get()
                
                l1=opening_stock1_.get()
                l2=production1_.get()
                l3=sales1_.get()

                l4=l1+l2-l3
                closing_stock1_.set(l4)

                k4=k1+k2-k3
                closing_stock1.set(k4)

        def feed_calc():
                k1=opening_stock2.get()
                k2=purchase2.get()
                k3=consumption2.get()
                
                k4=k1+k2-k3
                closing_stock2.set(k4)

                l1=opening_stock2_.get()
                l2=purchase2_.get()
                l3=consumption2_.get()
                
                l4=l1+l2-l3
                closing_stock2_.set(l4)

                m1=opening_stock2__.get()
                m2=purchase2__.get()
                m3=consumption2__.get()
                
                m4=m1+m2-m3
                closing_stock2__.set(m4)


        def clear():
                self.lblsave.delete(1.0,END)
                opening_stock2.set(0)
                purchase2.set(0)
                consumption2.set(0)
                closing_stock2.set(0)
                opening_stock2_.set(0)
                purchase2_.set(0)
                consumption2_.set(0)
                closing_stock2_.set(0)
                opening_stock2__.set(0)
                purchase2__.set(0)
                consumption2__.set(0)
                closing_stock2__.set(0)

        def clear2():
                self.lblsave.delete(1.0,END)
                opening_stock1.set(0)
                production1.set(0)
                sales1.set(0)
                closing_stock1.set(0)
                opening_stock1_.set(0)
                production1_.set(0)
                sales1_.set(0)
                closing_stock1_.set(0)
                opening_stock1__.set(0)
                production1__.set(0)
                sales1__.set(0)
                closing_stock1__.set(0)

                
        def exit1():
                self.root.destroy()
  

                
        
        def save2():
                self.lblsave.insert(END, "Feed Stocks" )
                self.lblsave.insert(END, "\n>>Date: " + date_bs.get())
                self.lblsave.insert(END,f"\n>>Opening Stock: {opening_stock2.get()}")
                self.lblsave.insert(END,f"\n>>Purchase: {purchase2.get()}")
                self.lblsave.insert(END,f"\n>>Consumption: {consumption2.get()}" )
                self.lblsave.insert(END,f"\n>>Closing Stock: {closing_stock2.get()}" )
                j=self.lblsave.get("1.0", "end-1c")
                file= open("C:/Users/saura/Desktop/stocks/Daily_Files/Feed/" + date_bs.get()+".txt" , "a")
                p=messagebox.askokcancel("Do you want to save it in a file")
                if(p>0):
                        file.write(j)
                elif(p<0):
                        pass

        def feed_msg():
                p=messagebox.askokcancel("Do you want to Send Message")
                if(p>0):
                        pyautogui.hotkey('winleft', 'r')
                        pyautogui.write("https://www.facebook.com/messages/t/4087111658009191/")
                        pyautogui.press("enter")
                        time.sleep(20)
                        pyautogui.write("Feed Stocks")
                        pyautogui.press("enter")
                        pyautogui.write(f"Date: {date_bs.get()}")
                        pyautogui.press("enter")

                        pyautogui.write("for L1 Feed")
                        pyautogui.press("enter")
                        pyautogui.write(f"Opening Stock: {opening_stock2.get()}")
                        pyautogui.press("enter")
                        pyautogui.write(f"Purchase: {purchase2.get()}")
                        pyautogui.press("enter")
                        pyautogui.write(f"Consumption: {consumption2.get()}")
                        pyautogui.press("enter")
                        pyautogui.write(f"Closing Stock: {closing_stock2.get()}")
                        pyautogui.press("enter")

                        pyautogui.write("for L2 Feed")
                        pyautogui.press("enter")
                        pyautogui.write(f"Opening Stock: {opening_stock2_.get()}")
                        pyautogui.press("enter")
                        pyautogui.write(f"Purchase: {purchase2_.get()}")
                        pyautogui.press("enter")
                        pyautogui.write(f"Consumption: {consumption2_.get()}")
                        pyautogui.press("enter")
                        pyautogui.write(f"Closing Stock: {closing_stock2_.get()}")
                        pyautogui.press("enter")

                        pyautogui.write("for L3 Feed")
                        pyautogui.press("enter")
                        pyautogui.write(f"Opening Stock: {opening_stock2__.get()}")
                        pyautogui.press("enter")
                        pyautogui.write(f"Purchase: {purchase2__.get()}")
                        pyautogui.press("enter")
                        pyautogui.write(f"Consumption: {consumption2__.get()}")
                        pyautogui.press("enter")
                        pyautogui.write(f"Closing Stock: {closing_stock2__.get()}")
                        pyautogui.press("enter")

                elif(p<0):
                        pass


        def eggs_msg():
                p=messagebox.askokcancel("Do you want to Send Message")
                if(p>0):
                        pyautogui.hotkey('winleft', 'r')
                        pyautogui.write("https://www.facebook.com/messages/t/4087111658009191/")
                        pyautogui.press("enter")
                        time.sleep(20)
                        pyautogui.write()
                        pyautogui.press("enter")
                elif(p<0):
                        pass
        
        def both_msg():
                p=messagebox.askokcancel("Do you want to Send Message")
                if(p>0):
                        pyautogui.hotkey('winleft', 'r')
                        pyautogui.write("https://www.facebook.com/messages/t/4087111658009191/")
                        pyautogui.press("enter")
                        time.sleep(20)
                        pyautogui.write()
                        pyautogui.press("enter")

                elif(p<0):
                        pass



top = LoginPage()
top.title("Moonshine stocks-Login Page")
top.overrideredirect(1)
top.mainloop()


root = Tk()
application =  Poultry_app(root)
root.mainloop()
