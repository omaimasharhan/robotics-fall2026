# Mission 2

## Comparison

Moving average and median results are somewhat similar. The moving average handles large errors better, while the median has a lower average error and response delay. The median is useful for handling outliers, while the moving average is better at smoothing overall fluctuations.

## Fusion Choice

Sensor A's weight is reasonable because, despite being more noisy and outlier-prone, it responds faster and updates more quickly. Sensor B is given a weight of 0.35 because it is slightly biased and updates only every fourth time step making it slower. 

## Responsiveness

The filter settings change the smoothing and response delay. For example, with the median method, it smoothed the filtered measurements, resulting in an RMSE of 0.15, an MAE of 0.07, and a response delay of 0.45. In the moving average method, the results were similar, with an RMSE of 0.15, an MAE of 0.08, and a response delay of 0.9. Overall, the moving average had a greater response delay than the median.
