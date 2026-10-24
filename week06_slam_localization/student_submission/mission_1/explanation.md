# Mission 1

## Drift And Revisit

When the robot revisited areas it had already scanned, the new scans lined up with the mapped walls. The old walls did not visibly shift or double. As it revisited these areas, it also completed some of the spots that were previously gray. I couldn't tell if SLAM corrected drift because there was no clear evidence of a loop closure.

## Limitations

The unknown areas were around and behind obstacles that the robot did not approach closely or view from different angles. These areas remained gray on the map because the LiDAR could not detect surfaces blocked by the obstacles. As a result, some object boundaries and nearby spaces were not fully mapped.


## Route.Original Prediction

The robot will start near the center-left of the house and follow the main hallway, exploring accessible rooms through their openings. It will revisit the main hallway and recognizable junctions as it moves between rooms. I predict that map coverage may be weaker in smaller rooms because the tight spaces make it difficult for the robot to maneuver and scan every corner. Map alignment may also be weaker in these areas if there are not enough distinctive features for the robot to estimate its position accurately.

## Route.Prediction Draft

The robot will start near the center-left of the house and follow the main hallway, exploring accessible rooms through their openings. It will revisit the main hallway and recognizable junctions as it moves between rooms. I predict that map coverage may be weaker in smaller rooms because the tight spaces make it difficult for the robot to maneuver and scan every corner. Map alignment may also be weaker in these areas if there are not enough distinctive features for the robot to estimate its position accurately.

