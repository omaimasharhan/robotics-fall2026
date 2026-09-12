# Mission 3

## Data To Command

The first function, front_distance(), calculates the angle of each LiDAR index and only reads values that are in the front sector, finite, and greater than zero. It stores the valid readings and finds the nearest distance. If there are no valid readings, it returns None. The second function, decide_velocity(), receives the nearest front distance. If the distance is None or an obstacle is too close, it returns 0.0 to stop the robot. If the path is clear, it returns the forward speed while limiting it to between 0 and 0.18 m/s.

## Missing Data Safety

It stops because it can’t tell if the path is clear or if there is an obstacle. It’s safer for the robot to stop instead of moving when it doesn’t have a valid reading.

## System Layers

The decision functions use the LiDAR readings to decide if the robot should move or stop. The ROS node gets the sensor information and sends the speed command. Then the command guard checks the command to make sure it is safe before it reaches the robot. 


