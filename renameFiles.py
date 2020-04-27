
import os 
import os.path
rootdir = "C:\\Users\\IronMan\\Desktop\\launch\\"
files = os.listdir(rootdir)
b=0  
for name in files:
  a=os.path.splitext(name)
  print a[0]# 字符串
  newname = str(b)+'.jpg'
  b = b + 1
  os.rename(rootdir+name,rootdir+newname)