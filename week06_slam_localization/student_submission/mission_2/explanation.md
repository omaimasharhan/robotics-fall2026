# Mission 2

## Comparison

Mission 1 took 16.05 minutes, while Mission 2 took 29.38 minutes, a difference of 13.33 minutes. Mission 2 had a higher known fraction of 39.93%, compared with Mission 1's 30.88%. However, Mission 1 mapped more total area, covering 137.47 m² compared with Mission 2's 90.05 m². Therefore, Mission 1 gave more useful coverage for the time spent because it mapped more area in less time. My prediction was partially supported because I expected Mission 2 to be faster, but it actually took longer, partly because the robot bumped into walls while following the inner perimeter route. In terms of map quality, Mission 1 showed more of the house's overall layout, while Mission 2 had a higher quality score and less speckle. This shows a tradeoff between coverage and map quality: Mission 1 was faster and covered more area, while Mission 2 had better numerical quality measurements but showed less of the house.

## Loop Closure

I can't confirm that loop closure happened because even though the robot moved and the map kept filling in I didn't see any previously mapped walls shift or line up differently. It looked more like the robot was just continuing to map new areas.

## Map Choice


I would trust Mission1's map more for a later robot task because it shows more of the house's layout, including more rooms and hallways. The walls are more clearly visible overall, although some duplicate lines appear in parts of the map. Mission2 has several overlapping lines that make the wall positions less clear, and some areas of the house are missing from the map. One limitation is that the map images and numerical measurements cannot prove the robot's exact position or guarantee that it would navigate safely in the real environment.

## Strategy.Original Prediction

My new route will be different from Mission 1 because I will explore the outer perimeter first, then enter the house and explore the right side before the left side. This should allow me to revisit the hallway only once, unlike Mission 1, where I explored the hallway first and then moved from room to room. I predict that Mission 2 will map the accessible space faster because the route should reduce unnecessary backtracking. Since Mission 1 already produced a clear map, I expect Mission 2 to produce a map with similar clarity.

## Strategy.Prediction Draft

My new route will be different from Mission 1 because I will explore the outer perimeter first, then enter the house and explore the right side before the left side. This should allow me to revisit the hallway only once, unlike Mission 1, where I explored the hallway first and then moved from room to room. I predict that Mission 2 will map the accessible space faster because the route should reduce unnecessary backtracking. Since Mission 1 already produced a clear map, I expect Mission 2 to produce a map with similar clarity.

## Strategy Prediction

The first strategy was  perimeter_then_interior , meaning that the robot explores the outer boundaries first and then the interior. The second strategy was frontier sweeps, which focuses on exploring the interior environment first. I think the frontier sweep strategy would improve coverage more because it would allow the robot to map areas that might not be accurately mapped using the  perimeter_then_interior  strategy. For continuity, I think  perimeter_then_interior  would perform better because it maps the walls first, helping establish the overall shape of the environment. For loop closure, I think  perimeter_then_interior  would perform better because it follows a more consistent path, making it easier for the robot to revisit previously mapped areas.
