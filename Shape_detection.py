import cv2 as cv

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

img = cv.imread('test.jpg')
img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)

img_original = cv.imread('test.jpg')
img_original = cv.resize(img_original, (0, 0), fx=0.5, fy=0.5)

img_gray = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
img_gray = cv.resize(img_gray, (0, 0), fx=0.5, fy=0.5)

canny = cv.Canny(img_gray, 50, 175)

contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(img, contours, -1, (255, 0, 0), 2)

for contour in contours:
    epsilon = 0.02 * cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)
    shape = identify_shape(approx)
   
    M = cv.moments(contour)
    if M['m00'] != 0:
        cX = int(M['m10'] / M['m00'])  
        cY = int(M['m01'] / M['m00'])  
        cv.putText(img, shape, (cX - 20, cY + 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

cv.imshow('Original', img_original)
cv.imshow('Detected_Shapes', img)

cv.imwrite('new shape_detection.png',img)

cv.waitKey(0)
cv.destroyAllWindows()
