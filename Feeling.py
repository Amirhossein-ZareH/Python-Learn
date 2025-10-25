import tkinter as tk
from tkinter import scrolledtext
import json, os, random, threading, time, re

MEMORY_FILE = "memory.json"
TYPING_DELAY = 0.02

# -------- حافظه کاربر --------
def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"messages": []}
    return {"messages": []}

def save_memory(mem):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(mem, f, ensure_ascii=False, indent=2)

memory = load_memory()

# -------- مدل Markov ساده --------
def build_markov(messages, order=2):
    model = {}
    for msg in messages:
        tokens = ["__BOW__"] + msg.split() + ["__EOW__"]
        for i in range(len(tokens)-order):
            key = tuple(tokens[i:i+order])
            model.setdefault(key, []).append(tokens[i+order])
    return model

def markov_generate(model, order=2, max_words=20):
    if not model: return ""
    start_keys = [k for k in model.keys() if k[0]=="__BOW__"]
    key = random.choice(start_keys) if start_keys else random.choice(list(model.keys()))
    words = list(key)
    out=[]
    for _ in range(max_words):
        nxt = model.get(tuple(words[-order:]), None)
        if not nxt: break
        nxt = random.choice(nxt)
        if nxt=="__EOW__": break
        out.append(nxt)
        words.append(nxt)
    return " ".join(out)

# -------- تولید پاسخ --------
def generate_response(user_text):
    user_text = user_text.strip()
    
    # ذخیره پیام کاربر
    memory.setdefault("messages", []).append(user_text)
    if len(memory["messages"])>500:
        memory["messages"] = memory["messages"][-500:]
    save_memory(memory)
    
    # مدل Markov
    model = build_markov(memory.get("messages", []))
    reply = markov_generate(model)
    
    # fallback ساده اگر خالی بود
    if not reply:
        fallback = [
            "می‌تونی بیشتر توضیح بدی؟",
            "جالبه، ادامه بده.",
            "اوه، واقعاً؟"
        ]
        reply = random.choice(fallback)
    return reply

# -------- رابط گرافیکی --------
root = tk.Tk()
root.title("چت‌بات واقعی کوچک 😎")
root.geometry("600x650")
root.configure(bg="#121212")

title = tk.Label(root, text="چت‌بات واقعی کوچک", font=("Tahoma",18,"bold"), bg="#121212", fg="#FFD580")
title.pack(pady=10)

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Tahoma",13), bg="#1b1b1b", fg="#e6e6e6", padx=12, pady=12)
chat_box.pack(padx=12, pady=6, fill=tk.BOTH, expand=True)
chat_box.config(state=tk.DISABLED)

status_label = tk.Label(root, text="", font=("Tahoma",10), bg="#121212", fg="#a0a0a0")
status_label.pack(pady=(0,6))

entry_frame = tk.Frame(root, bg="#121212")
entry_frame.pack(fill=tk.X, padx=12, pady=6)

entry = tk.Text(entry_frame, height=4, font=("Tahoma",13), bg="#151515", fg="#f0f0f0", wrap=tk.WORD)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,8))
entry.focus()

send_btn = tk.Button(entry_frame, text="ارسال", width=12, bg="#FFD580", fg="#121212", font=("Tahoma",12,"bold"))
send_btn.pack(side=tk.RIGHT)

def insert_chat(speaker, text):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"{'تو' if speaker=='user' else 'بات'}: {text}\n\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

def bot_typing_reply(user_text):
    status_label.config(text="بات: در حال تایپ...")
    time.sleep(0.5 + random.random()*0.5)
    reply = generate_response(user_text)
    
    # افکت تایپ
    def type_out(text, idx=0):
        if idx < len(text):
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, text[idx])
            chat_box.config(state=tk.DISABLED)
            chat_box.yview(tk.END)
            root.after(int(TYPING_DELAY*1000), lambda: type_out(text, idx+1))
        else:
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, "\n\n")
            chat_box.config(state=tk.DISABLED)
            chat_box.yview(tk.END)
            status_label.config(text="")
    
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "بات: ")
    chat_box.config(state=tk.DISABLED)
    type_out(reply)

def send_message(event=None):
    user_text = entry.get("1.0", tk.END).strip()
    if not user_text: return
    entry.delete("1.0", tk.END)
    insert_chat("user", user_text)
    threading.Thread(target=bot_typing_reply, args=(user_text,), daemon=True).start()

send_btn.config(command=send_message)
entry.bind("<Control-Return>", lambda e: entry.insert(tk.END,"\n"))
entry.bind("<Return>", lambda e: (send_message(), "break"))

insert_chat("bot","سلام! هر چیزی که دوست داری بگو، باهات حرف می‌زنم 😎")

root.mainloop()
