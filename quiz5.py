def make_shirt():
    size = input("lotfan size tshirt ra vared konid (s, l, xl, xxl): ").lower()
    text = input("matni ke mikhahid roye tshirt chap beshe ra benevisid: ")

    if size == "s":
        price = 350000
    elif size == "l":
        price = 380000
    elif size == "xl":
        price = 400000
    elif size == "xxl":
        price = 420000
    else:
        print("andaze eshtebah hast!")
        return

    length = len(text)

    if 0 < length <= 5:
        extra = 30000
    elif 6 <= length <= 10:
        extra = 50000
    elif 11 <= length <= 30:
        extra = 100000
    elif 31 <= length <= 60:
        extra = 150000
    else:
        extra = 200000

    total_price = price + extra

    print(f"\ntshirt size {size.upper()} ba matn '{text}' amade ast.")
    print(f"gheymat nahayi: {total_price:,} toman")

make_shirt()