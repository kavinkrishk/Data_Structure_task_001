# EX : 01

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

a = zip(first_list,second_list)
a1 = set (a)
print(a1)
print(type(a1))
print("@--------------------------------@")

#EX:02
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
inter = first_set.intersection(second_set)
print(inter)
for i in inter:
    first_set.remove(i)
    second_set.remove(i)
print(first_set)
print(second_set)

print("@--------------------------------@")
