
'''def add_sub():
    print("first number")
    first_num = float(input("first number:"))
    print("second number")
    sec_num = float(input("second number:"))
    add_result = first_num+sec_num
    sub_result = first_num-sec_num
    return([add_result,sub_result])
print(add_sub())

result =[]
for i in range(10):
    result.append(add_sub())
print(result)'''

res = [[5.0, -1.0], [9.0, -1.0], [11.0, -1.0], [13.0, -1.0], [15.0, -1.0], [17.0, -1.0], [19.0, -1.0], [21.0, -1.0], [23.0, -1.0], [25.0, -1.0]]

print(res[0][0])

new = []
for i in range(3):
    new.append(res)
print(new)

k = [[[5.0, -1.0], [9.0, -1.0], [11.0, -1.0], [13.0, -1.0], [15.0, -1.0], [17.0, -1.0], [19.0, -1.0], [21.0, -1.0], [23.0, -1.0], [25.0, -1.0]], [[5.0, -1.0], [9.0, -1.0], [11.0, -1.0], [13.0, -1.0], [15.0, -1.0], [17.0, -1.0], [19.0, -1.0], [21.0, -1.0], [23.0, -1.0], [25.0, -1.0]], [[5.0, -1.0], [9.0, -1.0], [11.0, -1.0], [13.0, -1.0], [15.0, -1.0], [17.0, -1.0], [19.0, -1.0], [21.0, -1.0], [23.0, -1.0], [25.0, -1.0]]]
print(k[0][5])

"""
for i,j in enumerate(res):
    print(i,j)""" 