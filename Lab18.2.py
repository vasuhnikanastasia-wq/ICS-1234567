import matplotlib.pyplot as plt

filename=input("Введіть ім'я файлу: ")
keys=[]
values=[]
file=open(filename, "r", encoding="utf-8")

for line in file:
    line=line.strip()
    if line == "":
        continue
    parts=line.split(":")
    key=parts[0].strip()
    value=float(parts[1].strip())

    keys.append(key)
    values.append(value)
file.close()

plt.bar(keys, values)
plt.title("Гістограма цін продутів")
plt.xlabel("Продукт")
plt.ylabel("Ціна")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()