def rnoun():
	import random
	if random.randint(0,1)==1:
		return 'mohammed'
	else: 
		return 'ali'
def rverb():
	import random
	if random.randint(0,1)==1:
		return 'run'
	else:
		return 'read'
verb = rverb()
noun = rnoun()
def addvn(txt):
	x=len(txt)
	i = 0
	newtxt =''
	while i<x :
		if(txt[i:i+4]=='NOUN'):
			newtxt=newtxt+noun
			i=i+4
	   	else:
	   		if(txt[i:i+4]=='VERB'):
	   		  newtxt = newtxt+verb
	   		  i = i+4
	   	 	else:
	   		  newtxt=newtxt+txt[i]
	   		  i=i+1
	print  newtxt

addvn('NOUN VERB every day')
