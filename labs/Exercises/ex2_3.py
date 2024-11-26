from math import pi, tan, cos

g = 9.81
y0 = 1
v0 = 44
x = 0.5
theta = 80 * (pi/180)

projectile_height = y0 + (x * tan(theta)) - ((g * pow(x, 2))/(2* (pow(v0 * cos(theta), 2))))

proj_height = y0 + x*tan(theta) - (g * x**2)/(2 * ((v0 * cos(theta))**2))

print(projectile_height)

print(proj_height)
