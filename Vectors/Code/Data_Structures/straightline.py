import numpy as np
import matplotlib.pyplot as plt
import math

#Define the coefficient matrix
A = np.array([[3, 1], [2, -1]])

#Defne the Vector
b = np.array([2, 3])

#solve the equations
solution = np.linalg.solve(A, b)

#Extract the Values
x_solution = solution[0]
y_solution = solution[1]
p_solution = (3-2*y_solution)/(x_solution)

#print the values
print(f"x : {math.trunc(x_solution)}")
print(f"y : {math.trunc(y_solution)}")
print(f"p : {math.trunc(p_solution)}")

m1 = -3 # slope of the 1st line
m2 =2
m3 =-p_solution/2

def line_dir_pt(m, P, k1, k2):
    length = 10
    dimensions = P.shape[0]
    x_AB = np.zeros((dimensions, length))
    lam_1 = np.linspace(k1, k2, length)
    for i in range(length):
        temp1 = P + lam_1[i] * m
        x_AB[:, i] = temp1.T
    return x_AB

# Input parameters
P = np.array([x_solution, y_solution])

# Generating the lines
k1 = -3
k2 = 3  # Adjusted range for Line 1
x_m1P = line_dir_pt(np.array([1, m1]),P , k1, k2)
x_m2P = line_dir_pt(np.array([1, m2]), P, k1, k2)
x_m3P = line_dir_pt(np.array([1, m3]), P, k1, k2)

# Plotting the lines
plt.plot(x_m1P[0, :], x_m1P[1, :], label='Line 1: 3x+y=2')
plt.plot(x_m2P[0, :], x_m2P[1, :], label='Line 2: 2x-y=3')
plt.plot(x_m3P[0, :], x_m3P[1, :], label='Line 3: 5x+2y = 3')

# Labeling the coordinates
tri_coords = np.vstack((P,)).T
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, (tri_coords[0, i], tri_coords[1, i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.grid(True)
plt.title('Line Equations')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
#plt.savefig('/home/nani/Codes/Data_Structures/figs/figure1.png')
