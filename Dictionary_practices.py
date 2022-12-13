# Practice for interview mode

print("dict Comprehension")

dict0 = {i : i**2 for i in range(6)}
print(dict0)
print("Dict 2 value is:",dict0[2])

print("@-------------------------------@")

dict2 = {i:i*i for i in range(10) if i%2!=0}
print(dict2)

print("@-------------------------------@")

k = {1:"parrot",2:"chicken",3:"duck"}

dict3 = {i : k for i in range(len(k))}
print(dict3)
print(type(k))
l = {0: {1: 'parrot', 2: 'chicken', 3: 'duck'},
     1: {"a": 'parrot', "b": 'chicken', "c": 'duck'},
     2: {"A": 'parrot', "B": 'chicken', "C": 'duck'}}

print("----------------------------------")

# Fetch the value from the dict using list Comprehension
roll_number = [47, 64, 69, 37, 76, 83, 95, 97,'Jhon','Kelly']
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

roll_number = [i for i  in roll_number if i in sample_dict.keys()]
print(roll_number)
print(type(roll_number))

print("----------------------------------")

# fetch the not repeat value from the dict to get list

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
d = []
for i in speed.values():
     if i not in d:
          d.append(i)
print(d)

print("----------------------------------")

# take the unique value from the list to set
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
k = []
for i in sample_list:
     if i not in k:
          k.append(i)
     else:
          k.remove(i)
f = tuple(k)
print(type(f))
print(f)
print("min num is:",min(f),"max num is:",max(f))

print("----------------------------------")

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = {}

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)
print(type(res_dict))

print("----------------------------------")

#merge two python in one
dict1a = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2a = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3a = {**dict1a,**dict2a}
print(dict3a)
print("--------- other Method----------")

dict4a = dict1a.copy()
print(dict4a)
dict4a.update(dict2a)
print(dict4a)
print("----------------------------------")


sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["physics"])
print(sampleDict["class"]["student"]["name"])
print("----------------------------------")

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

df_keys = dict.fromkeys(employees,defaults)
print(df_keys)
print(df_keys["Kelly"]["salary"])
print("----------------------------------")
lt1 = [{"Name": "harish", "Age":25},{"Name": "Somesh", "Age":26}]
lt2 = [{"Name": "suresh", "Age":31},{"Name": "dinesh", "Age":39}]
k={'bucket 20-29': [{'Name': 'harish', 'Age': 25}, {'Name': 'Somesh', 'Age': 26}], 'bucket 30-39': [], 'bucket 40-49': [], 'bucket 50-59': [], 'bucket 60-69': []}
j = ['bucket 20-29']
k1=['bucket 30-39']

h = (dict.fromkeys(j,lt1))
v = (dict.fromkeys(k1,lt2))
g = h.copy()
print(g.update(v))
print(g)
print("----------------------------------")

sample_dict1 = {
    "name": "Kelly",
    "age": 29,
    "salary": 50000,
    "city": "New york"}

print(sample_dict1["name"],"is",sample_dict1["age"],"years old","and his Salary is",sample_dict1["salary"],"and the city is",sample_dict1["city"])

print("----------------------------------")

del(sample_dict1["city"])
print(sample_dict1)

print("----------------------------------")

sample_dict2 = {
    "name": "Kelly",
    "age": 29,
    "salary": 50000,
    "city": "New york"}
keys1 = ["name","salary"]

sample_dict2 = {i:sample_dict2[i] for i in sample_dict2.keys()-keys1}

print(sample_dict2)
rt = {}
for i in keys:
     rt.update()
        

