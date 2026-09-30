import numpy as np

def analytical_solution(v0, theta, g=9.81, dt=0.01):

    theta_rad = np.radians(theta)

    t_flight = (2 * v0 * np.sin(theta_rad)) / g 

    t = np.arange(0, t_flight, dt)

    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2

    y[y < 0] = 0

    return t,x, y

