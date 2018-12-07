import os
flist =  os.listdir(r"C:\Users\admin\Desktop\py\nn\alphabet")
os.getcwd()
for fname in flist:
	os.chdir(r"C:\Users\admin\Desktop\py\nn\alphabet")
	os.rename(fname,fname.translate(None,"0123456789"))
    
print flist