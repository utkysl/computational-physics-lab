# Physical Model: Projectile Motion

## 1. The Physical System
We consider a point mass $m$ launched in a 2D plane with an initial velocity $v_0$ at an angle $\theta$ relative to the horizontal axis. 

Assumptions for this baseline model:
* The only force acting on the particle is a constant gravitational acceleration, $\vec{g} = (0, -g)$.
* Air resistance (drag) is neglected.

## 2. Equations of Motion (Analytical)
From Newton's second law, $\vec{F} = m\vec{a}$:
* $a_x = 0$
* $a_y = -g$

Integrating with respect to time ($t$) yields:
* $x(t) = x_0 + (v_0 \cos\theta)t$
* $y(t) = y_0 + (v_0 \sin\theta)t - \frac{1}{2}gt^2$

## 3. Numerical Integration (Forward Euler)
To solve this system numerically, we discretize time into steps of size $\Delta t$. The state at step $i+1$ is calculated from the state at step $i$:
1. $v_{x, i+1} = v_{x, i}$
2. $v_{y, i+1} = v_{y, i} - g \Delta t$
3. $x_{i+1} = x_i + v_{x, i} \Delta t$
4. $y_{i+1} = y_i + v_{y, i} \Delta t$