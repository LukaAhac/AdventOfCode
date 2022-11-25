#include <iostream>
#include <fstream>
#include <vector>


int main(void){

    std::ifstream infile("day5.txt");

    std::vector<int> jumpOffsets;
    int inputNumber;

    //Read numbers and put into vector
    while(infile >> inputNumber){
        jumpOffsets.push_back(inputNumber);
    }

    infile.close();

    //Copy vector for part2
    std::vector<int> jumpOffsetsForPart2 = jumpOffsets;

    //Part1
    //Performs jumps until we jump outside of the programm
    //After each jump icrement the offset
    int steps = 0;
    int index = 0;
    int maxIndex = jumpOffsets.size()-1;

    while(index <= maxIndex){

        jumpOffsets[index] += 1;
        index += jumpOffsets[index]-1;
        steps += 1;

    }

    std::cout << steps << "\n";

    //Part2
    //Performs jumps until we jump outisde of the programm
    //If jump offset was >=3 decrement it, otherwise increment it
    index = 0;
    steps = 0;

    while(index <= maxIndex){

        if (jumpOffsetsForPart2[index] >= 3){
            jumpOffsetsForPart2[index] -= 1;
            index += jumpOffsetsForPart2[index]+1;
        }
        else{
            jumpOffsetsForPart2[index] += 1;
            index += jumpOffsetsForPart2[index]-1;
        }
        steps += 1;

    }

    std::cout << steps;
}