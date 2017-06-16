def gcd(x,y):
	if x!=0 and y!=0:
		if x>y:
			r=x%y
			return gcd(y,r)
		elif x<y:
			r=y%x
			return gcd(x,r)
		else:
			return int(x)
	elif x==0:
		return y
	else:
		return x
a= raw_input("enter first element")
b= raw_input("enter second element")
d=gcd(int(a),int(b))
print "gcd = ",d
