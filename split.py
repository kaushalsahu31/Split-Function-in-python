def split(string,value=' '):
	st=''
	i=0
	splits=[]
	while i<len(string):
		val=string[i:i+len(value)]
		if val==value:
			if st!='':
				splits.append(st)
			st=''
			i+=len(value)
		else:
			st+=string[i]
			i+=1
	if st!='':
		splits.append(st)
	return(splits)



string=input('split element\n')
value = input('value to be split\n')


print(split(string,value))
