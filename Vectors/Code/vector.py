import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
#line 1
def line1(x):
  return (2-3*x)
#line 2
def line2(x):
  return (-3+2*x)

x, y = symbols('x y')

#Define the equations
eq1 = Eq(3*x + y - 2, 0)
eq2 = Eq(2*x - y - 3, 0)

#solve the equations
solution = solve((eq1, eq2), (x, y))

#Extract the solutions for x and y

x_solution = solution[x]
y_solution = solution[y]
print("Solution:")
print(f"x = {x_solution}")
print(f"y = {y_solution}")

def line3(x):
  return (3 - ((3 - 2*y_solution)/x_solution)*x)/2
  #return ((3 - 5*x)/2)
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

# Plot x and y axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Set the limits of the plot
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersection of Three lines at a point')

# Plot the intersection point
plt.plot(x_solution, y_solution, 'ro', label='Intersection Point')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()