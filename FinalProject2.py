import tkinter as tk
from tkinter import ttk, messagebox

class UniversitySystem:
    def __init__(self):
        self.students = {}
        self.professors = {
            "1001": {"password": "123456", "name": "مجتبی مددیار", "department": "برنامه سازی پیشرفته"},
            "1002": {"password": "123456", "name": "شعله اعلائی", "department": "فیزیک"},
            "2001": {"password": "123456", "name": "فردین اسماعیلی", "department": "کارگاه کامپیوتر"},
            "3001": {"password": "123456", "name": "نازنین صالح امین", "department": "ازمایشگاه سیستم عامل"},
            "4001": {"password": "123456", "name": "کیا عباسی", "department": "زبان"},
            "5001": {"password": "123456", "name": "عباس زارع", "department": "ریاضی"}
        }
        self.courses = {}
        self.admins = {
            "admin": {"password": "admin123", "name": "مدیر سیستم"},
            "admin2": {"password": "123456", "name": "مدیر آموزشی"},
            "supervisor": {"password": "super123", "name": "ناظر تحصیلی"}
        }
        self._init_sample_data()

    def _init_sample_data(self):
        samples = [
            {"course_code": "101", "course_name": "ریاضی عمومی ۱", "professor": "عباس زارع", "professor_id": "1001", "units": 3, "capacity": 40, "current_students": 0, "schedule": "شنبه و دوشنبه ۱۰-۱۲", "department": "ریاضی", "classroom": "۲۰۱", "exam_date": "۱۴۰۴/۰۳/۲۰"},
            {"course_code": "102", "course_name": "فیزیک ۱", "professor": "شعله اعلائی", "professor_id": "1002", "units": 3, "capacity": 35, "current_students": 0, "schedule": "یکشنبه و سه‌شنبه ۸-۱۰", "department": "فیزیک", "classroom": "۳۰۱", "exam_date": "۱۴۰۴/۰۳/۲۲"},
            {"course_code": "201", "course_name": "برنامه‌نویسی پایتون", "professor": " مجبتی مددیار", "professor_id": "2001", "units": 3, "capacity": 30, "current_students": 0, "schedule": "دوشنبه و چهارشنبه ۱۴-۱۶", "department": "کامپیوتر", "classroom": "۱۰۵", "exam_date": "۱۴۰۴/۰۳/۲۵"},
            {"course_code": "301", "course_name": "کارگاه کامپیوتر", "professor": "فرزین اسمعیلی", "professor_id": "3001", "units": 3, "capacity": 28, "current_students": 0, "schedule": "شنبه و چهارشنبه ۸-۱۰", "department": "کامپیوتر", "classroom": "۲۰۳", "exam_date": "۱۴۰۴/۰۳/۲۸"},
            {"course_code": "401", "course_name": "زبان انگلیسی", "professor": " کیا عباسی", "professor_id": "4001", "units": 2, "capacity": 50, "current_students": 0, "schedule": "یکشنبه ۱۶-۱۸", "department": "زبان", "classroom": "۱۰۱", "exam_date": "۱۴۰۴/۰۴/۰۱"},
            {"course_code": "501", "course_name": " ازمایشگاه سیستم عامل", "professor": " نازنین صالح امین", "professor_id": "5001", "units": 3, "capacity": 45, "current_students": 0, "schedule": "دوشنبه و چهارشنبه ۱۰-۱۲", "department": "ریاضی", "classroom": "۲۰۲", "exam_date": "۱۴۰۴/۰۴/۰۵"}
        ]
        for c in samples: self.add_course(c)
        
        for s in [
            {"sid": "400123456", "name": "حانیه اسماعیل زاده ", "password": "123456", "major": "کامپیوتر", "email": "ali@uni.ac.ir", "year": "1400"},
            {"sid": "400123457", "name": " عرشیا زارع", "password": "123456", "major": "ریاضی", "email": "fatemeh@uni.ac.ir", "year": "1400"},
            {"sid": "401123458", "name": " کیان باقری", "password": "123456", "major": "فیزیک", "email": "mohammad@uni.ac.ir", "year": "1401"}
        ]: self.add_student(**s)

    def add_student(self, sid, name, password, major, email="", year=""):
        if sid in self.students: return False, "شماره دانشجویی تکراری است!"
        if not all([sid, name, password, major]): return False, "لطفا تمام فیلدهای ضروری را پر کنید!"
        self.students[sid] = {"name": name, "password": password, "major": major, "email": email, "entry_year": year or "نامشخص", "courses": [], "total_units": 0}
        return True, "ثبت‌نام با موفقیت انجام شد!"

    def add_course(self, data):
        code = data["course_code"]
        if code in self.courses: return False, "کد درس تکراری است!"
        required = ["course_code", "course_name", "professor", "units", "capacity", "schedule", "department"]
        if not all(data.get(f) for f in required): return False, "لطفا تمام فیلدهای ضروری را پر کنید!"
        self.courses[code] = {k: data.get(k, "") for k in ["name", "professor", "professor_id", "units", "capacity", "schedule", "department", "classroom", "exam_date"]}
        self.courses[code].update({"current_students": 0, "units": int(data["units"]), "capacity": int(data["capacity"])})
        return True, "درس با موفقیت اضافه شد!"

    def delete_course(self, code):
        if code not in self.courses: return False, "درس یافت نشد!"
        for student in self.students.values():
            if code in student["courses"]:
                student["courses"].remove(code)
                student["total_units"] -= self.courses[code]["units"]
        del self.courses[code]
        return True, "درس با موفقیت حذف شد!"


class UniversityApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" سامانه آموزشی دانشگاه  ")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f8f9fa")

        self.colors = {'primary': '#006837', 'secondary': '#009f4f', 'success': '#27ae60', 'danger': '#e74c3c', 'warning': '#f39c12', 'bg': '#f8f9fa'}
        self.fonts = {'title': ('B Nazanin', 24, 'bold'), 'header': ('B Nazanin', 16, 'bold'), 'subheader': ('B Nazanin', 12, 'bold'), 'normal': ('B Nazanin', 11), 'small': ('B Nazanin', 10)}

        self.system = UniversitySystem()
        self.current_user = self.current_type = None
        self.show_welcome()

    def clear(self): [w.destroy() for w in self.root.winfo_children()]

    def show_welcome(self):
        self.clear()
        header = tk.Frame(self.root, bg=self.colors['primary'], height=150)
        header.pack(fill='x'); header.pack_propagate(False)
        tk.Label(header, text=" دانشگاه  ", font=('B Nazanin', 30, 'bold'), fg='white', bg=self.colors['primary']).pack(pady=30)
        tk.Label(header, text="سامانه جامع آموزشی - انتخاب واحد آنلاین", font=('B Nazanin', 14), fg='white', bg=self.colors['primary']).pack()

        body = tk.Frame(self.root, bg=self.colors['bg'])
        body.pack(fill='both', expand=True, padx=80, pady=40)

        for title, desc, color, cmd in [
            (" دانشجویان", "انتخاب واحد، مشاهده دروس و کارنامه", self.colors['secondary'], lambda: self.show_login("student")),
            (" اساتید", "مدیریت دروس و مشاهده دانشجویان", self.colors['warning'], lambda: self.show_login("professor")),
            (" مدیر سیستم", "تعریف درس، مدیریت دانشجویان و دروس", self.colors['danger'], lambda: self.show_login("admin")),
            (" ثبت نام جدید", "ثبت نام دانشجویان جدید در سامانه", self.colors['success'], self.show_register)
        ]:
            card = tk.Frame(body, bg='white', relief='raised', bd=3, width=250, height=200)
            card.pack(side='left', padx=15, expand=True); card.pack_propagate(False)
            tk.Label(card, text=title, font=self.fonts['header'], fg=color, bg='white').pack(pady=25)
            tk.Label(card, text=desc, font=self.fonts['normal'], bg='white', fg='#444', wraplength=200, justify='center').pack(pady=10, padx=10)
            tk.Button(card, text="ورود / ثبت نام", font=('B Nazanin', 12, 'bold'), bg=color, fg='white', bd=0, padx=30, pady=10, command=cmd, cursor="hand2").pack(pady=20)

    def show_register(self):
        self.clear()
        self._create_header(" ثبت نام دانشجوی جدید", self.colors['success'])
        entries = self._create_form([
            (" شماره دانشجویی *", "sid"), (" نام و نام خانوادگی *", "name"), (" ایمیل", "email"),
            (" رمز عبور *", "password", True), (" رشته تحصیلی *", "major"), (" سال ورود", "year")
        ])
        
        def register():
            data = {k: e.get().strip() for k, e in entries.items()}
            if not all(data.get(r) for r in ['sid', 'name', 'password', 'major']):
                return messagebox.showerror("خطا", " لطفا فیلدهای ستاره‌دار را پر کنید!")
            if not messagebox.askyesno("تأیید ثبت نام", f"آیا از اطلاعات زیر اطمینان دارید؟\n\nشماره دانشجویی: {data['sid']}\nنام: {data['name']}\nرشته: {data['major']}\nسال ورود: {data.get('year', 'تعیین نشده')}"):
                return
            success, msg = self.system.add_student(data['sid'], data['name'], data['password'], data['major'], data.get('email'), data.get('year'))
            messagebox.showinfo(" موفق", f"{msg}\n\nشماره دانشجویی شما: {data['sid']}") if success else messagebox.showerror(" خطا", msg)
            if success: self.show_welcome()

        self._create_buttons(" تایید و ثبت نام", register, self.colors['success'])

    def show_login(self, user_type):
        self.clear()
        colors = {"student": self.colors['secondary'], "professor": self.colors['warning'], "admin": self.colors['danger']}
        titles = {"student": " ورود دانشجویان", "professor": " ورود اساتید", "admin": " ورود مدیر سیستم"}
        
        self._create_header(titles[user_type], colors[user_type])
        user_entry = tk.Entry(self.root, font=self.fonts['normal'], width=30, justify='center')
        pass_entry = tk.Entry(self.root, font=self.fonts['normal'], width=30, show='*', justify='center')
        
        tk.Label(self.root, text=" نام کاربری:", font=self.fonts['subheader'], bg=self.colors['bg']).pack(pady=15)
        user_entry.pack(pady=10)
        tk.Label(self.root, text=" رمز عبور:", font=self.fonts['subheader'], bg=self.colors['bg']).pack(pady=15)
        pass_entry.pack(pady=10)

        def login():
            u, p = user_entry.get().strip(), pass_entry.get().strip()
            if not u or not p: return messagebox.showerror("خطا", " لطفا همه فیلدها را پر کنید!")
            
            user_data = getattr(self.system, f"{user_type}s", {})
            if u in user_data and user_data[u]["password"] == p:
                self.current_user, self.current_type = u, user_type
                getattr(self, f"show_{user_type}_panel")()
            else: messagebox.showerror("خطا", " نام کاربری یا رمز عبور اشتباه است!")

        self._create_buttons(" ورود به سامانه", login, colors[user_type])

    def show_student_panel(self):
        self._create_user_panel("student", self.colors['secondary'], [
            (" انتخاب واحد", self.show_course_selection),
            (" دروس من", self.show_my_courses),
            (" خروج", self.logout)
        ])

    def show_course_selection(self):
        self._clear_content()
        tk.Label(self.content, text=" انتخاب واحد ترم جاری", font=self.fonts['header'], bg=self.colors['bg']).pack(pady=15)
        
        if not self.system.courses: return tk.Label(self.content, text=" هیچ درسی تعریف نشده است.", font=self.fonts['normal'], fg='red').pack(expand=True)

        search_var = tk.StringVar()
        tk.Label(self.content, text=" جستجو:", font=self.fonts['normal'], bg=self.colors['bg']).pack(side='top', anchor='w', padx=20)
        tk.Entry(self.content, textvariable=search_var, font=self.fonts['normal'], width=35).pack(pady=10)

        tree = self._create_table(['کد', 'نام درس', 'استاد', 'دانشکده', 'واحد', 'زمان', 'ظرفیت', 'وضعیت'], [70, 200, 120, 100, 60, 150, 80, 100])
        
        def update_table():
            for w in self.content.winfo_children(): 
                if isinstance(w, tk.Button) and w._name == "action_btn": w.destroy()
            tree.delete(*tree.get_children())
            query = search_var.get().lower()
            enrolled = self.system.students[self.current_user]["courses"]
            
            for i, (code, course) in enumerate(self.system.courses.items()):
                if query and query not in course["name"].lower() and query not in code: continue
                
                status = " ثبت‌نام شده" if code in enrolled else " قابل ثبت‌نام" if course["current_students"] < course["capacity"] else " تکمیل ظرفیت"
                tree.insert('', 'end', values=(code, course["name"], course["professor"], course["department"], course["units"], course["schedule"], f"{course['current_students']}/{course['capacity']}", status))
                
                if code in enrolled:
                    btn = tk.Button(self.content, text=" حذف درس", font=self.fonts['small'], bg=self.colors['danger'], fg='white', bd=0, padx=8, pady=3, cursor="hand2", name="action_btn")
                    btn.place(x=900, y=180 + (i * 24), width=90, height=20)
                    btn.config(command=lambda c=code: self._course_action(c, "drop", update_table))
                elif course["current_students"] < course["capacity"]:
                    btn = tk.Button(self.content, text=" انتخاب درس", font=self.fonts['small'], bg=self.colors['success'], fg='white', bd=0, padx=8, pady=3, cursor="hand2", name="action_btn")
                    btn.place(x=900, y=180 + (i * 24), width=90, height=20)
                    btn.config(command=lambda c=code: self._course_action(c, "enroll", update_table))

        search_var.trace_add('w', lambda *args: update_table())
        update_table()

    def _course_action(self, course_code, action, callback):
        course = self.system.courses[course_code]
        student = self.system.students[self.current_user]
        
        if action == "enroll":
            if course_code in student["courses"]: return messagebox.showinfo(" توجه", "این درس قبلاً انتخاب شده است!")
            if course["current_students"] >= course["capacity"]: return messagebox.showwarning(" تکمیل ظرفیت", "ظرفیت این درس تکمیل است!")
            if student["total_units"] + course["units"] > 20: return messagebox.showwarning(" محدودیت واحد", "مجموع واحدهای شما نمی‌تواند از ۲۰ واحد بیشتر شود!")
            if messagebox.askyesno(" ثبت درس", f"آیا مایل به ثبت نام در درس '{course['name']}' هستید؟\n\nاستاد: {course['professor']}\nواحد: {course['units']}\nزمان: {course['schedule']}"):
                student["courses"].append(course_code)
                student["total_units"] += course["units"]
                course["current_students"] += 1
                callback()
                messagebox.showinfo(" موفق", f"ثبت نام در درس {course['name']} با موفقیت انجام شد")
        else:
            if course_code not in student["courses"]: return messagebox.showwarning(" خطا", "این درس در لیست دروس شما نیست!")
            if messagebox.askyesno(" حذف درس", f"آیا از حذف درس '{course['name']}' اطمینان دارید؟\n\nاستاد: {course['professor']}\nواحد: {course['units']}\nزمان: {course['schedule']}"):
                student["courses"].remove(course_code)
                student["total_units"] -= course["units"]
                course["current_students"] -= 1
                callback()
                messagebox.showinfo(" موفق", f"درس {course['name']} با موفقیت حذف شد")

    def show_my_courses(self):
        self._clear_content()
        tk.Label(self.content, text=" دروس ثبت‌نام شده شما", font=self.fonts['header'], bg=self.colors['bg']).pack(pady=20)
        courses = self.system.students[self.current_user]["courses"]
        if not courses: return tk.Label(self.content, text=" هیچ درسی انتخاب نکرده‌اید.", font=self.fonts['normal'], fg='gray').pack(expand=True)
        
        tree = self._create_table(['کد', 'نام درس', 'استاد', 'واحد', 'زمان', 'امتحان'], [80, 200, 120, 60, 150, 100])
        for code in courses:
            c = self.system.courses[code]
            tree.insert('', 'end', values=(code, c["name"], c["professor"], c["units"], c["schedule"], c.get("exam_date", "تعیین نشده")))

    def show_professor_panel(self):
        self._create_user_panel("professor", self.colors['warning'], [
            (" دروس من", self.show_professor_courses),
            (" دانشجویان من", self.show_professor_students),
            (" خروج", self.logout)
        ])

    def show_professor_courses(self):
        self._clear_content()
        tk.Label(self.content, text=" دروس تحت تدریس", font=self.fonts['header'], bg=self.colors['bg']).pack(pady=20)
        prof_courses = [(code, c) for code, c in self.system.courses.items() if c.get("professor_id") == self.current_user]
        if not prof_courses: return tk.Label(self.content, text=" هیچ درسی برای شما تعریف نشده است.", font=self.fonts['normal'], fg='red').pack(expand=True)
        
        tree = self._create_table(['کد', 'نام درس', 'دانشکده', 'واحد', 'دانشجویان', 'ظرفیت', 'زمان'], [70, 180, 100, 60, 80, 70, 150])
        for code, course in prof_courses:
            tree.insert('', 'end', values=(code, course["name"], course["department"], course["units"], course["current_students"], course["capacity"], course["schedule"]))

    def show_professor_students(self):
        self._clear_content()
        tk.Label(self.content, text=" دانشجویان تحت تدریس", font=self.fonts['header'], bg=self.colors['bg']).pack(pady=20)
        prof_students = {sid: s for code, course in self.system.courses.items() if course.get("professor_id") == self.current_user for sid, s in self.system.students.items() if code in s["courses"]}
        if not prof_students: return tk.Label(self.content, text=" هیچ دانشجویی در دروس شما ثبت‌نام نکرده است.", font=self.fonts['normal'], fg='gray').pack(expand=True)
        
        tree = self._create_table(['شماره', 'نام', 'رشته', 'سال ورود', 'واحدها'], [100, 150, 120, 80, 70])
        for sid, student in prof_students.items():
            tree.insert('', 'end', values=(sid, student["name"], student["major"], student["entry_year"], student["total_units"]))

    def show_admin_panel(self):
        self._create_user_panel("admin", self.colors['danger'], [
            (" تعریف درس جدید", self.show_add_course),
            (" مدیریت دروس", self.show_manage_courses),
            (" لیست دانشجویان", self.show_students_list),
            (" خروج", self.logout)
        ])

    def show_add_course(self):
        self._clear_admin_content()
        tk.Label(self.admin_content, text=" تعریف درس جدید", font=self.fonts['header'], bg=self.colors['bg']).pack(pady=15)
        entries = self._create_form([
            (" کد درس *", "course_code"), (" نام درس *", "course_name"), (" نام استاد *", "professor"),
            (" شماره استاد", "professor_id"), (" تعداد واحد *", "units"), (" ظرفیت *", "capacity"),
            (" زمان برگزاری *", "schedule"), (" دانشکده *", "department"), (" کلاس", "classroom"), (" تاریخ امتحان", "exam_date")
        ], self.admin_content)
        
        def add_course():
            data = {k: e.get().strip() for k, e in entries.items()}
            try: [int(data[k]) for k in ["units", "capacity"] if data[k]]
            except: return messagebox.showerror("خطا", " واحد و ظرفیت باید عدد باشند!")
            success, msg = self.system.add_course(data)
            messagebox.showinfo(" موفق", msg) if success else messagebox.showerror(" خطا", msg)
            if success: [e.delete(0, tk.END) for e in entries.values()]

        self._create_buttons(" ذخیره درس", add_course, self.colors['success'], self.admin_content)

    def show_manage_courses(self):
        self._clear_admin_content()
        tk.Label(self.admin_content, text=" مدیریت دروس سیستم", font=self.fonts['header'], bg=self.colors['bg']).pack(pady=15)
        if not self.system.courses: return tk.Label(self.admin_content, text=" هیچ درسی در سیستم تعریف نشده است.", font=self.fonts['normal'], fg='red').pack(expand=True)
        
        search_var = tk.StringVar()
        tk.Label(self.admin_content, text=" جستجو:", font=self.fonts['normal'], bg=self.colors['bg']).pack(side='top', anchor='w', padx=20)
        tk.Entry(self.admin_content, textvariable=search_var, font=self.fonts['normal'], width=35).pack(pady=10)
        
        tree = self._create_table(['کد', 'نام درس', 'استاد', 'دانشکده', 'واحد', 'دانشجویان', 'ظرفیت', 'زمان'], [70, 180, 120, 100, 60, 80, 70, 150], self.admin_content)
        
        def update_table():
            tree.delete(*tree.get_children())
            query = search_var.get().lower()
            for code, course in self.system.courses.items():
                if query and query not in course["name"].lower() and query not in code: continue
                tree.insert('', 'end', values=(code, course["name"], course["professor"], course["department"], course["units"], course["current_students"], course["capacity"], course["schedule"]))
        
        def delete_course():
            if not tree.selection(): return messagebox.showwarning("هشدار", " لطفا یک درس را انتخاب کنید!")
            code = tree.item(tree.selection()[0])["values"][0]
            if messagebox.askyesno(" حذف درس", f"آیا از حذف درس '{self.system.courses[code]['name']}' اطمینان دارید؟\n\n⚠️ این عمل باعث حذف این درس از کارنامه تمام دانشجویان خواهد شد!"):
                success, msg = self.system.delete_course(code)
                messagebox.showinfo(" موفق", msg) if success else messagebox.showerror(" خطا", msg)
                update_table()
        
        tk.Button(self.admin_content, text=" حذف درس انتخاب شده", font=self.fonts['normal'], bg=self.colors['danger'], fg='white', padx=15, pady=8, command=delete_course).pack(pady=10)
        search_var.trace_add('w', lambda *args: update_table())
        update_table()

    def show_students_list(self):
        self._clear_admin_content()
        tk.Label(self.admin_content, text=" لیست دانشجویان سیستم", font=self.fonts['header'], bg=self.colors['bg']).pack(pady=15)
        if not self.system.students: return tk.Label(self.admin_content, text=" هیچ دانشجویی در سیستم ثبت‌نام نکرده است.", font=self.fonts['normal'], fg='gray').pack(expand=True)
        
        search_var = tk.StringVar()
        tk.Label(self.admin_content, text=" جستجو:", font=self.fonts['normal'], bg=self.colors['bg']).pack(side='top', anchor='w', padx=20)
        tk.Entry(self.admin_content, textvariable=search_var, font=self.fonts['normal'], width=35).pack(pady=10)
        
        tree = self._create_table(['شماره', 'نام', 'رشته', 'سال ورود', 'ایمیل', 'واحدها', 'تعداد دروس'], [100, 150, 120, 80, 150, 70, 90], self.admin_content)
        
        def update_table():
            tree.delete(*tree.get_children())
            query = search_var.get().lower()
            for sid, student in self.system.students.items():
                if query and query not in student["name"].lower() and query not in sid: continue
                tree.insert('', 'end', values=(sid, student["name"], student["major"], student["entry_year"], student.get("email", ""), student["total_units"], len(student["courses"])))
        
        search_var.trace_add('w', lambda *args: update_table())
        update_table()

    def _create_header(self, text, color):
        header = tk.Frame(self.root, bg=color, height=120)
        header.pack(fill='x'); header.pack_propagate(False)
        tk.Label(header, text=text, font=self.fonts['title'], fg='white', bg=color).pack(pady=35)

    def _create_form(self, fields, parent=None):
        parent = parent or self.root
        form = tk.Frame(parent, bg='white', relief='raised', bd=3, padx=50, pady=40)
        form.pack(fill='both', expand=True, padx=80, pady=15)
        entries = {}
        for label, key, *pw in fields:
            row = tk.Frame(form, bg='white'); row.pack(fill='x', pady=10)
            tk.Label(row, text=label, font=self.fonts['normal'], bg='white', width=18, anchor='e').pack(side='left')
            e = tk.Entry(row, font=self.fonts['normal'], width=30, show='*' if pw else ''); e.pack(side='right', padx=10)
            entries[key] = e
        return entries

    def _create_buttons(self, text, command, color, parent=None):
        parent = parent or self.root
        btns = tk.Frame(parent, bg='white'); btns.pack(pady=25)
        tk.Button(btns, text=text, font=('B Nazanin', 14, 'bold'), bg=color, fg='white', padx=40, pady=12, command=command).pack(side='left', padx=15)
        tk.Button(btns, text=" بازگشت", font=self.fonts['normal'], bg='#95a5a6', fg='white', padx=30, pady=10, command=self.show_welcome).pack(side='left', padx=15)

    def _create_user_panel(self, user_type, color, menu_buttons):
        self.clear()
        user_data = getattr(self.system, f"{user_type}s")[self.current_user]
        header = tk.Frame(self.root, bg=color, height=140); header.pack(fill='x'); header.pack_propagate(False)
        tk.Label(header, text=f" خوش آمدید، {user_data['name']}", font=self.fonts['title'], fg='white', bg=color).pack(pady=25)
        if user_type == "student": tk.Label(header, text=f" رشته: {user_data['major']} | سال ورود: {user_data['entry_year']} | مجموع واحد: {user_data['total_units']}", font=self.fonts['normal'], fg='white', bg=color).pack()
        elif user_type == "professor": tk.Label(header, text=f" دانشکده: {user_data['department']}", font=self.fonts['normal'], fg='white', bg=color).pack()
        
        menu = tk.Frame(self.root, bg=self.colors['primary'], height=60); menu.pack(fill='x'); menu.pack_propagate(False)
        for text, cmd in menu_buttons:
            btn_color = self.colors['danger'] if text == " خروج" else self.colors['primary']
            tk.Button(menu, text=text, font=self.fonts['subheader'], bg=btn_color, fg='white', bd=0, padx=30, pady=15, command=cmd).pack(side='left', padx=15)
        
        setattr(self, "content" if user_type != "admin" else "admin_content", tk.Frame(self.root, bg=self.colors['bg']))
        getattr(self, "content" if user_type != "admin" else "admin_content").pack(fill='both', expand=True, padx=40, pady=20)
        getattr(self, f"show_{'course_selection' if user_type == 'student' else 'professor_courses' if user_type == 'professor' else 'manage_courses'}")()

    def _create_table(self, headers, widths, parent=None):
        parent = parent or self.content
        tree_frame = tk.Frame(parent); tree_frame.pack(fill='both', expand=True, pady=10)
        tree = ttk.Treeview(tree_frame, columns=range(len(headers)), show='headings', height=10)
        for i, (header, width) in enumerate(zip(headers, widths)):
            tree.heading(i, text=header); tree.column(i, width=width, anchor='center')
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side='left', fill='both', expand=True); scrollbar.pack(side='right', fill='y')
        return tree

    def _clear_content(self): [w.destroy() for w in self.content.winfo_children()]
    def _clear_admin_content(self): [w.destroy() for w in self.admin_content.winfo_children()]

    def logout(self):
        if messagebox.askyesno(" خروج", "آیا مایل به خروج از حساب کاربری هستید؟"):
            self.current_user = self.current_type = None
            self.show_welcome()

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversityApp(root)
    root.mainloop()
    
    