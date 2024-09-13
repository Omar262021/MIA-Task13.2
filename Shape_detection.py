import cv2 as cv
import numpy as np

def identify_shape(approx):
    if len(approx) == 3:
        return 'Triangle'
    elif len(approx) == 4:
        _, _, w, h = cv.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            return 'Square'
        else:
            return 'Rectangle'
    else:
        return 'Circle'
    
def get_color(hsv, contour):
    mask = np.zeros(hsv.shape[:2], dtype="uint8")
    cv.drawContours(mask, [contour], 0, 255, 0)
    masked_hsv = cv.bitwise_and(hsv, hsv, mask=mask)
    hist = cv.calcHist([masked_hsv], [0], mask, [180], [0, 180])
    dominant_hue = np.argmax(hist)
    if 0 <= dominant_hue <= 10 or 160 <= dominant_hue <= 180:
        return 'Red'
    elif 20 <= dominant_hue <= 30:
        return 'Yellow'
    elif 35 <= dominant_hue <= 85:
        return 'Green'
    elif 85 <= dominant_hue <= 125:
        return 'Blue'

img = cv.imread('test.jpg')
img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)

img_original = cv.imread('test.jpg')
img_original = cv.resize(img_original, (0, 0), fx=0.5, fy=0.5)

img_gray = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
img_gray = cv.resize(img_gray, (0, 0), fx=0.5, fy=0.5)

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


canny = cv.Canny(img_gray, 50, 175)

contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(img, contours, -1, (255, 0, 0), 2) 

for contour in contours:
    epsilon = 0.02 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)
    shape = identify_shape(approx)
    color = get_color(img_hsv, contour)
   
    M = cv.moments(contour)
    if M['m00'] != 0:
        cX = int(M['m10'] / M['m00'])  
        cY = int(M['m01'] / M['m00'])  
        cv.putText(img, f'{shape}, {color}', (cX - 20, cY + 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

cv.imshow('Original', img_original)
cv.imshow('Detected_Shapes', img)
cv.imwrite('new_shape_color_detection.png', img)

cv.waitKey(0)
cv.destroyAllWindows()
