import random
# Create random list of integers using while loop --------------------
random_list = []
list_length = 20
while len(random_list) < list_length:
  random_list.append(random.randint(0,10))
print random_list  
# --------------------------------------------------------------------
count_list = []
e = 0
while e < 11:
 i = 0 
 count = 0
 while i< len(random_list) :
    if random_list[i]==e:
        count+=1
    i += 1
 count_list.append(count)
 e = e+1
# Write code here to loop through every number in random_list and
# update count_list appropriately
print 'numbers'+'  |  '+'occurrence'
i=0
while i<10:
 print ' '*(len('numbers')-1)+ str(i)+' '*2+'|'+' '*2+str(count_list[i])
 i = i+1
print ' '*(len('numbers')-2)+ str(10)+' '*2+'|'+' '*2+str(count_list[10])

#print count_list
#print sum(count_list)
