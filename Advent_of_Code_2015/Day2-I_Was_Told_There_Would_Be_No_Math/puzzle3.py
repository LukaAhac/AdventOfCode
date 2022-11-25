# The elves are running low on wrapping paper, and so they need to submit an order for more. 
# They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: 
# find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

# For example:

# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day2-I_Was_Told_There_Would_Be_No_Math\input.txt") as f:
    data = f.readlines()

area = 0

#For each present calculate area
for line in data:
    #Devide input by "x"
    sizes = line.strip().split("x")
    #Turn input into numbers
    sizes = list(map(lambda x: int(x), sizes))
    #Sort
    sizes.sort()
    #Calculate area: 3 * smallest side + 2 * second side + 2 * third side
    area += 3*sizes[0]*sizes[1] + 2*sizes[0]*sizes[2] + 2*sizes[1]*sizes[2]

print("They should order {} square feet of wrapping paper".format(area))