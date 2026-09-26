"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper
    always publishes it and the evaluator verifies it.
    """
    if pattern_name != "rounded_rectangle":
        raise ValueError(f"Unknown pattern name: {pattern_name}")

    # Motion parameters
    straight_speed = 0.10
    radius = 0.15
    angular_speed = straight_speed / radius
    arc_angle = 3.141592653589793/2
    

    # Durations needed to travel the specified distances.
    long_straight = 0.40 / straight_speed
    short_straight = 0.25 / straight_speed
    arc = arc_angle / angular_speed

    segments = [Segment(straight_speed,0.0, long_straight),
                Segment(straight_speed,angular_speed, arc),
                Segment(straight_speed,0.0, short_straight),
                Segment(straight_speed,angular_speed, arc),
                Segment(straight_speed,0.0, long_straight),
                Segment(straight_speed,angular_speed, arc),
                Segment(straight_speed,0.0, short_straight),
                Segment(straight_speed,angular_speed, arc)]

    return segments
   
    