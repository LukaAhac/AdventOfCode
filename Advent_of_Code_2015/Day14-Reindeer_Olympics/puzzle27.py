# This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. 
# Santa would like to know which of his reindeer is fastest, and so he has them race.

# Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

# For example, suppose you have the following Reindeer:

# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
# After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, 
# Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. 
# They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

# In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). 
# So, in this situation, Comet would win (if the race ended at 1000 seconds).

# Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day14-Reindeer_Olympics\input.txt") as f:
    data = f.readlines()

#Race time in seconds
race_time = 2503
#Dictionary to trcat distance per reindeer
distance_flown = dict()

#For each reindeer calculte distnace he has flown
for information in data:
    information = information.strip().split()

    #Flying speed
    speed = int(information[3])
    #How long he can fly
    time_flying = int(information[6])
    #How long he needs to rest
    time_resting = int(information[-2])

    #Calculate how many times he has flown and rested
    times_flying_and_resting = race_time // (time_flying+time_resting)
    #Calculate the distance he has flown in that time
    distance_flown[information[0]] = times_flying_and_resting * speed * time_flying
    #Calculate the remaining time of the race
    time_left = race_time % (time_flying+time_resting)
    #If remaining time is bigger than time he can fly, add distance that he can fly in one go (Remaining time he will be resting so we dont need to worry about that)
    if time_left >= time_flying:
        distance_flown[information[0]] += speed * time_flying
    #Else add distance he can fly in remaining time
    else:
        distance_flown[information[0]] += speed * time_left

#Sort dictionary by distances flown
distance_flown = dict(sorted(distance_flown.items(), key = lambda x: x[1], reverse = True))

print("The winning reindeer has traveled {} distance".format(distance_flown[list(distance_flown.keys())[0]]))