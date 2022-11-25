#include <iostream>
#include <fstream>
#include <sstream>



int main(void){

    std::ifstream infile("day9.txt");

    std::string line;
    char c;

    int depth = 0;
    bool garbage = false;
    bool cancleNext = false;

    int score = 0;
    int garbageRemoved = 0;

    while(std::getline(infile,line)){

        std::istringstream iss(line);

        /*
        Read line by line
        First test whether or not the  current character should be canceled, skip it if it should be
        Test wheter we read canceling character and mark the flag if we did
        If we are within the garbage count the characters
        if we read < enter set garbage flag, if we read > remove garbage flag
        { increase the depth and add current depth to the score, while } decrease the depth
        */
        while(iss >> c){

            if(cancleNext == true) cancleNext = false;
            else if(c == '!') cancleNext = true;
            else if(garbage && c != '>') garbageRemoved += 1;
            else if(garbage && c == '>') garbage = false;
            else if(!garbage && c == '<') garbage = true;
            else if(c == '{'){
                depth += 1;
                score += depth;
            }
            else if(c == '}') depth -= 1;

        }

    }
    infile.close();

    std::cout << score << "\n" << garbageRemoved;
}