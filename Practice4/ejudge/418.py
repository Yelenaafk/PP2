x0, y0 = map(float, input().split())
x1, y1 = map(float, input().split())
x_reflect = x0 + y0 * (x1 - x0) / (y0 + y1)
y_reflect = 0.0
print(f"{x_reflect:.10f} {y_reflect:.10f}")