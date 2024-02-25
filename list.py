import os
os.system("cls")

ls = []
n = int(input("Royxat uzunligini kiriting: "))
for i in range(n):
    tup_int = tuple(map(int, input(f"{i + 1} Tuple malumotlarini proberl b/n kiriting yani(1 2 3)").split()))
    ls.append(tup_int)
output = [sum(t) for t in ls]
print(output)