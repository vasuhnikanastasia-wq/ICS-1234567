import matplotlib.pyplot as plt
a=-3
b=9
h=0.1

x=[]
y=[]

t=a
while t <= b:
    value= 0.5*t+0.1*(t**4)
    x.append(t)
    y.append(value)
    t+=h

plt.plot(x, y, '--k')
plt.title("Графік функції y=0.5x+0.1x^4")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.savefig("gr_file.tiff")
plt.show()