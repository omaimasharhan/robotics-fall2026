
"""Pure decision helpers for Mission 3.

Complete both functions. Keeping this logic independent of ROS makes it possible
to test safety decisions before running the simulated robot.
"""

from __future__ import annotations

from collections.abc import Sequence

import math

def front_distance(
    ranges: Sequence[float],
    angle_min: float,
    angle_increment: float,
    half_width_radians: float,

) -> float | None:
     
    valid_distances = []
    for index, distance in enumerate(ranges):
        angle = angle_min + index * angle_increment
        in_front = abs(angle) <= half_width_radians
        is_valid = math.isfinite(distance) and distance > 0

        if is_valid and in_front:
            valid_distances.append(distance)
    if not valid_distances:
        return None


    return min(valid_distances)


   


def decide_velocity(
    distance: float | None,
    stop_distance: float,
    forward_speed: float,
) -> float:
    if distance is None:
        return 0.0
    if distance <= stop_distance:
        return 0.0
    if distance > stop_distance:
        return max(0.0, min(float(forward_speed), 0.18))


