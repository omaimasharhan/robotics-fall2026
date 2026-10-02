# mission_1 Submission

- Name: (not provided)
- Section: (not provided)

## Explanations

### prediction

With too little Kp, I expect the controller to respond weakly to the error, even if the arm is far from its target. With too little Kd, I expect the arm to overshoot the target and oscillate .

### tuning_analysis

I predicted that too little Kp would cause a weak response to the error and too little Kd would cause the arm to overshoot and oscillate. I changed the shoulder and elbow controllers to improve their movement. The hold phase showed that both joints got close to their targets but still had some error. Gravity compensation helped the arm counteract gravity, allowing the shoulder and elbow to hold their positions more accurately and successfully complete all three poses.