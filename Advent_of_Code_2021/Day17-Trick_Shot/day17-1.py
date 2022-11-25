# You finally decode the Elves' message. HI, the message says. You continue searching for 
# the sleigh keys.

# Ahead of you is what appears to be a large ocean trench. Could the keys have fallen into it? 
# You'd better send a probe to investigate.

# The probe launcher on your submarine can fire the probe with any integer velocity in the x 
# (forward) and y (upward, or downward if negative) directions. For example, an initial x,y 
# velocity like 0,10 would fire the probe straight up, while an initial velocity like 10,-1 would 
# fire the probe forward at a slight downward angle.

# The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. 
# On each step, these changes occur in the following order:

# The probe's x position increases by its x velocity.
# The probe's y position increases by its y velocity.
# Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 
# if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
# Due to gravity, the probe's y velocity decreases by 1.
# For the probe to successfully make it into the trench, the probe must be on some trajectory 
# that causes it to be within a target area after any step. The submarine computer has already 
# calculated this target area (your puzzle input). For example:

# target area: x=20..30, y=-10..-5
# This target area means that you need to find initial x,y velocity values such that after any step, 
# the probe's x position is at least 20 and at most 30, and the probe's y position is at 
# least -10 and at most -5.

# Given this target area, one initial velocity that causes the probe to be within the target 
# area after any step is 7,2:

# .............#....#............
# .......#..............#........
# ...............................
# S........................#.....
# ...............................
# ...............................
# ...........................#...
# ...............................
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTT#TT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# In this diagram, S is the probe's initial position, 0,0. The x coordinate increases to the right, 
# and the y coordinate increases upward. In the bottom right, positions that are within the target 
# area are shown as T. After each step (until the target area is reached), the position of 
# the probe is marked with #. (The bottom-right # is both a position the probe reaches and a 
# position in the target area.)

# Another initial velocity that causes the probe to be within the target area after any step is 6,3:

# ...............#..#............
# ...........#........#..........
# ...............................
# ......#..............#.........
# ...............................
# ...............................
# S....................#.........
# ...............................
# ...............................
# ...............................
# .....................#.........
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................T#TTTTTTTTT
# ....................TTTTTTTTTTT
# Another one is 9,0:

# S........#.....................
# .................#.............
# ...............................
# ........................#......
# ...............................
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTT#
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# One initial velocity that doesn't cause the probe to be within the target area 
# after any step is 17,-4:

# S..............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# .................#.............................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT..#.............................
# ....................TTTTTTTTTTT................................
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ................................................#..............
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ..............................................................#
# The probe appears to pass through the target area, but is never within it after any step. 
# Instead, it continues down and to the right - only the first few steps are shown.

# If you're going to fire a highly scientific probe out of a super cool probe launcher, 
# you might as well do it with style. How high can you make the probe go while still 
# reaching the target area?

# In the above example, using an initial velocity of 6,9 is the best you can do, causing 
# the probe to reach a maximum y position of 45. (Any higher initial y velocity causes 
# the probe to overshoot the target area entirely.)

# Find the initial velocity that causes the probe to reach the highest y position and 
# still eventually be within the target area after any step. What is the highest 
# y position it reaches on this trajectory?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day17-Trick_Shot\input.txt") as f:
    data = f.readlines()
    
#Given input
inp = []

#Parse input
for line in data:
    line = line.strip().split()
    inp.append(line)

inp = inp[0]
x_range = inp[2].split("=")[1].split("..")
y_range = inp[3].split("=")[1].split("..")

#Create range ist
x_range = list(range(int(x_range[0]),int(x_range[1][:-1])+1))
y_range = list(range(int(y_range[0]),int(y_range[1])+1))

#Variable to track best y
best = None

#Function that simualtes the shoot
def simulate(x_velocity,y_velocity):

    x = 0
    y = 0
    maxY = 0

    #Loop until we cross one of target bounds
    while x<= x_range[-1] and y >= y_range[0]:

        #Calcualte postiion
        x += x_velocity
        y += y_velocity

        #If it is higher y, remember ti
        if y > maxY:
            maxY = y

        #If we hit the target, then return
        if x in x_range and y in y_range:
            return (True,maxY)
        
        #Update velocities
        if x_velocity > 0:
            x_velocity -= 1
        y_velocity -= 1

        #If x velocitiy is 0 and we did not reach x target, then no point in looping more
        if x_velocity == 0 and x not in x_range:
            return(False,0)

    #If we didnt hit target, return False
    return (False,0)

#Variable to track best height
best_y = 0

#For x in range (0,x_target_max)
for x in range(x_range[-1]+1):

    #For y in range(y_target_min,-y_target_min) - we go up to maximally to -y_target_min
    #because for every y higher than that y will drop from 0 to below y_target_min in one step
    for y in range(y_range[0],abs(y_range[0])):

        #Simulate
        flag,best = simulate(x,y)

        #If solution is valid, track best Y
        if flag and best_y < best:

            best_y = best
            by = y
#Output
print("The highest y position it reaches on this trajector is :",best_y)