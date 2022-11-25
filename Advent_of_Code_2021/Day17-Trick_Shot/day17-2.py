# Maybe a fancy trick shot isn't the best idea; after all, you only have one probe, 
# so you had better not miss.

# To get the best idea of what your options are for launching the probe, you need to find every 
# initial velocity that causes the probe to eventually be within the target area after any step.

# In the above example, there are 112 different initial velocity values that meet these criteria:

# 23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
# 25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
# 8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
# 26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
# 20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
# 25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
# 25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
# 8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
# 24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
# 7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
# 23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
# 27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
# 8,-2    27,-8   30,-5   24,-7
# How many distinct initial velocity values cause the probe to be within the target area after any step?

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

counter = 0

#For x in range (0,x_target_max)
for x in range(x_range[-1]+1):

    #For y in range(y_target_min,-y_target_min) - we go up to maximally to -y_target_min
    #because for every y higher than that y will drop from 0 to below y_target_min in one step
    for y in range(y_range[0],abs(y_range[0])):

        #Simulate
        flag,noNeedHere = simulate(x,y)

        #If solution is valid, increment counter
        if flag:

            counter += 1

#Output
print(counter,"distinct initial velocity values cause the probe to be within the target area after any step.")