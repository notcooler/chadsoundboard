import os

path ="./"
#we shall store all the file names in this list
filelist = []
nuts = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))

#print all the file names
for name in filelist:
    if(name.endswith(".mp3")):
    	a = name[2:]
    	b = a[:-4]
    	nuts.append(b)


msg = "[\""
for name in nuts:
	msg += name
	msg += "\", \""
msg = msg[:-3]
msg+="]"
print(msg)