#include <iostream>
#include <fstream>
#include <vector>
#include "utils.cpp"

int main(void){

    std::ifstream infile("day11.txt");
    std::string line;
    std::getline(infile,line);
    infile.close();

    std::vector<std::string> movements = splitby(line, ',');


    double xCord = 0;
    double yCord = 0;

    int furthest = 0;

    /*
    For each move update the coordinates
    If it is moving north/south we just update y by +1/-1
    If it is moving to the east side, we update the x by +0.5 and y by +0.5/-0.5 (for north/south)
    If it is moving to the west side, we update the x by -0.5 and y by +0.5/-0.5 (for north/south)
    Also track if we moved further than we ever been for Part 2
    With this types of coordinates, we can simply calculate the distance from origin by summing absolute valus of coordiantes
    */
    for(int i = 0; i<movements.size(); i++){

        if(movements[i] == "n") yCord += 1;
        else if(movements[i] == "ne"){
            xCord += 0.5;
            yCord += 0.5;
        }
        else if(movements[i] == "se"){
            xCord += 0.5;
            yCord -= 0.5;
        }
        else if(movements[i] == "s") yCord -= 1;
        else if(movements[i] == "sw"){
            xCord -= 0.5;
            yCord -= 0.5;
        }
        else if(movements[i] == "nw"){
            xCord -= 0.5;
            yCord += 0.5;
        }

        if(abs(xCord)+abs(yCord) > furthest) furthest = abs(xCord)+abs(yCord);

    }

    std::cout << abs(xCord) + abs(yCord) << "\n" << furthest;
}