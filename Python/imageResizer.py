import cv2

src="yuta.jpeg"
destination="newImage.png"
scale_percent=50

image = cv2.imread(src,cv2.IMREAD_UNCHANGED)

new_width=int(image.shape[1]*scale_percent/100)
new_height=int(image.shape[0]*scale_percent/100)

output=cv2.resize(image,(new_width,new_height))

cv2.imwrite(destination,output)
cv2.waitKey(0)
