# Mission 2

## Diagnostics

{'stale': '', 'typo': '', 'wrong_source': ''}

## Fixed Meaning



## Frame Context

The rear-camera transform stays fixed because the rear camera is attached to the robot’s body, so its position and orientation relative to the robot do not change as the robot moves. The hallway camera is fixed in the environment, so its position does not change. However, the robot moves relative to the hallway camera, causing the hallway-camera-to-`base_link` transform to change.


## Improved Changes

The improved prompt checks if the `frame_id` is `hall_camera`. If it is not, it raises an error. It then uses TF to transform the stamped point from `hall_camera` to `base_link` without hard-coding any offsets. It also keeps the point's original timestamp so the correct transform is used for when the point was observed. If the transform is not available, the function returns `None` instead of trying to move the robot.


## Initial Analysis

I think the code does the job it is intended to do, which is to convert a point detected by the hallway camera into the robot’s `base_link` frame. It does this by setting the point’s `frame_id` to `hall_camera`, so ROS knows which frame the point starts in. It also has the point information it needs. However, the code does not include a timestamp for the `PointStamped` message. It also uses hard-coded point values of x = 2.0, y = 1.0, and z = 0.0 instead of using an actual detected point. The code gives the TF listener some time to receive transforms using `rclpy.spin_once()`, but it may not be enough if the transform is unavailable. The code also does not use any robot motion topics, so it does not directly account for the robot moving.



## Initial Output

For this mission, you would use TF2 to transform the point from hall_camera into base_link. A basic ROS 2 Python example is:

import rclpy
from rclpy.node import Node
from tf2_ros import Buffer, TransformListener
from geometry_msgs.msg import PointStamped


class CameraToRobot(Node):
    def __init__(self):
        super().__init__('camera_to_robot')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # Example point detected by the hallway camera
        self.camera_point = PointStamped()
        self.camera_point.header.frame_id = 'hall_camera'
        self.camera_point.point.x = 2.0
        self.camera_point.point.y = 1.0
        self.camera_point.point.z = 0.0

    def transform_point(self):
        try:
            # Convert point from hall_camera frame to base_link frame
            robot_point = self.tf_buffer.transform(
                self.camera_point,
                'base_link'
            )

            self.get_logger().info(
                f'Robot frame: x={robot_point.point.x:.2f}, '
                f'y={robot_point.point.y:.2f}, '
                f'z={robot_point.point.z:.2f}'
            )

        except Exception as e:
            self.get_logger().warn(f'Transform failed: {e}')


def main(args=None):
    rclpy.init(args=args)

    node = CameraToRobot()

    # Give TF listener time to receive transforms
    rclpy.spin_once(node, timeout_sec=1.0)

    node.transform_point()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
The important part

This is the actual transformation:

robot_point = self.tf_buffer.transform(
    self.camera_point,
    'base_link'
)

The point starts in:

hall_camera

and ROS uses the available TF tree:

hall_camera → odom → base_link

to calculate where that same point is relative to the robot.

So conceptually:

Point detected by camera
        ↓
  hall_camera frame
        ↓
       TF2
        ↓
   base_link frame
        ↓
Point location relative to robot

You don't manually calculate the x/y/z changes yourself. TF2 uses the transformations in the ROS TF tree to do it for you.

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Source

import rclpy
from rclpy.node import Node
from tf2_ros import Buffer, TransformListener
from geometry_msgs.msg import PointStamped


class CameraToRobot(Node):
    def __init__(self):
        super().__init__('camera_to_robot')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # Example point detected by the hallway camera
        self.camera_point = PointStamped()
        self.camera_point.header.frame_id = 'hall_camera'
        self.camera_point.point.x = 2.0
        self.camera_point.point.y = 1.0
        self.camera_point.point.z = 0.0

    def transform_point(self):
        try:
            # Convert point from hall_camera frame to base_link frame
            robot_point = self.tf_buffer.transform(
                self.camera_point,
                'base_link'
            )

            self.get_logger().info(
                f'Robot frame: x={robot_point.point.x:.2f}, '
                f'y={robot_point.point.y:.2f}, '
                f'z={robot_point.point.z:.2f}'
            )

        except Exception as e:
            self.get_logger().warn(f'Transform failed: {e}')


def main(args=None):
    rclpy.init(args=args)

    node = CameraToRobot()

    # Give TF listener time to receive transforms
    rclpy.spin_once(node, timeout_sec=1.0)

    node.transform_point()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

## Live Pending

True

## Map Absent



## Moving Coordinates



## Point Answers

{'sensor_point_in_base': {'x': 0.97, 'y': 0.0}, 'sensor_point_in_odom': {'x': 1.03, 'y': 0.0}}

## Relationships

{'base_to_sensor': 'base_link → base_scan', 'map_role': 'Global frame corrected by localization or SLAM', 'odom_to_base': 'odom → base_link'}

## Sensor Offset



## Snapshot

{'source': 'reference', 'captured_at': '2026-09-24T03:04:43.158836+00:00', 'description': 'Instructor-defined frame geometry. No live ROS transforms were measured.', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'transforms': {'base_scan_to_base_link': {'translation': {'x': 0.2, 'y': 0.0, 'z': 0.14}, 'yaw': 0.0}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': 3.141592653589793}, 'hall_camera_to_base_link': {'translation': {'x': -1.5, 'y': 0.5, 'z': 1.2}, 'yaw': -1.5707963267948966}}}

## Synthesis

The AI output had hard-coded offsets, which could give an inaccurate point from the hall camera. The improved prompt uses TF to transform the point from hall_camera to base_link and keeps the timestamp. A wrong transform could cause the robot to detect people or objects in the wrong location. The rotation test checks for this problem. If the transform is unavailable, the robot should not move and return None.


## Live Issue

All five course tests passed but the live camera test didn't work because ROS couldn't complete the live check. I tried running the live test while Gazebo was running, but the hall_camera to base_link transform is still unverified.
