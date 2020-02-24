import sys
import numpy as np

def cost(X,Y,theta):
    sum = 0
    for i in range(len(X)):
        sum += (X[i]+theta - Y[i])**2
    return sum

def descent(X,Y):
    theta = X[0]
    if theta == 0:
        theta = 10

    while True:
        mid_cost = cost(X,Y,theta)
        neg_cost = cost(X,Y,theta/1.5)
        pos_cost = cost(X,Y,theta*1.5)

        if pos_cost < mid_cost:
            theta = theta*2
        elif neg_cost < mid_cost:
            theta = theta/2
        else:
            while True:
                mid_cost = cost(X,Y,theta)
                neg_cost = cost(X,Y,theta/1.00001)
                pos_cost = cost(X,Y,theta*1.00001)
                if pos_cost < mid_cost:
                    theta = theta*1.00001
                elif neg_cost < mid_cost:
                    theta = theta/1.00001
                else:
                    return theta

while True:
    start_line = sys.stdin.readline().split()
    if start_line:
        N = int(start_line[0])
        X = []
        Y = []
        for i in range(N):
            (x,y) = sys.stdin.readline().split()
            X.append(int(x))
            Y.append(int(y))
        a = round(descent(X,Y),6)

        print("{0:.6f}".format(a))
    else:
        break
