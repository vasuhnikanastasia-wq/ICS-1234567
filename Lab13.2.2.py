import json
with open("liquids.json", "r") as read_file:
    data=json.load(read_file)

min1_name=""
min2_name=""
min1_value=999999
min2_value=999999

for name in data:
    dens=data[name]
    if dens<min1_value:
        min2_value=min1_value
        min2_name=min1_name
        min1_value=dens
        min1_name=name
    elif dens<min2_value:
        min2_value=dens
        min2_name=name

m1=min1_value*3.7
m2=min2_value*3.7

print("Дві рідини з найменшою густиною: \n")
print(min1_name, "-", m1, "кг")
print(min2_name, "-", m2, "кг")
