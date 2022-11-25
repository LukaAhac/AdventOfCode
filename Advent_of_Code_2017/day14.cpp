#include <iostream>
#include <vector>
#include <set>
#include "utils.cpp"

int main(void){

    std::string input = "wenycdww";
    std::string temp;
    std::string bits;

    int used = 0;
    std::vector<std::string> rowsOfBits;

    /*
    Part1
    Perform knoting algo
    Store row of bits into vector
    Count the number of "1"
    */
    for(int i = 0; i<128; i++){
        temp = input + "-" + std::to_string(i);
        temp =  knotingAlgorithm(temp);

        bits = "";
        for(int j = 0; j<temp.size(); j++){
            bits += hexStringCharTObitsString[temp.substr(j,1)];
        }
        rowsOfBits.push_back(bits);
        for(int j= 0; j<bits.size(); j++){
            if(bits[j] == '1') used += 1;
        }
    }

    std::cout << used << "\n";


    /*
    Part2
    Iterate over bits
    If the bit of value 1 is found put its location into the grouoLocs and jump to group forming section
    If we finish iterating over bits without "1" being found then we coutned all the groups and we are done
    In the group froming section keep ading adjacent locations to the set if bits on that locaions are also "1"
    When we have nothing else to add, set all bits of that group to "0" and increae the group counter, also jump
    back to iterations over bit that starts again from beggining each time
    */
    std::set<std::pair<int,int>> groupLocs;
    int numberOfGroups = 0;
    int groupSize;

    lookingForGroups:

        for(int i = 0; i < rowsOfBits.size(); i++){
            for(int j = 0; j < rowsOfBits[i].size(); j++){
                if(rowsOfBits[i][j] == '1'){
                    groupLocs.clear();
                    groupLocs.insert({i,j});
                    goto groupForming;
                }
            }
        }
        std::cout << numberOfGroups;
        return 1;

    groupForming:

        groupSize = 0;

        while(groupLocs.size() != groupSize){

            groupSize = groupLocs.size();
            for(auto it = groupLocs.begin(); it != groupLocs.end(); it++){
                if((*it).first > 0 && rowsOfBits[(*it).first-1][(*it).second] == '1') groupLocs.insert({(*it).first-1,(*it).second});
                if((*it).first < rowsOfBits.size()-1 && rowsOfBits[(*it).first+1][(*it).second] == '1') groupLocs.insert({(*it).first+1,(*it).second});
                if((*it).second > 0 && rowsOfBits[(*it).first][(*it).second-1] == '1') groupLocs.insert({(*it).first,(*it).second-1});
                if((*it).second < rowsOfBits[0].size()-1 && rowsOfBits[(*it).first][(*it).second+1] == '1') groupLocs.insert({(*it).first,(*it).second+1});
            }
        }

    for(auto it = groupLocs.begin(); it != groupLocs.end(); it++){
        rowsOfBits[(*it).first][(*it).second] = '0';
    }
    numberOfGroups += 1;
    goto lookingForGroups;
}   