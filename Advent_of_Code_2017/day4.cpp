#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

int main(void){

    std::ifstream infile("day4.txt");

    std::string line;
    std::string word;

    int validCounterPart1 = 0;
    int validCounterPart2 = 0;

    //Iterate over lines in a file
    while(std::getline(infile,line)){

        std::istringstream lineStream(line);

        std::vector<std::string> wordsVecPart1;
        bool validPart1 = true;

        std::vector<std::string> wordsVecPart2;
        bool validPart2 = true;

        //Iterate over the woords in a line
        //For part1 put the words into wordsVecPart1 and if the word is already in the vector set valid flag to false
        //For part2 first sort word then do the same as for part1
        while(lineStream >> word){
            if(std::count(wordsVecPart1.begin(),wordsVecPart1.end(),word))
                validPart1 = false;
            else
                wordsVecPart1.push_back(word);

            sort(word.begin(),word.end());
            if(std::count(wordsVecPart2.begin(),wordsVecPart2.end(),word))
                validPart2 = false;
            else
                wordsVecPart2.push_back(word);
        }

        if(validPart1)
            validCounterPart1 += 1;
        if(validPart2)
            validCounterPart2 += 1;

    }
    
    infile.close();

    std::cout << validCounterPart1 << "\n" << validCounterPart2;

}