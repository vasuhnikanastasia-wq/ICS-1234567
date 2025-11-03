f=open("roman.txt", "r")
text=f.read()
f.close()
text=text.lower()
for ch in '. , ! ? ; : - " ()':
    text=text.replace(ch, "")

words=text.split()
freq={}
for word in words:
    if word in freq:
        freq[word] +=1
    else:
        freq[word] =1
print("Частота слів у тексті: ")
print(freq) 

unique_words=[]
for keys in freq:
    if freq[keys] ==1:
        unique_words.append(keys)
unique_words=tuple(unique_words)

print("\n Слова, які зустрічаються 1 раз: ")
print(unique_words)       