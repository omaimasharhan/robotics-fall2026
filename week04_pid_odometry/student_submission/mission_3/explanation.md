# mission_3 Submission

- Name: Omaima Sharhan
- Section: CSCI395

## Explanations

### technical_analysis

The prediction was that increasing speed may make it harder for the robot to follow the planned route accurately, while too little derivative control may cause overshooting and oscillation. The robot computes safely while visiting all four waypoints and avoids getting too close to pedestrians. The PID controller compares the desired heading with the robot's current heading and adjusts the steering to follow the planned route. The PID settings were balanced enough to follow the route accurately without excessive overshooting or oscillation. The green and orange paths showed the robot's actual path and its odometry estimate, and both were close to each other. However, if the wheel-radius estimate is inaccurate, the robot may calculate the wrong distance traveled. Even if the PID is tuned correctly, the robot could still end up following a different path than planned.

### human_centered_analysis

The consequential failure would be if the robot turns too early or too late, which could cause safety issues and make it bump into pedestrians. I would check the robot's PID and how accurately it follows the actual path. The robot should maintain a safe distance from pedestrians, and its speed should not be too fast so that it has enough time to turn without entering an unsafe zone. Responsibility belongs to the developers because it is our responsibility to make sure the robot is properly tested and safe before deployment.