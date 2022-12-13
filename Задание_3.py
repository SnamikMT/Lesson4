from random import randint
 
a = [ randint(0,10) for i in range(10)]
b = [randint(0,10) for i in range(10)]
print(f"Первый набор чисел {a}")
print(f"Второй набор чисел {b}")
result = list(set(a) & set(b))
print(f"Числа,входящие одновременно в оба набора {result}")
result1 = list(set(a) - set(b))
print(f"Числа,входящие только в первый набор {result1}")
result2 = list(set(b) - set(a))
print(f"Числа,входящие только в второй набор {result2}")
result3 = list(set(a) ^ set(b))
print(f"Уникальные числа,входящие в оба набора {result3}")