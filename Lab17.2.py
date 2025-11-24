import tkinter as tk
def calculate():
    m=float(ent_m.get())
    h=float(ent_h.get())
    v=float(ent_v.get())

    result= ""
    if var_p.get()== 1:
        Ep=m*9.8*h
        result+= f"Потенціальна: {Ep}\n"

    if var_k.get()==1:
        Ek=(m*v*v)/2
        result+= f"Кінетична: {Ek}"

    ibl_res["text"]=result

win=tk.Tk()
win.title("Energy")

tk.Label(text="m (маса):").grid(row=0, column=0)
ent_m=tk.Entry()
ent_m.grid(row=0, column=1)

tk.Label(text="h (висота):").grid(row=1, column=0)
ent_h=tk.Entry()
ent_h.grid(row=1, column=1)

tk.Label(text="v (швидкість): ").grid(row=2, column=0)
ent_v=tk.Entry()
ent_v.grid(row=2, column=1)

var_p=tk.IntVar()
var_k=tk.IntVar()

chk_p=tk.Checkbutton(text="Потенціальна енергія", variable=var_p)
chk_k=tk.Checkbutton(text="Кінетична енергія", variable=var_k)

chk_p.grid(row=3, column=0, sticky="w")
chk_k.grid(row=4, column=0, sticky="w")

btn=tk.Button(text="Обчислити", command=calculate)
btn.grid(row=5, column=0)

ibl_res=tk.Label(text="")
ibl_res.grid(row=6, column=0, columnspan=2)

win.mainloop()