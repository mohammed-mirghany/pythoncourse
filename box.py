def bar(n,ch='-'):
	return ch * n
def box(txt):
	print "+-" + bar(len(txt)) + "-+"
	print "| " +    txt        + " |"
	print "+-" + bar(len(txt)) + "-+"
box('Mohammed Mirghany')

