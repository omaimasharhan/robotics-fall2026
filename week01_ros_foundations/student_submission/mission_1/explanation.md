# Mission 1

## Command Path Explanation

A proposed command travels on /student _cmd_vel. The guard subscribes to it, checks the command and then publishes the approved command  on /cmd_vel

## Graph Explanation

A ROS 2 graph shows the components that are running and the ways they communicate.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found many numbers in the ranges field, which represent distance measurements in meters around the robot using LIDAR. It also includes the minimum and maximum range, as well as the minimum and maximum angle.

## Tools Explanation

Gazebo is responsible for simulation and sensing for the robot, while RViz is responsible for visualizing the robot and its information.
