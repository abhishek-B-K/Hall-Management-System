def payments():
    def all_payments():
        hallbase5 = Toplevel(master=master)
        hallbase5.grab_set()
        hallbase5.geometry("730x550+550+180")
        hallbase5.title("PAYMENT DETAILS")
        hallbase5.config(bg='rosybrown1')
        hallbase5.resizable(False, False)
        con = sqlite3.connect("hall_data.db")
        mycursor = con.cursor()
        mycursor.execute("select * from payments")
        list0 = mycursor.fetchall()

        scroll_x = Scrollbar(hallbase5, orient=HORIZONTAL)
        scroll_y = Scrollbar(hallbase5, orient=VERTICAL)
        tv = ttk.Treeview(hallbase5, columns=(1, 2, 3, 4, 5), show="headings", height=26,
                          yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=tv.xview)
        scroll_y.config(command=tv.yview)
        tv.pack()
        tv.column("1", width=90, anchor='c')
        tv.column("2", width=150, anchor='c')
        tv.column("3", width=150, anchor='c')
        tv.column("4", width=160, anchor='c')
        tv.column("5", width=160, anchor='c')
        tv.heading(1, text="ID")
        tv.heading(2, text="AMOUNT")
        tv.heading(3, text="PAYMENT MODE")
        tv.heading(4, text="PAYMENT DATE")
        tv.heading(5, text="PAYMENT TIME")
        for i in list0:
            tv.insert('', 'end', values=i)
        con.commit()
        con.close()

    def confirm():
        con = sqlite3.connect("hall_data.db")
        mycursor = con.cursor()
        '''
        CREATE TABLE payments (
                       payment_id     NUMERIC (10) REFERENCES booking (booking_id),
                       payment_amount VARCHAR (20),
                       payment_mode   VARCHAR (20),
                       payment_date   VARCHAR (20),
                       payment_time   VARCHAR (20) 
                              );

        '''
        pay_id = payidval.get()
        pay_amount = payamountval.get()
        pay_mode = paymodeval.get()
        pay_date = paydateval.get()
        pay_time = paytimeval.get()

        try:
            mycursor.execute("insert into payments values('%s','%s','%s','%s','%s')" % (
                pay_id,pay_amount,pay_mode,pay_date,pay_time))
            con.commit()
            con.close()
            res = messagebox.askyesnocancel('Notificatrions',
                                            'Id {} date {} Payment sucessfully.. and want to clean the form'.format(
                                                pay_id,
                                                pay_date),
                                            parent=hallbase5)
            if (res == True):
                payment_id_entry1.delete(0, END)
                payment_amount_entry1.delete(0, END)
                payment_date_entry1.delete(0, END)
                payment_time_entry1.delete(0, END)
                payment_mode_entry.delete(0, END)
        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=hallbase5)

    def reset_data1():
        payment_id_entry1.delete(0,END)
        payment_amount_entry1.delete(0,END)
        payment_date_entry1.delete(0,END)
        payment_time_entry1.delete(0,END)
        payment_mode_entry.delete(0,END)

    hallbase5 = Toplevel(master=master)
    hallbase5.grab_set()
    hallbase5.geometry("730x550+550+180")
    hallbase5.title("PAYMENT DETAILS")
    hallbase5.config(bg='rosybrown1')
    hallbase5.resizable(False, False)
    payment_hall_label = Label(hallbase5, text='PAYMENT  DETAILS ', width=27, font=('Times New Roman', 22, 'bold'),
                                  bg='rosybrown1')
    payment_hall_label.place(x=120, y=10)

    payment_id_label1 = Label(hallbase5, text='PAYMENT ID ', width=24,font=('Times New Roman', 12, 'bold'))
    payment_id_label1.place(x=50, y=80)

    payment_amount_label1 = Label(hallbase5, text='PAYMENT AMOUNT ', width=24, font=('Times New Roman', 12, 'bold'))
    payment_amount_label1.place(x=50, y=130)

    payment_mode_label1 = Label(hallbase5, text='PAYMENT MODE ', width=24, font=('Times New Roman', 12, 'bold'))
    payment_mode_label1.place(x=50, y=180)

    payment_date_label1 = Label(hallbase5, text='PAYMENT DATE ', width=24, font=('Times New Roman', 12, 'bold'))
    payment_date_label1.place(x=50, y=230)

    payment_time_label1 = Label(hallbase5, text='PAYMENT TIME ', width=24, font=('Times New Roman', 12, 'bold'))
    payment_time_label1.place(x=50, y=280)



    # ---------------------------------------------------All entrys--------------------------------#
    payidval = StringVar()
    payamountval = StringVar()
    paymodeval = StringVar()
    paydateval = StringVar()
    paytimeval = StringVar()

    payment_id_entry1 = Entry(hallbase5, font=('Times New Roman', 12, 'bold'), width=25,textvariable=payidval)
    payment_id_entry1.place(x=350, y=80)

    payment_amount_entry1 = Entry(hallbase5, font=('Times New Roman', 12, 'bold'), width=25,textvariable=payamountval)
    payment_amount_entry1.place(x=350, y=130)

    payment_mode_list = ("Credit/Debit card", "Bank transfers", "E-Wallets", "Cash", "Checks")
    payment_mode_entry = ttk.Combobox(hallbase5, values=payment_mode_list, width=25, font=('Times New Roman', 12, 'bold'),textvariable=paymodeval)
    payment_mode_entry.place(x=350, y=180)

    payment_date_entry1 = DateEntry(hallbase5, font=('Times New Roman', 12, 'bold'), width=25,textvariable=paydateval)
    payment_date_entry1.place(x=350, y=230)

    payment_time_entry1 = Entry(hallbase5, font=('Times New Roman', 12, 'bold'), width=25,textvariable=paytimeval)
    payment_time_entry1.place(x=350, y=280)

    #---------------------button
    confarm_booking_btn1 = Button(hallbase5, text="CONFIRM PAYMENT", font=('Times New Roman', 13, 'bold'), width=17,
                          bg='lightyellow2', relief=RIDGE, bd=3, command=confirm)
    confarm_booking_btn1.place(x=70, y=370)

    reset_btn1 = Button(hallbase5, text="Reset", font=('Times New Roman', 13, 'bold'), width=13,
                        bg='lightyellow2', relief=RIDGE, bd=3, command=reset_data1)
    reset_btn1.place(x=270, y=370)

    all_data_btn1 = Button(hallbase5, text="SHOW PAYMENTS", font=('Times New Roman', 13, 'bold'), width=16,
                        bg='lightyellow2', relief=RIDGE, bd=3, command=all_payments)
    all_data_btn1.place(x=440, y=370)


def hall_detlils():
    ShowDataFrame2.destroy()

def hall_admin():
    def add_admin():
        '''
        CREATE TABLE admin (
                      admin_id     NUMERIC (3)  PRIMARY KEY,
                      admin_name   VARCHAR (30),
                      join_date    VARCHAR (10),
                      mobile_no    NUMERIC (12),
                      hall_name_ad VARCHAR (30) 
                           );

        '''
        con = sqlite3.connect("hall_data.db")
        mycursor = con.cursor()

        admin_id = adminidval.get()
        admin_name = adminnameval.get()
        admin_date = adminjoindateval.get()
        admin_mobile = adminmobileval.get()
        admin_hall = adminhall.get()

        #print(admin_id,admin_name,admin_date,admin_mobile,admin_hall)

        mycursor.execute("insert into admin values('%s','%s','%s','%s','%s')"%(admin_id,admin_name,admin_date,admin_mobile,admin_hall))
        con.commit()
        con.close()
        res = messagebox.showinfo('Notificatrions',
                                        'Id {} Name {} Added sucessfully.. '.format(admin_id,admin_name),parent=hallbase4)

    def showinfo():
        con = sqlite3.connect("hall_data.db")
        mycursor = con.cursor()
        mycursor.execute("select * from admin")
        list0 = mycursor.fetchall()
        tv = ttk.Treeview(DataEntryFrame2, columns=(1, 2, 3, 4, 5), show="headings", height=13,
                          yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=tv.xview)
        scroll_y.config(command=tv.yview)
        tv.pack()
        tv.column("1", width=85, anchor='c')
        tv.column("2", width=130, anchor='c')
        tv.column("3", width=120, anchor='c')
        tv.column("4", width=120, anchor='c')
        tv.column("5", width=150, anchor='c')
        tv.heading(1, text="ID")
        tv.heading(2, text="NAME")
        tv.heading(3, text="JOINING DATE.")
        tv.heading(4, text="MOBILE NO")
        tv.heading(5, text="HALL NAME")
        for i in list0:
            tv.insert('', 'end', values=i)

    hallbase4 = Toplevel(master=master)
    hallbase4.grab_set()
    hallbase4.geometry("730x550+550+180")
    hallbase4.title("RUKMINI AUDITORIUM")
    hallbase4.config(bg='rosybrown1')
    hallbase4.resizable(False, False)
    admin_name_hall_label = Label(hallbase4, text='ADMIN  DETAILS ', width=27, font=('Times New Roman', 22, 'bold'),
                               bg='rosybrown1')
    admin_name_hall_label.place(x=120, y=10)

    admin_id = Label(hallbase4, text='ADMIN ID  ', font=('Times New Roman', 15, 'bold'),
                       bg='rosybrown1')
    admin_id.place(x=40, y=60)

    admin_name = Label(hallbase4, text='ADMIN NAME  ', font=('Times New Roman', 15, 'bold'),
                     bg='rosybrown1')
    admin_name.place(x=320, y=60)

    admin_join_date = Label(hallbase4, text='JOINING DATE  ', font=('Times New Roman', 15, 'bold'),
                       bg='rosybrown1')
    admin_join_date.place(x=40, y=120)

    admin_mobile_no = Label(hallbase4, text='MOBILE NO.  ', font=('Times New Roman', 15, 'bold'),
                            bg='rosybrown1')
    admin_mobile_no.place(x=320, y=120)

    admin_hall_name = Label(hallbase4, text='HALL NAME  ', font=('Times New Roman', 15, 'bold'),
                            bg='rosybrown1')
    admin_hall_name.place(x=40, y=180)

    #------------------------------entrys------------------------------
    adminidval = StringVar()
    adminnameval = StringVar()
    adminjoindateval = StringVar()
    adminmobileval=StringVar()
    adminhall=StringVar()


    admin_id_entry = Entry(hallbase4, font=('Times New Roman', 12, 'bold'), width=10,textvariable=adminidval)
    admin_id_entry.place(x=200, y=63)

    admin_name_entry = Entry(hallbase4, font=('Times New Roman', 12, 'bold'), width=20,textvariable=adminnameval)
    admin_name_entry.place(x=480, y=63)

    admin_join_date_entry = DateEntry(hallbase4, font=('Times New Roman', 12, 'bold'), width=10,textvariable=adminjoindateval)
    admin_join_date_entry.place(x=200, y=123)

    admin_mobile_entry = Entry(hallbase4, font=('Times New Roman', 12, 'bold'), width=20,textvariable=adminmobileval)
    admin_mobile_entry.place(x=480, y=123)

    hall_list = ("Rukmini Auditorium", "Aryabhatta Hall", "Vinobha Bhave Hall", "Einstein Hall", "Exihivition Hall")
    admin_hall_name_entry = ttk.Combobox(hallbase4, values=hall_list, width=25, font=('Times New Roman', 12, 'bold'),textvariable=adminhall)
    admin_hall_name_entry.place(x=200, y=183)

    #------------------------------------------------add BUTTON------------------

    admin_add_btn2 = Button(hallbase4, text="ADD ADMIN", font=('Times New Roman', 10, 'bold'), width=10,
                          bg='lightyellow2', relief=RIDGE, bd=3,command=add_admin)
    admin_add_btn2.place(x=500, y=180)

    #------------------------------------------------Frame------------------------

    DataEntryFrame2 = Frame(hallbase4, bg='lavender blush', relief=GROOVE, borderwidth=5)
    DataEntryFrame2.place(x=50, y=260, width=640, height=260)
    scroll_x = Scrollbar(DataEntryFrame2, orient=HORIZONTAL)
    scroll_y = Scrollbar(DataEntryFrame2, orient=VERTICAL)

    showinfo()

def Rukmini_hall():
    hallbase1 = Toplevel(master=master)
    hallbase1.grab_set()
    hallbase1.geometry("730x550+550+180")
    hallbase1.title("RUKMINI AUDITORIUM")
    hallbase1.config(bg='rosybrown1')
    hallbase1.resizable(False, False)

    rukmini_hall_label = Label(hallbase1, text='Rukmini Auditorium ', width=27, font=('Times New Roman', 25, 'bold'),
                       bg='rosybrown1')
    rukmini_hall_label.place(x=100, y=10)

    rukmini_id = Label(hallbase1, text='Hall Id : 1 ', font=('Times New Roman', 15, 'bold'),
                               bg='rosybrown1')
    rukmini_id.place(x=40, y=60)

    hall_capacity = Label(hallbase1, text='Hall Capacity : 1500 ', font=('Times New Roman', 15, 'bold'),
                       bg='rosybrown1')
    hall_capacity.place(x=40, y=90)

    hall_description = Label(hallbase1, text='DESCRIPTION.', font=('Times New Roman', 15, 'bold'),
                          bg='rosybrown1')
    hall_description.place(x=300, y=120)

    hall_title1 = Label(hallbase1,text='Rukmini Auditorium with a 1500-seating capacity is perhaps the largest', font=('Times New Roman', 15, 'bold'),
                          bg='rosybrown1')
    hall_title1.place(x=40,y=170)

    hall_title2 = Label(hallbase1, text='auditorium in an educational institution in the city.',font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title2.place(x=40, y=200)

    hall_title3 = Label(hallbase1, text='An indoor air-conditioned institution in the city.An indoor air-conditioned',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title3.place(x=40, y=230)

    hall_title4 = Label(hallbase1, text='campus, equipped with incandescent lights, excellent acoustics, audio',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title4.place(x=40, y=260)

    hall_title4 = Label(hallbase1, text='visual system and three green- rooms.',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title4.place(x=40, y=290)

    hall_title5 = Label(hallbase1, text='The stage also had the privilege of hosting various eminent personalities  ',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title5.place(x=40, y=330)

    hall_title6 = Label(hallbase1, text='including several renowned. names from the field of dance, music,literature and ',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title6.place(x=40, y=360)

    hall_title7 = Label(hallbase1,
                        text='its the venue for the annual concert of Mahagami Gurukul’s ‘Sharangdev’  ',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title7.place(x=40, y=390)

    hall_title8 = Label(hallbase1,
                        text='for many years. ',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title8.place(x=40, y=410)

def Aryabhatta_hall():
    hallbase2 = Toplevel(master=master)
    hallbase2.grab_set()
    hallbase2.geometry("730x550+550+180")
    hallbase2.title("ARYABHATTA HALL")
    hallbase2.config(bg='rosybrown1')
    hallbase2.resizable(False, False)

    rukmini_hall_label1 = Label(hallbase2, text='Aryabhatta Hall ', width=27, font=('Times New Roman', 25, 'bold'),
                               bg='rosybrown1')
    rukmini_hall_label1.place(x=100, y=10)

    rukmini_id1 = Label(hallbase2, text='Hall Id : 2 ', font=('Times New Roman', 15, 'bold'),
                       bg='rosybrown1')
    rukmini_id1.place(x=40, y=60)

    hall_capacity1 = Label(hallbase2, text='Hall Capacity : 200 ', font=('Times New Roman', 15, 'bold'),
                          bg='rosybrown1')
    hall_capacity1.place(x=40, y=90)

    hall_description1 = Label(hallbase2, text='DESCRIPTION.', font=('Times New Roman', 15, 'bold'),
                             bg='rosybrown1')
    hall_description1.place(x=300, y=120)

    hall1_title1 = Label(hallbase2, text='The recently constructed conference hall is a beautiful architectural piece.',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall1_title1.place(x=40, y=170)

    hall1_title2 = Label(hallbase2, text='The fully air-conditioned hall with the latest audio-visual facilities',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall1_title2.place(x=40, y=200)

    hall1_title3 = Label(hallbase2, text=' has a 200-seating capacity. Ideal venue with soothing ambience for',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall1_title3.place(x=40, y=230)

    hall1_title4 = Label(hallbase2, text='conducting conferences.',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall1_title4.place(x=40, y=260)


def Vinobhabhave_hall():
    hallbase1 = Toplevel(master=master)
    hallbase1.grab_set()
    hallbase1.geometry("730x550+550+180")
    hallbase1.title("VINOBHA BHAVE HALL")
    hallbase1.config(bg='rosybrown1')
    hallbase1.resizable(False, False)

    rukmini_hall_label = Label(hallbase1, text='Vinobha Bhave Hall ', width=27, font=('Times New Roman', 25, 'bold'),
                               bg='rosybrown1')
    rukmini_hall_label.place(x=100, y=10)

    rukmini_id = Label(hallbase1, text='Hall Id : 3 ', font=('Times New Roman', 15, 'bold'),
                       bg='rosybrown1')
    rukmini_id.place(x=40, y=60)

    hall_capacity = Label(hallbase1, text='Hall Capacity : 150 ', font=('Times New Roman', 15, 'bold'),
                          bg='rosybrown1')
    hall_capacity.place(x=40, y=90)

    hall_description = Label(hallbase1, text='DESCRIPTION.', font=('Times New Roman', 15, 'bold'),
                             bg='rosybrown1')
    hall_description.place(x=300, y=120)

    hall_title1 = Label(hallbase1, text='It is imperative to bring students face-to-face with contemporary industrial',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title1.place(x=40, y=170)

    hall_title2 = Label(hallbase1, text='developments and advancements in various fields. The seminar hall serves this',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title2.place(x=40, y=200)

    hall_title3 = Label(hallbase1, text='purpose. Leading professionals,industry captains, scientists and other eminent',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title3.place(x=40, y=230)

    hall_title4 = Label(hallbase1, text='practitioners impart ‘value addition’ programs to orient students to the',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title4.place(x=40, y=260)

    hall_title4 = Label(hallbase1, text='emerging needs of the industry, research and development. Equipped with',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title4.place(x=40, y=290)

    hall_title5 = Label(hallbase1, text='an inbuilt audio-visual system, the fully air conditioned   ',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title5.place(x=40, y=320)

    hall_title6 = Label(hallbase1,
                        text='seminar hall has a 150-seating capacity. ',
                        font=('Times New Roman', 15, 'bold'),
                        bg='rosybrown1')
    hall_title6.place(x=40, y=350)


def Exihivition_hall():
    pass
def Einstein_hall():
    pass

def new_booking():
    def confirm_booking():
        con = sqlite3.connect("hall_data.db")
        mycursor = con.cursor()
        '''
        CREATE TABLE booking (
                      booking_id     NUMERIC (5)  PRIMARY KEY NOT NULL,
                      cust_name      VARCHAR (30) NOT NULL,
                      cust_mobile_no NUMERIC (12) NOT NULL,
                      cust_email_id  VARCHAR (25),
                      program_date   DATE         NOT NULL,
                      start_time     NUMERIC (3)  NOT NULL,
                      end_time       NUMERIC (3)  NOT NULL,
                      hall_name      VARCHAR (30) NOT NULL
                             );

        '''

        cus_id = random.randint(1,10000)
        cus_name = cusnameval.get()
        cus_mobile = cusmobval.get()
        cus_email = cusemailval.get()
        pro_date = probookval.get()
        strt_time = strtimeval.get()
        end_time = endtimeval.get()
        hall_name = hallnameval.get()
        print(cus_id)
        print(cus_name)
        print(cus_mobile)
        print(cus_email)
        print(pro_date)
        print(strt_time)
        print(end_time)
        print(hall_name)

        #query = ("insert into booking values("+cus_id+",'"+cus_name+"' ,"+cus_mobile+" ,'"+cus_email+"' ,'"+pro_date+"' ,"+strt_time+" ,"+end_time+" ,'"+hall_name+"')")
        #mycursor.execute("insert into booking values(2018,'abhishek',564513,'xys@gmai.com','12/45/2000',10,12,'Rukmini hall')")
        try:
            mycursor.execute("insert into booking values('%s','%s','%s','%s','%s','%s','%s','%s')" % (
            cus_id, cus_name, cus_mobile, cus_email, pro_date, strt_time, end_time, hall_name))
            con.commit()
            con.close()
            res = messagebox.askyesnocancel('Notificatrions',
                                            'Id {} Name {} booking sucessfully.. and want to clean the form'.format(cus_id,
                                                                                                                  cus_name),
                                            parent=hallbase)
            if (res == True):
                customer_name_entry.delete(0, END)
                cutomer_mobile_entry.delete(0, END)
                customer_email_entry.delete(0, END)
                program_book_entry.delete(0, END)
                start_time_entry.delete(0, END)
                end_time_entry.delete(0, END)
                hall_name_entry.delete(0, END)
        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=hall_name)

    def reset_data():
        customer_name_entry.delete(0,END)
        cutomer_mobile_entry.delete(0,END)
        customer_email_entry.delete(0,END)
        program_book_entry.delete(0,END)
        start_time_entry.delete(0,END)
        end_time_entry.delete(0,END)
        hall_name_entry.delete(0,END)

    hallbase = Toplevel(master=master)
    hallbase.grab_set()
    hallbase.geometry("730x550+550+180")
    hallbase.title("NEW BOOKING")
    hallbase.config(bg='rosybrown1')
    hallbase.resizable(False, False)

    new_booking_label = Label(hallbase, text='NEW BOOKING ', width=15, bg='indianred1',
                                font=('Times New Roman', 17, 'bold'))
    new_booking_label.place(x=250, y=40)

    customer_name_label = Label(hallbase, text='CUSTOMER NAME ', width=24, font=('Times New Roman', 12, 'bold'))
    customer_name_label.place(x=50, y=120)

    customer_mobile_label = Label(hallbase, text='CUSTOMER MOBILE NO ', width=24, font=('Times New Roman', 12, 'bold'))
    customer_mobile_label.place(x=50, y=160)

    customer_email_label = Label(hallbase, text='CUSTOMER EMAIL-ID ', width=24, font=('Times New Roman', 12, 'bold'))
    customer_email_label.place(x=50, y=210)

    program_book_label = Label(hallbase, text='PROGRAM BOOKING DATE ', width=24, font=('Times New Roman', 12, 'bold'))
    program_book_label.place(x=50, y=260)

    start_time_label = Label(hallbase, text='START TIME ', width=24, font=('Times New Roman', 12, 'bold'))
    start_time_label.place(x=50, y=310)

    end_time_label = Label(hallbase, text='END TIME ', width=24, font=('Times New Roman', 12, 'bold'))
    end_time_label.place(x=50, y=360)

    hall_name_label = Label(hallbase, text='HALL NAME ', width=24, font=('Times New Roman', 12, 'bold'))
    hall_name_label.place(x=50, y=410)

    #---------------------------------------------------All entrys--------------------------------#
    cusnameval = StringVar()
    cusmobval=StringVar()
    cusemailval = StringVar()
    probookval = StringVar()
    strtimeval = StringVar()
    endtimeval = StringVar()
    hallnameval = StringVar()

    customer_name_entry = Entry(hallbase, font=('Times New Roman', 12, 'bold'), width=25,textvariable=cusnameval)
    customer_name_entry.place(x=350, y=120)

    cutomer_mobile_entry = Entry(hallbase, font=('Times New Roman', 12, 'bold'), width=25,textvariable=cusmobval)
    cutomer_mobile_entry.place(x=350, y=160)

    customer_email_entry = Entry(hallbase, font=('Times New Roman', 12, 'bold'), width=25,textvariable=cusemailval)
    customer_email_entry.place(x=350, y=210)

    program_book_entry = DateEntry(hallbase, font=('Times New Roman', 12, 'bold'), width=25,textvariable=probookval)
    program_book_entry.place(x=350, y=260)

    start_time_list = ("10","11","12","13","14","15","16","17","18")
    start_time_entry = ttk.Combobox(hallbase,values=start_time_list,width=25,font=('Times New Roman', 12, 'bold'),textvariable=strtimeval)
    start_time_entry.place(x=350, y=310)

    end_time_list = ("10", "11", "12", "13", "14", "15", "16", "17", "18")
    end_time_entry = ttk.Combobox(hallbase,values=end_time_list,width=25,font=('Times New Roman', 12, 'bold'),textvariable=endtimeval)
    end_time_entry.place(x=350, y=360)

    hall_list = ("Rukmini Auditorium","Aryabhatta Hall","Vinobha Bhave Hall","Einstein Hall","Exihivition Hall")
    hall_name_entry =ttk.Combobox(hallbase,values=hall_list,width=25, font=('Times New Roman', 12, 'bold'),textvariable=hallnameval)
    hall_name_entry.place(x=350, y=410)

    #--------------------------------------------button

    booking_btn = Button(hallbase, text="Confirm booking", font=('Times New Roman', 13, 'bold'), width=13,
                         bg='lightyellow2', relief=RIDGE, bd=3, command=confirm_booking)
    booking_btn.place(x=180, y=470)

    reset_btn = Button(hallbase, text="Reset", font=('Times New Roman', 13, 'bold'), width=13,
                         bg='lightyellow2', relief=RIDGE, bd=3, command=reset_data)
    reset_btn.place(x=400, y=470)


def update_booking():
    def reset_data1():
        customer_id_entry1.delete(0,END)
        customer_name_entry1.delete(0, END)
        cutomer_mobile_entry1.delete(0, END)
        customer_email_entry1.delete(0, END)
        program_book_entry1.delete(0, END)
        start_time_entry1.delete(0, END)
        end_time_entry1.delete(0, END)
        hall_name_entry1.delete(0, END)

    def retrive_data():
        con = sqlite3.connect("hall_data.db")
        mycursor = con.cursor()

        get_by_id = cusidval1.get()

        if get_by_id != '':
            mycursor.execute("select * from booking where booking_id='%s'" % get_by_id)
            list0 = mycursor.fetchone()
            print(list0)
            reset_data1()

            customer_id_entry1.insert(0,list0[0])
            customer_name_entry1.insert(0,list0[1])
            cutomer_mobile_entry1.insert(0,list0[2])
            customer_email_entry1.insert(0,list0[3])
            program_book_entry1.insert(0,list0[4])
            start_time_entry1.insert(0,list0[5])
            end_time_entry1.insert(0,list0[6])
            hall_name_entry1.insert(0,list0[7])

    def update_date():
          id = customer_id_entry1.get()
          nam = customer_name_entry1.get()
          mob =  cutomer_mobile_entry1.get()
          emai =  customer_email_entry1.get()
          book =  program_book_entry1.get()
          stattim =  start_time_entry1.get()
          endtim =  end_time_entry1.get()
          hallnam =  hall_name_entry1.get()

          #print(id,nam,mob,emai,book,stattim,endtim,hallnam)
          con = sqlite3.connect("hall_data.db")
          mycursor = con.cursor()

          #strr = 'update booking set  cust_name=%s,cust_mobile_no=%s,cust_email_id=%s, program_date=%s,start_time=%s,end_time=%s,hall_name =%s where booking_id=%s'
          query="update booking set cust_name='%s',cust_mobile_no='%s',cust_email_id='%s', program_date='%s',start_time='%s',end_time='%s',hall_name ='%s' where booking_id='%s'"%(nam,mob,emai,book,stattim,endtim,hallnam,id)
          mycursor.execute(query)
          con.commit()
          con.close()
          messagebox.showinfo("Info", "Record Update")
          print("update now")
    hallbase1 = Toplevel(master=master)
    hallbase1.grab_set()
    hallbase1.geometry("730x550+550+180")
    hallbase1.title("UPDATE BOOKING")
    hallbase1.config(bg='rosybrown1')
    hallbase1.resizable(False, False)

    update_booking_label1 = Label(hallbase1, text='UPDATE BOOKING ', width=17, bg='indianred1',
                              font=('Times New Roman', 17, 'bold'))
    update_booking_label1.place(x=250, y=30)

    customer_id_label1 = Label(hallbase1, text='CUSTOMER ID ', width=24, font=('Times New Roman', 12, 'bold'))
    customer_id_label1.place(x=50, y=80)

    customer_name_label1 = Label(hallbase1, text='CUSTOMER NAME ', width=24, font=('Times New Roman', 12, 'bold'))
    customer_name_label1.place(x=50, y=120)

    customer_mobile_label1 = Label(hallbase1, text='CUSTOMER MOBILE NO ', width=24, font=('Times New Roman', 12, 'bold'))
    customer_mobile_label1.place(x=50, y=160)

    customer_email_label1 = Label(hallbase1, text='CUSTOMER EMAIL-ID ', width=24, font=('Times New Roman', 12, 'bold'))
    customer_email_label1.place(x=50, y=210)

    program_book_label1 = Label(hallbase1, text='PROGRAM BOOKING DATE ', width=24, font=('Times New Roman', 12, 'bold'))
    program_book_label1.place(x=50, y=260)

    start_time_label1 = Label(hallbase1, text='START TIME ', width=24, font=('Times New Roman', 12, 'bold'))
    start_time_label1.place(x=50, y=310)

    end_time_label1 = Label(hallbase1, text='END TIME ', width=24, font=('Times New Roman', 12, 'bold'))
    end_time_label1.place(x=50, y=360)

    hall_name_label1 = Label(hallbase1, text='HALL NAME ', width=24, font=('Times New Roman', 12, 'bold'))
    hall_name_label1.place(x=50, y=410)

    cusidval1 = StringVar()
    cusnameval1 = StringVar()
    cusmobval1 = StringVar()
    cusemailval1 = StringVar()
    probookval1 = StringVar()
    strtimeval1 = StringVar()
    endtimeval1 = StringVar()
    hallnameval1 = StringVar()
    # ---------------------------------------------------All entrys--------------------------------#
    customer_id_entry1 = Entry(hallbase1, font=('Times New Roman', 12, 'bold'), width=25,textvariable=cusidval1)
    customer_id_entry1.place(x=350, y=80)

    customer_name_entry1 = Entry(hallbase1, font=('Times New Roman', 12, 'bold'), width=25,textvariable=cusnameval1)
    customer_name_entry1.place(x=350, y=120)

    cutomer_mobile_entry1 = Entry(hallbase1, font=('Times New Roman', 12, 'bold'), width=25,textvariable=cusmobval1)
    cutomer_mobile_entry1.place(x=350, y=160)

    customer_email_entry1 = Entry(hallbase1, font=('Times New Roman', 12, 'bold'), width=25,textvariable=cusemailval1)
    customer_email_entry1.place(x=350, y=210)

    program_book_entry1 = DateEntry(hallbase1, font=('Times New Roman', 12, 'bold'), width=25,textvariable=probookval1)
    program_book_entry1.place(x=350, y=260)

    start_time_list1 = ("10", "11", "12", "13", "14", "15", "16", "17", "18")
    start_time_entry1 = ttk.Combobox(hallbase1, values=start_time_list1, width=25, font=('Times New Roman', 12, 'bold'),textvariable=strtimeval1)
    start_time_entry1.place(x=350, y=310)

    end_time_list1 = ("10", "11", "12", "13", "14", "15", "16", "17", "18")
    end_time_entry1 = ttk.Combobox(hallbase1, values=end_time_list1, width=25, font=('Times New Roman', 12, 'bold'),textvariable=endtimeval1)
    end_time_entry1.place(x=350, y=360)

    hall_list1 = ("Rukmini Auditorium", "Aryabhatta Hall", "Vinobha Bhave Hall", "Einstein Hall", "Exihivition Hall")
    hall_name_entry1 = ttk.Combobox(hallbase1, values=hall_list1, width=25, font=('Times New Roman', 12, 'bold'),textvariable=hallnameval1)
    hall_name_entry1.place(x=350, y=410)

    # --------------------------------------------button
    retrive_btn2 = Button(hallbase1, text="Retrive", font=('Times New Roman', 10, 'bold'), width=10,
                          bg='lightyellow2', relief=RIDGE, bd=3,command=retrive_data)
    retrive_btn2.place(x=600, y=80)


    booking_btn1 = Button(hallbase1, text="UPDATE BOOKING", font=('Times New Roman', 13, 'bold'), width=15,
                         bg='lightyellow2', relief=RIDGE, bd=3,command=update_date)
    booking_btn1.place(x=180, y=470)

    reset_btn1 = Button(hallbase1, text="Reset", font=('Times New Roman', 13, 'bold'), width=13,
                       bg='lightyellow2', relief=RIDGE, bd=3,command=reset_data1)
    reset_btn1.place(x=400, y=470)




def search_booking():
    def search_booking():
        con = sqlite3.connect("hall_data.db")
        mycursor = con.cursor()

        sear_by_date = searbydate.get()
        sear_by_name = searbycusname.get()
        sear_by_mo=searbymobile.get()
        #print(sear_by_date)
        #print(sear_by_name)
        #print(sear_by_mo)

        try:
            if sear_by_date != '':
                DataEntryFrame1 = Frame(hallbase, bg='lavender blush', relief=GROOVE, borderwidth=5)
                DataEntryFrame1.place(x=50, y=240, width=640, height=280)

                scroll_x = Scrollbar(DataEntryFrame1, orient=HORIZONTAL)
                scroll_y = Scrollbar(DataEntryFrame1, orient=VERTICAL)
                mycursor.execute("select * from booking where program_date='%s'" % sear_by_date)
                list0 = mycursor.fetchall()
                tv = ttk.Treeview(DataEntryFrame1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height=13,
                                 yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_x.config(command=tv.xview)
                scroll_y.config(command=tv.yview)
                tv.pack()
                tv.column("1",width=85,anchor='c')
                tv.column("2",width=120,anchor='c')
                tv.column("3",width=85,anchor='c')
                tv.column("4",width=90,anchor='c')
                tv.column("5",width=85,anchor='c')
                tv.column("6",width=70,anchor='c')
                tv.column("7",width=70,anchor='c')
                tv.column("8",width=90,anchor='c')
                tv.heading(1, text="Booking ID")
                tv.heading(2, text="Name")
                tv.heading(3, text="Mobile no.")
                tv.heading(4, text="Email-Id")
                tv.heading(5, text="Program date")
                tv.heading(6, text="Start Time")
                tv.heading(7, text="End Time")
                tv.heading(8, text="Hall Name")

                for i in list0:
                    tv.insert('', 'end', values=i)
            elif sear_by_name != '':
                DataEntryFrame1 = Frame(hallbase, bg='lavender blush', relief=GROOVE, borderwidth=5)
                DataEntryFrame1.place(x=50, y=240, width=640, height=280)

                scroll_x = Scrollbar(DataEntryFrame1, orient=HORIZONTAL)
                scroll_y = Scrollbar(DataEntryFrame1, orient=VERTICAL)
                mycursor.execute("select * from booking where cust_name='%s'" % sear_by_name)
                list0 = mycursor.fetchall()

                tv = ttk.Treeview(DataEntryFrame1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height=13,
                                  yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_x.config(command=tv.xview)
                scroll_y.config(command=tv.yview)
                tv.pack()
                tv.column("1", width=85, anchor='c')
                tv.column("2", width=120, anchor='c')
                tv.column("3", width=85, anchor='c')
                tv.column("4", width=90, anchor='c')
                tv.column("5", width=85, anchor='c')
                tv.column("6", width=70, anchor='c')
                tv.column("7", width=70, anchor='c')
                tv.column("8", width=90, anchor='c')
                tv.heading(1,text="Booking ID")
                tv.heading(2,text="Name")
                tv.heading(3,text="Mobile no.")
                tv.heading(4,text="Email-Id")
                tv.heading(5,text="Program date")
                tv.heading(6,text="Start Time")
                tv.heading(7,text="End Time")
                tv.heading(8,text="Hall Name")

                for i in list0:
                    tv.insert('','end',values=i)
            else:
                DataEntryFrame1 = Frame(hallbase, bg='lavender blush', relief=GROOVE, borderwidth=5)
                DataEntryFrame1.place(x=50, y=240, width=640, height=280)

                scroll_x = Scrollbar(DataEntryFrame1, orient=HORIZONTAL)
                scroll_y = Scrollbar(DataEntryFrame1, orient=VERTICAL)
                mycursor.execute("select * from booking where cust_mobile_no='%s'" % sear_by_mo)
                list0 = mycursor.fetchall()
                tv = ttk.Treeview(DataEntryFrame1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height=13,
                                  yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_x.config(command=tv.xview)
                scroll_y.config(command=tv.yview)
                tv.pack()
                tv.column("1", width=85, anchor='c')
                tv.column("2", width=120, anchor='c')
                tv.column("3", width=85, anchor='c')
                tv.column("4", width=90, anchor='c')
                tv.column("5", width=85, anchor='c')
                tv.column("6", width=70, anchor='c')
                tv.column("7", width=70, anchor='c')
                tv.column("8", width=90, anchor='c')
                tv.heading(1, text="Booking ID")
                tv.heading(2, text="Name")
                tv.heading(3, text="Mobile no.")
                tv.heading(4, text="Email-Id")
                tv.heading(5, text="Program date")
                tv.heading(6, text="Start Time")
                tv.heading(7, text="End Time")
                tv.heading(8, text="Hall Name")

                for i in list0:
                    tv.insert('', 'end', values=i)
            con.commit()
            con.close()
        except:
            messagebox.showinfo('No Data','No Such data available...',parent=hallbase)
            print("no data found")

    def reset_booking():
        search_by_date_entry.delete(0,END)
        search_by_customer_entry.delete(0,END)
        search_by_mobile_entry.delete(0,END)
    def all_data():
        DataEntryFrame1 = Frame(hallbase, bg='lavender blush', relief=GROOVE, borderwidth=5)
        DataEntryFrame1.place(x=50, y=240, width=640, height=280)

        scroll_x = Scrollbar(DataEntryFrame1, orient=HORIZONTAL)
        scroll_y = Scrollbar(DataEntryFrame1, orient=VERTICAL)

        con = sqlite3.connect("hall_data.db")
        mycursor = con.cursor()
        mycursor.execute("select * from booking")
        list0 = mycursor.fetchall()
        tv = ttk.Treeview(DataEntryFrame1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height=13,
                          yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=tv.xview)
        scroll_y.config(command=tv.yview)
        tv.pack()
        tv.column("1", width=85, anchor='c')
        tv.column("2", width=120, anchor='c')
        tv.column("3", width=85, anchor='c')
        tv.column("4", width=90, anchor='c')
        tv.column("5", width=85, anchor='c')
        tv.column("6", width=70, anchor='c')
        tv.column("7", width=70, anchor='c')
        tv.column("8", width=90, anchor='c')
        tv.heading(1, text="Booking ID")
        tv.heading(2, text="Name")
        tv.heading(3, text="Mobile no.")
        tv.heading(4, text="Email-Id")
        tv.heading(5, text="Program date")
        tv.heading(6, text="Start Time")
        tv.heading(7, text="End Time")
        tv.heading(8, text="Hall Name")

        for i in list0:
            tv.insert('', 'end', values=i)


    hallbase = Toplevel(master=master)
    hallbase.grab_set()
    hallbase.geometry("730x550+550+180")
    hallbase.title("SEARCH BOOKING")
    hallbase.config(bg='rosybrown1')
    hallbase.resizable(False, False)

    search_booking_label = Label(hallbase, text='SEARCH BOOKING ', width=17, bg='indianred1',
                                 font=('Times New Roman', 17, 'bold'))
    search_booking_label.place(x=250, y=30)

    #-------------------------------label--------------------------#
    search_by_date_label = Label(hallbase, text='SEARCH BY DATE ', width=27, font=('Times New Roman', 12, 'bold'))
    search_by_date_label.place(x=50, y=100)

    search_by_customer_label = Label(hallbase, text='SEARCH BY CUSTOMER NAME ', width=27, font=('Times New Roman', 12, 'bold'))
    search_by_customer_label.place(x=50, y=150)

    search_by_mobile_label = Label(hallbase, text='SEARCH BY MOBILE NUMBER ', width=27, font=('Times New Roman', 12, 'bold'))
    search_by_mobile_label.place(x=50, y=200)

    searbydate = StringVar()
    searbycusname = StringVar()
    searbymobile = StringVar()
    #--------------------------------entry----------------------#

    search_by_date_entry = DateEntry(hallbase, font=('Times New Roman', 12, 'bold'), width=25,textvariable=searbydate)
    search_by_date_entry.place(x=350, y=100)

    search_by_customer_entry = Entry(hallbase, font=('Times New Roman', 12, 'bold'), width=25,textvariable=searbycusname)
    search_by_customer_entry.place(x=350, y=150)

    search_by_mobile_entry = Entry(hallbase, font=('Times New Roman', 12, 'bold'), width=25,textvariable=searbymobile)
    search_by_mobile_entry.place(x=350, y=200)

    #-------------------------------Frame------------------------#

    DataEntryFrame1 = Frame(hallbase, bg='lavender blush', relief=GROOVE, borderwidth=5)
    DataEntryFrame1.place(x=50, y=240, width=640, height=280)

    scroll_x = Scrollbar(DataEntryFrame1,orient=HORIZONTAL)
    scroll_y = Scrollbar(DataEntryFrame1,orient=VERTICAL)


    #--------------------------------button---------------------#

    search_booking_btn = Button(hallbase, text="Search ", font=('Times New Roman', 12, 'bold'), width=10,
                        bg='lightyellow2', relief=RIDGE, bd=3, command=search_booking)
    search_booking_btn.place(x=600, y=95)

    reset_booking_btn = Button(hallbase, text="Reset ", font=('Times New Roman', 12, 'bold'), width=10,
                                bg='lightyellow2', relief=RIDGE, bd=3, command=reset_booking)
    reset_booking_btn.place(x=600, y=145)

    alldata_booking_btn = Button(hallbase, text="All Data ", font=('Times New Roman', 12, 'bold'), width=10,
                               bg='lightyellow2', relief=RIDGE, bd=3, command=all_data)
    alldata_booking_btn.place(x=600, y=195)

def expenditure():
    pass

def exit():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if (res == True):
        master.destroy()




from datetime import time
from tkcalendar import Calendar, DateEntry
from turtledemo import clock
import random
from tkinter import Toplevel,messagebox,filedialog
from tkinter import ttk
from tkinter import *
import time
from tkinter import messagebox,filedialog
from PIL import Image,ImageTk
import webbrowser as wb
import sqlite3
#--------------------------------------Time and color-------------------
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(1000,tick)

colors = ['red','green','black','red2','gold2','indianred1','sienna1','orange2','darkorchid1','cornflower blue','saddle brown','cornsilk3','steelblue4']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(1000,IntroLabelColorTick)

def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(300,IntroLabelTick)


#--------------------------------------------------main tk---------------------#

master = Tk()
master.geometry("1174x700+200+50")
master.title("HALL BOOKING SYSTEM")
master.iconbitmap('cc.ico')
master.resizable(False,False)
master.config(bg='LightSky blue')

#--------------------------------------------------Image---------------------#
image = Image.open("ss.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(master,image=photo,bg='white')
label.pack(side='bottom',fill='both',expand='yes')

ss = 'Jawaharlal Nehru Engineering College'
count = 0
text = ''

clock = Label(master,font=('Times new roman',14,'bold'),relief=RIDGE,borderwidth=4,bg='linen')
clock.place(x=0,y=0)
tick()

SliderLabel = Label(master,text=ss,font=('Times new roman',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='linen')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()

#-----------------------------------------------Left frame------------------
DataEntryFrame = Frame(master,bg='peach puff',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=50,y=100,width=230,height=570)

frontlabel = Label(DataEntryFrame,text='-------Welcome-------',width=30,font=('arial',22,'italic bold'),bg='peach puff')
frontlabel.pack(side=TOP,expand=True)

hall_det_btn = Button(DataEntryFrame,text='1. HALLS DETAILS',width=25,font=('Times new roman',15,'bold'),bd=4,bg='lavender',activebackground='alice blue',relief=RIDGE,
                activeforeground='black',command=hall_detlils)
hall_det_btn.pack(side=TOP,expand=True)

new_book_btn = Button(DataEntryFrame,text='2. NEW BOOKING',width=25,font=('Times new roman',15,'bold'),bd=4,bg='lavender',activebackground='alice blue',relief=RIDGE,
                activeforeground='black',command=new_booking)
new_book_btn.pack(side=TOP,expand=True)

update_book_btn = Button(DataEntryFrame,text='3. UPDATE BOOKING',width=25,font=('Times new roman',15,'bold'),bd=4,bg='lavender',activebackground='alice blue',relief=RIDGE,
                activeforeground='black',command=update_booking)
update_book_btn.pack(side=TOP,expand=True)

search_book_btn = Button(DataEntryFrame,text='4. SEARCH BOOKING',width=25,font=('Times new roman',15,'bold'),bd=4,bg='lavender',activebackground='alice blue',relief=RIDGE,
                activeforeground='black',command=search_booking)
search_book_btn.pack(side=TOP,expand=True)

exp_btn = Button(DataEntryFrame,text='5. PAYMENT DETAIL',width=25,font=('Times new roman',15,'bold'),bd=4,bg='lavender',activebackground='alice blue',relief=RIDGE,
                activeforeground='black',command=payments)
exp_btn.pack(side=TOP,expand=True)

admin_btn = Button(DataEntryFrame,text='6. ADMINISTRATOR',width=25,font=('Times new roman',15,'bold'),bd=4,bg='lavender',activebackground='alice blue',relief=RIDGE,
                activeforeground='black',command=hall_admin)
admin_btn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7.  Exit',width=25,font=('Times new roman',15,'bold'),bd=4,bg='lavender',activebackground='alice blue',relief=RIDGE,
                activeforeground='black',command=exit)
exitbtn.pack(side=TOP,expand=True)

#---------------------------------------------Right frame----------------------------------#

ShowDataFrame = Frame(master,bg='old lace',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=350,y=100,width=730,height=570)

hall_label = Label(ShowDataFrame, text='AVALIABLE HALLS ', width=27, font=('Times New Roman', 25, 'bold'),bg='old lace')
hall_label.place(x=100, y=10)

img1 = PhotoImage(file = 'Rukmini_audo.PNG')
b1 = Button(ShowDataFrame,image=img1,bd=0,bg='peach puff',command=Rukmini_hall)
b1.place(x=70,y=100)

img2 = PhotoImage(file = 'Arya.PNG')
b2 = Button(ShowDataFrame,image=img2,bd=0,bg='peach puff',command=Aryabhatta_hall)
b2.place(x=400,y=100)

img5 = PhotoImage(file = 'vino.PNG')
b15 = Button(ShowDataFrame,image=img5,bd=0,bg='peach puff',command=Vinobhabhave_hall)
b15.place(x=70,y=230)

img4 = PhotoImage(file = 'exi.PNG')
b4 = Button(ShowDataFrame,image=img4,bd=0,bg='peach puff',command=Exihivition_hall)
b4.place(x=400,y=230)

img3 = PhotoImage(file = 'ein.PNG')
b3 = Button(ShowDataFrame,image=img3,bd=0,bg='peach puff',command=Einstein_hall)
b3.place(x=265,y=380)




ShowDataFrame2 = Frame(master,bg='old lace',relief=GROOVE,borderwidth=5)
ShowDataFrame2.place(x=350,y=100,width=730,height=570)

hall_book_label = Label(ShowDataFrame2, text='HALL BOOKING ', font=('Times New Roman', 20, 'bold'),bg='old lace')
hall_book_label.place(x=240, y=30)

img6 = PhotoImage(file = 'seminar-hall6.PNG')
b3 = Button(ShowDataFrame2,image=img6,bd=0,bg='peach puff')
b3.place(x=30,y=100)

img8 = PhotoImage(file = 'Rukmini_audo_img.PNG')
b3 = Button(ShowDataFrame2,image=img8,bd=0,bg='old lace')
b3.place(x=380,y=100)

img7 = PhotoImage(file = 'cc.PNG')
b3 = Button(ShowDataFrame2,image=img7,bd=0,bg='old lace')
b3.place(x=30,y=330)

img9 = PhotoImage(file = 'ppjj.PNG')
b3 = Button(ShowDataFrame2,image=img9,bd=0,bg='old lace')
b3.place(x=380,y=330)


master.mainloop()