#include <iostream>
#include <fstream>
#include <vector>
#include "utils.cpp"
#include <algorithm>
#include <map>

/*
Function that checks wheter the remaining positions correctly correlate to the accelerations
In the long term particles with the bigger acceleration will always be further away from origin than a particle
with a smaller acceleration.
This function checks wheter we have achieved that state.
When we are in this state we know that there will be no more intersection of particles because particles can no
longer surpass each other because the one that moves(accelerates) the most is also furthest away an no particle
ever can surpass it
*/
bool testPositionsOverAccelerations(const std::vector<std::vector<int>>& positions, 
    const std::vector<std::vector<int>>& accelerations){

    std::vector<int> indexes;

    for(int i = 0; i < positions.size(); i++){
        indexes.push_back(i);
    }

    std::sort(indexes.begin(),indexes.end(),[accelerations](int a, int b){return (abs(accelerations[a][0]) + 
        abs(accelerations[a][1]) + abs(accelerations[a][2])) > (abs(accelerations[b][0]) + abs(accelerations[b][1]) + 
        abs(accelerations[b][2]));});

    for(int i = 0; i < positions.size()-1; i++){
        int idx1 = indexes[i];
        int idx2 = indexes[i+1];

        //If we encounter the particles with the same absolute acceleration we ignore it since we cannot know which one
        //should be further witohut looking at their initiall positions
        if((abs(accelerations[idx1][0]) + abs(accelerations[idx1][1]) + abs(accelerations[idx1][2])) ==
            (abs(accelerations[idx2][0]) + abs(accelerations[idx2][1]) + abs(accelerations[idx2][2]))) continue;

        if((abs(positions[idx1][0]) + abs(positions[idx1][1]) + abs(positions[idx1][2])) < (abs(positions[idx2][0]) + 
        abs(positions[idx2][1]) + abs(positions[idx2][2]))) return false;
    }

    return true;

}


int main(void){

    std::ifstream infile("day20.txt");

    std::vector<std::vector<int>> positions, velocities, accelerations;
    std::string line;

    //Read input data
    while(std::getline(infile, line)){
        std::vector<std::string> temp = splitby(line, ' ');
        std::vector<std::string> temp2;
        std::vector<int> temp3;

        temp2 = splitby(temp[0].substr(3,temp[0].size()-5), ',');
        for(int i = 0; i < 3; i++){
            temp3.push_back(std::stoi(temp2[i]));
        }
        positions.push_back(temp3);

        temp2 = splitby(temp[1].substr(3,temp[1].size()-5), ',');
        temp3.clear();
        for(int i = 0; i < 3; i++){
            temp3.push_back(std::stoi(temp2[i]));
        }
        velocities.push_back(temp3);

        temp2 = splitby(temp[2].substr(3,temp[2].size()-4), ',');
        temp3.clear();
        for(int i = 0; i < 3; i++){
            temp3.push_back(std::stoi(temp2[i]));
        }
        accelerations.push_back(temp3);
    }
    infile.close();

    /*
    Part1
    Need to find out which particle will be the closest to the origin in the long term
    That will be the one with the lowest acceleration calculated by summing absolute accelerations over all of the three
    axis, that type of acceleration will tell us what is the accelreation of the parcticle going away from the origin
    If there are multiple particles with the same value of that accelreation then we will find the closest by looking their
    distance to the origin after performing few iterations of the movement untl we are sure that all of them are going away
    and not going clsoer to the origin.
    */
    int smallestAcceleration = abs(accelerations[0][0]) + abs(accelerations[0][1]) + abs(accelerations[0][2]);
    std::vector<int> indexesWithSameSmallestAcceleration = {0};

    //Calculate smallest acceleration vector
    for(int i = 1; i < accelerations.size();i++){
        int curr = abs(accelerations[i][0]) + abs(accelerations[i][1]) + abs(accelerations[i][2]);

        if(curr < smallestAcceleration){
            smallestAcceleration = curr;
            indexesWithSameSmallestAcceleration.clear();
            indexesWithSameSmallestAcceleration.push_back(i);
        }
        else if(curr == smallestAcceleration) indexesWithSameSmallestAcceleration.push_back(i);
    }
    //If we have more then one with equaly small accelerations decide for one, otherwise print one that we have
    if(indexesWithSameSmallestAcceleration.size() > 1){
        bool allGoingAway = false;

        std::vector<std::vector<int>> positionsCopy = positions;
        std::vector<std::vector<int>> velocitiesCopy = velocities;

        //Perform movements until all particles are going away from origin
        while(!allGoingAway){

            allGoingAway = true;

            for(int i = 0; i < indexesWithSameSmallestAcceleration.size(); i++){
                int currIndex = indexesWithSameSmallestAcceleration[i];

                for(int j = 0; j < 3; j++){
                    velocitiesCopy[i][j] += accelerations[i][j];
                }

                int oldDistance = abs(positionsCopy[i][0]) + abs(positionsCopy[i][1]) + abs(positionsCopy[i][2]);

                for(int j = 0; j < 3; j++){
                    positionsCopy[i][j] += velocitiesCopy[i][j];
                }

                int newDistance = abs(positionsCopy[i][0]) + abs(positionsCopy[i][1]) + abs(positionsCopy[i][2]);

                if(newDistance < oldDistance) allGoingAway = false;

            }
        }

        //Now get the one that is closest to the origin
        int indexClosestToOrigin = indexesWithSameSmallestAcceleration[0];

        for(int i = 0; i < indexesWithSameSmallestAcceleration.size(); i++){

            int index = indexesWithSameSmallestAcceleration[i];
            if((abs(positionsCopy[index][0]) + abs(positionsCopy[index][1]) + abs(positionsCopy[index][2])) < 
                (abs(positionsCopy[indexClosestToOrigin][0]) + abs(positionsCopy[indexClosestToOrigin][1]) + 
                abs(positionsCopy[indexClosestToOrigin][2]))){

                    indexClosestToOrigin = index;
                }
        }

        std::cout << indexClosestToOrigin << "\n";
    }
    else std::cout << indexesWithSameSmallestAcceleration[0] << "\n";

    /*
    Part2
    Performe movements until
        1. we reach given number of steps (this solution uses heuristic for the number of steps, because my solution
            is reached with very few numbers of steps <50)
        2. we reach the state where all remaining particles are moving away from the origin and they are all sorted
            in a way where no particle ever can surpass another one(that state is checked by the function 
            testPositionsOverAccelerations)

        The first soltuion works fine and fast, the second is much slower with this implementation, didn't bother to
        optimize it beacuse the first solution is superfast, while second is guaranteed to give us the correct answer
    */

    bool allGoingAway = false;
    int oldDistance;
    std::map<std::string,std::vector<int>> distToIndexes;
    std::string key;

    int it = 0;

    //Solution 1 using heuristic steps, increase it if necessary
    while(it < 100){
    //Solution 2 that is slower but guarantees the correct answer
    //while(!allGoingAway || !testPositionsOverAccelerations(positions,accelerations)){

        it++;

        allGoingAway = true;
        distToIndexes.clear();

        for(int i = 0; i < positions.size(); i++){

            for(int j = 0; j < 3; j++){
                velocities[i][j] += accelerations[i][j];
            }

            int oldDistance = abs(positions[i][0]) + abs(positions[i][1]) + abs(positions[i][2]);

            for(int j = 0; j < 3; j++){
                positions[i][j] += velocities[i][j];
            }

            int newDistance = abs(positions[i][0]) + abs(positions[i][1]) + abs(positions[i][2]);
            key = std::to_string(positions[i][0]) + "-" + std::to_string(positions[i][1]) + "-" + 
                std::to_string(positions[i][2]);
            distToIndexes[key].push_back(i);

            if(newDistance < oldDistance) allGoingAway = false;
        }

        std::vector<int> indexesToRemove;

        for(auto x: distToIndexes){
            if(x.second.size() > 1) std::copy(x.second.begin(), x.second.end(), std::back_inserter(indexesToRemove));
        }

        //We always need to remove them from the end because otherwise we would mess up indexes
        std::sort(indexesToRemove.begin(),indexesToRemove.end(), std::greater<int>());
        for(int i = 0; i < indexesToRemove.size(); i++){
            positions.erase(positions.begin() + indexesToRemove[i]);
            velocities.erase(velocities.begin() + indexesToRemove[i]);
            accelerations.erase(accelerations.begin() + indexesToRemove[i]);
        }

    }

    std::cout << positions.size();

}