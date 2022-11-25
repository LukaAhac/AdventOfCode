#include <iostream>
#include <fstream>
#include <vector>
#include "utils.cpp"
#include <map>
#include <algorithm>

//Function that takes refference ot the scanner Location and performs one movement of scanners
void moveScanners(std::map<int,int>& layers, std::map<int,std::pair<int,std::string>>& scannerLocations){

    for(auto it = scannerLocations.begin(); it != scannerLocations.end(); it++){
            if(scannerLocations[(*it).first].second == "D"){
                if(scannerLocations[(*it).first].first == (layers[(*it).first] - 1)){
                    scannerLocations[(*it).first].first -= 1;
                    scannerLocations[(*it).first].second = "U";
                }
                else scannerLocations[(*it).first].first += 1;
            }
            else{
                if(scannerLocations[(*it).first].first == 0){
                    scannerLocations[(*it).first].first += 1;
                    scannerLocations[(*it).first].second = "D";
                }
                else scannerLocations[(*it).first].first -= 1;
            }
        }

}

//Function that calculates the severity for the given startin scanner locations
int calculateSeverity(int& lastDepth, std::map<int,int>& layers, std::map<int,std::pair<int,std::string>> scannerLocations){

    int severity = 0;

    for(int i = 0; i <= lastDepth; i++){

        if(layers.find(i) != layers.end()){
            if(scannerLocations[i].first == 0) severity += i*layers[i];
        }

        moveScanners(layers,scannerLocations);
    }

    return severity;

}

/*
Function that checks wheter or not we can pass the scanners without being caught
Returns true if we can pass witought being caught and false otherwise
*/
bool tryToPass(int& lastDepth, std::map<int,int>& layers, std::map<int,std::pair<int,std::string>> scannerLocations){

    for(int i = 0; i <= lastDepth; i++){

        if(layers.find(i) != layers.end()){
            if(scannerLocations[i].first == 0) return false;
        }

        moveScanners(layers,scannerLocations);
    }

    return true;
}


int main(void){

    std::ifstream infile("day13.txt");
    std::string line;
    std::vector<std::string> lineElements;

    std::map<int,int> layers;
    std::map<int,std::pair<int,std::string>> scannerLocations;
    int lastDepth;

    //Read input and form layers map that maps layers to depths
    //Also form initiall scanner locations
    while(std::getline(infile,line)){
        lineElements = splitby(line, ' ');
        lastDepth = std::stoi(lineElements[0].substr(0,lineElements[0].size()-1));
        layers[lastDepth] = std::stoi(lineElements[1]);
        scannerLocations[lastDepth] = {0,"D"};
    }
    infile.close();

    //Part 1, calculate the severtiy for the pass without the delay
    int severity = calculateSeverity(lastDepth,layers, scannerLocations);
    std::cout << severity << "\n";

    //Part 2, until we pass without being caught perofrm scanner movement and try to pass
    int delay = 0;
    bool passed;
    if(severity != 0) passed = false;
    else passed = true;

    while(!passed){

        delay += 1;
        moveScanners(layers,scannerLocations);
        passed = tryToPass(lastDepth, layers,scannerLocations);
    }

    std::cout << delay;
}