#include <iostream>
#include <fstream>
#include <vector>
#include "utils.cpp"
#include <algorithm>

int main(void){

    std::ifstream infile("day16.txt");
    std::string line;
    int numberOfPrograms = 16;

    std::getline(infile,line);
    infile.close();

    std::vector<std::string> danceMoves = splitby(line, ',');

    std::string programs = "abcdefghijklmnop";

    std::vector<char> moves;
    std::vector<int> numberOfElements;
    std::vector<std::vector<std::string>> parameters;
    std::vector<std::pair<int,int>> positionsVector;
    std::vector<std::pair<char,char>> chars;

    //Read input and store informations into vectors
    //There are bunch of trash in those vectors but i was doing it to speed the program at the cost of the memory
    for(int i = 0; i < danceMoves.size(); i++){
        moves.push_back(danceMoves[i].substr(0,1)[0]);

        if(moves[i] == 's') numberOfElements.push_back(std::stoi(danceMoves[i].substr(1,danceMoves[i].size()-1)));
        else numberOfElements.push_back(0);

        if(moves[i] == 'x'){
            std::vector<std::string> res = splitby(danceMoves[i].substr(1,danceMoves[i].size()-1),'/');
            positionsVector.push_back({std::stoi(res[0]),std::stoi(res[1])});
        }
        else positionsVector.push_back({0,0});

        if(moves[i] == 'p'){
            std::vector<std::string> res = splitby(danceMoves[i].substr(1,danceMoves[i].size()-1),'/');
            chars.push_back({res[0][0],res[1][0]});
        }
        else chars.push_back({'0','0'});
    }

    /*
    Petform 1 billion of dance iterations
    Print solution before iteration 2 for part 1
    Cache all transitions into vector called seenOnes
    Before doing dance manually check the vector if we encountered that sequance represented as string already
    If we did we have solution already and do not need to perform any more dances because since we encountered
    already seen sequance that means there is a loop that will happen all over again untiil we run all 1 bill
    of iterations and we can calculate what would be the output after 1 bill iterations
    */
    int pos1,pos2;
    std::vector<std::string> seenOnes;

    for(int d = 0; d < 1000000000; d++){

        if(d == 1){
            std::cout << programs << "\n";
        }

        for(int i = 0; i < seenOnes.size(); i++){
            if(seenOnes[i] == programs){
                /*
                Index i is where the loop starts, 1bill - d is the amount of iterations that is left to perform
                d - i is the length of the loop
                Now we can just do modulo to find out what will be the result after 1 bill iterations
                */
                std::cout << seenOnes[i + (1000000000 - d) % (d-i)];
                return 1;
            } 
        }

        seenOnes.push_back(programs);

        for(int i = 0; i < danceMoves.size(); i++){

            if(moves[i] == 's'){
                
                programs = programs.substr(numberOfPrograms-numberOfElements[i],numberOfElements[i])+programs.substr(0,numberOfPrograms-numberOfElements[i]);
            }
            else{
                if(moves[i] == 'x'){

                    pos1 = positionsVector[i].first;
                    pos2 = positionsVector[i].second;
                }
                else{

                    pos1 = programs.find(chars[i].first);
                    pos2 = programs.find(chars[i].second);
                }
                
                std::swap(programs[pos1], programs[pos2]);
            }
        }
    }

    std::cout << programs;
}