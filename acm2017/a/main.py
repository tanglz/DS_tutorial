import numpy as np
from pytreemap import TreeSet

from acm2017.a.line import Line
from acm2017.a.vect import Vect

def point_in_poly(myl,lam):
    mypoint = myl.eval(lam)
    x = mypoint[0]
    y = mypoint[1]
    for i in range(n):
        if lines[i].contains(x,y):
            return True
    cross = 0
    for j in range(n):

        den = lines[i].dir.y + lines[i].dir.x;
        if (abs(den) < 1e-9):
            continue;
        subX = lines[i].s.x - x;
        subY = lines[i].s.y - y;
        num = -subX * lines[i].dir.y + subY * lines[i].dir.x;
        div = num / den;
        num2 = subY - subX;
        div2 = num2 / den;
        if (div > 1e-9 and div2 > 1e-6 and div2 < 1 - 1e-9):
            cross = cross+1
    return cross%2 == 1


def solve(myl, ll):
    sz = len(ll)
    maxF = ll[sz-1]-ll[0]

    lineLen = myl.seg_length()
    maxL = maxF*lineLen

    if maxL < res:
        return 0
    ans= 0
    cur = 0
    for i in range(sz-1):
        if not point_in_poly(myl,(ll[i]+ll[i+1])/2):
            cur = 0
            if (ll[sz-1]-ll[i+1])*lineLen < res:
                return ans
        cur = cur + lineLen*(ll[i+1]-ll[i])
        if cur>ans:
            ans = cur
    return ans


# inputs = input()
# l = inputs.split(',')
# print(l)
# l2 = list((map(int,l)))
# print(l2)
# n = l2[0]
# print(n)
# # example 1
# n = 3
# l2 = [0, 2017, -2017, -2017, 2017, 0]
# example 2
n = 7
l2 = [0,20,40, 0,40, 20,70, 50,50, 70,30, 50,0, 50]


# start test
vects = []
lines = []

i = 0
while i < len(l2):
    vects.append(Vect(l2[i],l2[i+1]))
    i = i+2

for j in range(n):
    lines.append(Line(vects[j], vects[(j+1)%n]))

res = 0
for p in range(n):
    for k in range(p+1,n):
        myl = Line(vects[p],vects[k])
        intersections = TreeSet()
        intersections.add(0.0)
        intersections.add(1.0)

        for z in range(n):
            temp = myl.intersect(lines[z])
            if temp is not None:
                intersections.add(temp)
        ll = []
        while intersections.size()>0:
            ll.append(intersections.poll_first())
        res = max(res, solve(myl,ll))
print(res)
