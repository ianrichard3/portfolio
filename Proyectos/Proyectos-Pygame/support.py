import math


def dist_points(p1, p2):
    return math.sqrt( (p2[0]-p1[0])**2 + (p2[1]-p2[1])**2 )


def angle_points(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])


def mid_point(p1, p2):
    return (p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2