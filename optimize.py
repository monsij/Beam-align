import numpy as np
import matplotlib.pyplot as plt
from constants import *
from mpl_toolkits import mplot3d

SMALL_SIZE = 15
MEDIUM_SIZE = 16
BIGGER_SIZE = 18

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


beam_widh_avg = [0.5107132213,	2.253482713,	3.332988013,	5.402778179,
7.232845341,	9.132660372,   11.409317,	12.69019839,
14.58297946,    15.16578467,	18.31799185,	19.19034909,
21.97136459,	22.74056641,	23.87716745]

beam_widh_max = [1.390314647,	4.829486405,	6.467216062,	7.945709593,
11.49356875,	13.03281282,	15.7254996,	17.52626206,
20.28306692,	20.65942554, 24.1170712,	24.47597979,
30.37138547,	29.84894391,	31.27158444]

time_delay = list(0.1*np.array(range(1, 16, 1)))

beam_widh_max_rad = [np.radians(x) for x in beam_widh_max]

power_wastage = [x**2 for x in beam_widh_max_rad]

directivity = [ 2.0/(1-np.cos(x)) for x in beam_widh_max_rad]


d_scale = (max(directivity) -  min(directivity))/2.0
t_scale =(max(time_delay) - min(time_delay))/2.0


# print(beam_widh_avg)
# print(time_delay)
#
# plt.scatter(time_delay, beam_widh_avg, color= 'blue', label='$ \\bar{ \\theta} _{min}  $')
# plt.scatter(time_delay, beam_widh_max, color= 'red', marker='^', label='$ max\{\\theta_{min}\} $')
# plt.xlabel("$ t_{delay} $")
# plt.ylabel("$ \\theta_{min} $")
# plt.legend(loc=2)
# plt.grid()

# Optimization

# fig = plt.figure()
# ax = plt.axes(projection='3d')

X_data= []
Y_data= []
Z_data= []
t_delay_reci = [1.0/x for x in time_delay]

for A in range(A_min, A_max):
    for B in range(B_min, B_max):
        f1 = np.multiply(0.01*A, directivity)
        f2 = np.multiply(B, time_delay)
        BUDGET = np.add(f1,f2)
        # print(BUDGET)
        X_data.append(0.1*A)
        plt.plot(time_delay[2:], f1[2:])
        plt.plot(time_delay[2:], f2[2:], color='red', linewidth=0.1)
        # Z_data.append( beam_widh_max[list(BUDGET).index( BUDGET[9] )] )

print(len(X_data))

# ax.scatter3D(X_data, Y_data, Z_data, c=Z_data, alpha=0.3)

# plt.plot(beam_widh_max, f1, color = 'blue')
# plt.plot(beam_widh_max, f2, color = 'red')

# plt.plot(beam_widh_max, BUDGET)

# print(beam_widh_max[list(BUDGET).index(min(BUDGET))])
plt.ylabel('$ A \\cdot D , B \\cdot t_{delay}$')
plt.xlabel('Time delay')
# plt.zlabel('$ A\\cdot D + B\\cdot t_{delay}  $')
# plt.plot(beam_widh_max, BUDGET, color= 'green')
plt.show()
