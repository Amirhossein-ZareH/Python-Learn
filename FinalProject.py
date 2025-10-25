import tkinter as tk
from tkinter import messagebox
import time
import threading

cards = [
    [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31],
    [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31],
    [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31],
    [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31],
    [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
]

current_card = 0
number = 0

root = tk.Tk()
root.title("جادوگر پایتونی")
root.geometry("720x480")
root.config(bg="#1e1e2e")

title_label = tk.Label(root, text="جادوگر پایتونی", fg="#ffcc00", bg="#1e1e2e", font=("B Titr", 20))
title_label.pack(pady=15)

info_label = tk.Label(root, text="یه عدد رو تو ذهنت انتخاب کن", fg="#ffffff", bg="#1e1e2e", font=("B Nazanin", 14))
info_label.pack(pady=10)

card_box = tk.Text(root, height=8, width=50, bg="#292942", fg="#ffffff", font=("Consolas", 12))
card_box.pack(pady=10)

result_label = tk.Label(root, text="", fg="#00ff88", bg="#1e1e2e", font=("B Nazanin", 16))
result_label.pack(pady=15)

def show_card():
    global current_card
    if current_card < len(cards):
        card_box.delete(1.0, tk.END)
        card_text = ", ".join(map(str, cards[current_card]))
        card_box.insert(tk.END, f"کارت شماره {current_card+1}\n\n{card_text}")
        result_label.config(text="")
    else:
        reveal_result()

def yes_answer():
    global number, current_card
    if current_card < len(cards):
        number += 2 ** current_card
        current_card += 1
        show_card()

def no_answer():
    global current_card
    if current_card < len(cards):
        current_card += 1
        show_card()

def reveal_result():
    card_box.delete(1.0, tk.END)
    result_label.config(text=f"بود {number} عدد تو ذهنت")
    messagebox.showinfo("حدس جادویی!", f"عددی که تو ذهن تو بود {number} بود")

btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=10)

yes_btn = tk.Button(btn_frame, text="✅ بله", command=yes_answer, width=10, font=("B Nazanin", 13), bg="#33cc66", fg="white")
yes_btn.grid(row=0, column=0, padx=15)

no_btn = tk.Button(btn_frame, text="❌ خیر", command=no_answer, width=10, font=("B Nazanin", 13), bg="#ff6666", fg="white")
no_btn.grid(row=0, column=1, padx=15)

show_card()

root.mainloop()