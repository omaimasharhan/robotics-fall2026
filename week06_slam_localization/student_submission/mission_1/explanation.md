# Mission 1

## Drift And Revisit

When the robot revisited areas it had already scanned, the new scans lined up with the mapped walls. The old walls did not visibly shift or double. As it revisited these areas, it also completed some of the spots that were previously gray. I couldn't tell if SLAM corrected drift because there was no clear evidence of a loop closure.

## Limitations

The unknown areas were around and behind obstacles that the robot did not approach closely or view from different angles. These areas remained gray on the map because the LiDAR could not detect surfaces blocked by the obstacles. As a result, some object boundaries and nearby spaces were not fully mapped.

## Map Interpretation

The map has a known fraction of 74%, which means that most of the area was mapped. The speckle fraction was low at 1.6%, meaning that the map had few scattered spots. The border contact fraction was 17.6%, which might suggest that some mapped areas reached the map's boundaries or that parts of the environment extended beyond the mapped area. The quality score was 88.6, suggesting that the mapped areas appear reasonably reliable. However, some areas remain unknown, which makes those parts of the map questionable. 

## Route.Original Prediction

The robot will start near the center-left of the house and follow the main hallway, exploring accessible rooms through their openings. It will revisit the main hallway and recognizable junctions as it moves between rooms. I predict that map coverage may be weaker in smaller rooms because the tight spaces make it difficult for the robot to maneuver and scan every corner. Map alignment may also be weaker in these areas if there are not enough distinctive features for the robot to estimate its position accurately.

## Route.Prediction Draft

The robot will start near the center-left of the house and follow the main hallway, exploring accessible rooms through their openings. It will revisit the main hallway and recognizable junctions as it moves between rooms. I predict that map coverage may be weaker in smaller rooms because the tight spaces make it difficult for the robot to maneuver and scan every corner. Map alignment may also be weaker in these areas if there are not enough distinctive features for the robot to estimate its position accurately.

## System Observation

As the robot moved through the area, red lines appeared to represent the /scan measurements, which detected objects and walls around the robot. The robot's position and orientation were reflected by the odometry, which showed a red arrow indicating the direction the robot was facing. TF appeared as connected lines representing the different coordinate frames, and these relationships changed as the robot moved. As the robot continued exploring and scanning the area, the /map updated to reflect the surrounding environment. 
