''' Problem statement
You have been given two sorted arrays/lists of closed intervals ‘INTERVAL1’ and ‘INTERVAL2’. A closed interval [x, y] with x < y denotes the set of real numbers ‘z’ with x <= z <= y.

Now, your task is to find the intersection of these two interval lists.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [0, 2] and [1, 3] is [1, 2].

 '''

 from os import *
from sys import *
from collections import *
from math import *

def intersectionIntervals(interval1, interval2, n1, n2):
    # Write your code here.
    i,j = 0,0
    intersections = []
    while i < n1 and j < n2 :

        a1, b1 = interval1[i] 
        a2, b2 = interval2[j]

        start = max (a1,a2)
        end = min(b1,b2)

        if start <= end :
            intersections.append([start, end])

        if b1 < b2 :
            i+=1
        else :
            j+=1

    return intersections
    

