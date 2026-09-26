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