S=input("Введіть рядок слів, розділених комами або пробілами: ")
S=S.replace(",", " ")
words = S.split()

if not words:
    print("Рядок порожній.")
else: 
    Lengths=[len(word) for word in words]

min_len =min(Lengths)
max_len =max(Lengths)

print("Довжина найменшого слова: ", min_len)
print("Довжина найбільшого слова: ", max_len)