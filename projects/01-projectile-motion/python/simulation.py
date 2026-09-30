import matplotlib.pyplot as plt
import numpy as np
import os
from analytical import analytical_solution
from euler import calculate_euler_trajectory


v0 = 50.0        
theta = 45.0     


dt_euler = 0.5   

t_ana, x_ana, y_ana = analytical_solution(v0, theta, dt=0.01)

t_eul, x_eul, y_eul = calculate_euler_trajectory(v0, theta, dt=dt_euler)


plt.figure(figsize=(10, 6))

plt.plot(x_ana, y_ana, label='Analitik (Kesin)', color='blue', linewidth=2)

plt.plot(x_eul, y_eul, label=f'Euler (Sayısal, dt={dt_euler}s)', color='red', linestyle='--', marker='o')


plt.title(f'Eğik Atış: Analitik vs Euler Metodu ($v_0$={v0} m/s, $\\theta$={theta}°)')
plt.xlabel('Mesafe X (m)')
plt.ylabel('Yükseklik Y (m)')
plt.axhline(0, color='black', linewidth=1) 
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)


results_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'results')
os.makedirs(results_dir, exist_ok=True)
save_path = os.path.join(results_dir, 'trajectory.png')

plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"Deney tamamlandı. Grafik kaydedildi: {save_path}")

# --- 5. Verileri CSV Olarak Kaydet ---
data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
os.makedirs(data_dir, exist_ok=True)
csv_path = os.path.join(data_dir, 'euler_trajectory.csv')

# t, x ve y dizilerini yan yana sütunlar halinde birleştirip CSV'ye yazıyoruz
np.savetxt(csv_path, np.column_stack((t_eul, x_eul, y_eul)), delimiter=",", header="time,x,y", comments="")
print(f"Simülasyon verisi kaydedildi: {csv_path}")

plt.show()