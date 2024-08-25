import math as m
import numpy as np

initial_height = float(input("What is the initial height of the projectile? "))
final_height = float(input("What is the final height of the projectile? "))
initial_angle = float(input("What is the initial angle (degrees) of the projectile? "))
initial_velocity = float(input("What is the initial velocity (m/s) of the projectile? "))
data_points = float(input("How many data points for height vs time data? "))

def calculate_trajectory(initial_height, final_height, initial_angle, initial_velocity, data_points):

    Yi = initial_height
    Yf = final_height
    theta = (m.pi/180) * (initial_angle)
    V = initial_velocity
    dp = data_points

    Viy = (V)*m.sin(theta)
    g = 9.807

    tf = (Viy)/((1/2)*g)

calculate_trajectory(initial_height, final_height, initial_angle, initial_velocity, data_points)