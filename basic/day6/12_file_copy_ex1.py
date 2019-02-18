# coding: utf-8
'''
文件拷贝
'''
tmp = []


'''
方法一
with open('notex.md','r',encoding='utf-8') as f1:
	for line in f1:
		tmp.append(line)

with open('notex_copy.md','w',encoding='utf-8') as f2:
	f2.writelines(tmp)
'''

with open('notex.md','r',encoding='utf-8') as f1:
	with open('notex2.md','w',encoding='utf-8') as f2:
		for line in f1:
			f2.writelines(line)