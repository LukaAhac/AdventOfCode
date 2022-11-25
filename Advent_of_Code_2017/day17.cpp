#include <iostream>
#include <vector>


int main(void){

    int input = 316;
    int part1Range = 2017;
    int part2Range = 50000000;
    std::vector<int> nums {0};

    int insertionPosition;
    int currentPostition = 0;;

    /*
    Part1
    Iterate 2017 times and insert numbers
    At the end look the number after 2017
    */
    for(int i = 1; i <= part1Range; i++){

        insertionPosition = (currentPostition + input) % nums.size() + 1;

        if(insertionPosition >= nums.size()) nums.push_back(i);
        else nums.insert(nums.begin() + insertionPosition, i);

        currentPostition = insertionPosition;
    }

    std::cout << nums[(currentPostition+1)%nums.size()] << "\n";

    int behindZero;
    int size = 1;

    /*
    Part2
    Since there is 50 mill iterations now we cant just perform insertions beacuse it takes to long
    Luckily, we only need to track the number after 0 and given the rules of the task 0 will never move
    and will always be at position 0, so we keep increasing the size of the sequence without acctualy
    inserting items, and each time that we should insert at position 1, (acctualy insert after position 0)
    we just remember the number that should be there
    */
    for(int i = 1; i < part2Range; i++){

        insertionPosition = (currentPostition + input) % size + 1;

        if(insertionPosition == 1) behindZero = i;

        size++;
        
        currentPostition = insertionPosition;
    }

    std::cout << behindZero;
}