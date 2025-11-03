import pickle

f=open("numbers4.dat", "rb")
data=pickle.load(f)
f.close()

print("Дані з файлу:")
print(data)