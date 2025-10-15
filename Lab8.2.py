import random
M=int(input("Введіть кількість слів(M): "))
N=int(input("Введіть кількість символів у кожному слові(N): "))

alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
words=[]

for i in range(M):
    word =" "
    for j in range(N):
        letter=random.choice(alphabet)
        word +=letter
    words.append(word)

result=" ".join(words)

print("Згенеровані слова: ")
print(result)
