str1=input("Введіть перший рядок: ")
str2=input("Введіть другий рядок: ")

set1=set(str1)
set2=set(str2)
common= set1&set2
unique=set1 -set2

print("Спільні символи: ", common)
print("Символи, яких немає у другому: ", unique)