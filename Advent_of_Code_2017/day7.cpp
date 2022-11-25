#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

//Recursively calculate weight of each tower and return it
//If the tower has no subtower simply return its weight, otherwise add all subtower weight and current tower weight
//and return that value. Each time check if all subtowers have the same weight
//If they do not have the same weight, find the index and then the name of a tower that does not have the wieht like
//the reset (here i assumed that faulty tower will always be on a level with 3 or more subtowersm if there were only 2
//it would be unclear which tower should we modify and solution would be ambiguous)
//Find the differenc betwen the faulty tower and the rest and calculate the value that the tower should have
//If we found faulty tower we found solution so we exit program
int recursiveDepth(std::string towerName, std::map<std::string,std::pair<std::vector<std::string>,int>>& towers){
    if(towers[towerName].first.size() == 0) return towers[towerName].second;

    int depth = 0;
    std::vector<int> depths;

    for(int i = 0; i<towers[towerName].first.size();i++){
        depths.push_back(recursiveDepth(towers[towerName].first[i],towers));
    }

    for(int i = 0; i < depths.size();i++){
        depth += depths[i];
    }
        depth += towers[towerName].second;

 
    if(std::count(depths.begin(),depths.end(),depths[0]) != depths.size()){
        int indexOfDiff;
        int diff;
        if (depths[0] != depths[1] and depths[0] != depths[2]){
            indexOfDiff = 0;
            diff = depths[1] - depths[0];
        }
        else{
                
            for(int i = 1; i < depths.size();i++){
                if(depths[0] != depths[i]){
                    indexOfDiff = i;
                    diff = depths[0] - depths[i];
                }
            }
        }
        std::string nameOfDiffrent = towers[towerName].first[indexOfDiff];
        std::cout << towers[nameOfDiffrent].second + diff;
        exit(0);
    }
 

    return depth;
}


int main(void){

    std::ifstream infile("day7.txt");

    std::string line;
    std::string linePart;

    std::map<std::string,std::pair<std::vector<std::string>,int>> towers; 

    //Read input and store it into map that mapps tower to pair that contains vector of subtowers and tower weight
    while(std::getline(infile,line)){

        std::istringstream iss(line);

        std::vector<std::string> lineElements;

        while(iss >> linePart){
            lineElements.push_back(linePart);
        }

        std::vector<std::string> subTowers;

        if(lineElements.size() > 2){
            for(int i = 3; i < lineElements.size()-1;i++){
                subTowers.push_back(lineElements[i].substr(0,lineElements[i].length()-1));
            }
            subTowers.push_back(lineElements[lineElements.size()-1]);

        }

        towers[lineElements[0]] = {subTowers,std::stoi(lineElements[1].substr(1,lineElements[1].size()-1))};

    }

    infile.close();

    //For part 1 just simply iterate over map and put the keys into the vector named leftSide
    //and put the all of the subtowers to the vector named rightSide, and then simply find the element
    //that is in the leftSide vector and not in the rightSide vector adn that will be our root tower
    std::vector<std::string> leftSide;
    std::vector<std::string> rightSide;
    std::string rootTower;

     for ( const auto &keyValuePair : towers ) {
         leftSide.push_back(keyValuePair.first);
         for(int i = 0;i < keyValuePair.second.first.size();i++){
             rightSide.push_back(keyValuePair.second.first[i]);
         }
    }

    for(int i = 0;i<leftSide.size();i++){
        bool notIn = true;
        for(int j = 0; j<rightSide.size();j++){
            if(leftSide[i] == rightSide[j]) notIn =false;
        }
        if(notIn){
            rootTower = leftSide[i];
            std::cout << leftSide[i] <<"\n";
            goto part2;
        }
    }

    //Part 2 solved by recursive function explaind above
    part2:
    std::cout<< recursiveDepth(rootTower,towers);
}