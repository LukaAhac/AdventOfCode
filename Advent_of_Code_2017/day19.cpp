#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>

int main(void){

    std::ifstream infile("day19.txt");
    std::vector<std::string> map;
    std::string line;

    while(std::getline(infile,line)) map.push_back(line);

    infile.close();

    int x = 0;
    int y;

    for(int i = 0; i < map[0].size(); i++){
        if(map[0][i] == '|'){
            y = i;
            break;
        }
    }

    std::string letters;

    char movingDirection = 'D';

    std::map<char,char> oppositeDirection = {{'D','U'}, {'U','D'}, {'L','R'}, {'R','L'}};
    std::map<char,std::pair<int,int>> moves = {{'D',{1,0}}, {'U',{-1,0}}, {'R',{0,1}}, {'L',{0,-1}}};

    std::vector<int> dx = {1, 0, -1, 0};
    std::vector<int> dy = {0, 1, 0, -1};

    int newX,newY;

    int steps = 0;

    while(map[x][y] != ' '){

        if(map[x][y] == '+'){

            std::vector<char> possibleMoves;

            for(auto var: moves){
                newX = x + var.second.first;
                newY = y + var.second.second;

                if((map.size() > newX >= 0) && (map[0].size() > newY >= 0)){
                    if(map[newX][newY] != ' ') possibleMoves.push_back(var.first);
                }
            }

            possibleMoves.erase(std::remove(possibleMoves.begin(), possibleMoves.end(), oppositeDirection[movingDirection]), 
                possibleMoves.end());

            movingDirection = possibleMoves[0];
            x += moves[possibleMoves[0]].first;
            y += moves[possibleMoves[0]].second;
        }
        else{
            if(map[x][y] != '|' && map[x][y] != '-') letters += map[x][y];

            x += moves[movingDirection].first;
            y += moves[movingDirection].second;

        }

        steps += 1;

    }

    std::cout <<letters << "\n" << steps;
}