#include <iostream>
#include <fstream>
#include "utils.cpp"
#include <vector>
#include <algorithm>
#include <sstream>

// integer to hex 
#define to_hex_str(hex_val) (static_cast<std::stringstream const&>(std::stringstream() << std::hex << hex_val)).str()


/*
Function that performs one iteration of the knot tying algorithm
*/
void oneIteration(int& pos, int& skip, std::vector<int>& lenghts, std::vector<int>& numberList, int listSize = 256){

    for(int i = 0; i<lenghts.size(); i++){

        int currLen = lenghts[i];

        std::vector<int> toReverse;

        for(int j = 0; j<currLen;j++){
            toReverse.push_back(numberList[(pos+j)%listSize]);
        }
        std::reverse(toReverse.begin(),toReverse.end());

        for(int j = 0; j < currLen; j++){
            numberList[(pos+j)%listSize] = toReverse[j];
        }

        pos += currLen + skip;
        skip += 1;
    }
}

int main(void){

    std::ifstream infile("day10.txt");
    std::string line;
    int listSize = 256;

    //Read input form file and store number as strings into the vector
    std::getline(infile,line);
    infile.close();
    std::vector<std::string> lenghtsStrings = splitby(line, ',');

    //Transform lenghts from strings to ints
    std::vector<int> lenghts;
    for(int i = 0; i < lenghtsStrings.size(); i++){
        lenghts.push_back(std::stoi(lenghtsStrings[i]));
    }
  
    //Vector of numbers 0-256
    std::vector<int> numberList;
    for(int i = 0;i <= listSize ;i++){
        numberList.push_back(i);
    }

    //Part1 perform one iteration and multiply numbers found on first and second place of the list
    int currPos = 0;
    int skipSize = 0;

    oneIteration(currPos, skipSize,lenghts, numberList);

    std::cout << numberList[0]*numberList[1] << "\n";

    //Make lenghts list for part2, transform each char in input file to number
    //Also add aditionall lenghts given in task and reset number vector to 0-256
    std::istringstream iss(line);
    std::vector<int> newLenghts;
    char c;

    while(iss >> c){
        newLenghts.push_back((int)c);
    }

    newLenghts.push_back(17);
    newLenghts.push_back(31);
    newLenghts.push_back(73);
    newLenghts.push_back(47);
    newLenghts.push_back(23);


    numberList.clear();
    for(int i = 0;i <= listSize ;i++){
        numberList.push_back(i);
    }

    /*
    For Part2 do 64 iterations of the Knot tying algorithm then separate 256 numbers into blocks of 16 elements
    Do the bitwise XOR across each block and transform the block number into hexadecimal representation
    It is important to add leading zeros if needed
    */
    currPos = 0;
    skipSize = 0;

    for(int rounds = 0; rounds < 64; rounds++){
        oneIteration(currPos,skipSize,newLenghts,numberList);
    }

    std::string hex;

    for(int i = 0; i < 16; i++){

        int res = numberList[16*i] ^ numberList[16*i+1];
        for(int j = 2; j < 16; j++){
            res ^= numberList[16*i+j];
        }
        hex = to_hex_str(res);
        if(hex.size() == 2) std::cout << hex;
        else std::cout << 0 << hex;

    }

}