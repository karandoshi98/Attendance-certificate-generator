import calendar
import time
import pyrebase
import firebase_admin
from firebase_admin import credentials
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from firebase_admin import db

# import matplotlib
from reportlab.pdfgen import canvas

#matplotlib.use("TkAgg")

cred = credentials.Certificate('attendencecerti-firebase-adminsdk-h5te4-5b8d24862a.json')
# default_app = firebase_admin.initialize_app(cred)

firebase_admin.initialize_app(cred,{
    'databaseURL':'https://attendencecerti.firebaseio.com/'
})

ref = db.reference()

sem = ""
ac_year = ""
branch = ""
fulldate=""
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")
        self.wm_title("Practical Exam Details")
        self.wm_geometry("600x450")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # self.configure(background='#A9A9A9')
        self.label = tk.Label(self, text="Welcome to DJ Sanghvi", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=40)
        # label1 = tk.Label(self, text="Enter the Academic Year",font=10)
        # label1.pack(side="top", fill="x", pady=30)
        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.05, rely=0.50, height=28, width=300)
        self.Label2.configure(text='''Enter Academic Year''', font=5)
        self.Label2.configure(width=46)
        # button1 = tk.Button(self, text="CLICK, to view Graphs",
        #                     command=lambda: controller.show_frame("PageOne"), font=10)
        # button2 = tk.Button(self, text="CLICK, to Enter your Disease",
        #                     command=lambda: controller.show_frame("PageTwo"), font=10)

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.40, rely=0.80, height=28, width=70)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Submit''')
        self.Button1.configure(command=self.submit)

        self.TCombobox1 = ttk.Combobox(self)
        self.TCombobox1.place(relx=0.6, rely=0.50, relheight=0.07, relwidth=0.30)

        self.TCombobox1.configure(width=97)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.set('Choose')
        self.TCombobox1['values'] = (
            '2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17',
            '2017-18', '2018-19')

    def submit(self):
        # import sqlite3
        # conn = sqlite3.connect('proj.db')
        self.dropdown1 = self.TCombobox1.get()

        if len(self.dropdown1) == 0 or self.dropdown1 == 'Choose':
            import tkinter.messagebox
            tkinter.messagebox.showinfo('Warning', 'Please choose a Academic year')
            self.cancel()
        elif len(self.dropdown1) != 0 and self.dropdown1 != 'Choose':
            global ac_year
            ac_year = self.TCombobox1.get()
            self.controller.show_frame("PageTwo")
            # c = conn.cursor()
            # c.execute("INSERT INTO hospital VALUES(?,?,?,?,?,?)",
            #           (self.dropdown1,))
            # conn.commit()
            # conn.close()

    def cancel(self):
        self.TCombobox1.set('Choose')


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please Enter your Details", font=controller.title_font)
        label.pack(side="top", fill="x", pady=40)

        # self.Label1 = tk.Label(self)
        # self.Label1.place(relx=0.19, rely=0.27, height=28, width=56)
        # self.Label1.configure(text="Name:")
        # self.Label1.configure(width=56)

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.19, rely=0.27, height=28, width=46)
        self.Label2.configure(text='''Branch:''')
        self.Label2.configure(width=46)

        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.19, rely=0.35, height=28, width=56)
        self.Label3.configure(text='''Sem:''')
        self.Label3.configure(width=56)

        # self.Label4 = tk.Label(self)
        # self.Label4.place(relx=0.02, rely=0.43, height=28, width=276)
        # self.Label4.configure(text='''Subject:''')
        # self.Label4.configure(width=276)

        # self.Text1 = tk.Text(self)
        # self.Text1.place(relx=0.6, rely=0.27, relheight=0.07, relwidth=0.30)
        # self.Text1.configure(background="white")
        # self.Text1.configure(font="TkTextFont")
        # self.Text1.configure(selectbackground="#c4c4c4")
        # self.Text1.configure(width=86)
        # Text1.configure(wrap=WORD)

        self.TCombobox2 = ttk.Combobox(self)
        self.TCombobox2.place(relx=0.6, rely=0.27, relheight=0.07, relwidth=0.30)

        self.TCombobox2.configure(width=97)
        self.TCombobox2.configure(takefocus="")
        self.TCombobox2.set('IT')
        self.TCombobox2['values'] = (
            'IT', 'Comps', 'Mechanical', 'EXTC', 'Electronics', 'Bio-med', 'Chemical', 'Production')

        # self.Text2 = tk.Text(self)
        # self.Text2.place(relx=0.6, rely=0.35, relheight=0.07, relwidth=0.30)
        # self.Text2.configure(background="white")
        # self.Text2.configure(font="TkTextFont")
        # self.Text2.configure(selectbackground="#c4c4c4")
        # self.Text2.configure(width=86)
        # Text2.configure(wrap=WORD)

        self.TCombobox3 = ttk.Combobox(self)
        self.TCombobox3.place(relx=0.6, rely=0.35, relheight=0.07, relwidth=0.30)

        self.TCombobox3.configure(width=97)
        self.TCombobox3.configure(takefocus="")
        self.TCombobox3.set('Choose')
        self.TCombobox3['values'] = (
            'Sem 3', 'Sem 4', 'Sem 5', 'Sem 6', 'Sem 7', 'Sem 8')




        # self.Text3 = tk.Text(self)
        # self.Text3.place(relx=0.6, rely=0.43, relheight=0.07, relwidth=0.30)
        # self.Text3.configure(background="white")
        # self.Text3.configure(font="TkTextFont")
        # self.Text3.configure(selectbackground="#c4c4c4")
        # self.Text3.configure(width=86)
        # Text3.configure(wrap=WORD)
        #
        # self.TCombobox4 = ttk.Combobox(self)
        # self.TCombobox4.place(relx=0.6, rely=0.43, relheight=0.07, relwidth=0.30)
        #
        # self.TCombobox4.configure(width=97)
        # self.TCombobox4.configure(takefocus="")
        # self.TCombobox4.set('Choose')
        # self.sem = self.TCombobox3.get()
        # print(self.sem)
        # self.TCombobox4['values'] = (
        #         'LDC', 'DSA', 'Maths', 'PCOM', 'DBMS', 'JAVA')

        # self.Text4 = tk.Text(self)
        # self.Text4.place(relx=0.6, rely=0.51, relheight=0.07, relwidth=0.30)
        # self.Text4.configure(background="white")
        # self.Text4.configure(font="TkTextFont")
        # self.Text4.configure(selectbackground="#c4c4c4")
        # self.Text4.configure(width=86)
        # Text4.configure(wrap=WORD)

        # self.Text4 = tk.Text(self)
        # self.Text4.place(relx=0.6, rely=0.67, relheight=0.07, relwidth=0.30)
        # self.Text4.configure(background="white")
        # self.Text4.configure(font="TkTextFont")
        # self.Text4.configure(selectbackground="#c4c4c4")
        # self.Text4.configure(width=86)
        #
        # self.Label6 = tk.Label(self)
        # self.Label6.place(relx=0.17, rely=0.59, height=28, width=76)
        # self.Label6.configure(text='''Date:''')
        # self.Label6.configure(width=76)
        #
        # self.Label6 = tk.Label(self)
        # self.Label6.place(relx=0.17, rely=0.67, height=28, width=100)
        # self.Label6.configure(text='''College Name:''')
        # self.Label6.configure(width=76)

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.18, rely=0.80, height=28, width=70)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Submit''')
        self.Button1.configure(command=self.submit)

        self.Button2 = tk.Button(self)
        self.Button2.place(relx=0.45, rely=0.80, height=28, width=70)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(text='''Cancel''')
        self.Button2.configure(command=self.cancel)

        self.Button3 = tk.Button(self)
        self.Button3.place(relx=0.70, rely=0.80, height=28, width=70)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(text='''Startpage''')
        self.Button3.configure(command=lambda: controller.show_frame("StartPage"))


    # def branch(self):
    #     branch = self.TCombobox2.get()
    #     return branch
    #
    # def sem(self):
    #     sem = self.TCombobox3.get()
    #     return sem

    def submit(self):
        import sqlite3
        conn = sqlite3.connect('proj.db')
        c = conn.cursor()
        global sem
        global branch
        sem = self.TCombobox3.get()
        branch = self.TCombobox2.get()
        global ac_year

        if len(branch) == 0 or branch == 'Choose' or len(branch) == 0 or branch == 'Choose':
            import tkinter.messagebox
            tkinter.messagebox.showinfo('Warning', 'Please choose all the details')
            self.cancel()
        else:
            c.execute("INSERT INTO TABLE1 VALUES(?,?,?)", (ac_year, branch, sem,))
            conn.commit()
            conn.close()
            self.controller.show_frame("PageThree")

    def cancel(self):
        self.TCombobox2.set('Choose')
        self.TCombobox3.set('Choose')


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select Appropriate Detalis", font=controller.title_font)
        label.pack(side="top", fill="x", pady=40)


        self.Label5 = tk.Label(self)
        self.Label5.place(relx=0.02, rely=0.30, height=28, width=276)
        self.Label5.configure(text='''External Examiner Name''')
        self.Label5.configure(width=276)

        self.Label6 = tk.Label(self)
        self.Label6.place(relx=0.02, rely=0.40, height=28, width=276)
        self.Label6.configure(text='''External College Name''')
        self.Label6.configure(width=276)

        self.Label7 = tk.Label(self)
        self.Label7.place(relx=0.02, rely=0.50, height=28, width=276)
        self.Label7.configure(text='''Internal Examiner Name''')
        self.Label7.configure(width=276)

        #External Examiner Name
        self.Text4 = tk.Text(self)
        self.Text4.place(relx=0.6, rely=0.30, relheight=0.07, relwidth=0.30)
        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(width=86)

        #College Name
        self.Text5 = tk.Text(self)
        self.Text5.place(relx=0.6, rely=0.40, relheight=0.07, relwidth=0.30)
        self.Text5.configure(background="white")
        self.Text5.configure(font="TkTextFont")
        self.Text5.configure(selectbackground="#c4c4c4")
        self.Text5.configure(width=86)

        #Internal Examiner Name
        self.Text6 = tk.Text(self)
        self.Text6.place(relx=0.6, rely=0.50, relheight=0.07, relwidth=0.30)
        self.Text6.configure(background="white")
        self.Text6.configure(font="TkTextFont")
        self.Text6.configure(selectbackground="#c4c4c4")
        self.Text6.configure(width=86)



        self.Button3 = tk.Button(self)
        self.Button3.place(relx=0.70, rely=0.80, height=28, width=70)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(text='''Back''')
        self.Button3.configure(command=lambda: controller.show_frame("PageTwo"))

        self.Button4 = tk.Button(self)
        self.Button4.place(relx=0.40, rely=0.80, height=28, width=110)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(text='''Display Subjects''')
        self.Button4.configure(command=self.disp)

        self.Button5 = tk.Button(self)
        self.Button5.place(relx=0.10, rely=0.80, height=28, width=80)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(text='''Create PDF''')
        self.Button5.configure(command=self.pdf)

        self.Button6 = tk.Button(self)
        self.Button6.place(relx=0.10, rely=0.70, height=28, width=70)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(text='''Date''')
        self.Button6.configure(command=self.date)

    def pdf(self):
        self.name = self.Text4.get("1.0",'end-1c')
        self.college = self.Text5.get("1.0",'end-1c')
        self.name_INT = self.Text6.get("1.0",tk.END)
        self.subject = self.TCombobox4.get()
        global fulldate
        p = canvas.Canvas("Sample.pdf")
        p.drawImage("header-black.png", 50, 680, width=500, height=250, mask='auto', preserveAspectRatio=True)
        p.drawString(50, 650, "     I have to inform you that %s of your college "%(self.name,))
        p.drawString(50, 630, "attended this college on %s for oral/Practical/TW "%(fulldate))
        p.drawString(50, 610, "asssessment for the subject of %s for the "%(self.subject))
        p.drawString(50, 590, "candidates at the %s-%s examination held in the "%(branch,sem))
        p.drawString(50, 570, "First/Second half of the year ."%())
        p.showPage()
        p.save()
        import sqlite3
        conn = sqlite3.connect('proj.db')
        c = conn.cursor()
        c.execute("INSERT INTO TABLE2 VALUES(?,?,?,?,?)", (self.subject,self.name,self.college,self.name_INT,fulldate,))
        conn.commit()
        conn.close()
        user_ref = ref.child('users')
        user_ref.child(self.name).set({
            'CollegeName':self.college,
            'Subject':self.subject,
            'InternalName':self.name_INT,
            'Date':fulldate
        })

    def disp(self):
        self.Label4 = tk.Label(self)
        self.Label4.place(relx=0.02, rely=0.60, height=28, width=276)
        self.Label4.configure(text='''Subject:''')
        self.Label4.configure(width=276)
        self.TCombobox4 = ttk.Combobox(self)
        self.TCombobox4.place(relx=0.6, rely=0.60, relheight=0.07, relwidth=0.30)
        self.TCombobox4.configure(width=97)
        self.TCombobox4.configure(takefocus="")
        self.TCombobox4.set('Choose')
        global sem
        global branch
        if sem == 'Sem 3' and branch == 'IT':
            self.TCombobox4['values'] = (
                'LDC', 'DSA', 'MATHS', 'PCOM', 'DBMS', 'JAVA')
        elif sem == 'Sem 4' and branch == 'IT':
            self.TCombobox4['values'] = (
                'OS', 'COA', 'CN', 'MATHS', 'AT', 'PYTHON')
        else:
            import tkinter.messagebox
            tkinter.messagebox.showinfo("Warning","Please Select apropriate branch and sem")
            self.controller.show_frame("PageTwo")

    def date(self):
        class MyDatePicker(tk.Toplevel):
            """
            Description:
                A tkinter GUI date picker.
            """

            def __init__(self, widget=None, format_str=None):
                """
                :param widget: widget of parent instance.

                :param format_str: print format in which to display date.
                :type format_str: string

                Example::
                    a = MyDatePicker(self, widget=self.parent widget,
                                     format_str='%02d-%s-%s')
                """

                super().__init__()
                self.widget = widget
                self.str_format = format_str

                self.title("Date Picker")
                self.resizable(0, 0)
                self.geometry("+630+390")

                self.init_frames()
                self.init_needed_vars()
                self.init_month_year_labels()
                self.init_buttons()
                self.space_between_widgets()
                self.fill_days()
                self.make_calendar()

            def init_frames(self):
                self.frame1 = tk.Frame(self)
                self.frame1.pack()

                self.frame_days = tk.Frame(self)
                self.frame_days.pack()

            def init_needed_vars(self):
                self.month_names = tuple(calendar.month_name)
                self.day_names = tuple(calendar.day_abbr)
                self.year = time.strftime("%Y")
                self.month = time.strftime("%B")

            def init_month_year_labels(self):
                self.year_str_var = tk.StringVar()
                self.month_str_var = tk.StringVar()

                self.year_str_var.set(self.year)
                self.year_lbl = tk.Label(self.frame1, textvariable=self.year_str_var,
                                         width=3)
                self.year_lbl.grid(row=0, column=5)

                self.month_str_var.set(self.month)
                self.month_lbl = tk.Label(self.frame1, textvariable=self.month_str_var,
                                          width=8)
                self.month_lbl.grid(row=0, column=1)

            def init_buttons(self):
                self.left_yr = ttk.Button(self.frame1, text="←", width=5,
                                          command=self.prev_year)
                self.left_yr.grid(row=0, column=4)

                self.right_yr = ttk.Button(self.frame1, text="→", width=5,
                                           command=self.next_year)
                self.right_yr.grid(row=0, column=6)

                self.left_mon = ttk.Button(self.frame1, text="←", width=5,
                                           command=self.prev_month)
                self.left_mon.grid(row=0, column=0)

                self.right_mon = ttk.Button(self.frame1, text="→", width=5,
                                            command=self.next_month)
                self.right_mon.grid(row=0, column=2)

            def space_between_widgets(self):
                self.frame1.grid_columnconfigure(3, minsize=40)

            def prev_year(self):
                self.prev_yr = int(self.year_str_var.get()) - 1
                self.year_str_var.set(self.prev_yr)

                self.make_calendar()

            def next_year(self):
                self.next_yr = int(self.year_str_var.get()) + 1
                self.year_str_var.set(self.next_yr)

                self.make_calendar()

            def prev_month(self):
                index_current_month = self.month_names.index(self.month_str_var.get())
                index_prev_month = index_current_month - 1

                #  index 0 is empty string, use index 12 instead,
                # which is index of December.
                if index_prev_month == 0:
                    self.month_str_var.set(self.month_names[12])
                else:
                    self.month_str_var.set(self.month_names[index_current_month - 1])

                self.make_calendar()

            def next_month(self):
                index_current_month = self.month_names.index(self.month_str_var.get())

                try:
                    self.month_str_var.set(self.month_names[index_current_month + 1])
                except IndexError:
                    #  index 13 does not exist, use index 1 instead, which is January.
                    self.month_str_var.set(self.month_names[1])

                self.make_calendar()

            def fill_days(self):
                col = 0
                #  Creates days label
                for day in self.day_names:
                    self.lbl_day = tk.Label(self.frame_days, text=day)
                    self.lbl_day.grid(row=0, column=col)
                    col += 1

            def make_calendar(self):
                #  Delete date buttons if already present.
                #  Each button must have its own instance attribute for this to work.
                try:
                    for dates in self.m_cal:
                        for date in dates:
                            if date == 0:
                                continue

                            self.delete_buttons(date)

                except AttributeError:
                    pass

                year = int(self.year_str_var.get())
                month = self.month_names.index(self.month_str_var.get())
                self.m_cal = calendar.monthcalendar(year, month)

                #  build dates buttons.
                for dates in self.m_cal:
                    row = self.m_cal.index(dates) + 1
                    for date in dates:
                        col = dates.index(date)

                        if date == 0:
                            continue

                        self.make_button(str(date), str(row), str(col))

            def make_button(self, date, row, column):
                """
                Description:
                    Build a date button.

                :param date: date.
                :type date: string

                :param row: row number.
                :type row: string

                :param column: column number.
                :type column: string
                """
                exec(
                    "self.btn_" + date + " = ttk.Button(self.frame_days, text=" + date
                    + ", width=5)\n"
                      "self.btn_" + date + ".grid(row=" + row + " , column=" + column
                    + ")\n"
                      "self.btn_" + date + ".bind(\"<Button-1>\", self.get_date)"
                )

            def delete_buttons(self, date):
                """
                Description:
                    Delete a date button.

                :param date: date.
                :type: string
                """
                exec(
                    "self.btn_" + str(date) + ".destroy()"
                )

            def get_date(self, clicked=None):
                """
                Description:
                    Get the date from the calendar on button click.

                :param clicked: button clicked event.
                :type clicked: tkinter event
                """

                clicked_button = clicked.widget
                year = self.year_str_var.get()
                month = self.month_str_var.get()
                date = clicked_button['text']
                global fulldate
                fulldate = self.str_format % (date, month, year)
                print("Selected Date is:", fulldate)
                #  Replace with parent 'widget' of your choice.
                try:
                    self.widget.delete(0, tk.END)
                    self.widget.insert(0, fulldate)
                except AttributeError:
                    pass

        if __name__ == '__main__':

            MyDatePicker(format_str='%02d-%s-%s')
            root = tk.Tk()
            root.mainloop()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()