def bigger(a,b):
	if(a>b):
		return a
	else :
		return b
def biggest(a,b,c):
    return bigger(a,bigger(b,c))
def median(a,b,c):
	x = biggest(a,b,c)
	if x==a:
		return bigger(b,c)
	else:
	 if x==b:
		return bigger(a,c)
	 else :
	    return bigger(a,b) 
print median(8,10,5)
