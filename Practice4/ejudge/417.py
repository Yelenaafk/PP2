import math
R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
dx = x2 - x1
dy = y2 - y1
a = dx*dx + dy*dy
b = dx*x1 + dy*y1
c = x1*x1 + y1*y1 - R*R
discriminant = b*b - a*c
if discriminant < 0:
    length_inside = 0.0
else:
    sqrt_disc = math.sqrt(discriminant)
    t1 = (-b - sqrt_disc) / a
    t2 = (-b + sqrt_disc) / a
    t_in = max(0, min(t1, t2))
    t_out = min(1, max(t1, t2))
    if t_out < t_in:
        length_inside = 0.0
    else:
        length_inside = (t_out - t_in) * math.sqrt(a)
print(f"{length_inside:.10f}")