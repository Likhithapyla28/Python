from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
S=int(input())
E=int(input())
W=int(input())
for i in range(S,E,W):
    c=((i-32)*5)/9
    if(c>0):
        print(i,"\t",floor(c))
    else:
        print(i,"\t",ceil(c))























