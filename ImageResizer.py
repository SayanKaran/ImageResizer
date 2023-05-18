import cv2
source = "abc.jpg" #Enter your imagefile name with extension
des="Nabc.png"     #Enter your new imagefile name with extension

s_per=int(input("Enter Scale Percent(<100-->Small_Image_Size, >100-->Big_Image_Size): "))
src=cv2.imread(source,cv2.IMREAD_UNCHANGED)
n_width=int(src.shape[1]*s_per/100)
n_height=int(src.shape[0]*s_per/100)
output=cv2.resize(src,(n_width,n_height))
cv2.imwrite(des,output)
cv2.waitKey(0)