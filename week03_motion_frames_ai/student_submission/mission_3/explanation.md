# Mission 3

## Assigned Pattern

rounded_rectangle

## Original Output

There is one important detail in the specification: “eight segments” conflicts with the described sequence.

A rounded rectangle normally has 8 motion segments: 4 straight sections + 4 quarter-circle arcs.
But your written sequence says 0.40 m straight → 90° arc → 0.25 m straight, repeated 4 times, which produces 12 segments total.
I would follow the explicit motion sequence, because it defines the actual geometry: 4 × 0.40 m straight, 4 × 0.25 m straight, and 4 arcs.

A safe speed choice is 0.10 m/s. For a radius of 0.15 m:

$$ \omega=\frac{v}{r}=\frac{0.10}{0.15}=0.6667\text{ rad/s} $$

For a 90° arc:

$$ t=\frac{\pi/2}{0.6667}\approx2.356\text{ s} $$

This stays below both the 0.22 m/s and 0.80 rad/s limits.

pattern.py

Replace only build_pattern() with:

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper
    always publishes it and the evaluator verifies it.
    """
    if pattern_name != "rounded_rectangle":
        raise ValueError(f"Unknown pattern name: {pattern_name}")

    # Motion parameters
    straight_speed = 0.10       # m/s
    radius = 0.15               # m
    angular_speed = straight_speed / radius  # rad/s
    arc_angle = 3.141592653589793 / 2.0

    # Durations needed to travel the specified distances.
    long_straight_time = 0.40 / straight_speed
    short_straight_time = 0.25 / straight_speed
    arc_time = arc_angle / angular_speed

    segments = []

    # Four repetitions of:
    # 0.40 m straight -> 90-degree left arc -> 0.25 m straight
    for _ in range(4):
        segments.append(
            Segment(
                linear_x=straight_speed,
                angular_z=0.0,
                duration=long_straight_time,
            )
        )

        segments.append(
            Segment(
                linear_x=straight_speed,
                angular_z=angular_speed,
                duration=arc_time,
            )
        )

        segments.append(
            Segment(
                linear_x=straight_speed,
                angular_z=0.0,
                duration=short_straight_time,
            )
        )

    return segments
Why these values work
Motion	Distance/angle	Speed	Duration
Straight	0.40 m	0.10 m/s	4.00 s
Arc	90° = 1.571 rad	0.667 rad/s	2.356 s
Straight	0.25 m	0.10 m/s	2.50 s

Total time:

$$ 4(4.00+2.356+2.50)\approx35.42\text{ s} $$

So it is comfortably under the 60-second total and 30-second-per-segment limits.

The arc radius is:

$$ r=\frac{v}{\omega}=\frac{0.10}{0.6667}=0.15\text{ m} $$

which is exactly the requested radius.

## Original Prompt

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper
    always publishes it and the evaluator verifies it.
    """
    if pattern_name != "rounded_rectangle":
        raise ValueError(f"Unknown pattern name: {pattern_name}")

    # Motion parameters
    straight_speed = 0.10       # m/s
    radius = 0.15               # m
    angular_speed = straight_speed / radius  # rad/s
    arc_angle = 3.141592653589793 / 2.0

    # Durations needed to travel the specified distances.
    long_straight_time = 0.40 / straight_speed
    short_straight_time = 0.25 / straight_speed
    arc_time = arc_angle / angular_speed

    segments = []

    # Four repetitions of:
    # 0.40 m straight -> 90-degree left arc -> 0.25 m straight
    for _ in range(4):
        segments.append(
            Segment(
                linear_x=straight_speed,
                angular_z=0.0,
                duration=long_straight_time,
            )
        )

        segments.append(
            Segment(
                linear_x=straight_speed,
                angular_z=angular_speed,
                duration=arc_time,
            )
        )

        segments.append(
            Segment(
                linear_x=straight_speed,
                angular_z=0.0,
                duration=short_straight_time,
            )
        )

    return segments

## Original Source


def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper
    always publishes it and the evaluator verifies it.
    """
    if pattern_name != "rounded_rectangle":
        raise ValueError(f"Unknown pattern name: {pattern_name}")

    # Motion parameters
    straight_speed = 0.10       # m/s
    radius = 0.15               # m
    angular_speed = straight_speed / radius  # rad/s
    arc_angle = 3.141592653589793 / 2.0

    # Durations needed to travel the specified distances.
    long_straight_time = 0.40 / straight_speed
    short_straight_time = 0.25 / straight_speed
    arc_time = arc_angle / angular_speed

    segments = []

    # Four repetitions of:
    # 0.40 m straight -> 90-degree left arc -> 0.25 m straight
    for _ in range(4):
        segments.append(
            Segment(
                linear_x=straight_speed,
                angular_z=0.0,
                duration=long_straight_time,
            )
        )

        segments.append(
            Segment(
                linear_x=straight_speed,
                angular_z=angular_speed,
                duration=arc_time,
            )
        )

        segments.append(
            Segment(
                linear_x=straight_speed,
                angular_z=0.0,
                duration=short_straight_time,
            )
        )

    return segments


## Specification

I would want the robot to drive in a rounded rectangle with eight segments. It will move forward 0.40 m, then make a left 90-degree arc with a radius of 0.15 m, then move forward 0.25 m. This pattern will repeat four times, and the robot should finish near the starting pose. The speed will stay within the required limits. I will plan the motion in a clear 2 m by 2 m area. The intended distances should be within 0.02 m, the angles within 0.04 rad, and the arc radius within 0.02 m.

## Saved Specification

I would want the robot to drive in a rounded rectangle with eight segments. It will move forward 0.40 m, then make a left 90-degree arc with a radius of 0.15 m, then move forward 0.25 m. This pattern will repeat four times, and the robot should finish near the starting pose. The speed will stay within the required limits. I will plan the motion in a clear 2 m by 2 m area. The intended distances should be within 0.02 m, the angles within 0.04 rad, and the arc radius within 0.02 m.

## Assumptions

The AI assumed the motion would be forward, then a left 90-degree arc, and then forward again. It used the exact units specified in the assignment, such as meters, meters per second, and radians per second. It chose a safe speed of 0.10 m/s and calculated the angular speed using the 0.15 m radius, which kept the speed below the 0.22 m/s and 0.80 rad/s limits. It also calculated the duration needed for each type of motion. The AI did not make any special assumptions about coordinate frames because the existing ROS wrapper handles publishing the motion commands.

## Problems

The code produced 12 segments instead of the required 8 segments. This may have happened because my wording about the motion pattern was not clear enough. The code followed the sequence of 0.40 m forward, 90-degree arc, and 0.25 m forward four times, which resulted in 12 segments. Therefore, the code was not accurate for the eight-segment requirement.



## Test Plan

For the pattern test, I would check that the robot produces 8 segments in the correct order and makes the rounded rectangle and for the velocity-limit test I would check that the linear speed stays at or below 0.22 m/s and the angular speed stays at or below 0.80 rad/s. For the stop test I would check that the robot stops after the last segment.

## Modifications

I changed the code from 12 segments to 8 segments to match the task requirements. I also added the segments manually to the list instead of using a loop, so I could make sure the order and number of segments were correct.


## Live Pending

True

## Evidence Analysis

The tests establish that the code has 8 segments, the segments have the correct basic order, and the speed limits are being followed. All 9 tests passed. However, these tests do not fully confirm the robot's actual movement. One additional test I would add is checking the total duration to make sure it does not exceed the required 60-second limit.


## Ai Disclosure

I used ChatGPT to generate code for the implementation section. I reviewed the code before running it and noticed that it did not match the assignment because it generated 12 segments instead of 8. I changed the code to match the required pattern and verified it with the tests.


## Live Issue

The robot did move, but the live check did not finish. All 9 tests passed, but I could not fully verify the rounded rectangle pattern and the final stop.

