# Pose detection module

Hey, welcome to the pose detection module of bumpin'.

## Pre-requisites
Make sure the following libraries are installed:
1) openCV
2) Mediapipe
3) numpy
4) matplotlib

## body_points.py

Open the file in any IDE like VScode. Then run the script and for every body detected, it'll give you a set of parameters that'd look like following:


![image](https://user-images.githubusercontent.com/74321084/203639695-fdc4f5aa-cf1d-4a1b-8056-513995f26a31.png)

The upper part of the output shows the location of points on the screen.

Next part will show the angles subtended at different parts as required.

Last part will show you the mid-point of your shoulders, that can be aligned with your nose to keep your head straight.




You can use this module to get the angles subtended at perfect pose and then go to the templates.py file.



## template.py

This file will give you a template to add your own posture, with some variation. You are free to play with the code or can use the if-else ladder to construct the code. Examples are added in the folder.
Points can be plotted manually as:

![image](https://user-images.githubusercontent.com/74321084/203640740-ce8e7cc9-2ba1-48db-a3ea-fdb387ee1795.png)

Just add some conditions, brush off your pythons skills and you're good to go.
Make sure: you return the fucntion with 3 values:
1) points: all the points detected.
2) Boolean value: True if pose is correct, False if pose is wrong.
3) message: The text you want to display on screen.




## Interview_det.py

This code is made using the template.py file by making changes in the conditions part. The conditions are added as follow:

![image](https://user-images.githubusercontent.com/74321084/203642305-909369ee-1be7-4891-a381-ba259d8dd933.png)


This is how the conditions are added and the pose is detected.
