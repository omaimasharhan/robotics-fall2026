# Week 5: Sensors, Noise, and Uncertainty

- Course Id: CSCI345
- Email: omaima.sharhan19@myhunter.cuny.edu
- Name: Omaima Sharhan

## concepts.observation

When I increased the noise, the measurements became more scattered around the true distance and fluctuated more. When the noise was at its highest, 0.40, the mean was 1.97 and the median was 1.96, so they were still close to the true distance of 2.0 m. When I increased the bias, the measurements shifted to one side from the true distance. When the bias was at its highest, 0.40, the mean was 2.40 and the median was 2.39, so most of the measurements were higher than the true distance. The mean with high noise was only 0.03 m away from the true distance, while the mean with high bias was 0.40 m away. Therefore, increasing the bias produced less accurate measurements because the measurements were shifted farther from the true distance, while increasing noise mainly caused the measurements to fluctuate more around the true distance.

## final.course_reflection

This activity gave me a better understanding of sensor errors and uncertainty when working with different types of errors. One error could produce a different outcome than another error, which is why it is important to consider the best approach to fixing them depending on the type of error. It also showed me how filtering and estimation can improve measurements, and how robots use those estimates to make safe decisions depending on their environment and task. Overall, it gave me a better understanding of how a functional robot should react and complete its tasks in a certain environment. This activity motivated me to learn more about robot sensors and work to fix any problems that might be causing measurement errors so the robot can function safely and as expected. What stood out to me about the activity was how changing different filters could produce different outcomes and how acceptable errors depend on the people, setting, and consequences involved. A small error in a measurement can affect the decisions a robot makes. 

## final.synthesis

For a robot to function properly in different environments and complete different tasks, it needs to be tested before deployment, which is why measurement and estimation choices matter. In Mission 1, we analyzed a dataset and looked at its main defect. We were able to see how noise and bias produce different measurement patterns. Increasing noise caused the measurements to fluctuate around the true distance. When the noise was at its highest, 0.40, the mean was 1.97 and the median was 1.96, which were still close to the true distance of 2.00 m. In contrast, increasing bias caused the measurements to shift to one side. When the bias was at its highest, 0.40, the mean was 2.40 and the median was 2.39, meaning most measurements were higher than the true distance. In Mission 2, we focused on estimation choices, such as filtering and sensor weighting, which can affect response speed and accuracy. For example, using the median filter gave an RMSE of 0.15, an MAE of 0.07, and a response delay of 0.45. This shows how different estimation choices can affect the robot's accuracy and response time. In Mission 3, we focused on how the deployment context affects robot decisions. For the Warehouse robot, unnecessary stops can delay tasks, while false-safe decisions can cause safety issues and equipment damage. For the Assistive robot, unnecessary stops can reduce access and trust, while false-safe decisions could cause injury. 

## mission_1.bias

-0.02

## mission_1.bias_vs_variance

Variance shows how much the 236 valid measurements vary from each other. In this case, the variance is 0.11, which shows the spread of the measurements. Bias measures how far the average measurement is from the target point of 2.00 m. In this case, the bias is only -0.02 m, meaning the average measurement is slightly below the target.

## mission_1.dropouts

4

## mission_1.mean

1.98

## mission_1.median

1.99

## mission_1.more_samples

No, because collecting more samples would not fix the sensor's main problem. It would only collect more data that could produce the same error. What needs to be done is to find and fix the cause of the problem rather than just collecting more measurements.

## mission_1.outliers

32

## mission_1.profile

outlier_prone

## mission_1.robot_consequence

One decision the robot might make is to stop when its sensor indicates that it has reached the target. If the sensor gives an incorrect measurement, the robot could stop too early and never actually reach the target.

## mission_1.variance

0.11

## mission_2.comparison

Moving average and median results are somewhat similar. The moving average handles large errors better, while the median has a lower average error and response delay. The median is useful for handling outliers, while the moving average is better at smoothing overall fluctuations.

## mission_2.fusion_choice

Sensor A's weight is reasonable because, despite being more noisy and outlier-prone, it responds faster and updates more quickly. Sensor B is given a weight of 0.35 because it is slightly biased and updates only every fourth time step making it slower. 

## mission_2.responsiveness

The filter settings change the smoothing and response delay. For example, with the median method, it smoothed the filtered measurements, resulting in an RMSE of 0.15, an MAE of 0.07, and a response delay of 0.45. In the moving average method, the results were similar, with an RMSE of 0.15, an MAE of 0.08, and a response delay of 0.9. Overall, the moving average had a greater response delay than the median.

## mission_3.context_comparison

One parameter difference is the unsafe distance, where the Warehouse robot policy uses a 0.70 m distance while the Assistive robot policy uses 0.90 m. Since the Assistive robot operates near people with varied mobility, it needs a larger distance to keep between the robot and people for safety. The Warehouse robot uses 0.70 m because it operates in a controlled aisle. Another parameter difference is the caution margin, where the Warehouse robot policy is set to 0.25 m while the Assistive robot policy is set to 0.30 m. The larger caution margin for the Assistive robot provides an additional safety buffer because it operates near people. The Warehouse robot uses a smaller margin because it operates in a controlled environment. Both policies had a false-safe rate of zero in the tests, showing that these settings prevented false-safe decisions. 

## mission_3.error_costs

In the Warehouse robot policy, if unnecessary-stop errors occur frequently tasks will be delayed and slowed down which could affect the completion of tasks within a certain amount of time. A false-safe decision could cause safety issues and damage equipment because the robot will be moving when it is not safe. In the Assistive robot policy having unnecessary-stop errors would reduce access and trust and a false-safe decision could cause injury because the robot operates near people with varied mobility. Neither metric can simply be ignored because both work together to operate safely and while also performing its task effectively.

## mission_3.limitations

This simulation fails to represent unexpected conditions the robot might encounter in its environment, such as an object blocking the way and causing the robot to stop completely instead of redirecting itself and continuing its task. One stakeholder I would consult is the people working around the robots, since they will be the ones interacting with them. One additional test I would run before deployment would be sensor response because it will test how quickly and accurately the sensors respond when an unexpected object appears, which will help address safety concerns. 
