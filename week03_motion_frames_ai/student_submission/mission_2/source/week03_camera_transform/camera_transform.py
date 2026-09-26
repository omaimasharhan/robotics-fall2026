"""Mission 2 student implementation.

Complete only ``transform_camera_point`` after preserving the initial AI output
in the guide. Course tests supply both real and simulated TF buffers.
"""
from geometry_msgs.msg import PointStamped
from rclpy.duration import Duration
from tf2_ros import TransformException
import tf2_geometry_msgs


def transform_camera_point(tf_buffer, point: PointStamped) -> PointStamped | None:

    if point.header.frame_id != "hall_camera":
        raise ValueError("point must be hall_camera frame")
    try:
        transformed_point = tf_buffer.transform(point, "base_link", timeout=Duration(seconds=0.05))
        return transformed_point
    
    except TransformException:
        return None



    

  