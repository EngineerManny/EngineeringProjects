import numpy as np

data_points = int(input("How many data points for height vs time data? "))

height_vs_time_array = np.zeros((data_points, 2), float)

tf = 7.22
time_step = tf/(data_points - 1)


for i in range(data_points):
    time_value = i * time_step
    height_vs_time_array[i, 0] = time_value

print("Array with Time Values: ")
print(height_vs_time_array)