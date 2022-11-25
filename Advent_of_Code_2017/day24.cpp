#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "utils.cpp"


int main() {

	std::fstream infile("day24.txt");

	std::string line;
	std::vector<std::pair<int, int>> components;

	while (std::getline(infile, line)) {
		std::vector<std::string> splitted = splitby(line, '/');
		components.emplace_back(std::stoi(splitted[0]), std::stoi(splitted[1]));
	}
	infile.close();

	std::vector<std::pair<std::vector<int>, std::vector<std::pair<int,int>>>> possibleBridges;
	possibleBridges.emplace_back(std::vector<int>{0}, components);
	
	//Part1
	int maxStrength = 0;
	//Part2
	int longestBridge = 0;
	int longestBrdigeStrength = 0;

	while (possibleBridges.size() > 0) {
		std::vector<std::pair<std::vector<int>, std::vector<std::pair<int, int>>>> possibleBridgesNext;

		for (std::pair<std::vector<int>, std::vector<std::pair<int, int>>>& bridge : possibleBridges) {
			int connector = bridge.first.back();
			bool newBrdigeConstructedFromThis = false;

			for (std::pair<int, int>& comp : bridge.second) {
				if (comp.first == connector || comp.second == connector) {
					newBrdigeConstructedFromThis = true;
					std::vector<int> bridgeNumbers = bridge.first;

					if (comp.first == connector) {
						bridgeNumbers.push_back(comp.first);
						bridgeNumbers.push_back(comp.second);
					}
					else {
						bridgeNumbers.push_back(comp.second);
						bridgeNumbers.push_back(comp.first);
					}
					std::vector<std::pair<int, int>> bridgeComponents = bridge.second;
					bridgeComponents.erase(std::remove(bridgeComponents.begin(), bridgeComponents.end(), comp), bridgeComponents.end());
					possibleBridgesNext.emplace_back(bridgeNumbers, bridgeComponents);
				}
			}
			if (!newBrdigeConstructedFromThis) {
				int strength = 0;
				for (int x : bridge.first) {
					strength += x;
				}
				if (strength > maxStrength) {
					maxStrength = strength;
				}
				if (bridge.first.size() > longestBridge) {
					longestBridge = bridge.first.size();
					longestBrdigeStrength = strength;
				}
				else if (bridge.first.size() == longestBridge && strength > longestBrdigeStrength) {
					longestBrdigeStrength = strength;
				}
			}
		}
		possibleBridges = possibleBridgesNext;
	}

	std::cout << maxStrength << "\n";
	std::cout << longestBrdigeStrength;
}