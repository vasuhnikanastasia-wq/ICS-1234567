import numpy as np
N=int(input("Введіть розмір матриці N: "))

numbers=np.arange(1, N*N +1)
A=numbers.reshape(N, N)
print("Матриця:")
print(A)

sum_diag=0
for i in range(N):
    sum_diag +=A[i][N-1-i]
print("Сума допоміжної діагоналі:", sum_diag)

for i in range(N):
    max_in_row=max(A[i])
    print("Найбільше у рядку {i+1}= ", max_in_row)
