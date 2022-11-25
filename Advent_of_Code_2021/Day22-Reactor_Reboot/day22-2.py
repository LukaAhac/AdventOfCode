# Now that the initialization procedure is complete, you can reboot the reactor.

# Starting with all cubes off, run all of the reboot steps for all cubes in the reactor.

# Consider the following reboot steps:

# on x=-5..47,y=-31..22,z=-19..33
# on x=-44..5,y=-27..21,z=-14..35
# on x=-49..-1,y=-11..42,z=-10..38
# on x=-20..34,y=-40..6,z=-44..1
# off x=26..39,y=40..50,z=-2..11
# on x=-41..5,y=-41..6,z=-36..8
# off x=-43..-33,y=-45..-28,z=7..25
# on x=-33..15,y=-32..19,z=-34..11
# off x=35..47,y=-46..-34,z=-11..5
# on x=-14..36,y=-6..44,z=-16..29
# on x=-57795..-6158,y=29564..72030,z=20435..90618
# on x=36731..105352,y=-21140..28532,z=16094..90401
# on x=30999..107136,y=-53464..15513,z=8553..71215
# on x=13528..83982,y=-99403..-27377,z=-24141..23996
# on x=-72682..-12347,y=18159..111354,z=7391..80950
# on x=-1060..80757,y=-65301..-20884,z=-103788..-16709
# on x=-83015..-9461,y=-72160..-8347,z=-81239..-26856
# on x=-52752..22273,y=-49450..9096,z=54442..119054
# on x=-29982..40483,y=-108474..-28371,z=-24328..38471
# on x=-4958..62750,y=40422..118853,z=-7672..65583
# on x=55694..108686,y=-43367..46958,z=-26781..48729
# on x=-98497..-18186,y=-63569..3412,z=1232..88485
# on x=-726..56291,y=-62629..13224,z=18033..85226
# on x=-110886..-34664,y=-81338..-8658,z=8914..63723
# on x=-55829..24974,y=-16897..54165,z=-121762..-28058
# on x=-65152..-11147,y=22489..91432,z=-58782..1780
# on x=-120100..-32970,y=-46592..27473,z=-11695..61039
# on x=-18631..37533,y=-124565..-50804,z=-35667..28308
# on x=-57817..18248,y=49321..117703,z=5745..55881
# on x=14781..98692,y=-1341..70827,z=15753..70151
# on x=-34419..55919,y=-19626..40991,z=39015..114138
# on x=-60785..11593,y=-56135..2999,z=-95368..-26915
# on x=-32178..58085,y=17647..101866,z=-91405..-8878
# on x=-53655..12091,y=50097..105568,z=-75335..-4862
# on x=-111166..-40997,y=-71714..2688,z=5609..50954
# on x=-16602..70118,y=-98693..-44401,z=5197..76897
# on x=16383..101554,y=4615..83635,z=-44907..18747
# off x=-95822..-15171,y=-19987..48940,z=10804..104439
# on x=-89813..-14614,y=16069..88491,z=-3297..45228
# on x=41075..99376,y=-20427..49978,z=-52012..13762
# on x=-21330..50085,y=-17944..62733,z=-112280..-30197
# on x=-16478..35915,y=36008..118594,z=-7885..47086
# off x=-98156..-27851,y=-49952..43171,z=-99005..-8456
# off x=2032..69770,y=-71013..4824,z=7471..94418
# on x=43670..120875,y=-42068..12382,z=-24787..38892
# off x=37514..111226,y=-45862..25743,z=-16714..54663
# off x=25699..97951,y=-30668..59918,z=-15349..69697
# off x=-44271..17935,y=-9516..60759,z=49131..112598
# on x=-61695..-5813,y=40978..94975,z=8655..80240
# off x=-101086..-9439,y=-7088..67543,z=33935..83858
# off x=18020..114017,y=-48931..32606,z=21474..89843
# off x=-77139..10506,y=-89994..-18797,z=-80..59318
# off x=8476..79288,y=-75520..11602,z=-96624..-24783
# on x=-47488..-1262,y=24338..100707,z=16292..72967
# off x=-84341..13987,y=2429..92914,z=-90671..-1318
# off x=-37810..49457,y=-71013..-7894,z=-105357..-13188
# off x=-27365..46395,y=31009..98017,z=15428..76570
# off x=-70369..-16548,y=22648..78696,z=-1892..86821
# on x=-53470..21291,y=-120233..-33476,z=-44150..38147
# off x=-93533..-4276,y=-16170..68771,z=-104985..-24507
# After running the above reboot steps, 2758514936282235 cubes are on. (Just for fun, 474140 of those 
# are also in the initialization procedure region.)

# Starting again with all cubes off, execute all reboot steps. Afterward, considering all cubes, how many cubes are on?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day22-Reactor_Reboot\input.txt") as f:
    data = f.readlines()
    
#Given input
inp = []

#Parse input
for line in data:
    line = line.strip().split()
    inp.append(line)

#List of cubes that are whole turned on
cubes = []

#Function that splits thecube and returns the cubes that does not need to be affected
def splitCube(axisRangeCoords,workingCube):


    #Unaffecetd cubes are section of the cube that needs no action taken on them
    #While working cube is the cube we are working on, the cube that passes to next steps
    unaffectedCubes = []
    workingCube = r

    #Go over each axis of the cube
    for axis in range(3):

        #Get the current axis range
        axisFrom = axisRangeCoords[axis*2]
        axisTo = axisRangeCoords[axis*2+1]

        #If the range does not intersect with the cube axis then there is no action needed on that cube
        if axisTo < workingCube[axis*2] or axisFrom > workingCube[axis*2+1]:
            #Return None and the flag that we have not splitted the cube
            return (None,False)

        #If the whole cube axis is cointained within the given range, then we need to work on the whole axis of the cube
        elif axisFrom <= workingCube[axis*2] <= workingCube[axis*2+1] <= axisTo:
            workingCube = workingCube

        #If the cube axis contains whole axis range within itself, then split that cube into 3 new cubes
        #Left and right are the cubes that do not intersect with the axis and needs no action on them
        #While the middle cube needs to be affected
        elif workingCube[axis*2] < axisFrom < axisTo < workingCube[axis*2+1]:
            
            unaffectedCubes.append([workingCube[0],workingCube[1],workingCube[2],workingCube[3],workingCube[4],workingCube[5]])
            unaffectedCubes[-1][axis*2+1] = axisFrom-1
            unaffectedCubes.append([workingCube[0],workingCube[1],workingCube[2],workingCube[3],workingCube[4],workingCube[5]])
            unaffectedCubes[-1][axis*2] = axisTo+1

            workingCube = [workingCube[0],workingCube[1],workingCube[2],workingCube[3],workingCube[4],workingCube[5]]
            workingCube[axis*2] = axisFrom
            workingCube[axis*2+1] = axisTo

        #Case when the staring range is inside the cube axis, split the cube into two pieces
        #Left piece needs no affection while the right one needs to be affected
        elif workingCube[axis*2] < axisFrom <= workingCube[axis*2+1]:

            unaffectedCubes.append([workingCube[0],workingCube[1],workingCube[2],workingCube[3],workingCube[4],workingCube[5]])
            unaffectedCubes[-1][2*axis+1] = axisFrom-1
            workingCube = [workingCube[0],workingCube[1],workingCube[2],workingCube[3],workingCube[4],workingCube[5]]
            workingCube[2*axis] = axisFrom

        #Last case si when the ending range is inside the cube, again split cube into two peices
        #Left piece needs to be affected, while right piece does not need to be affected
        elif  workingCube[axis*2] <= axisTo < workingCube[axis*2+1]:

            unaffectedCubes.append([workingCube[0],workingCube[1],workingCube[2],workingCube[3],workingCube[4],workingCube[5]])
            unaffectedCubes[-1][2*axis] = axisTo+1
            workingCube = [workingCube[0],workingCube[1],workingCube[2],workingCube[3],workingCube[4],workingCube[5]]
            workingCube[axis*2+1] = axisTo

    #Return the cubes that does not need to be affected, and flag that we have splitted the cube
    return (unaffectedCubes,True)




#Performe each instruction
for ins in inp:

    #Pare instrcution
    asd = ins[1].split(",")

    x = asd[0].split("..")
    xfrom = int(x[0][2:])
    xto = int(x[1])

    y = asd[1].split("..")
    yfrom = int(y[0][2:])
    yto = int(y[1])

    z = asd[2].split("..")
    zfrom = int(z[0][2:])
    zto = int(z[1])

    #List of coordination ranges for the affected cube
    coords = [xfrom,xto,yfrom,yto,zfrom,zto]

    #List for cubes that will be in next iteration
    nextCubes = []

    #For each cube in the list of cubes that are on, check wheter there exist an intersection between them and 
    #cube that needs to be affecte
    #The idea is to check each axis separately (x -> y -> z) and split the cube into sections where there will
    #be one section that needs to be affected and the remaining, one or two, sections that needs no action taken on them
    #There needs to be an intersection on each of the three axis for the two cubes to have intersection, if we find
    #and axis that has no intersection we know that those cubse wont intersect and we keep the cube as a whole and 
    #continue to the next one
    for r in cubes:

        #Split the cube in a way that we take out the intersection of the cubes
        unaffectedCubes,intercestionExists = splitCube(coords,r)

        #If we did not split the cube because there are no intersection between them then add original cube to the list
        #for next iteration and go to the next cube
        if not intercestionExists:
            nextCubes.append(r)
            continue
        
        #Otherwise add all new cubes to the list
        for cr in unaffectedCubes:

            nextCubes.append(cr)

    #If instruction was sto turn on the cube, then add the intersection cube to the list aswell
    #If the instrcution was tu turn off the cube then we dont need to do anything else since we already 
    #removed the intersection from the cubes that are oon
    if ins[0] == "on":
        nextCubes.append([xfrom,xto,yfrom,yto,zfrom,zto])

    cubes = nextCubes

#Count the little 1x1x1 cubes that are on
#Basically we are calculating the volumes of the big cubes that are on and summing them
counter = 0

for r in cubes:

    counter += (r[1]-r[0]+1)*(r[3]-r[2]+1)*(r[5]-r[4]+1)

print(counter,"cubes are on.")