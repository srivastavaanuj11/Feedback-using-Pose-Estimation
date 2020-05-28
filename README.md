# Feedback using Pose Estimation
Objective - To alert the person if he does wrong body movements in realtime while he is doing the excercise.

Algorithm - Pose estimation algorithm generates human body key point coordinates and we take the angles form between the lines formed from these points and determine whether excercise is right or wrong.

Implementation- Here pose estimation algorithm will be used for getting realtime information about the body movements. Then I will check whether the values from information gathered are in the acceptable range for that particular excercise or not. If not he would get a realtime feedback from the system. The feedback system would be designed using Fuzzy Logic. It would also keep track of all the excercises the user has performed for the day and also saves a seperate excercise schedule for each user.
