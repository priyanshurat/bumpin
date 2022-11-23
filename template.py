#Importing libraries
import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
from time import time
import math 
good_posture_frame=5
bad_posture_frame=0
#Declare a mediapipe class
mp_pose=mp.solutions.pose
pose=mp_pose.Pose(static_image_mode=False ,min_detection_confidence=0.3,model_complexity=1)

 
# Colors.
blue = (255, 127, 0)
red = (50, 50, 255)
green = (127, 255, 0)
dark_blue = (127, 20, 0)
light_green = (127, 233, 100)
yellow = (0, 255, 255)
pink = (255, 0, 255)

mp_drawing=mp.solutions.drawing_utils
def detectPose(image,pose):
    output_image=image.copy()
    imageRGB=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    results=pose.process(imageRGB)
    height,width,_=image.shape
    landmarks=[]
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image=output_image,landmark_list=results.pose_landmarks,
                                 connections=mp_pose.POSE_CONNECTIONS)
        for landmark in results.pose_landmarks.landmark:
            landmarks.append((int(landmark.x*width),int(landmark.y*height),(landmark.z*width)))
    return output_image,landmarks
    
def midpoint(point1, point2):
    x =(point1[0]+point2[0]) / 2
    y = (point1[1]+point2[1] )/ 2
    return [x,y]

def calculateAngle(landmark1,landmark2,landmark3):
    #get the required landmarks coordinates
    x1,y1=landmark1
    x2,y2=landmark2
    x3,y3=landmark3
    
    #calculate the angle between the three points
    angle=math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
    
    #check if angle is less than 0
    if angle<0:
        angle +=360
    return angle

def classifyPose(landmarks):
    points = []
    # print("LEFT SHOULDER: ",landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value])
    points.append([landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][0],landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value][1]])
    # print("RIGHT SHOULDER: ",landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value])
    points.append([landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value][0],landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value][1]])
    # print("LEFT ELBOW: ",landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value])
    points.append([landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value][0],landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value][1]])
    # print("RIGHT ELBOW: ",landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value])
    points.append([landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value][0],landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value][1]])
    # print("LEFT WRIST: ",landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])
    points.append([landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value][0],landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value][1]])
    # print("RIGHT WRIST: ",landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])
    points.append([landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value][0],landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value][1]])
    # print("LEFT HIP: ",landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
    points.append([landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][0],landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1]])
    # print("RIGHT HIP: ",landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value])
    points.append([landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value][0],landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value][1]])
    # print("LEFT KNEE: ",landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value])
    points.append([landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value][0],landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value][1]])
    # print("RIGHT KNEE: ",landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value])
    points.append([landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value][0],landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value][1]])
    # print("LEFT ANKLE: ",landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])
    points.append([landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value][0],landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value][1]])
    # print("RIGHT ANKLE: ",landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
    points.append([landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value][0],landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value][1]])
    # print("NOSE: ",landmarks[mp_pose.PoseLandmark.NOSE.value])
    points.append([landmarks[mp_pose.PoseLandmark.NOSE.value][0],landmarks[mp_pose.PoseLandmark.NOSE.value][1]])


    left_elbow_angle=calculateAngle(points[0],
                                     points[2],
                                     points[4])
    
    right_elbow_angle=calculateAngle(points[1],
                                     points[3],
                                     points[5])
    
    left_shoulder_angle=calculateAngle(points[2],
                                     points[0],
                                     points[6])

    right_shoulder_angle=calculateAngle(points[3],
                                     points[1],
                                     points[7])

    left_hip_angle=calculateAngle(points[0],
                                     points[6],
                                     points[8])

    right_hip_angle=calculateAngle(points[1],
                                     points[7],
                                     points[9])

    left_knee_angle=calculateAngle(points[6],
                                     points[8],
                                     points[10])

    right_knee_angle=calculateAngle(points[7],
                                     points[9],
                                     points[11])

    # print("left elbow angle",left_elbow_angle)
    # print("right elbow angle: ",right_elbow_angle)
    # print("left shoulder angle",left_shoulder_angle)
    # print("right shoulder angle: ",right_shoulder_angle)
    # print("left hip angle",left_hip_angle)
    # print("right hip angle: ",right_hip_angle)
    # print("left knee angle",left_knee_angle)
    # print("right knee angle: ",right_knee_angle)

    mp = midpoint(points[0],points[1])
    # print("Mid Point", mp)
    




    #Add your conditions here and return in the format of
    #return points,<bool val>,<message>
    #points are all the detected points
    #bool val if set to true means, the posture is correct.
    #message contains the text of string displayed on the image.
    return points, True, "Test pose"

    


pose_video = mp_pose.Pose(static_image_mode=True,min_detection_confidence=0.5,model_complexity=1)
video = cv2.VideoCapture(0)


while True:
    ret,frame = video.read()
    frame,landmarks=detectPose(frame,pose_video)
    if landmarks:
        essential_points,flag,message= classifyPose(landmarks)  
        if flag == True:
            good_posture_frame+=1
            cv2.circle(frame, [50,50], 30, green, 20)
            cv2.putText(frame, message, (20,450), cv2.FONT_HERSHEY_SIMPLEX, fontScale= 1, color= green, thickness=3)  
        else:
            bad_posture_frame+=1
            cv2.circle(frame, [50,50], 30, red, 20)
            cv2.putText(frame, message, (20,450), cv2.FONT_HERSHEY_SIMPLEX, fontScale= 1, color= red, thickness=3)  
    accuracy=(good_posture_frame/(good_posture_frame+bad_posture_frame))*100
    cv2.putText(frame, f"Accuracy: {accuracy:.2f}%", (300,30), cv2.FONT_HERSHEY_SIMPLEX, fontScale= 1, color= blue, thickness=3) 
    cv2.imshow('Image',frame)

    #press 'Q' to exit

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()