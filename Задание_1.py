from random import randint
 
n = int(input("Введите количество чисел в массиве для сортировки: "))
mas = [randint(0,100) for i in range(n)]
print(f"Неотсортированный массив - {mas}")
for i in range (n-1) :
    for j in range(n-1):
        if mas[j] > mas[j+1]:
            mas[j],mas[j+1] = mas[j+1],mas[j]
print(f"Отсортированный массив - {mas}")

