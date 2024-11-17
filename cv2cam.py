import cv2
import time
  
# initialize the camera 
# If you have multiple camera connected with  
# current device, assign a value in cam_port  
# variable according to that 
cam_port = 0
cam = cv2.VideoCapture(cam_port) 
  
def camera_walk():

    
    # reading the input using the camera 
    result, image = cam.read() 
  
    # If image will detected without any error,  
    # show result 
    if result: 
  
        # showing result, it take frame name and image  
        # output 
        #cv2.imshow("GeeksForGeeks", image) 
  
        # saving image in local storage 
        cv2.imwrite(r"C:\Users\salim\GetFiles\face_photo\now_photo\image.jpg", image) 
  
        # If keyboard interrupt occurs, destroy image  
        # window 
        #cv2.waitKey(0) 
        #cv2.destroyWindow("GeeksForGeeks") 
        

        return True
    # If captured image is corrupted, moving to else part 
    else: 
        print("No image detected. Please! try again")
        return False
    
    