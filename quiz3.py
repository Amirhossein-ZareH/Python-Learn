#سوال 1

username = "admin"
password = "1234"

user_input = input("نام کاربری را وارد کنید: ")
pass_input = input("رمز عبور را وارد کنید: ")

if user_input == username and pass_input == password:
    print("خوش آمدید")
elif user_input == username and pass_input != password:
    print("رمز اشتباه است")
else:
    print("شما ثبت‌نام نکرده‌اید")


#سوال 2

products = {
    "laptop": 20000,
    "phone": 10000,
    "mouse": 200
}

product_name = input("نام محصول را وارد کنید: ")
money = int(input("مقدار پول خود را وارد کنید: "))

if product_name in products:
    if money >= products[product_name]:
        print("خرید موفق")
    else:
        print("موجودی ناکافی")
else:
    print("محصول یافت نشد")