a = ("cropy",12,"python")
print(a[1])
new_a = a[0:2]
reversed_a = a[-1::-1]   #a[::-1] 
print(new_a)
print(reversed_a)

# 解组操作
username,age,hobby = a
print(username)
print(age)
print(hobby)

# index
b = a.index("python")
# count
c = a.count(12)
print(b,c)