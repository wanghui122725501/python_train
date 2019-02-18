# coding: utf-8

tmp = []

with open('test.html','r',encoding='utf-8') as f1:
	is_extra = False
	for line in f1:
		if line.startswith('<script type="text/javascript">'):
			is_extra = True
		elif line.startswith('</script>'):
			is_extra = False
		else:
			if not is_extra:
				tmp.append(line)

print(tmp)

with open('test.html','w',encoding='utf-8') as f2:
	f2.writelines(tmp)