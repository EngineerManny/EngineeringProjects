import math as m
import numpy as np
import os

# Get user inputs
initial_height = 0.0
final_height = 0.0
initial_angle = float(input("What is the initial angle (degrees) of the projectile? "))
initial_velocity = float(input("What is the initial velocity (m/s) of the projectile? "))
data_points = int(input("How many data points for height vs time data? "))

def save_to_csv(array, folder_name, file_name):
    # Construct the full path for the file
    file_path = os.path.join(folder_name, file_name)
    
    # Ensure the folder exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Save the data array to a .csv file
    np.savetxt(file_path, array, delimiter=',', header='Time,Height', comments='')

def calculate_height(Yi, Viy, time_value, g):
    # Formula: Y = Yi + Viy * t - 0.5 * g * t^2
    return Yi + Viy * time_value - 0.5 * g * (time_value ** 2)

def calculate_trajectory(initial_height, final_height, initial_angle, initial_velocity, data_points):
    Yi = initial_height
    Yf = final_height
    theta = (m.pi / 180) * initial_angle
    V = initial_velocity
    dp = data_points

    Viy = V * m.sin(theta)
    g = 9.807

    # Time of flight calculation assuming height returns to 0
    tf = (2 * Viy) / g  # Time to return to the initial height (0)

    height_vs_time_array = np.zeros((data_points, 2), float)

    # Time step for evenly spaced time values
    time_step = tf / (data_points - 1) if data_points > 1 else tf  # Ensure non-zero time_step

    for i in range(data_points):
        time_value = i * time_step  # Starts at 0 and ends at tf
        height_vs_time_array[i, 0] = time_value
        height_vs_time_array[i, 1] = calculate_height(Yi, Viy, time_value, g)

    print("Array with Time Values and Heights: ")
    print(height_vs_time_array)
    
    # Path to the data folder
    data_folder = 'Projects/Projectile motion simulation v1/data'
    
    # Save the array to a .csv file in the data folder
    save_to_csv(height_vs_time_array, data_folder, 'times_heights.csv')

calculate_trajectory(initial_height, final_height, initial_angle, initial_velocity, data_points)
