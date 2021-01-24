c,*d=0,
with open("./input","r") as a:
	b = a.readlines()
	while c < len(b):
		d.append(b[c][:-1])
		c+=1
	a.close()
for n1 in d:
	for n2 in d:
		for n3 in d:
			res = int(n1)+int(n2)+int(n3)
			if res ==2020:
				print(int(n1)*int(n2)*int(n3))