import cv2

image = cv2.imread(r"C:\Users\dmags\OneDrive\Desktop\new\Indian-Railways-770x433.webp")
#print(image)
Gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny1 = cv2.Canny(Gray,100,170)
canny2 = cv2.Canny(Gray,200,170)

cv2.imshow("p",canny1)
cv2.imshow("d",canny2)
cv2.waitKgit addey(0)        
