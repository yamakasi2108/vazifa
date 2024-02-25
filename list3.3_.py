import os
os.system("cls")

# Input massiv
input_array = [7, 8, 1, 3, 4, 6, 7, 5]

# Nusxa olish
copied_array = input_array[:]

# Juft indexdagilarni 2 chi darajaga ko'tarish
for i in range(0, len(copied_array), 2):
    copied_array[i] = copied_array[i] ** 2

# Toq indexdagilarni kubga ko'tarish
for i in range(1, len(copied_array), 2):
    copied_array[i] = copied_array[i] ** 3

# Natijani chiqarish
print("Input:", input_array)
print("Output:", copied_array)
