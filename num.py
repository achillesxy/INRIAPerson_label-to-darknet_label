import Image
import os
import re
import numpy as np
import cv2

print(os.getcwd())
os.chdir('/home/xy/Desktop/aaa')
a1=[]

try:
    data=open("/home/xy/darknet/annotations/crop001001.txt")
    for each_line in data:
        try:
            (role, line_spoken)=each_line.split(':', 1)
            line_spoken=line_spoken.strip()
            if role=='Bounding box for object 1 "PASperson" (Xmin, Ymin) - (Xmax, Ymax) ':
                a1.append(line_spoken)
            if role=='Bounding box for object 2 "PASperson" (Xmin, Ymin) - (Xmax, Ymax) ':
                a1.append(line_spoken)
            if role=='Bounding box for object 3 "PASperson" (Xmin, Ymin) - (Xmax, Ymax) ':
                a1.append(line_spoken)
            if role=='Bounding box for object 4 "PASperson" (Xmin, Ymin) - (Xmax, Ymax) ':
                a1.append(line_spoken)
            if role=='Bounding box for object 5 "PASperson" (Xmin, Ymin) - (Xmax, Ymax) ':
                a1.append(line_spoken)
        except ValueError:
                pass
    data.close()
except IOError:
    print('The datafile is missing!')
print (a1)
i=0
f = open("man.txt",'wb')

im = cv2.imread("/home/xy/darknet/pos/crop001001.png")
while (i < len(a1)):
    t=int(i)
    m = re.findall(r'(\w*[0-9]+)\w*',a1[t])
    x = (int(m[0])+int(m[2]))/2
    y = (int(m[1])+int(m[3]))/2
    w = int(m[2])-int(m[0])
    h = int(m[3])-int(m[1])
    rect = cv2.rectangle(im,(int(m[0]),int(m[1])),(int(m[2]),int(m[3])),(0,255,0),3)
    f.write("1"+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+"\n")
    i = i+1
cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

f.close()

im = Image.open("/home/xy/darknet/pos/crop001001.png")
size = im.size
truth_x = int(size[0])
truth_y = int(size[1])

txtpath="man.txt"
fp=open(txtpath)
arr=[]
for lines in fp.readlines():
    lines=lines.replace("\n","").split(" ")
    arr.append(lines)


j = 1
i = 0
os.remove("labels.txt")
while (i < len(arr)):
    if arr[i][0] :
        x = int(arr[i][1])*1.0/truth_x
        y = int(arr[i][2])*1.0/truth_y
        w = int(arr[i][3])*1.0/truth_x
        h = int(arr[i][4])*1.0/truth_y
        f = open("labels.txt",'ab')
        f.write("0"+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+"   "+str(i)+"\n")
        print("0"+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h))
        i = i + 1
    else:break

fp.close()
