#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <vector>
#include <set>

/*
Fnction that expands the group by adding all group elements
IMPORTANT: It requires that gorup already have at least 1 element in the set, and then builds the group around
that element
*/
void formGroup(int& lastSize, std::set<std::string>& group, std::map<std::string,std::vector<std::string>>& IDMap){

    do{
            lastSize = group.size();

            for(auto it = group.begin(); it != group.end();it++){
                for(int i = 0; i < IDMap[(*it)].size();i++){
                    group.insert(IDMap[(*it)][i]);
                }
            }

        }while(lastSize != group.size());

}

int main(void){

    std::ifstream infile("day12.txt");

    std::string line;
    std::string linePart;
    std::map<std::string,std::vector<std::string>> IDMap;

    //Read data in map thath maps ID to the vector of IDs that can communicate to each other
    while(std::getline(infile,line)){

        std::istringstream iss(line);
        std::vector<std::string> linePartsVec;

        while(iss >> linePart){
            linePartsVec.push_back(linePart);
        }

        for(int i = 2; i < linePartsVec.size() - 1; i++){
            IDMap[linePartsVec[0]].push_back(linePartsVec[i].substr(0,linePartsVec[i].size()-1));
        }

        IDMap[linePartsVec[0]].push_back(linePartsVec[linePartsVec.size()-1]);

    }
    infile.close();

    /*
    Part 1
    Keep iterating over set and keep adding new IDs over each iteration
    We are done when one iteration pass that does not add new IDs to the gorup
    */
    std::set<std::string> group {"0"};
    int lastSize;

    formGroup(lastSize, group, IDMap);

    std::cout << lastSize << "\n";

    /*
    Part 2
    Iterate unitl we left with no elements in the map
    At the beggining of each iteration add the first element in the map to the gorup set
    Afterwards, form the group just like for the part 1
    At the end erase all the elements from the map that forms a group and increase gorup counter by 1
    By doing this we will for sure count all the groups, and even can see the IDs that from it, but that
    is not required by the task*/
    int numberOfGroups = 0;

    while(IDMap.size() > 0){

        group.clear();
        group.insert((*IDMap.begin()).first);

        formGroup(lastSize, group, IDMap);

        for(auto it = group.begin(); it != group.end(); it++){
            IDMap.erase(*it);
        }
        numberOfGroups += 1;


    }
        std::cout << numberOfGroups;
}