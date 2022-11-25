#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <map>

// integer to hex 
#define to_hex_str(hex_val) (static_cast<std::stringstream const&>(std::stringstream() << std::hex << hex_val)).str()


//Function to split string by given separator
std::vector<std::string> splitby(std::string string,char splitter) {
    int splits = 0;
    std::vector<std::string> result = {};
    std::string locresult = "";
    for (unsigned int i = 0; i < string.size(); i++) {
        if ((char)string.at(i) != splitter) {
            locresult += string.at(i);
        }
        else {
            result.push_back(locresult);
            locresult = "";
        }
    }
    if (splits == 0) {
        result.push_back(locresult);
    }
    return result;
}


/*
Function that performs one iteration of the knot tying algorithm
*/
void oneIteration1(int& pos, int& skip, std::vector<int>& lenghts, std::vector<int>& numberList, int listSize = 256){

    for(int i = 0; i<lenghts.size(); i++){

        int currLen = lenghts[i];

        std::vector<int> toReverse;

        for(int j = 0; j<currLen;j++){
            toReverse.push_back(numberList[(pos+j)%listSize]);
        }
        std::reverse(toReverse.begin(),toReverse.end());

        for(int j = 0; j < currLen; j++){
            numberList[(pos+j)%listSize] = toReverse[j];
        }

        pos += currLen + skip;
        skip += 1;
    }

}

//Function that pefroms knot tying algorithm introduced in day 10
std::string knotingAlgorithm(std::string& line, int listSize = 256){

    std::istringstream iss(line);
    std::vector<int> newLenghts;
    char c;

    while(iss >> c){
        newLenghts.push_back((int)c);
    }

    newLenghts.push_back(17);
    newLenghts.push_back(31);
    newLenghts.push_back(73);
    newLenghts.push_back(47);
    newLenghts.push_back(23);
    
    std::vector<int> numberList;
    for(int i = 0;i <= listSize ;i++){
        numberList.push_back(i);
    }


    int currPos = 0;
    int skipSize = 0;

    for(int rounds = 0; rounds < 64; rounds++){
        oneIteration1(currPos,skipSize,newLenghts,numberList);
    }

    std::string hex;
    std::string out = "";

    for(int i = 0; i < 16; i++){

        int res = numberList[16*i] ^ numberList[16*i+1];
        for(int j = 2; j < 16; j++){
            res ^= numberList[16*i+j];
        }
        hex = to_hex_str(res);
        if(hex.size() == 2) out += hex;
        else out+= "0" + hex;

    }
    return out;
}

//Map that maps hexa char given as string to its bite representation
std::map<std::string,std::string> hexStringCharTObitsString =
    {
        {"0","0000"},
        {"1","0001"},
        {"2","0010"},
        {"3","0011"},
        {"4","0100"},
        {"5","0101"},
        {"6","0110"},
        {"7","0111"},
        {"8","1000"},
        {"9","1001"},
        {"a","1010"},
        {"b","1011"},
        {"c","1100"},
        {"d","1101"},
        {"e","1110"},
        {"f","1111"}
    };

//Function that checks if the given string is a number
bool isNumber(std::string s)
{
    if (s[0] == '-') s = s.substr(1, s.size() - 1);
    for (char const& ch : s) {
        if (std::isdigit(ch) == 0)
            return false;
    }
    return true;
}