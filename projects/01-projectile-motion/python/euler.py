import numpy as np

def calculate_euler_trajectory(v0, theta_deg, g=9.81, dt=0.01):
    theta_rad = np.radians(theta_deg)
    
    # Başlangıç koşulları: t=0 anında cisim orijinde (0,0)
    x_list = [0.0]
    y_list = [0.0]
    t_list = [0.0]
    
    vx = v0 * np.cos(theta_rad)
    vy = v0 * np.sin(theta_rad)
    
    while y_list[-1] >= 0:

        vy_new = vy - g * dt
        
        x_new = x_list[-1] + vx * dt
        y_new = y_list[-1] + vy * dt
        
        x_list.append(x_new)
        y_list.append(y_new)
        t_list.append(t_list[-1] + dt)
        
        vy = vy_new
        
    return np.array(t_list), np.array(x_list), np.array(y_list)