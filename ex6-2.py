import math
def hypotenuse(x,y):
	h1=x**2
	h2=y**2
	d=h1+h2
	hyp=math.sqrt(d)
	return hyp
a=raw_input('Enter first side length')
b=raw_input('Enter second side length')
hypotenuse(int(a),int(b))
