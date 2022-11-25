#include <iostream>
#include <fstream>
#include "utils.cpp"
#include <vector>
#include <bitset>

int main(void){

    std::ifstream infile("day15.txt");
    std::string line;

    unsigned long long a = 0;
    unsigned long long b = 0;

    int aInit = 0;
    int bInit = 0;

    //Values given in task
    int aFactor = 16807;
    int bFactor = 48271;
    int devidor = 2147483647;

    //Read input values
    while(std::getline(infile,line)){
        std::vector<std::string> lineParts = splitby(line, ' ');
        if(aInit == 0) aInit = std::stoi(lineParts[lineParts.size()-1]);
        else bInit = std::stoi(lineParts[lineParts.size()-1]);
    }
    infile.close();

    /*
    Part1
    Perform 40 mil iterations of multiplications and moduls
    Take the 16 least significant bits and xor them
    If the result is all zeros, that means that operands were the same and increase the counter
    */
    a = aInit;
    b = bInit;
    
    int counter = 0;

    for(int i = 0; i < 40000000; i++){

        a *= aFactor;
        a %= devidor;
        b *= bFactor;
        b %= devidor;
        std::bitset<16> aBits(a);
        std::bitset<16> bBits(b);
        aBits ^= bBits;
        if(aBits.none()) counter += 1;
    }

    std::cout << counter << "\n";

    /*
    Part2
    Perform 5 mil iterations
    In each iteration perform multiplication and moduols for generator A until the number is multipler of 4
    Then do the same for generator B until its number is multiplier of 8
    Again XOR their least significat 16 bits, and if the result is all zeros, increase the counter
    */
    a = aInit;
    b = bInit;
    counter = 0;

    for(int i = 0; i < 5000000; i++){

        do{
            a *= aFactor;
            a %= devidor;
        }while(a%4 != 0);

        do{
        b *= bFactor;
        b %= devidor;
        }while(b%8 != 0);
        std::bitset<16> aBits(a);
        std::bitset<16> bBits(b);
        aBits ^= bBits;
        if(aBits.none()) counter += 1;

    }

    std::cout << counter;

}