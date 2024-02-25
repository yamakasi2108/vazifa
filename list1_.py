import os
os.system("cls")

input_list_1 = []
n = int(input("Birinchi ro'yxat uzunligini kiriting: "))
for i in range(n):
    tuple_input = tuple(map(int, input(f"{i + 1}-chi tuple elementlarini vergul bilan kiriting: ").split(", ")))
    input_list_1.append(tuple_input)

output_list_1 = [sum(t) for t in input_list_1]
print("Output 1:", output_list_1)

input_list_2 = []
m = int(input("Ikkinchi ro'yxat uzunligini kiriting: "))
for i in range(m):
    tuple_input = tuple(map(int, input(f"{i + 1}-chi tuple elementlarini vergul bilan kiriting: ").split(", ")))
    input_list_2.append(tuple_input)

output_list_2 = [sum(t) for t in input_list_2]
print("Output 2:", output_list_2)

