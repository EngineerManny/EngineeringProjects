import numpy as np
import os

def save_to_csv(height_vs_time_array, data, trajectory_data):
    # Construct the full path for the file
    file_path = os.path.join(data, trajectory_data)
    
    # Ensure the folder exists
    if not os.path.exists(data):
        os.makedirs(data)
    
    # Save the data array to a .csv file
    np.savetxt(file_path, height_vs_time_array, delimiter=' , ', header='(Time , Height)', comments='')