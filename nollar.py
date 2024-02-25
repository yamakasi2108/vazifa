import os
os.system("cls")

nollar = []
input_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
for i in input_list:
    if i == 0:
        nollar.append(i)
for nol in nollar:
    input_list.remove(nol)
input_list.extend(nollar)
print(input_list)