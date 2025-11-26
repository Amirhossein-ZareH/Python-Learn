import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont

class UniversitySystem:
    def __init__(self):
        self.students = {}
        self.professors = {}
        self.courses = {}
        self.admins = {}
        
        self._create_admin_data()
    
    def _create_admin_data(self):
        # فقط ادمین پیشفرض ایجاد شود
        self.admins["admin"] = {
            "name": "مدیر سیستم",
            "password": "admin123"
        }
    
    def add_student(self, student_id, name, password, major, email="", entry_year=""):
        """افزودن دانشجوی جدید"""
        if student_id in self.students:
            return False, "این شماره دانشجویی قبلاً ثبت شده است"
        
        self.students[student_id] = {
            "name": name,
            "password": password,
            "email": email,
            "major": major,
            "entry_year": entry_year,
            "courses": [],
            "total_units": 0
        }
        return True, "ثبت نام با موفقیت انجام شد"
    
    def add_course(self, course_data):
        """افزودن درس جدید"""
        course_code = course_data["course_code"]
        if course_code in self.courses:
            return False, "این کد درس قبلاً ثبت شده است"
        
        self.courses[course_code] = {
            "name": course_data["course_name"],
            "professor": course_data["professor"],
            "professor_id": course_data["professor_id"],
            "capacity": int(course_data["capacity"]),
            "current_students": 0,
            "schedule": course_data["schedule"],
            "units": int(course_data["units"]),
            "department": course_data["department"],
            "classroom": course_data.get("classroom", ""),
            "exam_date": course_data.get("exam_date", "")
        }
        return True, "درس جدید با موفقیت تعریف شد"

class ModernUniversityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 سامانه آموزشی دانشگاه")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f8f9fa')
        
        # تنظیم تم تاریک/روشن
        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#34495e',
            'accent': '#3498db',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'light': '#ecf0f1',
            'dark': '#2c3e50',
            'background': '#f8f9fa',
            'card_bg': '#ffffff'
        }
        
        # تنظیم فونت‌ها
        self.fonts = {
            'title': ('B Nazanin', 24, 'bold'),
            'header': ('B Nazanin', 18, 'bold'),
            'subheader': ('B Nazanin', 14, 'bold'),
            'normal': ('B Nazanin', 12),
            'small': ('B Nazanin', 10)
        }
        
        self.system = UniversitySystem()
        self.current_user = None
        self.current_user_type = None
        
        self.create_styles()
        self.show_welcome_page()
    
    def create_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # استایل برای Treeview
        style.configure('Custom.Treeview',
                       background='white',
                       foreground=self.colors['dark'],
                       rowheight=25,
                       fieldbackground='white')
        
        style.configure('Custom.Treeview.Heading',
                       background=self.colors['primary'],
                       foreground='white',
                       font=self.fonts['subheader'])
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_welcome_page(self):
        self.clear_frame()
        
        # هدر اصلی
        header = tk.Frame(self.root, bg=self.colors['primary'], height=150)
        header.pack(fill='x', padx=0, pady=0)
        
        # محتوای هدر
        header_content = tk.Frame(header, bg=self.colors['primary'])
        header_content.pack(expand=True, fill='both', padx=50, pady=20)
        
        # لوگو و عنوان
        title_frame = tk.Frame(header_content, bg=self.colors['primary'])
        title_frame.pack()
        
        tk.Label(title_frame, text="🎓", font=('Arial', 40), 
                bg=self.colors['primary'], fg='white').pack()
        tk.Label(title_frame, text="سامانه آموزشی دانشگاه", font=self.fonts['title'],
                bg=self.colors['primary'], fg='white').pack(pady=10)
        tk.Label(title_frame, text="مدیریت تحصیلی و انتخاب واحد", font=self.fonts['subheader'],
                bg=self.colors['primary'], fg=self.colors['light']).pack()
        
        # محتوای اصلی
        main_content = tk.Frame(self.root, bg=self.colors['background'])
        main_content.pack(expand=True, fill='both', padx=50, pady=30)
        
        # عنوان بخش
        section_title = tk.Label(main_content, text="ورود به سامانه", 
                                font=self.fonts['header'], bg=self.colors['background'])
        section_title.pack(pady=(0, 30))
        
        # کارت‌های ورود
        cards_frame = tk.Frame(main_content, bg=self.colors['background'])
        cards_frame.pack(expand=True, fill='both')
        
        # ردیف اول کارت‌ها
        row1 = tk.Frame(cards_frame, bg=self.colors['background'])
        row1.pack(pady=10)
        
        # کارت دانشجو
        student_card = tk.Frame(row1, bg=self.colors['card_bg'], relief='raised', bd=2, 
                               highlightbackground=self.colors['light'], highlightthickness=1)
        student_card.pack(side='left', padx=15, pady=15, fill='both', expand=True)
        
        tk.Label(student_card, text="👨‍🎓", font=('Arial', 32), bg=self.colors['card_bg']).pack(pady=10)
        tk.Label(student_card, text="دانشجویان", font=self.fonts['header'],
                bg=self.colors['card_bg'], fg=self.colors['accent']).pack(pady=5)
        tk.Label(student_card, text="سیستم انتخاب واحد و مدیریت تحصیلی", 
                font=self.fonts['small'], bg=self.colors['card_bg'], fg=self.colors['dark'],
                wraplength=200).pack(pady=5, padx=10)
        tk.Button(student_card, text="ورود", font=self.fonts['normal'],
                 bg=self.colors['accent'], fg='white', padx=30, pady=8, bd=0,
                 command=lambda: self.show_login_page("student")).pack(pady=15)
        
        # کارت مدیر
        admin_card = tk.Frame(row1, bg=self.colors['card_bg'], relief='raised', bd=2, 
                             highlightbackground=self.colors['light'], highlightthickness=1)
        admin_card.pack(side='left', padx=15, pady=15, fill='both', expand=True)
        
        tk.Label(admin_card, text="⚙️", font=('Arial', 32), bg=self.colors['card_bg']).pack(pady=10)
        tk.Label(admin_card, text="مدیر سیستم", font=self.fonts['header'],
                bg=self.colors['card_bg'], fg=self.colors['danger']).pack(pady=5)
        tk.Label(admin_card, text="تعریف دروس و مدیریت کاربران", 
                font=self.fonts['small'], bg=self.colors['card_bg'], fg=self.colors['dark'],
                wraplength=200).pack(pady=5, padx=10)
        tk.Button(admin_card, text="ورود", font=self.fonts['normal'],
                 bg=self.colors['danger'], fg='white', padx=30, pady=8, bd=0,
                 command=lambda: self.show_login_page("admin")).pack(pady=15)
        
        # ردیف دوم کارت‌ها
        row2 = tk.Frame(cards_frame, bg=self.colors['background'])
        row2.pack(pady=10)
        
        # کارت ثبت نام
        register_card = tk.Frame(row2, bg=self.colors['card_bg'], relief='raised', bd=2, 
                                highlightbackground=self.colors['light'], highlightthickness=1)
        register_card.pack(side='left', padx=15, pady=15, fill='both', expand=True)
        
        tk.Label(register_card, text="📝", font=('Arial', 32), bg=self.colors['card_bg']).pack(pady=10)
        tk.Label(register_card, text="ثبت نام", font=self.fonts['header'],
                bg=self.colors['card_bg'], fg=self.colors['success']).pack(pady=5)
        tk.Label(register_card, text="ثبت نام دانشجویان جدید در سیستم", 
                font=self.fonts['small'], bg=self.colors['card_bg'], fg=self.colors['dark'],
                wraplength=200).pack(pady=5, padx=10)
        tk.Button(register_card, text="ثبت نام", font=self.fonts['normal'],
                 bg=self.colors['success'], fg='white', padx=30, pady=8, bd=0,
                 command=self.show_register_page).pack(pady=15)
        
        # فوتر
        footer = tk.Frame(self.root, bg=self.colors['secondary'], height=60)
        footer.pack(fill='x', side='bottom')
        
        footer_text = tk.Label(footer, 
                              text="دانشگاه آزاد اسلامی - کلیه حقوق محفوظ است © 1402", 
                              font=self.fonts['small'], 
                              fg='white', bg=self.colors['secondary'])
        footer_text.pack(pady=20)
    
    def show_login_page(self, user_type):
        self.clear_frame()
        
        # هدر
        header = tk.Frame(self.root, bg=self.colors['primary'], height=120)
        header.pack(fill='x', padx=0, pady=0)
        
        titles = {
            "student": "ورود دانشجویان 👨‍🎓",
            "admin": "ورود مدیران ⚙️"
        }
        
        tk.Label(header, text=titles[user_type], font=self.fonts['title'],
                fg='white', bg=self.colors['primary']).pack(pady=40)
        
        # محتوای اصلی
        main_content = tk.Frame(self.root, bg=self.colors['background'])
        main_content.pack(expand=True, fill='both', padx=100, pady=50)
        
        # فرم لاگین
        login_card = tk.Frame(main_content, bg=self.colors['card_bg'], 
                             relief='raised', bd=2, padx=40, pady=40)
        login_card.pack(expand=True, fill='both')
        
        # فیلدهای ورود
        input_frame = tk.Frame(login_card, bg=self.colors['card_bg'])
        input_frame.pack(pady=30)
        
        # نام کاربری
        user_frame = tk.Frame(input_frame, bg=self.colors['card_bg'])
        user_frame.pack(fill='x', pady=15)
        
        tk.Label(user_frame, text="🔑 نام کاربری:", font=self.fonts['subheader'], 
                bg=self.colors['card_bg']).pack(side='left')
        self.username_entry = tk.Entry(user_frame, font=self.fonts['normal'], 
                                      width=25, bd=1, relief='solid')
        self.username_entry.pack(side='right', padx=10)
        
        # رمز عبور
        pass_frame = tk.Frame(input_frame, bg=self.colors['card_bg'])
        pass_frame.pack(fill='x', pady=15)
        
        tk.Label(pass_frame, text="🔒 رمز عبور:", font=self.fonts['subheader'], 
                bg=self.colors['card_bg']).pack(side='left')
        self.password_entry = tk.Entry(pass_frame, font=self.fonts['normal'], 
                                      width=25, show='•', bd=1, relief='solid')
        self.password_entry.pack(side='right', padx=10)
        
        # دکمه‌ها
        button_frame = tk.Frame(login_card, bg=self.colors['card_bg'])
        button_frame.pack(pady=30)
        
        login_btn = tk.Button(button_frame, text="🚀 ورود به سامانه", 
                             font=self.fonts['subheader'],
                             bg=self.colors['success'], fg='white',
                             padx=30, pady=12, bd=0,
                             command=lambda: self.login(user_type))
        login_btn.pack(side='left', padx=10)
        
        back_btn = tk.Button(button_frame, text="↩️ بازگشت", 
                            font=self.fonts['normal'],
                            bg=self.colors['secondary'], fg='white',
                            padx=20, pady=10, bd=0,
                            command=self.show_welcome_page)
        back_btn.pack(side='left', padx=10)
        
        # اطلاعات نمونه
        sample_frame = tk.Frame(login_card, bg=self.colors['light'], 
                               relief='solid', bd=1, padx=15, pady=10)
        sample_frame.pack(pady=20)
        
        tk.Label(sample_frame, text="💡 اطلاعات نمونه برای تست:", 
                font=self.fonts['subheader'], bg=self.colors['light']).pack()
        
        if user_type == "student":
            if self.system.students:
                sample_text = "از شماره دانشجویی ثبت‌نام شده استفاده کنید"
            else:
                sample_text = "ابتدا ثبت نام کنید"
            tk.Label(sample_frame, text=sample_text, 
                    font=self.fonts['normal'], bg=self.colors['light']).pack()
        elif user_type == "admin":
            tk.Label(sample_frame, text="نام کاربری: admin - رمز: admin123", 
                    font=self.fonts['normal'], bg=self.colors['light']).pack()
    
    def show_register_page(self):
        self.clear_frame()
        
        # هدر
        header = tk.Frame(self.root, bg=self.colors['success'], height=120)
        header.pack(fill='x', padx=0, pady=0)
        
        tk.Label(header, text="📝 ثبت نام دانشجوی جدید", font=self.fonts['title'],
                fg='white', bg=self.colors['success']).pack(pady=40)
        
        # محتوای اصلی
        main_content = tk.Frame(self.root, bg=self.colors['background'])
        main_content.pack(expand=True, fill='both', padx=100, pady=50)
        
        # فرم ثبت نام
        register_card = tk.Frame(main_content, bg=self.colors['card_bg'], 
                                relief='raised', bd=2, padx=40, pady=40)
        register_card.pack(expand=True, fill='both')
        
        # فیلدهای ثبت نام
        input_frame = tk.Frame(register_card, bg=self.colors['card_bg'])
        input_frame.pack(pady=20)
        
        fields = [
            ("🔢 شماره دانشجویی:", "student_id"),
            ("👤 نام و نام خانوادگی:", "name"),
            ("📧 ایمیل:", "email"),
            ("🔒 رمز عبور:", "password"),
            ("🎓 رشته تحصیلی:", "major"),
            ("📅 سال ورود:", "entry_year")
        ]
        
        self.register_entries = {}
        
        for i, (label, field) in enumerate(fields):
            row_frame = tk.Frame(input_frame, bg=self.colors['card_bg'])
            row_frame.pack(fill='x', pady=12)
            
            tk.Label(row_frame, text=label, font=self.fonts['normal'], 
                    bg=self.colors['card_bg'], width=20, anchor='e').pack(side='left')
            
            if field == "password":
                entry = tk.Entry(row_frame, font=self.fonts['normal'], 
                                width=25, show='•', bd=1, relief='solid')
            else:
                entry = tk.Entry(row_frame, font=self.fonts['normal'], 
                                width=25, bd=1, relief='solid')
                
            entry.pack(side='right', padx=10)
            self.register_entries[field] = entry
        
        # دکمه‌ها
        button_frame = tk.Frame(register_card, bg=self.colors['card_bg'])
        button_frame.pack(pady=30)
        
        register_btn = tk.Button(button_frame, text="✅ ثبت نام", 
                               font=self.fonts['subheader'],
                               bg=self.colors['success'], fg='white',
                               padx=30, pady=12, bd=0,
                               command=self.register_student)
        register_btn.pack(side='left', padx=10)
        
        back_btn = tk.Button(button_frame, text="↩️ بازگشت", 
                            font=self.fonts['normal'],
                            bg=self.colors['secondary'], fg='white',
                            padx=20, pady=10, bd=0,
                            command=self.show_welcome_page)
        back_btn.pack(side='left', padx=10)
    
    def register_student(self):
        try:
            student_id = self.register_entries["student_id"].get()
            name = self.register_entries["name"].get()
            email = self.register_entries["email"].get()
            password = self.register_entries["password"].get()
            major = self.register_entries["major"].get()
            entry_year = self.register_entries["entry_year"].get()
            
            if not all([student_id, name, password, major]):
                messagebox.showerror("خطا", "❌ لطفا فیلدهای ضروری را پر کنید")
                return
            
            # ثبت دانشجوی جدید
            success, message = self.system.add_student(student_id, name, password, major, email, entry_year)
            
            if success:
                messagebox.showinfo("موفق", f"✅ {message}")
                self.show_welcome_page()
            else:
                messagebox.showerror("خطا", f"❌ {message}")
            
        except Exception as e:
            messagebox.showerror("خطا", f"❌ خطا در ثبت نام: {str(e)}")
    
    def login(self, user_type):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if user_type == "student":
            if username in self.system.students:
                if self.system.students[username]["password"] == password:
                    self.current_user = username
                    self.current_user_type = "student"
                    self.show_student_dashboard()
                else:
                    messagebox.showerror("خطا", "❌ رمز عبور اشتباه است")
            else:
                messagebox.showerror("خطا", "❌ دانشجو یافت نشد")
        
        elif user_type == "admin":
            if username in self.system.admins:
                if self.system.admins[username]["password"] == password:
                    self.current_user = username
                    self.current_user_type = "admin"
                    self.show_admin_dashboard()
                else:
                    messagebox.showerror("خطا", "❌ رمز عبور اشتباه است")
            else:
                messagebox.showerror("خطا", "❌ مدیر سیستم یافت نشد")
    
    def show_student_dashboard(self):
        self.clear_frame()
        
        student_info = self.system.students[self.current_user]
        
        # هدر
        header = tk.Frame(self.root, bg=self.colors['accent'], height=140)
        header.pack(fill='x', padx=0, pady=0)
        
        header_content = tk.Frame(header, bg=self.colors['accent'])
        header_content.pack(expand=True, fill='both', padx=30, pady=20)
        
        # اطلاعات دانشجو
        info_frame = tk.Frame(header_content, bg=self.colors['accent'])
        info_frame.pack(expand=True, fill='both')
        
        welcome_text = f"👋 سلام {student_info['name']}"
        tk.Label(info_frame, text=welcome_text, font=self.fonts['title'],
                fg='white', bg=self.colors['accent']).pack(pady=5)
        
        details_text = f"🎓 {student_info['major']} | 📅 سال ورود: {student_info['entry_year']} | 🔢 کد: {self.current_user}"
        tk.Label(info_frame, text=details_text, font=self.fonts['subheader'],
                fg='white', bg=self.colors['accent']).pack(pady=5)
        
        # آمار
        stats_frame = tk.Frame(header_content, bg=self.colors['secondary'])
        stats_frame.pack(fill='x', pady=10)
        
        courses_count = len(student_info['courses'])
        total_units = student_info['total_units']
        
        stats_text = f"📚 {courses_count} درس | ⚖️ {total_units} واحد"
        tk.Label(stats_frame, text=stats_text, font=self.fonts['subheader'],
                fg='white', bg=self.colors['secondary']).pack(pady=8)
        
        # منو
        menu_frame = tk.Frame(self.root, bg=self.colors['primary'], height=60)
        menu_frame.pack(fill='x', padx=0, pady=0)
        
        menu_buttons = [
            ("📖 انتخاب واحد", self.show_course_selection),
            ("📚 دروس من", self.show_my_courses),
            ("🚪 خروج", self.logout)
        ]
        
        for text, command in menu_buttons:
            btn = tk.Button(menu_frame, text=text, font=self.fonts['normal'],
                          bg=self.colors['primary'], fg='white', bd=0,
                          padx=20, pady=15, command=command)
            btn.pack(side='left', padx=5)
            
            # افکت hover برای منو
            def on_enter(e, b=btn):
                b.configure(bg=self.colors['accent'])
            
            def on_leave(e, b=btn):
                b.configure(bg=self.colors['primary'])
            
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
        
        # محتوای اصلی
        self.main_content = tk.Frame(self.root, bg=self.colors['background'])
        self.main_content.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.show_course_selection()
    
    def show_course_selection(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # هدر بخش
        section_header = tk.Frame(self.main_content, bg=self.colors['primary'], height=60)
        section_header.pack(fill='x', pady=(0, 20))
        
        tk.Label(section_header, text="📖 سیستم انتخاب واحد", 
                font=self.fonts['header'], fg='white', bg=self.colors['primary']).pack(pady=15)
        
        if not self.system.courses:
            empty_frame = tk.Frame(self.main_content, bg=self.colors['background'])
            empty_frame.pack(expand=True, fill='both')
            
            tk.Label(empty_frame, text="📭 درسی برای نمایش وجود ندارد\nلطفا مدیر سیستم دروس را تعریف کند", 
                    font=self.fonts['header'], bg=self.colors['background'],
                    fg=self.colors['secondary'], justify='center').pack(expand=True)
            return
        
        # فیلترها
        filter_frame = tk.Frame(self.main_content, bg=self.colors['light'], padx=15, pady=15)
        filter_frame.pack(fill='x', pady=10)
        
        tk.Label(filter_frame, text="🔍 جستجو:", font=self.fonts['normal'], 
                bg=self.colors['light']).pack(side='left', padx=10)
        self.search_entry = tk.Entry(filter_frame, font=self.fonts['normal'], 
                                    width=30, bd=1, relief='solid')
        self.search_entry.pack(side='left', padx=10)
        self.search_entry.bind('<KeyRelease>', self.filter_courses)
        
        tk.Label(filter_frame, text="🎓 دانشکده:", font=self.fonts['normal'], 
                bg=self.colors['light']).pack(side='left', padx=10)
        self.department_var = tk.StringVar(value="همه")
        
        # گرفتن لیست دانشکده‌ها از دروس موجود
        departments = ["همه"]
        for course in self.system.courses.values():
            if course["department"] not in departments:
                departments.append(course["department"])
        
        dept_combo = ttk.Combobox(filter_frame, textvariable=self.department_var, 
                                 values=departments, state="readonly", width=15)
        dept_combo.pack(side='left', padx=10)
        dept_combo.bind('<<ComboboxSelected>>', self.filter_courses)
        
        # جدول دروس
        table_frame = tk.Frame(self.main_content, bg='white')
        table_frame.pack(expand=True, fill='both', pady=10)
        
        columns = ('code', 'name', 'professor', 'department', 'units', 'schedule', 'capacity', 'classroom', 'action')
        self.courses_tree = ttk.Treeview(table_frame, columns=columns, show='headings', 
                           style='Custom.Treeview', height=15)
        
        # تعریف ستون‌ها
        headings = {
            'code': '🆔 کد درس',
            'name': '📖 نام درس', 
            'professor': '👨‍🏫 استاد',
            'department': '🎓 دانشکده',
            'units': '⚖️ واحد',
            'schedule': '🕒 زمان',
            'capacity': '👥 ظرفیت',
            'classroom': '🏫 مکان',
            'action': '⚡ عملیات'
        }
        
        for col in columns:
            self.courses_tree.heading(col, text=headings[col])
        
        self.courses_tree.column('code', width=80)
        self.courses_tree.column('name', width=180)
        self.courses_tree.column('professor', width=120)
        self.courses_tree.column('department', width=100)
        self.courses_tree.column('units', width=60)
        self.courses_tree.column('schedule', width=120)
        self.courses_tree.column('capacity', width=80)
        self.courses_tree.column('classroom', width=80)
        self.courses_tree.column('action', width=100)
        
        # اسکرول بار
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.courses_tree.yview)
        self.courses_tree.configure(yscrollcommand=scrollbar.set)
        self.courses_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.populate_courses_table()
        
        # دکمه‌های عملیات
        action_frame = tk.Frame(self.main_content, bg=self.colors['background'])
        action_frame.pack(pady=15)
        
        enroll_btn = tk.Button(action_frame, text="✅ ثبت نام در درس انتخاب شده", 
                              font=self.fonts['normal'],
                              bg=self.colors['success'], fg='white',
                              padx=20, pady=10, bd=0,
                              command=self.enroll_selected_course)
        enroll_btn.pack(side='left', padx=10)
        
        drop_btn = tk.Button(action_frame, text="❌ حذف درس انتخاب شده", 
                            font=self.fonts['normal'],
                            bg=self.colors['danger'], fg='white',
                            padx=20, pady=10, bd=0,
                            command=self.drop_selected_course)
        drop_btn.pack(side='left', padx=10)
        
        # اضافه کردن event برای دابل کلیک
        self.courses_tree.bind('<Double-1>', self.on_course_double_click)
    
    def on_course_double_click(self, event):
        """وقتی روی یک درس دابل کلیک میشه"""
        item = self.courses_tree.selection()[0]
        course_code = self.courses_tree.item(item)['values'][0]
        self.enroll_in_course(course_code)
    
    def populate_courses_table(self):
        for item in self.courses_tree.get_children():
            self.courses_tree.delete(item)
        
        student_courses = self.system.students[self.current_user]["courses"]
        
        for course_code, course in self.system.courses.items():
            enrolled = course_code in student_courses
            if enrolled:
                action_text = "❌ حذف"
            else:
                if course["current_students"] < course["capacity"]:
                    action_text = "✅ ثبت نام"
                else:
                    action_text = "⛔ تکمیل"
            
            self.courses_tree.insert('', 'end', values=(
                course_code,
                course["name"],
                course["professor"],
                course["department"],
                course["units"],
                course["schedule"],
                f"👥 {course['current_students']}/{course['capacity']}",
                course.get("classroom", "-"),
                action_text
            ))
    
    def filter_courses(self, event=None):
        search_term = self.search_entry.get().lower()
        department = self.department_var.get()
        
        for item in self.courses_tree.get_children():
            self.courses_tree.delete(item)
        
        student_courses = self.system.students[self.current_user]["courses"]
        
        for course_code, course in self.system.courses.items():
            # اعمال فیلتر
            if search_term and search_term not in course["name"].lower() and search_term not in course_code.lower():
                continue
            
            if department != "همه" and course["department"] != department:
                continue
            
            enrolled = course_code in student_courses
            if enrolled:
                action_text = "❌ حذف"
            else:
                if course["current_students"] < course["capacity"]:
                    action_text = "✅ ثبت نام"
                else:
                    action_text = "⛔ تکمیل"
            
            self.courses_tree.insert('', 'end', values=(
                course_code,
                course["name"],
                course["professor"],
                course["department"],
                course["units"],
                course["schedule"],
                f"👥 {course['current_students']}/{course['capacity']}",
                course.get("classroom", "-"),
                action_text
            ))
    
    def enroll_selected_course(self):
        selected_item = self.courses_tree.selection()
        if not selected_item:
            messagebox.showwarning("اخطار", "⚠️ لطفا یک درس را انتخاب کنید")
            return
        
        item = self.courses_tree.item(selected_item[0])
        course_code = item['values'][0]
        self.enroll_in_course(course_code)
    
    def enroll_in_course(self, course_code):
        course = self.system.courses[course_code]
        student_info = self.system.students[self.current_user]
        
        if course_code in student_info["courses"]:
            messagebox.showwarning("اخطار", "⚠️ شما قبلاً در این درس ثبت‌نام کرده‌اید")
            return
        
        if course["current_students"] >= course["capacity"]:
            messagebox.showerror("خطا", "❌ ظرفیت این درس تکمیل است")
            return
        
        # ثبت نام
        student_info["courses"].append(course_code)
        student_info["total_units"] += course["units"]
        self.system.courses[course_code]["current_students"] += 1
        
        messagebox.showinfo("موفق", f"✅ ثبت نام در درس {course['name']} با موفقیت انجام شد")
        self.populate_courses_table()
    
    def drop_selected_course(self):
        selected_item = self.courses_tree.selection()
        if not selected_item:
            messagebox.showwarning("اخطار", "⚠️ لطفا یک درس را انتخاب کنید")
            return
        
        item = self.courses_tree.item(selected_item[0])
        course_code = item['values'][0]
        self.drop_course(course_code)
    
    def drop_course(self, course_code):
        course = self.system.courses[course_code]
        student_info = self.system.students[self.current_user]
        
        if course_code not in student_info["courses"]:
            messagebox.showerror("خطا", "❌ شما در این درس ثبت‌نام نکرده‌اید")
            return
        
        # حذف درس
        student_info["courses"].remove(course_code)
        student_info["total_units"] -= course["units"]
        self.system.courses[course_code]["current_students"] -= 1
        
        messagebox.showinfo("موفق", f"✅ درس {course['name']} با موفقیت حذف شد")
        self.populate_courses_table()
    
    def show_my_courses(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # هدر بخش
        section_header = tk.Frame(self.main_content, bg=self.colors['success'], height=60)
        section_header.pack(fill='x', pady=(0, 20))
        
        tk.Label(section_header, text="📚 دروس ثبت‌نام شده من", 
                font=self.fonts['header'], fg='white', bg=self.colors['success']).pack(pady=15)
        
        student_info = self.system.students[self.current_user]
        student_courses = student_info["courses"]
        total_units = student_info["total_units"]
        
        # اطلاعات کلی
        info_frame = tk.Frame(self.main_content, bg=self.colors['light'], padx=15, pady=15)
        info_frame.pack(fill='x', pady=10)
        
        info_text = f"📊 تعداد دروس: {len(student_courses)} | ⚖️ مجموع واحدها: {total_units}"
        tk.Label(info_frame, text=info_text, font=self.fonts['subheader'],
                bg=self.colors['light']).pack()
        
        if not student_courses:
            empty_frame = tk.Frame(self.main_content, bg=self.colors['background'])
            empty_frame.pack(expand=True, fill='both')
            
            tk.Label(empty_frame, text="📭 هیچ درسی ثبت‌نام نکرده‌اید", 
                    font=self.fonts['header'], bg=self.colors['background'],
                    fg=self.colors['secondary']).pack(expand=True)
            return
        
        # جدول دروس من
        table_frame = tk.Frame(self.main_content, bg='white')
        table_frame.pack(expand=True, fill='both', pady=10)
        
        columns = ('code', 'name', 'professor', 'units', 'schedule', 'exam', 'classroom', 'action')
        tree = ttk.Treeview(table_frame, columns=columns, show='headings', 
                           style='Custom.Treeview', height=12)
        
        headings = {
            'code': '🆔 کد درس',
            'name': '📖 نام درس',
            'professor': '👨‍🏫 استاد',
            'units': '⚖️ واحد',
            'schedule': '🕒 زمان کلاس',
            'exam': '📝 تاریخ امتحان',
            'classroom': '🏫 مکان',
            'action': '⚡ عملیات'
        }
        
        for col in columns:
            tree.heading(col, text=headings[col])
            tree.column(col, width=110)
        
        for course_code in student_courses:
            course = self.system.courses[course_code]
            tree.insert('', 'end', values=(
                course_code,
                course["name"],
                course["professor"],
                course["units"],
                course["schedule"],
                course.get("exam_date", "-"),
                course.get("classroom", "-"),
                "❌ حذف"
            ))
        
        tree.pack(fill='both', expand=True)
        
        # دکمه حذف
        def drop_selected():
            selected_item = tree.selection()
            if selected_item:
                item = tree.item(selected_item[0])
                course_code = item['values'][0]
                self.drop_course(course_code)
                self.show_my_courses()  # رفرش صفحه
        
        drop_btn = tk.Button(self.main_content, text="❌ حذف درس انتخاب شده", 
                            font=self.fonts['normal'],
                            bg=self.colors['danger'], fg='white',
                            padx=20, pady=10, bd=0,
                            command=drop_selected)
        drop_btn.pack(pady=15)
    
    def show_admin_dashboard(self):
        self.clear_frame()
        
        # هدر
        header = tk.Frame(self.root, bg=self.colors['danger'], height=120)
        header.pack(fill='x', padx=0, pady=0)
        
        tk.Label(header, text="⚙️ پنل مدیریت سیستم", font=self.fonts['title'],
                fg='white', bg=self.colors['danger']).pack(pady=40)
        
        # منو
        menu_frame = tk.Frame(self.root, bg=self.colors['secondary'], height=60)
        menu_frame.pack(fill='x', padx=0, pady=0)
        
        menu_buttons = [
            ("➕ تعریف درس جدید", self.show_add_course),
            ("📚 مدیریت دروس", self.show_manage_courses),
            ("👥 مدیریت دانشجویان", self.show_manage_students),
            ("🚪 خروج", self.logout)
        ]
        
        for text, command in menu_buttons:
            btn = tk.Button(menu_frame, text=text, font=self.fonts['normal'],
                          bg=self.colors['secondary'], fg='white', bd=0,
                          padx=15, pady=15, command=command)
            btn.pack(side='left', padx=5)
        
        self.main_content = tk.Frame(self.root, bg=self.colors['background'])
        self.main_content.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.show_manage_courses()
    
    def show_add_course(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # هدر بخش
        section_header = tk.Frame(self.main_content, bg=self.colors['success'], height=60)
        section_header.pack(fill='x', pady=(0, 20))
        
        tk.Label(section_header, text="➕ تعریف درس جدید", 
                font=self.fonts['header'], fg='white', bg=self.colors['success']).pack(pady=15)
        
        # فرم تعریف درس
        form_card = tk.Frame(self.main_content, bg=self.colors['card_bg'], 
                            relief='raised', bd=2, padx=30, pady=30)
        form_card.pack(expand=True, fill='both')
        
        # فیلدها
        fields = [
            ("🆔 کد درس:", "course_code"),
            ("📖 نام درس:", "course_name"),
            ("👨‍🏫 استاد:", "professor"),
            ("🔢 کد استاد:", "professor_id"),
            ("⚖️ تعداد واحد:", "units"),
            ("👥 ظرفیت:", "capacity"),
            ("🕒 زمان برگزاری:", "schedule"),
            ("🎓 دانشکده:", "department"),
            ("🏫 مکان کلاس:", "classroom"),
            ("📝 تاریخ امتحان:", "exam_date")
        ]
        
        self.course_entries = {}
        
        for i, (label, field) in enumerate(fields):
            row_frame = tk.Frame(form_card, bg=self.colors['card_bg'])
            row_frame.pack(fill='x', pady=8)
            
            tk.Label(row_frame, text=label, font=self.fonts['normal'], 
                    bg=self.colors['card_bg'], width=20, anchor='e').pack(side='left')
            
            entry = tk.Entry(row_frame, font=self.fonts['normal'], 
                            width=30, bd=1, relief='solid')
            entry.pack(side='right', padx=10)
            self.course_entries[field] = entry
        
        # دکمه‌ها
        button_frame = tk.Frame(form_card, bg=self.colors['card_bg'])
        button_frame.pack(pady=30)
        
        save_btn = tk.Button(button_frame, text="💾 ذخیره درس", 
                           font=self.fonts['subheader'],
                           bg=self.colors['success'], fg='white',
                           padx=25, pady=10, bd=0,
                           command=self.save_course)
        save_btn.pack(side='left', padx=10)
        
        clear_btn = tk.Button(button_frame, text="🗑️ پاک کردن فرم", 
                            font=self.fonts['normal'],
                            bg=self.colors['secondary'], fg='white',
                            padx=20, pady=8, bd=0,
                            command=self.clear_course_form)
        clear_btn.pack(side='left', padx=10)
    
    def save_course(self):
        try:
            course_data = {
                "course_code": self.course_entries["course_code"].get(),
                "course_name": self.course_entries["course_name"].get(),
                "professor": self.course_entries["professor"].get(),
                "professor_id": self.course_entries["professor_id"].get(),
                "units": self.course_entries["units"].get(),
                "capacity": self.course_entries["capacity"].get(),
                "schedule": self.course_entries["schedule"].get(),
                "department": self.course_entries["department"].get(),
                "classroom": self.course_entries["classroom"].get(),
                "exam_date": self.course_entries["exam_date"].get()
            }
            
            if not all([course_data["course_code"], course_data["course_name"], course_data["professor"], 
                       course_data["units"], course_data["capacity"], course_data["schedule"], course_data["department"]]):
                messagebox.showerror("خطا", "❌ لطفا فیلدهای ضروری را پر کنید")
                return
            
            # ذخیره درس جدید
            success, message = self.system.add_course(course_data)
            
            if success:
                messagebox.showinfo("موفق", f"✅ {message}")
                self.clear_course_form()
            else:
                messagebox.showerror("خطا", f"❌ {message}")
            
        except Exception as e:
            messagebox.showerror("خطا", f"❌ خطا در ذخیره درس: {str(e)}")
    
    def clear_course_form(self):
        for entry in self.course_entries.values():
            entry.delete(0, tk.END)
    
    def show_manage_courses(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # هدر بخش
        section_header = tk.Frame(self.main_content, bg=self.colors['warning'], height=60)
        section_header.pack(fill='x', pady=(0, 20))
        
        tk.Label(section_header, text="📚 مدیریت دروس", 
                font=self.fonts['header'], fg='white', bg=self.colors['warning']).pack(pady=15)
        
        if not self.system.courses:
            empty_frame = tk.Frame(self.main_content, bg=self.colors['background'])
            empty_frame.pack(expand=True, fill='both')
            
            tk.Label(empty_frame, text="📭 هیچ درسی تعریف نشده است", 
                    font=self.fonts['header'], bg=self.colors['background'],
                    fg=self.colors['secondary']).pack(expand=True)
            return
        
        # جدول دروس
        table_frame = tk.Frame(self.main_content, bg='white')
        table_frame.pack(expand=True, fill='both', pady=10)
        
        columns = ('code', 'name', 'professor', 'department', 'units', 'capacity', 'students', 'schedule')
        tree = ttk.Treeview(table_frame, columns=columns, show='headings', 
                           style='Custom.Treeview', height=15)
        
        headings = {
            'code': '🆔 کد درس',
            'name': '📖 نام درس',
            'professor': '👨‍🏫 استاد',
            'department': '🎓 دانشکده',
            'units': '⚖️ واحد',
            'capacity': '👥 ظرفیت',
            'students': '🎒 دانشجویان',
            'schedule': '🕒 زمان'
        }
        
        for col in columns:
            tree.heading(col, text=headings[col])
            tree.column(col, width=120)
        
        for course_code, course in self.system.courses.items():
            tree.insert('', 'end', values=(
                course_code,
                course["name"],
                course["professor"],
                course["department"],
                course["units"],
                course["capacity"],
                f"🎒 {course['current_students']}",
                course["schedule"]
            ))
        
        tree.pack(fill='both', expand=True)
    
    def show_manage_students(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # هدر بخش
        section_header = tk.Frame(self.main_content, bg=self.colors['accent'], height=60)
        section_header.pack(fill='x', pady=(0, 20))
        
        tk.Label(section_header, text="👥 مدیریت دانشجویان", 
                font=self.fonts['header'], fg='white', bg=self.colors['accent']).pack(pady=15)
        
        if not self.system.students:
            empty_frame = tk.Frame(self.main_content, bg=self.colors['background'])
            empty_frame.pack(expand=True, fill='both')
            
            tk.Label(empty_frame, text="📭 هیچ دانشجویی ثبت‌نام نکرده است", 
                    font=self.fonts['header'], bg=self.colors['background'],
                    fg=self.colors['secondary']).pack(expand=True)
            return
        
        # جدول دانشجویان
        table_frame = tk.Frame(self.main_content, bg='white')
        table_frame.pack(expand=True, fill='both', pady=10)
        
        columns = ('student_id', 'name', 'email', 'major', 'entry_year', 'courses_count', 'total_units')
        tree = ttk.Treeview(table_frame, columns=columns, show='headings', 
                           style='Custom.Treeview', height=15)
        
        headings = {
            'student_id': '🔢 شماره دانشجویی',
            'name': '👤 نام و نام خانوادگی',
            'email': '📧 ایمیل',
            'major': '🎓 رشته',
            'entry_year': '📅 سال ورود',
            'courses_count': '📚 تعداد دروس',
            'total_units': '⚖️ مجموع واحدها'
        }
        
        for col in columns:
            tree.heading(col, text=headings[col])
            tree.column(col, width=120)
        
        for student_id, student in self.system.students.items():
            tree.insert('', 'end', values=(
                student_id,
                student["name"],
                student.get("email", "-"),
                student["major"],
                student["entry_year"],
                len(student["courses"]),
                student["total_units"]
            ))
        
        tree.pack(fill='both', expand=True)
    
    def logout(self):
        self.current_user = None
        self.current_user_type = None
        self.show_welcome_page()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernUniversityApp(root)
    root.mainloop()