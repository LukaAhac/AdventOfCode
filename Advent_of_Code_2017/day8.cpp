#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <map>
#include "utils.cpp"

//Function that evalueates the conditon
bool evaluateCondition(int& a, std::string op, int& b){
    if(op == "<=") return a <= b;
    else if(op == "<") return a < b;
    else if (op == ">=") return a >= b;
    else if(op == ">") return a > b;
    else if(op == "==") return a == b;
    else if(op == "!=") return a != b;
}

int main(void){


    std::ifstream infile("day8.txt");

    std::string line;

    std::map<std::string,int> registers;

    int b;
    int largestValueOverall = 0;

    //Read file line by line, split line into vector by spaces
    //Test the condition with the function and inc/dec value if the condition is met
    //Also if we increased something check if that value is new largest and update it if it is
    while(std::getline(infile,line)){

        std::vector<std::string> lineParts = splitby(line,' ');

        b = std::stoi(lineParts[6]);

        if(evaluateCondition(registers[lineParts[4]],lineParts[5],b)){
            if(lineParts[1] == "inc"){
                registers[lineParts[0]] += std::stoi(lineParts[2]);
                if(registers[lineParts[0]] > largestValueOverall) largestValueOverall = registers[lineParts[0]];
            }
            else registers[lineParts[0]] -= std::stoi(lineParts[2]);
        }


        
    }


    infile.close();

    //At the end check for the largest value in register for Part1 soluton
    int largest = -999999;

    for(auto keyValue : registers){
        if(largest < keyValue.second) largest = keyValue.second;
    }


    std::cout << largest << "\n" << largestValueOverall;
}