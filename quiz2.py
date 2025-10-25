#سوال 1 قسمت اول
guest_list = ['sara', 'farhad', 'mohammad']

unable_to_come = 'mohammad'
print(f"{unable_to_come} نمی‌تواند بیاید.")

guest_list[2] = 'ali'

print("لیست جدید مهمان‌ها:")
print(guest_list[0])
print(guest_list[1])
print(guest_list[2])



#سوال 1 قسمت 2
guest_list = ['sara', 'farhad', 'ali']

print("خبر خوب! میز بزرگ‌تری پیدا کرده‌ایم.")

guest_list.insert(0, 'nima')
guest_list.insert(2, 'maryam')
guest_list.append('reza')

print("لیست جدید مهمان‌ها:")
print(guest_list[0])
print(guest_list[1])
print(guest_list[2])
print(guest_list[3])
print(guest_list[4])
print(guest_list[5])

print("متأسفانه میز جدید به موقع نمی‌رسد و فقط می‌توانیم دو نفر دعوت کنیم.")

removed_guest = guest_list.pop()
print(f"{removed_guest}، متأسفیم که نمی‌توانیم شما را دعوت کنیم.")
removed_guest = guest_list.pop()
print(f"{removed_guest}، متأسفیم که نمی‌توانیم شما را دعوت کنیم.")
removed_guest = guest_list.pop()
print(f"{removed_guest}، متأسفیم که نمی‌توانیم شما را دعوت کنیم.")
removed_guest = guest_list.pop()
print(f"{removed_guest}، متأسفیم که نمی‌توانیم شما را دعوت کنیم.")

print("دو مهمان باقی‌مانده برای شام:")
print(guest_list[0])
print(guest_list[1])


#سوال 1 قسمت سوم
guest_list = ['sara', 'farhad', 'ali']

print(f"تعداد مهمان‌ها: {len(guest_list)}")

guest_list.sort()

print(f"{guest_list[0]} همچنان دعوت است.")
print(f"{guest_list[1]} همچنان دعوت است.")
print(f"{guest_list[2]} همچنان دعوت است.")

del guest_list[2]
del guest_list[1]
del guest_list[0]

print(guest_list)


#سوال 2 قسمت اول
people = {}

national_id = input("کد ملی را وارد کنید: ")
first_name = input("نام: ")
last_name = input("نام خانوادگی: ")
age = int(input("سن: "))
birth_city = input("شهر محل تولد: ")
living_city = input("شهر محل زندگی: ")

info = []
info.append(first_name)
info.append(last_name)
info.append(age)
info.append(birth_city)
info.append(living_city)

people[national_id] = info

print("اطلاعات ثبت شد:")
print(people)


#سوال 2 قسمت دوم
people = {
    '2951': ['mohammad', 'mohammadi', 25, 'urmia', 'tehran'],
    '2952': ['sara', 'bagheri', 30, 'tabriz', 'isfahan'],
    '2953': ['amir', 'rezaei', 35, 'tehran', 'shiraz']
}

search_id = input("کد ملی برای جستجو: ")
found_person = people.get(search_id, ["", "", "", "", ""])
print("فرد یافت شد." * (found_person[0] != "") + "فردی با این کد ملی موجود نیست." * (found_person[0] == ""))

move_id = input("کد ملی فرد برای تغییر شهر محل زندگی: ")
new_city = input("شهر جدید محل زندگی: ")
person_move = people.get(move_id, ["", "", "", "", ""])
person_move[4] = new_city
people[move_id] = person_move
print("شهر محل زندگی به‌روزرسانی شد")

change_id = input("کد ملی فرد برای تغییر نام یا نام خانوادگی: ")
new_first = input("نام جدید: ")
new_last = input("نام خانوادگی جدید: ")
person_change = people.get(change_id, ["", "", "", "", ""])
person_change[0] = new_first or person_change[0]
person_change[1] = new_last or person_change[1]
people[change_id] = person_change
print("نام و نام خانوادگی به‌روزرسانی شد")

delete_id = input("کد ملی فرد برای حذف: ")
removed_person = people.pop(delete_id, ["", "", "", "", ""])
print("فرد حذف شد" * (removed_person[0] != ""))

print_id = input("کد ملی فرد برای نمایش اطلاعات: ")
person_print = people.get(print_id, ["-", "-", "-", "-", "-"])
print(f"name : {person_print[0]}    last name : {person_print[1]}    age : {person_print[2]}    birth city : {person_print[3]}    lives in : {person_print[4]}")

