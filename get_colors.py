import cv2 as cv
import numpy as np


def get_limits(color):
    c = np.uint8 ([[color]])
    hsvC = cv.cvtColor(c,cv.COLOR_BGR2HSV)
    lower_limit = hsvC[0][0][0] - 10 , 100 , 100
    upper_limit = hsvC[0][0][0]+10 , 255 , 255
    lower_limit = np.array(lower_limit , dtype=np.uint8)
    upper_limit = np.array(upper_limit , dtype=np.uint8)
    return lower_limit , upper_limit

def get_color_from_user():
  
  while True:
    try:
      color_str = input("Enter the B (blue), G (green), R (red) value of the color you want to detect (separate by spaces): ").split()
      if len(color_str) != 3:
        raise ValueError("Please enter three values separated by spaces.")
      b, g, r = map(int, color_str)
      # Validate color values (0-255)
      if not (0 <= b <= 255 and 0 <= g <= 255 and 0 <= r <= 255):
        raise ValueError("Color values must be between 0 and 255.")
      return [b, g, r]
    except ValueError as e:
      print(f"Invalid input: {e}. Please try again.")





     
