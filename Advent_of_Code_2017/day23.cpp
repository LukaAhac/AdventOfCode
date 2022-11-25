#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include "utils.cpp"

int main() {

	std::vector<std::vector<std::string>> instructionList;

	std::fstream infile("day23.txt");

	std::string line;
	while (getline(infile, line)) {
		instructionList.push_back(splitby(line, ' '));
	}
	infile.close();

	std::map<std::string, int> registers = { {"a",0}, {"b",0}, {"c",0}, {"d",0}, {"e",0}, {"f",0}, {"g",0}, {"h",0},};
	
	int instructionPointer = 0;

	//Part1
	int mulInvoked = 0;

	while (instructionPointer < instructionList.size()) {
		int y;
		if (!isNumber(instructionList[instructionPointer][2])) {
			y = registers[instructionList[instructionPointer][2]];
		}
		else {
			y = std::stoi(instructionList[instructionPointer][2]);
		}

		if (instructionList[instructionPointer][0] == "set") {
			registers[instructionList[instructionPointer][1]] = y;
		}
		else if (instructionList[instructionPointer][0] == "sub") {
			registers[instructionList[instructionPointer][1]] -= y;
		}
		else if (instructionList[instructionPointer][0] == "mul") {
			registers[instructionList[instructionPointer][1]] *= y;
			mulInvoked++;
		}
		else if (instructionList[instructionPointer][0] == "jnz") {
			int x;

			if (!isNumber(instructionList[instructionPointer][1])) {
				x = registers[instructionList[instructionPointer][1]];
			}
			else {
				x = std::stoi(instructionList[instructionPointer][1]);
			}

			if (x != 0) {
				instructionPointer += (y - 1);
			}
		}
		
		instructionPointer++;
	}

	std::cout << mulInvoked << "\n";

	//Part 2
	//By closer inspection of given assembly code, we can see that the goal of the program is to count numbers that are not prime in the range [106500, 123500] while incrementing the number by 17
	int counter = 0;

	for (int i = 106500; i <= 123500; i += 17) {

		for (int j = 2; j < i / 2; j++) {
			if (i % j == 0) {
				counter++;
				break;
			}
		}
	}

	std::cout << counter;
}