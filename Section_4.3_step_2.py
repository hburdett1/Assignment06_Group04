import numpy as np
import matplotlib.pyplot as plt

# equations 8-10 are necessary for equation 1
# Equation 8
def canopEvap(Sc, Sc_max = 3.0, nonlinear_wf = 2/3, Ep = 5):
    return [(Ep*(n/Sc_max)**nonlinear_wf) if n<Sc_max else (Ep*1) for n in Sc]

# Equation 9
def canopThro(Sc, SC_max = 3.0, P=100.0):
    return [(P*n/SC_max) if n<SC_max else P for n in Sc]

# Equation 10
def canopDrain(Sc, Sc_max = 3.0, kcan = 0.5):
    return [0 if n<Sc_max else (kcan*(n-Sc_max)) for n in Sc]

# Equation 1
def dSc_dt(Sc, P = 100):
    return [(P - canopEvap([n])[0] - canopThro([n])[0] - canopDrain([n])[0]) for n in Sc]

# one day interval
Sc = [0] # setting the initial value to zero
t = np.arange(0, 10, 1) # indicating the time steps, so the time step starts at zero, will repeat for 10 days at an interval of 1 day

for n in t[1:]: # a for loop is utilized to compute each interception storage value for each of the 10 days
    Sc.append(Sc[n-1] + dSc_dt([n-1])[0] * 1) # the values are added to the empty list

print(t, Sc)
plt.plot(t, Sc, color='r')
plt.xlabel('Time (days)')
plt.ylabel('Interception storage (mm/day)')
plt.title("One Day Interval")
plt.show()


# one hour interval
Sc = [0]
t = np.arange(0, 10, 0.042) # indicating the time steps, so the time step starts at zero, will repeat for 10 days at an interval of 1 hour

for n in t[1:]:
    Sc.append(Sc[-1] + dSc_dt([n-0.042])[0] * 0.042)

plt.plot(t, Sc)
plt.xlabel('Time (days)')
plt.ylabel('Interception storage (mm/day)')
plt.title("One hour Interval")
plt.show()

# 5 min interval
Sc = [0]
t = np.arange(0, 10, 0.0035)

for n in t[1:]:
    Sc.append(Sc[-1] + dSc_dt([n-0.0035])[0] * (0.0035)) # indicating the time steps, so the time step starts at zero, will repeat for 10 days at an interval of 5 minutes

plt.plot(t, Sc, color='g')
plt.xlabel('Time (days)')
plt.ylabel('Interception storage (mm/day)')
plt.title("Five Minute Interval")
plt.show()

# when the timestep interval is changed fromm daily to hourly and 5-min the model similations improve
# this is likely due to the increase in points that fill in the "missing" values present between the daily intervals
