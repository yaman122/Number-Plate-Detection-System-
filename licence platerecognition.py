
import cv2
import imutils #to resize image
import pytesseract
import xlsxwriter

#pytesseract engine location
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
#reading the img
img =cv2.imread('car1.jpg')
#resizing and standardizing
img = imutils.resize(img,width=500)
cv2.imshow('original',img) #showing original image
cv2.waitKey(0)

#from rgb to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('grayscale',gray)  #showing grayscale image
cv2.waitKey(0)

#reducing noise and making it smooth
gray = cv2.bilateralFilter(gray,11,17,17)
cv2.imshow('smooth img',gray)
cv2.waitKey(0)

#finding edge

edged =  cv2.Canny(gray,170,200)
cv2.imshow('edge',edged)
cv2.waitKey(0)

#finding contours

cnts,new =cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

img1 =img.copy()
cv2.drawContours(img1,cnts,-1,(0,255,0),3)

cv2.imshow('contour',img1)
cv2.waitKey(0)

#sorting top 30 contours
cnts = sorted(cnts,key=cv2.contourArea,reverse=True)[:30]

img2 =img.copy()
cv2.drawContours(img2,cnts,-1,(0,255,0),3)
cv2.imshow('top 30 contours',img2)
cv2.waitKey(0)

#to find possibile number plate
count = 0
name =1
for i in cnts:
    perimeter = cv2.arcLength(i,True)
    approx = cv2.approxPolyDP(i,0.02*perimeter,True)
    if(len(approx)==4): #4 corners
        NumberPlateCount = approx
        x,y,w,h =cv2.boundingRect(i)
        crop = img[y:y+h,x:x+w]

        cv2.imwrite(str(name)+'.png',crop)
        name+=1
        break
cv2.drawContours(img,[NumberPlateCount],-1,(0,255,0),3)
cv2.imshow('final img',img)
cv2.waitKey(0)

#cropping the number plate

crop_img = '1.png'
cv2.imshow('cropped img',cv2.imread(crop_img))
cv2.waitKey(0)

#extracting the number


text = pytesseract.image_to_string(crop_img,lang='eng',config='--psm 6')
print('License Plate Number is :',text)

#adding the result to an excel sheet

outworkbook = xlsxwriter.Workbook('out.xlsx')
outsheet = outworkbook.add_worksheet()

outsheet.write('A1','NUM_PLATE')
outsheet.write('A2',text)
outworkbook.close()

cv2.waitKey(0)



