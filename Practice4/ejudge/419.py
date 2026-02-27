import math
r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])
A = (x1, y1)
B = (x2, y2)
def dist_point_to_segment(p, a, b):
    dx, dy = b[0]-a[0], b[1]-a[1]
    if dx == 0 and dy == 0:
        return math.hypot(p[0]-a[0], p[1]-a[1])
    t = ((p[0]-a[0])*dx + (p[1]-a[1])*dy) / (dx*dx + dy*dy)
    t = max(0, min(1, t))
    closest = (a[0]+t*dx, a[1]+t*dy)
    return math.hypot(p[0]-closest[0], p[1]-closest[1])
if dist_point_to_segment((0,0), A, B) >= r:
    print(f"{distance(A,B):.10f}")
else:
    dA = math.hypot(x1, y1)
    dB = math.hypot(x2, y2)
    tA = math.sqrt(dA**2 - r**2)
    tB = math.sqrt(dB**2 - r**2)
    angleA = math.atan2(y1, x1)
    angleB = math.atan2(y2, x2)
    alphaA = math.acos(r/dA)
    alphaB = math.acos(r/dB)
    theta = (angleB - angleA) % (2*math.pi)
    if theta > math.pi:
        theta = 2*math.pi - theta
    arc = theta - alphaA - alphaB
    total = tA + tB + r*arc
    print(f"{total:.10f}")