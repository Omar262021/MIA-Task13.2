MIA-Task13.2

In this task, the requirement is to detect shapes and their colors.

I will explain the steps I followed to complete the first requirement:

1. I used imread to read the image.

2. I used resize to make the image smaller.

3. Then, I converted the image to grayscale to make edge detection easier.

4. I used the Canny method to detect edges.

5. I used contours to detect and draw the shapes.

6. I created a function that detects the shape based on the number of contour points.

7. Finally, I added text to label the shapes and displayed the new image.

Color Detection

1-i took the contour of every shape and extracted the hsv values in it

2-i made a histogram of all the hues inside the contour

3-i took the most dominent hue and compared it to definte values for Red,Blue.Green and Yellow
