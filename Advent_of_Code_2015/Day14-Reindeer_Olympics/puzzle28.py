# Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

# Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, 
# they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

# Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until 
# several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since 
# Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

# After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, 
# Dancer would win (if the race ended at 1000 seconds).

# Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day14-Reindeer_Olympics\input.txt") as f:
    data = f.readlines()

#Race time in seconds
race_time = 2503
#Dictionary to track new scoring system
new_scoring_system = dict()

#For each second look who has traveled furthest
for time in range(1,race_time+1):
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
        times_flying_and_resting = time // (time_flying+time_resting)
        #Calculate the distance he has flown in that time
        distance_flown[information[0]] = times_flying_and_resting * speed * time_flying
        #Calculate the remaining time of the race
        time_left = time % (time_flying+time_resting)
        #If remaining time is bigger than time he can fly, add distance that he can fly in one go (Remaining time he will be resting so we dont need to worry about that)
        if time_left >= time_flying:
            distance_flown[information[0]] += speed * time_flying
        #Else add distance he can fly in remaining time
        else:
            distance_flown[information[0]] += speed * time_left

    #Sort dictionary by distances flown
    distance_flown = dict(sorted(distance_flown.items(), key = lambda x: x[1], reverse = True))

    #Look what is the best distance for that race time
    best_distance = distance_flown[list(distance_flown.keys())[0]]
    #List of the reindeers that will get a point
    scored_point = []

    #If a reindeer has the best distance add him to the list
    for key in distance_flown.keys():
        if distance_flown[key] == best_distance:
            scored_point.append(key)

    #Give each reindeer in a list one point
    for reindeer in scored_point:
        if reindeer in new_scoring_system:
            new_scoring_system[reindeer] += 1
        else:
            new_scoring_system[reindeer] = 1

#Sort final points
new_scoring_system = dict(sorted(new_scoring_system.items(), key = lambda x: x[1], reverse = True))

print("The winning reindeer has {} points".format(new_scoring_system[list(new_scoring_system.keys())[0]]))