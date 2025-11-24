import tkinter as tk
from tkinter import scrolledtext, messagebox
import math
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

history = []

# ذخیره تاریخچه در فایل CSV
def save_history_to_csv():
    try:
        with open("history.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Expression", "Result"])
            for record in history:
                expr, res = record.split(" = ")
                writer.writerow([expr, res])
        messagebox.showinfo("ذخیره شد", "تاریخچه در فایل history.csv ذخیره شد!")
    except Exception as e:
        messagebox.showerror("خطا", f"مشکل در ذخیره فایل:\n{e}")

def click(btn_text):
    if btn_text == "^":
        entry.insert(tk.END, "**")
    else:
        entry.insert(tk.END, btn_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    expr = entry.get()
    try:
        result = eval(expr, {"__builtins__":None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        history.append(f"{expr} = {result}")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def show_history():
    hist_win = tk.Toplevel(root)
    hist_win.title("تاریخچه محاسبات")
    hist_win.geometry("400x450")
    hist_win.config(bg="#2c3e50")
    
    tk.Label(hist_win, text="تاریخچه محاسبات:", font=("Arial",14,"bold"), bg="#2c3e50", fg="white").pack(pady=5)
    
    hist_text = scrolledtext.ScrolledText(hist_win, font=("Consolas",12), bg="#34495e", fg="white")
    hist_text.pack(expand=True, fill="both", padx=10, pady=5)
    hist_text.insert(tk.END, "\n".join(history))
    hist_text.config(state="disabled")

    save_btn = tk.Button(hist_win, text="ذخیره CSV", font=("Arial",12,"bold"), bg="#f39c12", fg="white", command=save_history_to_csv)
    save_btn.pack(pady=5)

def plot_function():
    func = entry.get()
    try:
        x = np.linspace(-10,10,400)
        y = [eval(func.replace("x",str(val)), {"__builtins__":None}, math.__dict__) for val in x]
        fig = Figure(figsize=(5,3), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(x, y, color='royalblue')
        ax.set_title(f"Graph: {func}")
        ax.grid(True)
        for widget in chart_frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# پنجره اصلی
root = tk.Tk()
root.title("ماشین حساب پیشرفته فوق حرفه‌ای")
root.geometry("520x650")
root.config(bg="#1abc9c")

entry = tk.Entry(root, font=("Arial",22), bd=5, relief="ridge")
entry.pack(fill=tk.BOTH, padx=15, pady=15)

chart_frame = tk.Frame(root, bg="#1abc9c")
chart_frame.pack(expand=True, fill="both", padx=10, pady=5)

# دکمه‌ها
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
    ['sin','cos','tan','sqrt'],
    ['log','exp','^','C'],
    ['Graph','History']
]

colors = {
    "num":"#ecf0f1",
    "op":"#2980b9",
    "eq":"#27ae60",
    "clear":"#c0392b",
    "hist":"#f1c40f",
    "graph":"#8e44ad"
}

def make_btn(frame, text, bg, cmd):
    b = tk.Button(frame, text=text, font=("Arial",16,"bold"), bg=bg, fg="white",
                command=cmd, bd=0, relief="raised", activebackground="#16a085", activeforeground="white")
    b.pack(side="left", expand=True, fill="both", padx=5, pady=5)
    # Hover effect
    b.bind("<Enter>", lambda e: b.config(bg="#16a085"))
    b.bind("<Leave>", lambda e: b.config(bg=bg))
    return b

for row in buttons:
    frame = tk.Frame(root, bg="#1abc9c")
    frame.pack(expand=True, fill="both", padx=10, pady=5)
    for btn_text in row:
        if btn_text == "=":
            make_btn(frame, btn_text, colors["eq"], calculate)
        elif btn_text == "C":
            make_btn(frame, btn_text, colors["clear"], clear)
        elif btn_text == "History":
            make_btn(frame, btn_text, colors["hist"], show_history)
        elif btn_text == "Graph":
            make_btn(frame, btn_text, colors["graph"], plot_function)
        elif btn_text in ['+','-','*','/','^','sin','cos','tan','sqrt','log','exp']:
            make_btn(frame, btn_text, colors["op"], lambda x=btn_text: click(x))
        else:
            make_btn(frame, btn_text, colors["num"], lambda x=btn_text: click(x))

root.mainloop()