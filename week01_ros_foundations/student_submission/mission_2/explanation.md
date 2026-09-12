# Mission 2

## Predictions

{'straight': 'I predict the robot will finish 0.45 m from its starting point.', 'rotation': 'I predict its position will stay the same while its direction will rotate left 1.5 radians.', 'curve': 'I predict a curved path because the robot moves forward and turns right at the same time for 4s', 'curve_modified': ' This curve should be tighter because the robots linear velocity is smaller and its angular velocity is larger making the curve tighter than the previous example.'}

## Prediction Locks

{'straight': '2026-09-08T03:10:34.121919+00:00', 'rotation': '2026-09-08T03:17:42.089095+00:00', 'curve': '2026-09-08T03:30:25.461352+00:00', 'curve_modified': '2026-09-08T03:40:41.176084+00:00'}

## Motion Comparison

For the straight motion trial, my prediction was accurate because I predicted that the command path length would be 0.45 m, which matched the measured value in the table. The forward speed was 0.15 m/s, the command time was 3.0 s, and the turning speed was 0 rad/s, so I calculated the path length as 0.15 × 3.0 = 0.45 m.

## Measurement Explanation

For the curve motion trial, the estimated traveled path was 0.366 m and the start-to-end distance was 0.317 m. They are different because the start-to-end distance measures the straight-line distance between the robot's starting and ending positions, while the estimated traveled path measures the distance the robot traveled along its curved path using its forward and turning motion.

## Safety Explanation

The command guard checks all driving commands before they reach the robot by checking whether the speed is too large or contains invalid values and rejecting invalid commands.
The final zero command sets the forward and turning speeds to 0 after a trial is finished so the robot stops moving.
The timeout is needed if a program crashes or stops sending commands. After 0.5 seconds without a new command, the guard sends a stop command to prevent the robot from continuing to move.

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}
