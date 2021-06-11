import numpy as np
import cv2

#https://stackoverflow.com/questions/36817133/identifying-the-range-of-a-color-in-hsv-using-opencv/51686953
   
def exit():
    sys.exit

def wait():
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def blue():
    lower_range = np.array([90, 50, 70])
    upper_range = np.array([128, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('reso', res)

def yellow():
    lower_range = np.array([25,50,70])
    upper_range = np.array([35,255,255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('reso', res)

def green():
    lower_range = np.array([36, 50, 70])
    upper_range = np.array([89, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('reso', res)
    
def red():
    lower_range = np.array([160,100,20])
    upper_range = np.array([179,255,255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('reso', res)

def orange():
    lower_range = np.array([10, 50, 70])
    upper_range = np.array([24, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('reso', res)

print("""
  ,--,  .---.  ,-.    .---.  ,---.       .---. ,---.    .--.    ,--,  ,---.   
.' .') / .-. ) | |   / .-. ) | .-.\     ( .-._)| .-.\  / /\ \ .' .')  | .-'   
|  |(_)| | |(_)| |   | | |(_)| `-'/    (_) \   | |-' )/ /__\ \|  |(_) | `-.   
\  \   | | | | | |   | | | | |   (     _  \ \  | |--' |  __  |\  \    | .-'   
 \  `-.\ `-' / | `--.\ `-' / | |\ \   ( `-'  ) | |    | |  |)| \  `-. |  `--. 
  \____\)---'  |( __.')---'  |_| \)\   `----'  /(     |_|  (_)  \____\/( __.' 
       (_)     (_)   (_)         (__)         (__)                   (__)     
""")
path = input("Enter the Path and Name of the Image File: ")
img = cv2.imread(path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

choice = input("""
    1. Red
    2. Green
    3. Blue
    4. Yellow
    5. Orange
    Q. Quit
    
Please enter your choice: """)

if choice == "1":
    red()
    wait()

elif choice == "2":
    green()
    wait()

elif choice == "3":
    blue()
    wait()

elif choice == "4":
    yellow()
    wait()

elif choice == "5":
    orange()
    wait()
    
elif choice=="Q" or choice=="q":
    exit()
    
else:
    print("Invalid Choice")
    print("Please try again")
