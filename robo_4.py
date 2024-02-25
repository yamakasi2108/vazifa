import os
os.system("cls")
input_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

zeros = [x for x in input_list if x == 0]

for zero in zeros:
    input_list.remove(zero)

input_list.extend(zeros)

print("Input:", input_list)
