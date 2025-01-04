import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
from IPython.display import HTML

# Simple flying in a straight line in terms of x and y coordinates

# Set up the boids

# Set the number of boids

boid_count = 10

# Define the edges of simulation area

limits = np.array([2000, 2000])

# Set the intial position of the boids
# Note: Position is an array of x and y coordinates with shape 2 x N 

# limits needs to be changed from (2,) to (2,1) to allow broadcasting
# (2, 10) * (2, 1) = (2, 10)
# Element-wise multiplication
# We multiply random positions and the limits to get the position of the boids within the limits
# as np.random.rand(2, boid_count) generates random positions between 0 and 1 (so it will always be within the limits)
positions = np.random.rand(2, boid_count) * limits[:, np.newaxis]
positions

# Define function
# Explaination: 
# 1. Lower_limits - (small_x, small_y)
# 2. Upper_limits - (big_x, big_y)
# 3. Width - (big_x - small_x, big_y - small_y)
def new_flock(count, lower_limits, upper_limits):
    width = upper_limits - lower_limits
    return lower_limits[:, np.newaxis] + np.random.rand(2, count) * width[:, np.newaxis]

positions = new_flock(10, np.array([100, 900]), np.array([200, 1100]))
print(positions)

# Define initial random velocities for the boids
# By using the previous function to save time

velocities = new_flock(boid_count, np.array([0, -20]), np.array([10, 20]))
print(velocities)

# change in velocity is defined as change in x/ change in time so change in x = change in time * change in velocity (with respect to time)

positions += velocities

# Matplotlib Animations

# Create plot of first frame of the initial positions of the boids

# Intial x position in [100, 200], initial y position in [900, 1100]
# initial x velocitiy in [0, 10], initial y velocitiy in [-20, 20]


figure = plt.figure()
axes = plt.axes(xlim=(0, limits[0]), ylim=(0, limits[1])) # Set the limits of the plot
scatter = axes.scatter(
    positions[0, :], positions[1, :], marker="o", edgecolors="k", lw = 0.5
)
scatter
plt.show()

# Update positions of boids in each timestep

def update_boids(positions, velocities):
    positions += velocities

def animate(frame):
    update_boids(positions, velocities)
    scatter.set_offsets(positions.T)

anim = animation.FuncAnimation(figure, animate, frames = 50, interval = 50)  

# Save out the figure:

positions = new_flock(100, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(100, np.array([0, -20]), np.array([10, 20]))
anim.save("/Users/jamesjlin/Desktop/Projects/pythonprojects-1/boids_algorithm/boids_1.gif")
HTML(anim.to_jshtml()) # Display the animation on the notebook  

# Fly towards the center of the flock

positions = new_flock(4, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(4, np.array([0, -20]), np.array([10, 20]))

positions
velocities

move_to_middle_strength = 0.01

# Update function to animate the central movement

def update_boids(positions, velocities):
    move_to_middle_strength = 0.01
    middle = np.mean(positions, 1)
    direction_to_middle = positions - middle[:, np.newaxis]
    velocities -= direction_to_middle * move_to_middle_strength
    positions += velocities

def animate(frame):
    update_boids(positions, velocities)
    scatter.set_offsets(positions.T)

anim = animation.FuncAnimation(figure, animate, frames = 50, interval = 50)

positions = new_flock(100, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(100, np.array([0, -20]), np.array([10, 20]))
HTML(anim.to_jshtml())
anim.save("/Users/jamesjlin/Desktop/Projects/pythonprojects-1/boids_algorithm/boids_2.gif")