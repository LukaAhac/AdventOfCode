#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <map>


int main(void){

    //Read input into a vector
    std::ifstream infile("day6.txt");
    int inputNumber;
    std::vector<int> memoryBank;

    while(infile >> inputNumber){
        memoryBank.push_back(inputNumber);
    }

    infile.close();

    int cycles = 0;
    std::map<std::string,int> seenStates;

    int indexOfBiggestBank = 0;
    int sizeOfBiggestBank = 0;
    int memoryBankSize = memoryBank.size();
    std::string stateString;

    //Until we find a loop
    while(true){

        //Make a string from a vector separating elements with "-"
        //That string represents the current state of the memory banks
        stateString = "";

        for(auto x: memoryBank){
            stateString += std::to_string(x) + "-";
        }

        //If we already seen that string that means we found a loop and we break
        //Otherweise add that string to the map of seen state where value is amount
        //of cycles needed to reach that state
        if(seenStates.count(stateString)) break;
        seenStates[stateString] = cycles;

        //Find biggest memory bank - both value and index
        for(int index = 0;index < memoryBankSize;index++){
            if(memoryBank[index] > sizeOfBiggestBank){
                sizeOfBiggestBank = memoryBank[index];
                indexOfBiggestBank = index;
            }
        }

        //Reset biggest bank to 0 and distrubute its previous owned value among all of the
        //banks in a cyclic way
        memoryBank[indexOfBiggestBank] = 0;
        int index = indexOfBiggestBank;
        for(int i = 0;i<sizeOfBiggestBank;i++){
            index = (index+1)%memoryBankSize;
            memoryBank[index] += 1;
        }

        //Increase amount of cycles passed and reset bank variables
        cycles += 1;
        sizeOfBiggestBank = 0;
        indexOfBiggestBank = 0;

    }


    std::cout << cycles << "\n" << cycles - seenStates[stateString];

}