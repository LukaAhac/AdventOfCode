#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {

	std::ifstream infile("day22.txt");
	std::vector<std::vector<char>> grid;

	std::string line;
	while (std::getline(infile, line)) {
		std::vector<char> gridRow;
		for (char& c : line) {
			gridRow.push_back(c);
		}
		grid.push_back(gridRow);
	}
	infile.close();

	//Test example
	//grid.clear();
	//grid.push_back(std::vector<char>{ '.', '.', '#' });
	//grid.push_back(std::vector<char>{ '#', '.', '.' });
	//grid.push_back(std::vector<char>{ '.', '.', '.' });

	std::vector<std::vector<char>> gridForPart2 = grid;

	std::pair<int, int> currentPosition(grid.size() - (grid.size() / 2 + 1), grid.size() - (grid.size() / 2 + 1));
	char lookingTowards = 'U';
	std::string lookingTowardsPossibilities = "URDL";

	//Part 1
	int burstsCausingInfection = 0;

	for (int i = 0; i < 10000; ++i) {
		//Node turning
		if (grid[currentPosition.first][currentPosition.second] == '#') {
			lookingTowards = lookingTowardsPossibilities[((int)lookingTowardsPossibilities.find(lookingTowards) + 1) > 3 ? 0 : ((int)lookingTowardsPossibilities.find(lookingTowards) + 1)];
		}
		else {
			lookingTowards = lookingTowardsPossibilities[(((int)lookingTowardsPossibilities.find(lookingTowards) - 1) < 0 ? 3 : ((int)lookingTowardsPossibilities.find(lookingTowards) - 1))];
		}
		//Infection or cleaning
		if (grid[currentPosition.first][currentPosition.second] == '#') {
			grid[currentPosition.first][currentPosition.second] = '.';
		}
		else {
			grid[currentPosition.first][currentPosition.second] = '#';
			burstsCausingInfection++;
		}
		//Move ... first is for row and they increase as we go down, second is for column and they increase to the right
		if (lookingTowards == 'U') {
			currentPosition.first--;
		}
		else if (lookingTowards == 'D') {
			currentPosition.first++;
		}
		else if (lookingTowards == 'L') {
			currentPosition.second--;
		}
		else if (lookingTowards == 'R') {
			currentPosition.second++;
		}
		//Expand the grid in each way if the position went outiside of the current grid
		if (currentPosition.first >= grid.size() || currentPosition.first < 0 || currentPosition.second >= grid.size() || currentPosition.second < 0) {
			std::vector<std::vector<char>> newGrid;
			newGrid.push_back(std::vector<char>(grid.size() + 2, '.'));
			for (auto gridRow : grid) {
				gridRow.push_back('.');
				gridRow.insert(gridRow.begin(), '.');
				newGrid.push_back(gridRow);
			}
			newGrid.push_back(std::vector<char>(grid.size() + 2, '.'));

			grid = newGrid;
			currentPosition.first++;
			currentPosition.second++;
		}
	}

	std::cout << burstsCausingInfection << "\n";

	//Part 2
	int burstsCausingInfectionPart2 = 0;
	grid = gridForPart2;
	currentPosition = std::pair<int,int>(grid.size() - (grid.size() / 2 + 1), grid.size() - (grid.size() / 2 + 1));
	lookingTowards = 'U';

	for (int i = 0; i < 10000000; ++i) {
		//Node turning
		if (grid[currentPosition.first][currentPosition.second] == '#') {
			lookingTowards = lookingTowardsPossibilities[((int)lookingTowardsPossibilities.find(lookingTowards) + 1) > 3 ? 0 : ((int)lookingTowardsPossibilities.find(lookingTowards) + 1)];
		}
		else if (grid[currentPosition.first][currentPosition.second] == '.') {
			lookingTowards = lookingTowardsPossibilities[(((int)lookingTowardsPossibilities.find(lookingTowards) - 1) < 0 ? 3 : ((int)lookingTowardsPossibilities.find(lookingTowards) - 1))];
		}
		else if (grid[currentPosition.first][currentPosition.second] == 'F') {
			lookingTowards = lookingTowardsPossibilities[(((int)lookingTowardsPossibilities.find(lookingTowards) + 2) % 4)];
		}
		//Infection, weakaning, cleaning and falgging
		if (grid[currentPosition.first][currentPosition.second] == '#') {
			grid[currentPosition.first][currentPosition.second] = 'F';
		}
		else if (grid[currentPosition.first][currentPosition.second] == '.') {
			grid[currentPosition.first][currentPosition.second] = 'W';
		}
		else if (grid[currentPosition.first][currentPosition.second] == 'W') {
			grid[currentPosition.first][currentPosition.second] = '#';
			burstsCausingInfectionPart2++;
		}
		else if (grid[currentPosition.first][currentPosition.second] == 'F') {
			grid[currentPosition.first][currentPosition.second] = '.';
		}
		//Move ... first is for row and they increase as we go down, second is for column and they increase to the right
		if (lookingTowards == 'U') {
			currentPosition.first--;
		}
		else if (lookingTowards == 'D') {
			currentPosition.first++;
		}
		else if (lookingTowards == 'L') {
			currentPosition.second--;
		}
		else if (lookingTowards == 'R') {
			currentPosition.second++;
		}
		//Expand the grid in each way if the position went outiside of the current grid
		if (currentPosition.first >= grid.size() || currentPosition.first < 0 || currentPosition.second >= grid.size() || currentPosition.second < 0) {
			std::vector<std::vector<char>> newGrid;
			newGrid.push_back(std::vector<char>(grid.size() + 2, '.'));
			for (auto gridRow : grid) {
				gridRow.push_back('.');
				gridRow.insert(gridRow.begin(), '.');
				newGrid.push_back(gridRow);
			}
			newGrid.push_back(std::vector<char>(grid.size() + 2, '.'));

			grid = newGrid;
			currentPosition.first++;
			currentPosition.second++;
		}
	}

	std::cout << burstsCausingInfectionPart2;
}