import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#in file
fpi = 'in.png'
#out file
fpo = 'out.png'

##message to be hidden
msg = "this is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source imagethis is a test message which is to be hidden in the source image"


#mesage terminator
terminal = "\0"

msg += terminal

#read image
cimg = mpimg.imread(fpi)



omtrx = cimg.astype(float)

#add stenograpgic data
for i in range(cimg.shape[0]):
    for j in range(cimg.shape[1]):
        try:
            omtrx[i,j,0] = (ord(msg[i*cimg.shape[0]+j]) +1 )/256
        except:
            pass

#print(omtrx)

#save output
plt.imsave(fpo, omtrx)
