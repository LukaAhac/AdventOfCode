#include <iostream>
#include <fstream>
#include <sstream>

int main(void){
    
    std::ifstream infile("day2.txt");

    std::string str;
    std::string number;
    std::string number2;

    int currNum;
    int currNum2;

    int rowMax = -1;
    int rowMin = -1;

    int checksum = 0;
    int rowResult = 0;

    //Read line by line from the file
    while (std::getline(infile, str)){

        //Iterate over the string lin and compare each number to the row minimum and row maximum which
        //are initially set to -1 since there are no negative values in the input
        //At the end of the row update the check sum and reset the row min and max value to the -1
        std::istringstream iss(str);

        while(iss >> number){

            currNum = stoi(number);
            if (rowMax == -1 || rowMax < currNum){
                rowMax = currNum;
            }
            if (rowMin == -1 || rowMin > currNum){
                rowMin = currNum;
            }

            //For the part2 iterate over the string one more time for each number of the row
            //Check if the modulo operation equals to 0 and tha we are not dealing with the same number
            //If the condition is met devide those numbers and add it to the row result
            std::istringstream stream2(str);
            while (stream2 >> number2){
                currNum2 = stoi(number2);
                if((currNum % currNum2) == 0 && currNum != currNum2){
                    rowResult += currNum/currNum2;
                }
            }

        }

        checksum += rowMax - rowMin;
        rowMax = -1;
        rowMin = -1;
    }

    infile.close();

    std::cout << checksum << "\n" << rowResult;
}