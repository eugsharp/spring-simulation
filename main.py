import matplotlib.pyplot as plt

l = 5 # equilibrium length of the spring
k = 0.1 # spring constant
m = 1 # mass of the object attached to the spring
x = l + 2 # position 
x_dot = 0 # velocity
delta_t = 0.01 # small time step
t = 0 # current time
total_time = 100

# lists to store results
x_values = [x]
t_values = [t]

# simulation loop
for n in range(int(total_time/delta_t)):
    x_doubledot = -k * (x - l) / m  
    
    # update velocity and position using Euler integration
    x_dot += x_doubledot * delta_t
    x += x_dot * delta_t
    t += delta_t

    # store results
    x_values.append(x)
    t_values.append(t)

# plotting x vs t
plt.figure(figsize=(8, 5))
plt.plot(t_values, x_values)
plt.title("Displacement vs Time (Spring Oscillation)")
plt.xlabel("Time (t)")
plt.ylabel("Displacement (x)")
plt.grid(True)
plt.legend()
plt.show()