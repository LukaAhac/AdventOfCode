# Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. 
# He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

# An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

# The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

# For example:

# (()) and ()() both result in floor 0.
# ((( and (()(()( both result in floor 3.
# ))((((( also results in floor 3.
# ()) and ))( both result in floor -1 (the first basement level).
# ))) and )())()) both result in floor -3.
# To what floor do the instructions take Santa?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day1-Not_Quite_Lisp\input.txt") as f:
    data = f.readlines()

#Input is only one row
data = data[0]

left_brackets = 0
right_brackets = 0

#Count the number of brackets
for symbol in data:
    if symbol == "(":
        left_brackets += 1
    else:
        right_brackets += 1

#Result is difference in numbers of left brackets and right brackets
result = left_brackets - right_brackets

print("Instructions will take Santa to the floor",result)