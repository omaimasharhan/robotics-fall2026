# pillar_search

## diagnosis
One successful centering attempt shows that the mask detected the blue pillar clearly, with the pillar appearing white against the black background. The processing region and center line are also visible in the annotated image. However, the yellow contour centroid is slightly off-center, showing that the pillar was not perfectly centered. The centroid error was approximately 0.30. To improve the result, I increased the steering gain and center tolerance and lowered the minimum contour fraction. The error decreased from 0.3637 to 0.3038, and camera waits decreased from 8 to 0.  

## evidence
All colors were centered except turquoise, which was slightly off center and to the right. In the state timeline, the robot kept switching between different states, but it held its position after detecting a color. For the camera evidence, a positive horizontal image error means the detected region is to the right of center. The robot's turning direction can be compared with this error to see how it responded when the region was off center. Overall, a centered colored region does not guarantee that the robot has identified the correct object because multiple pillars could share the same color. Also, even if a pillar is centered in the camera image, this does not tell us how far away it actually is. 
