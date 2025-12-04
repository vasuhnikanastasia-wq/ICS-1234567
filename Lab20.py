import sqlite3 
import tkinter as tk
from tkinter import messagebox, Listbox
import matplotlib.pyplot as plt

conn=sqlite3.connect("vasiukhnyk.db")
cur=conn.cursor()

def show_all():
    Listbox.delete(0, tk.END)
    cur.execute("SELECT* FROM storms")
    rows=cur.fetchall()
    for r in rows:
        Listbox.insert(tk.END, f"День {r[0]} - індекс {r[1]}")

def count_high():
    cur.execute("SELECT COUNT(*) FROM storms WHERE index_value  >3")
    result=cur.fetchone()[0]
    messagebox.showinfo("Результат", f"Кількість днів з індексом >3: {result}")

def show_plot():
    cur.execute("SELECT day, index_value FROM storms")
    data=cur.fetchall()

    days=[d[0] for d in data]
    values=[d[1] for d in data]

    plt.plot(days, values)
    plt.xlabel("День")
    plt.ylabel("Індекс бурі")
    plt.title("Індекс магніних бурь за жовтень 2025")
    plt.grid(True)
    plt.show()

root=tk.Tk()
root.title("Магнітні бурі - жовтень 2025")
root.configure(bg="#d8e4ff")

Listbox=Listbox(root, width=40, height=15)
Listbox.pack(pady=10)

btn_show=tk.Button(root, text="Показати всі записи", command=show_all)
btn_show.pack()

btn_count=tk.Button(root, text="Порахувати дні з індексом >3", command=count_high)
btn_count.pack()

btn_plot=tk.Button(root, text="Побудувати графік", command=show_plot)
btn_plot.pack()

root.mainloop()