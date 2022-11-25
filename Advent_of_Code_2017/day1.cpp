#include <iostream>
#include <fstream>

int main(){

    std::string str;

    std::ifstream infile("day1.txt");
    if (infile.is_open()) {
        infile >> str;
    }
    infile.close();

    int count1 = 0;
    int count2 = 0;

    //We need to know length of the whole string and half of that length
    int len = str.length();
    int half = len/2;

    //For each element of the string check wheter his next (for the part1) or halfway throught the circle
    //(for part2) elements are the same and add them to the counter if they are the same
    //There is character conversion to the integer which is:
    //  convert char to its ASCII representation - 48, where 48 is representation for the "0"
    for (int i = 0;i<len;i++){

        if (str[i] == str[(i+1)%len]){
            count1 += (int)str[i] - 48;
        }

        if(str[i]== str[(i+half)%len]){
            count2 += (int)str[i] - 48;
        }
    }


    std::cout << count1 << "\n" << count2;

}