# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

i = int(input('Введите число: ')) 

def sequence(i):

    return[round((1 + 1 / n) ** n, 3) for n in range (1, i + 1)]   
        
print(sequence(i))
print(round(sum(sequence(i)), 3))