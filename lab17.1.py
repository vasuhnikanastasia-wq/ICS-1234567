import tkinter as tk
def check():
    word=ent_word.get()
    word2=word[:: -1]
    if word == word2:
        ibl_result["text"]="Це паліндром"
    else:
        ibl_result["text"]="Це НЕ паліндром"

win=tk.Tk()
win.title("Перевірка паліндрому")

ibl=tk.Label(text="Введіть слово: ")
ibl.pack()

ent_word=tk.Entry()
ent_word.pack()

btn=tk.Button(text="Перевірити", command=check)
btn.pack()

ibl_result=tk.Label(text="")
ibl_result.pack()

win.mainloop()