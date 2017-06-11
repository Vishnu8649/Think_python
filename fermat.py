#
#Program to verify fermat theorem --> a^n + b^n != c^n for n>2
#

def power_n(x,n):
	return int(x**n)

def check_fermat(a,b,c,n):
	x=power_n(a,n)
	y=power_n(b,n)
 	z=power_n(c,n)
	if n>2 :
		if z==x+y:
			print 'Holy smokes, Fermat was wrong'
		else :
			print 'No, that does not work'
	else :
		print 'The conditions for fermat deosnt satisfy'

m= raw_input("Enter the first number")
n= raw_input("enter the second number")
o= raw_input("Enter the third number")
k= raw_input("Enter which power is to be checked")

check_fermat(int(m),int(n),int(o),int(k))
