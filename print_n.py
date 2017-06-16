def print_n(s,n):
	while n!=0:
		print s
		n=n-1
s=raw_input("enter a string ")
n=raw_input("how many times to be printed ")
print_n(str(s),int(n))
