# Mission 3

## Context Comparison

One parameter difference is the unsafe distance, where the Warehouse robot policy uses a 0.70 m distance while the Assistive robot policy uses 0.90 m. Since the Assistive robot operates near people with varied mobility, it needs a larger distance to keep between the robot and people for safety. The Warehouse robot uses 0.70 m because it operates in a controlled aisle. Another parameter difference is the caution margin, where the Warehouse robot policy is set to 0.25 m while the Assistive robot policy is set to 0.30 m. The larger caution margin for the Assistive robot provides an additional safety buffer because it operates near people. The Warehouse robot uses a smaller margin because it operates in a controlled environment. Both policies had a false-safe rate of zero in the tests, showing that these settings prevented false-safe decisions. 

## Error Costs

In the Warehouse robot policy, if unnecessary-stop errors occur frequently tasks will be delayed and slowed down which could affect the completion of tasks within a certain amount of time. A false-safe decision could cause safety issues and damage equipment because the robot will be moving when it is not safe. In the Assistive robot policy having unnecessary-stop errors would reduce access and trust and a false-safe decision could cause injury because the robot operates near people with varied mobility. Neither metric can simply be ignored because both work together to operate safely and while also performing its task effectively.

## Limitations

This simulation fails to represent unexpected conditions the robot might encounter in its environment, such as an object blocking the way and causing the robot to stop completely instead of redirecting itself and continuing its task. One stakeholder I would consult is the people working around the robots, since they will be the ones interacting with them. One additional test I would run before deployment would be sensor response because it will test how quickly and accurately the sensors respond when an unexpected object appears, which will help address safety concerns. 
