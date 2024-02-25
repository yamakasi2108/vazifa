import os
os.system("cls")







# dct = {1: 100, 2: 220}
# if 200 in dct.values():
#     print("bor")
# else:
#     print("yoq")



# seample_set = {'Yellow', 'Orange', 'black'}
# seample_list = ['blue', 'grren', 'red']
# ax = set(seample_list)
# seample_set.update(ax)
# print(seample_set)


# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# # 80 ni chiqarish
# print(sampleDict["class"]["student"]["marks"]["history"])


# input_dict = {1: 10, 2: 20, 3: 30, 4: 15, 5: 25}
# min_value = min(input_dict, key=input_dict.get)
# del input_dict[min_value]
# print(input_dict)


# input_dict = {'data1': 100, 'data2': -54, 'data3': 247}

# total_sum = sum(input_dict.values())

# print(total_sum)

        


# ll_tup = [(1,2),(2,3),(4,5)]
# out_put = [sum(t) for t in ll_tup]
# print(out_put)

# list1 = ['salom', 123, True, 'Hayr', 'world', 3.14, '7214']

# TEXT = []
# OTHER = []

# for i in list1:
#     if isinstance(i, str):
#         TEXT.append(i)
#     else:
#         OTHER.append(i)
# TEXT.sort()
# OTHER.sort(reverse=True)
# print(TEXT)
# print(OTHER)



# a, b = 10, 20
# ls = []
# for i in range(a,b, 1):
#     if i % 2 != 0:
#        ls.append(i)
# ls.reverse()
# print(ls)

# ls = [7,8,1,3,4,6,7,5]
# ls1 = ls[:]
# for i in range(0, len(ls1), 2):
#     ls1[i] = ls1[i] ** 2
# for i in range(1, len(ls1), 2):
#     ls1[i] = ls1[i] ** 3
# print(ls)
# print(ls1)