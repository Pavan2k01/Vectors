import numpy as np
import matplotlib.pyplot as plt
import math

#line 1
def line1(x):
  return (2-3*x)
#line 2
def line2(x):
   return (-3+2*x)
def line3(x):
  return (3 - ((3 - 2*y_solution)/x_solution)*x)/2

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

# Define the x values for the lines
x_values = np.linspace(-10, 10, 100)

# Calculate the y values for each line
y_values1 = line1(x_values)
y_values2 = line2(x_values)
y_values3 = line3(x_values)

# Plot line 1
plt.plot(x_values, y_values1, label='3x + y - 2 = 0')

# Plot line 2
plt.plot(x_values, y_values2, label='2x - y - 3 = 0')

#plot solution line i.e line3
plt.plot(x_values, y_values3, label='5x + 2y -3 = 0')

# Plot the intersection point
plt.plot(x_solution, y_solution, 'ro', label='Intersection Point')

# Plot x and y axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Set the limits of the plot
def display_coordinates(x, y):
    plt.scatter(x, y, color='black')  # Plot the point
    plt.text(x, y, f'({x}, {y})', verticalalignment='bottom')
#display_coordinates((x_solution + y_solution), 0)
#display_coordinates(0,(x_solution + y_solution))
display_coordinates(math.trunc(x_solution), math.trunc(y_solution))

plt.xlim(-1, 3)
plt.ylim(-3, 1)
plt.legend()
