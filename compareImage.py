import cv2 
import numpy as np

orig = cv2.imread("./component1.jpg")
dup = cv2.imread("./component2.jpg")

##cv2.imshow("original", orig)
##cv2.imshow("duplicate", dup)

print(orig.shape) # gives the resolution
print(dup.shape) # gives the resolution
#3channel bcoz RBG, color image . If grayscale image then it is 2 channel
#count = 0 # see how many 'b' pixels are there

# 1) Check if same size(resolution) and same channel
if(orig.shape == dup.shape):
    print("same size and same channel")
    difference = cv2.subtract(orig,dup) #difference is an array
    print(difference.size) # difference number which is number of pixels
    ##cv2.imshow("Subtract", difference) # if result is 0 then displays black window as there is no deifference in pixels.
    #channel difference
    b,g,r = cv2.split(difference)
    print(b.size, g.size, r.size) # sum of b,g,r pixels is equal to difference.size
    #print(b,g,r) #is an array
    #show those b,g,r seperately
    ##cv2.imshow("b",b)
    ##cv2.imshow("g",b)
    ##cv2.imshow("r",b)
    #count pixel for each b,g,r
    #for x in b:#b or g or r
    #    for y in x:
    #        if(y != 0 ):
    #            count  += 1
    #simple count pixel for each b,g,r is to use the cv2.countNonZero(param)
    print("blue pixels : ", cv2.countNonZero(b))#b,g,r
    print("green pixels : ", cv2.countNonZero(g)) 
    print("red pixels : ",cv2.countNonZero(r))

    #check if the they are exactly same or not
    if((cv2.countNonZero(b) == 0) and (cv2.countNonZero(g) == 0) and (cv2.countNonZero(r) == 0)):
        print("Images are same")
    else:
        print("Images are not same")

    #For calculating %age of how different the images are, use below. ensure difference is not '0'
    print(str(((cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / difference.size) * 100) + "%")

#print(count) #for b

#cv2.waitKey(0)
#cv2.destroyAllWindows()