def compare(x,y):
	if x>y:
		return 1
	elif x==y:
		return 0
	else :
		return -1
a=raw_input('Enter the first element')
b=raw_input('Enter the second element')
c=compare(a,b)
print 'Returns' 
print c

