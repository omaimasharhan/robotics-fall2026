# Autosaved responses

- Name: Omaima Sharhan
- Student ID: 23805819
- Section: CSCI345

## Check-in answers

### m1_prediction

With too little Kp, I expect the controller to respond weakly to the error, even if the arm is far from its target. With too little Kd, I expect the arm to overshoot the target and oscillate .

### m1_arm_tuning

I predicted that too little Kp would cause a weak response to the error and too little Kd would cause the arm to overshoot and oscillate. I changed the shoulder and elbow controllers to improve their movement. The hold phase showed that both joints got close to their targets but still had some error. Gravity compensation helped the arm counteract gravity, allowing the shoulder and elbow to hold their positions more accurately and successfully complete all three poses.

### final_reflection

This activity helped me understand how mobile robots use sensors to measure their environment and why those measurements are not always accurate. It was an eye-opening lab because we were able to test how a robot's motion reacts to different sensor measurements and how speed affects the robot's overall path. As developers, our job is to make sure the robot can understand its sensor measurements and account for how accurate and reliable they are. This activity motivated me to learn more about robotics in general and understand the importance of proper calibration, odometry, and control systems to help robots perform accurately and minimize errors. What stood out to me the most was how a robot cannot rely on forward speed alone to perform a task accurately. It also needs to consider other measurements, such as wheel movement, speed, and rotation. I also learned how important PID control is for helping the robot adjust its movement and follow the intended path more accurately. This made me realize how much goes into making a robot perform a task correctly and how even small errors in measurements or movement can affect the final result. I think understanding these concepts is important because robots need to perform safely and accurately, especially when working around people.

## Mission explanations

### mission_1

**prediction**: With too little Kp, I expect the controller to respond weakly to the error, even if the arm is far from its target. With too little Kd, I expect the arm to overshoot the target and oscillate .

**tuning_analysis**: I predicted that too little Kp would cause a weak response to the error and too little Kd would cause the arm to overshoot and oscillate. I changed the shoulder and elbow controllers to improve their movement. The hold phase showed that both joints got close to their targets but still had some error. Gravity compensation helped the arm counteract gravity, allowing the shoulder and elbow to hold their positions more accurately and successfully complete all three poses.
