sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

c1 = sample_list[:3]
c2 = sample_list[3:6]
c3 = sample_list[6:]

for num in sample_list:
    if num%2==0:
        print(num)

print(c1)
print(c2)
print(c3)

print("@-------------@")


