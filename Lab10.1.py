CA=(10, 3.5, "hello", "S", 2, 1.7, 'text', 4.0, 9)
sum_floats=0
for elem in CA:
    if type(elem) ==float:
        sum_floats +=elem

print("Сума всіх дійсних елементів кортежу:", sum_floats)