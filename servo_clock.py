import numpy as np
import math

chars = {
    "0": [[0,72],[2,74],[3,77],[4,80],[7,82],[9,84],[11,85],[13,86],[15,87],[17,88],[19,89],[22,89],[25,89],[27,87],[30,86],[34,84],[37,81],[39,78],[41,74],[43,70],[43,66],[45,63],[45,59],[45,56],[45,52],[46,47],[47,41],[47,36],[48,32],[48,28],[48,23],[48,19],[48,14],[48,10],[48,6],[48,3],[48,0],[46,-3],[44,-4],[41,-5],[38,-6],[35,-7],[32,-7],[30,-8],[27,-8],[24,-8],[20,-8],[17,-7],[14,-5],[12,-2],[10,2],[8,4],[6,6],[5,9],[4,11],[4,15],[3,19],[3,23],[3,27],[3,30],[3,33],[2,37],[2,41],[1,46],[1,50],[1,54],[1,58],[1,61],[1,64],[1,67],[1,70]],
    "1": [[2,68],[4,71],[6,73],[8,74],[9,76],[11,78],[12,80],[14,81],[16,82],[17,84],[19,86],[21,88],[21,85],[21,81],[21,76],[21,70],[21,66],[21,62],[21,58],[21,54],[21,50],[21,46],[21,42],[21,39],[21,35],[21,32],[22,27],[22,23],[23,21],[23,17],[24,14],[24,10],[24,7],[21,7],[15,7],[10,7],[6,7],[3,7],[5,7],[13,7],[19,7],[25,8],[29,9],[32,9],[35,10],[38,10],[41,10],[44,10],[45,10],[42,10],[39,9],[37,8],[33,8],[30,7],[26,7]],
    "2": [[1,70],[3,73],[4,75],[7,77],[9,80],[11,82],[15,84],[18,85],[20,86],[24,86],[27,86],[30,84],[33,80],[35,76],[37,72],[37,67],[37,61],[37,57],[37,54],[36,50],[34,46],[31,42],[27,37],[23,34],[19,31],[15,29],[12,26],[8,23],[6,21],[3,19],[1,18],[5,18],[15,19],[24,19],[30,19],[34,20],[37,21],[40,21]],
    ".": [[5,16],[5,17]]
}

def plot_point(p, l):
    x, y = p
    theta1 = math.acos((math.sqrt(x**2 + y**2)/2)/l) + math.acos(x/math.sqrt(x**2 + y**2))
    theta2 = 2*math.acos((math.sqrt(x**2 + y**2)/2)/l)
    return (theta1, theta2)

def draw_time(time):
    greatest = 0
    for char in list(time):
        char = chars.get(char)
        for coord in char:
            adj = [(coord[0] + greatest + 5)/10, coord[1]/10]
            plot_point(adj, length)
        greatest = greatest + max(char, key = lambda x: x[0])[0]

length = 11.9
draw_time("1.02")