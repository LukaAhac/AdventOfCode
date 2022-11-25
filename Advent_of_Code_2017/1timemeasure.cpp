#include <chrono>
#include <iostream>
#include <vector>

int main(int argc, char *argv[]){

    using namespace std::chrono;
    
    // Use auto keyword to avoid typing long
    // type definitions to get the timepoint
    // at this instant use function now()

    system("cd D:\\Coding\\Advent_of_Code_2017");

    std::vector<const char*> programms;

    for(int i = 1;i<argc;i++){
        std::string programToStart = argv[i];
        programToStart = "start " + programToStart;
        const char * toStart = programToStart.c_str();
        programms.push_back(toStart);
    }


    auto start = high_resolution_clock::now();

    for(auto programm : programms)
        system(programm);


    
    // After function call
    auto stop = high_resolution_clock::now();

    
    // Subtract stop and start timepoints and
    // cast it to required unit. Predefined units
    // are nanoseconds, microseconds, milliseconds,
    // seconds, minutes, hours. Use duration_cast()
    // function.
    auto duration = duration_cast<milliseconds>(stop - start);
    
    // To get the value of duration use the count()
    // member function on the duration object
    std::cout << duration.count() << std::endl;
    }