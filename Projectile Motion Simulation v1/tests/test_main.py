from test_calculations import save_to_csv
from test_calculations import calculate_height
from test_calculations import calculate_trajectory

# Get user inputs
initial_height = float(input("What is the initial height (meters) of the projectile? "))
final_height = float(input("What is the final height (meters) of the projectile? "))
initial_angle = float(input("What is the initial angle (degrees) of the projectile? "))
initial_velocity = float(input("What is the initial velocity (m/s) of the projectile? "))
data_points = int(input("How many data points for height vs time data? "))

calculate_trajectory(initial_height, final_height, initial_angle, initial_velocity, data_points)