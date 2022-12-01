import random
import statistics as stat
import matplotlib.pyplot as plt
import numpy as np

def point_gen(num,min,max):
    points = []
    for x in range(num):
        point = (random.randint(min,max),random.randint(min,max))
        while point in points:
            point = (random.randint(min,max),random.randint(min,max))
        points.append(point)
    return points

def lin_reg(points):
    slopes = []
    intercepts = []
    for x in points:
        for y in points:
            if x[0] != y[0]:
                slope = (y[1]-x[1])/(y[0]-x[0])
                intercept = y[1]-(slope*y[0])
                slopes.append(slope)
                intercepts.append(intercept)
    avg_slope = stat.median(slopes)
    avg_intercept = stat.median_grouped(intercepts)
    return avg_slope,avg_intercept


points = point_gen(15,0,100)

slope,intercept = lin_reg(points)

x = np.array([point[0] for point in points])
y = np.array([point[1] for point in points])

rslope,rintercept = stat.linear_regression(x,y)

plt.plot(x,y,'o')

plt.plot(x,slope*x + intercept,color='red')

plt.plot(x,rslope*x + rintercept,color='blue')

plt.show()

print(points)
print(slope)
print(intercept)


