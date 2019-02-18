f = open('notex.md','r',encoding='utf-8')
position1 = f.tell()
print(position1)
p = f.read(5)
print(p)
position2 = f.tell()
print(position2)

f.close()