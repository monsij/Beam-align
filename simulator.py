from constants import *
import numpy as np
import matplotlib.pyplot as plt

def findAngle(x,y):
    if x< 0 and y> 0:
        return 180.0 +(180.0/np.pi)*np.arctan(y/x)
    if x>0 and y> 0:
        return (180.0/np.pi)*np.arctan(y/x)

def pos_error():
    return np.random.normal(3,1)

def change_velx():
    return np.random.choice([-1,1])*np.random.normal(max_acc, 1)

def change_vely():
    return np.random.choice([-1,1])*np.random.normal(max_acc*0.01, 1)

class Vehicle:
    x, y, vx, vy = None, None, None, None
    def __init__(self, x, y, vx, vy):
        self.x= x
        self.y= y
        self.vx= vx
        self.vy= vy

    def update(self):
        self.vx = self.vx + change_velx()
        self.vy = self.vy + change_vely()
        self.x = self.x + self.vx*time_step
        self.y = self.y + self.vy*time_step

class Antenna:
    angle = 0.0
    new_angle = 0.0
    def __init__(self, angle):
        self.angle= angle
        self.new_angle = angle

    def CalculateNext(self, x, y, vx, vy):
        tan_theta= y/x
        A = (vx*tan_theta - vy)/x
        B = (vx + vy*tan_theta)/x
        C = 1 + tan_theta**2

        delta = (A - omega_max*C )/(omega_max*B)
        self.new_angle = 90.0 + (180.0/np.pi)*np.arctan((y + vy*delta)/(x + vx*delta))

    def steerBeam(self):
        self.angle = self.new_angle
        # while self.angle > self.new_angle:
        #     self.angle = self.angle - omega_max*time_step

    def inRange(self, vehicle):
        current_angle = findAngle(vehicle.x, vehicle.y)
        # x= int(input())
        # if np.abs(current_angle- self.angle) < beam_width:
        #     return True
        # return False
        return True

def main(plot_):
    v = Vehicle(-L/2, H+lane_width/2, v_max , 0)
    a = Antenna(135.0)

    V_angles = []
    A_angles = []

    while v.x < L/2 :
        # print(v.x)
        if a.inRange(v):
            # print('In Range')
            # send details to the antenna and calculate next position
            a.CalculateNext(v.x+pos_error(), v.y+pos_error(), v.vx, v.vy)
            # x= input()

            # steer beam in that direction
            a.steerBeam()

            # print(v.x, v.y)

        # update position of the car
        v.update()

        V_angles.append(findAngle(v.x, v.y))
        A_angles.append(a.angle)



    try:
        if plot_ is True:
            # plt.plot(list(range(len(V_angles))), V_angles, color='red')
            # plt.plot(list(range(len(A_angles))), A_angles, color='blue')
            # plt.show()
            pass

        beamwidth_reqd = np.abs(np.sum(np.add(A_angles, np.multiply(-1.0, V_angles)))/len(A_angles))
        return beamwidth_reqd
    except:
        return 0.0

for j in range(10):
    print(main(plot_=True))
