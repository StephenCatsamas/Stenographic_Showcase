import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math


#in file
fpi = 'out.png'


msg = list()
terminal = "\0"

#read image
cimg = mpimg.imread(fpi)

#convert colourspace
omtrx = cimg*256

omtrx = omtrx.astype(int)


brk = False

#read data
for i in range(cimg.shape[0]):
    for j in range(cimg.shape[1]):
        try:
          if (omtrx[i,j,0] != 0):
              msg.append(chr(omtrx[i,j,0]))
          else:
              brk = True
              break
        except:
            pass
    if brk:
        break
 
#print message 
msg = ''.join(msg)
print(msg)


