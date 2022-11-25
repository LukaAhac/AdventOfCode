#include <iostream>
#include <fstream>
#include <vector>
#include "utils.cpp"
#include <map>

/*
Function that runs one instruction of the program and returns status of the program
If the index went out of the instrcution range, returns "T"
If the current instruction is "rcv" and there is no value to take from queue, return "W"
Else perform instruction and return "R"
*/
std::string runProgram(std::vector<std::vector<std::string>>& instructions, int& currentIndex, 
    std::map<std::string,long long>& registers, std::vector<int>& myQueue, std::vector<int>& hisQueue, bool count, int& counter){
    
    if(currentIndex >= instructions.size()) return "T";

    std::vector<std::string> currentInstruction = instructions[currentIndex];
    long long a,b;


    if(isNumber(currentInstruction[1])) a = std::stoi(currentInstruction[1]);
    else a = registers[currentInstruction[1]];

    if(currentInstruction[0] == "snd"){
        hisQueue.push_back(a);
        if(count) counter += 1;
    }
    else if(currentInstruction[0] == "rcv"){
        if(myQueue.size() == 0) return "W";
        registers[currentInstruction[1]] = myQueue[0];
        myQueue.erase(myQueue.begin());
    }
    else{
        if(isNumber(currentInstruction[2])) b = std::stoi(currentInstruction[2]);
        else b = registers[currentInstruction[2]];

        if(currentInstruction[0] == "set") registers[currentInstruction[1]] = b;
        else if (currentInstruction[0] == "add") registers[currentInstruction[1]] += b;
        else if (currentInstruction[0] == "mul") registers[currentInstruction[1]] *= b;
        else if (currentInstruction[0] == "mod") registers[currentInstruction[1]] %= b;
        else if (currentInstruction[0] == "jgz" && a > 0) currentIndex += b-1;
    }
    currentIndex += 1;
    
    return "R";
}


int main(void){

    std::ifstream infile("day18.txt");
    std::string line;
    std::vector<std::vector<std::string>> instructions;

    while(std::getline(infile,line)){
        instructions.push_back(splitby(line, ' '));
    }
    infile.close();

    std::map<std::string,long long> registers;
    int currentIndex = 0;
    long long a,b;
    long long lastSND;
    std::vector<std::string> currentInstruction;


    /*
    Part1
    Go through instructions until we reach "rcv" that is active and then break to loop
    Each time we have "snd" remember the value
    */
    while(currentIndex < instructions.size()){

        currentInstruction = instructions[currentIndex];

        if(isNumber(currentInstruction[1])) a = std::stoi(currentInstruction[1]);
        else a = registers[currentInstruction[1]];

        if(currentInstruction[0] == "snd") lastSND = a;
        else if(currentInstruction[0] == "rcv"){
            if(a != 0) break;
        }
        else{
            if(isNumber(currentInstruction[2])) b = std::stoi(currentInstruction[2]);
            else b = registers[currentInstruction[2]];

            if(currentInstruction[0] == "set") registers[currentInstruction[1]] = b;
            else if (currentInstruction[0] == "add") registers[currentInstruction[1]] += b;
            else if (currentInstruction[0] == "mul") registers[currentInstruction[1]] *= b;
            else if (currentInstruction[0] == "mod") registers[currentInstruction[1]] %= b;
            else if (currentInstruction[0] == "jgz" && a > 0) currentIndex += b-1;
        }
        currentIndex += 1;
    }

    std::cout << lastSND << "\n";

    /*
    Part2
    Create registers, indexes for both programms and message queues
    Create status for programs that can be "T" - Terminated, "W" - Waiting and "R" - Running
    Run the main loop until both programs are terminated or both programs are waiting
    In each iteration if the program is running call the runProgram function that runs one instruction
    */
    std::map<std::string,long long> prog0Regs, prog1Regs;
    prog0Regs["p"] = 0;
    prog1Regs["p"] = 1;

    int prog0Index = 0;
    int prog1Index = 0;
    
    std::string prog0Status = "R";
    std::string prog1Status = "R";
    std::vector<int> prog0MessageQueue, prog1MessageQueue;
    int counter = 0;


    while(true){

        if(prog0Status == "T" && prog1Status == "T") break;

        if(prog0MessageQueue.size() > 0 && prog0Status == "W") prog0Status = "R";
        if(prog1MessageQueue.size() > 0 && prog1Status == "W") prog1Status = "R";

        if(prog0Status == "W" && prog1Status == "W") break;

        if(prog0Status == "R") prog0Status = runProgram(instructions,prog0Index,prog0Regs,prog0MessageQueue,prog1MessageQueue,false,counter);
        if(prog1Status == "R") prog1Status = runProgram(instructions, prog1Index,prog1Regs,prog1MessageQueue,prog0MessageQueue,true,counter);
    }

    std::cout << counter;

}