#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "utils.cpp"


int main(void){

    std::ifstream infile("day21.txt");

    std::string line;

    std::vector<std::pair<std::vector<std::vector<std::string>>,std::vector<std::string>>> rules2x2;
    std::vector<std::pair<std::vector<std::vector<std::string>>,std::vector<std::string>>> rules3x3;

    std::vector<std::string> stringParts;
    std::vector<std::string> left, right;

    std::vector<std::vector<std::string>> rules;

    while(std::getline(infile,line)){

        stringParts = splitby(line, ' ');

        left = splitby(stringParts[0], '/');
        right = splitby(stringParts[2], '/');

        rules.clear();
        rules.push_back(left);

        int indexOfLastElement = rules[0].size()-1;

        //Rotate given pattern 3 times to achieve all possible rotations
        for(int i = 0; i < 3; i++){

            std::vector<std::string> newRule = rules[rules.size()-1];

            std::string topRow = newRule[0];

            for(int i = 0; i <= indexOfLastElement; i++){
                newRule[0][i] = newRule[i][indexOfLastElement];
            }

            for(int i = 0; i <= indexOfLastElement; i++){
                newRule[i][indexOfLastElement] = newRule[indexOfLastElement][indexOfLastElement-i];
            }

            for(int i = 0; i <= indexOfLastElement; i++){
                newRule[indexOfLastElement][indexOfLastElement-i] = newRule[indexOfLastElement-i][0];
            }

            for(int i = 0; i <= indexOfLastElement; i++){
                newRule[indexOfLastElement-i][0] = topRow[i];
            }

            rules.push_back(newRule);
        }

        //Flipp each of 4 rotations both ways to achieve total of 8 possible patterns

        for (int i = 0; i < 4; ++i) {

            std::vector<std::string> newRule = rules[i];
            std::string topRow = newRule[0];

            for (int i = 0; i < topRow.size(); i++) {
                newRule[0][i] = newRule[indexOfLastElement][i];
            }

            for (int i = 0; i < topRow.size(); i++) {
                newRule[indexOfLastElement][i] = topRow[i];
            }

            rules.push_back(newRule);

            newRule = rules[0];
            std::string leftColumn = "";

            for (int i = 0; i < topRow.size(); i++) {
                leftColumn += newRule[i][0];
                newRule[i][0] = newRule[i][indexOfLastElement];
            }

            for (int i = 0; i < topRow.size(); i++) {
                newRule[i][indexOfLastElement] = leftColumn[i];
            }

            rules.push_back(newRule);

            if (indexOfLastElement == 1) rules2x2.push_back({ rules,right });
            else rules3x3.push_back({ rules,right });

        }
    }
    infile.close();

    std::vector<std::string> grid = { ".#.", "..#", "###" };
    int iterations = 18;

    //Now just look for the patterns in each iteration and create new grid each iteration
    for (int it = 0; it < iterations; it++) {

        std::vector<std::string> newGrid;

        if (grid.size() % 2 == 0) {

            int numberOfBlocks = grid.size() / 2;
            int newSize = grid.size() + numberOfBlocks;

            for (int i = 0; i < newSize; ++i) {
                newGrid.push_back(std::string(newSize, 'x'));
            }

            for (int blockRow = 0; blockRow < numberOfBlocks; ++blockRow) {
                for (int blockColumn = 0; blockColumn < numberOfBlocks; ++blockColumn) {

                    std::vector<std::string> oldBlock;
                    for (int k = 0; k < 2; ++k) {
                        oldBlock.push_back(std::string(2, 'x'));
                    }

                    for (int i = 0; i < 2; ++i) {
                        for (int j = 0; j < 2; ++j) {
                            oldBlock[i][j] = grid[blockRow * 2 + i][blockColumn * 2 + j];
                        }
                    }

                    for (auto& rules : rules2x2) {
                        for (auto& leftPart : rules.first) {
                            if (leftPart == oldBlock) {
                                for (int i = 0; i < 3; ++i) {
                                    for (int j = 0; j < 3; ++j) {
                                        newGrid[blockRow * 3 + i][blockColumn * 3 + j] = rules.second[i][j];
                                    }
                                }
                                goto out2x2;
                            }
                        }
                    }
                out2x2:
                    continue;
                }
            }
        }
        else {
            int numberOfBlocks = grid.size() / 3;
            int newSize = grid.size() + numberOfBlocks;

            for (int i = 0; i < newSize; ++i) {
                newGrid.push_back(std::string(newSize, 'x'));
            }

            for (int blockRow = 0; blockRow < numberOfBlocks; ++blockRow) {
                for (int blockColumn = 0; blockColumn < numberOfBlocks; ++blockColumn) {

                    std::vector<std::string> oldBlock;
                    for (int k = 0; k < 3; ++k) {
                        oldBlock.push_back(std::string(3, 'x'));
                    }

                    for (int i = 0; i < 3; ++i) {
                        for (int j = 0; j < 3; ++j) {
                            oldBlock[i][j] = grid[blockRow * 3 + i][blockColumn * 3 + j];
                        }
                    }

                    for (auto& rules : rules3x3) {
                        for (auto& leftPart : rules.first) {
                            if (leftPart == oldBlock) {
                                for (int i = 0; i < 4; ++i) {
                                    for (int j = 0; j < 4; ++j) {
                                        newGrid[blockRow * 4 + i][blockColumn * 4 + j] = rules.second[i][j];
                                    }
                                }
                                goto out3x3;
                            }
                        }
                    }
                out3x3:
                    continue;
                }
            }
        }

        grid = newGrid;

        if (it == 4) {
            int onPixelsCounter = 0;

            for (auto& row : grid) {
                for (auto& character : row) {
                    if (character == '#') {
                        onPixelsCounter++;
                    }
                }
            }

            std::cout << onPixelsCounter << "\n";
        }

    }

    int onPixelsCounter = 0;

    for (auto& row : grid) {
        for (auto& character : row) {
            if (character == '#') {
                onPixelsCounter++;
            }
        }
    }

    std::cout << onPixelsCounter;
}