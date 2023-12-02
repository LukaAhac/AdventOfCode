#include <iostream>
#include <fstream>
#include <string>
#include <map>

int isNumber(std::string testingString)
{
    std::map<std::string, int> numbersMappings = {
        {"one", 1},
        {"two", 2},
        {"three", 3},
        {"four", 4},
        {"five", 5},
        {"six", 6},
        {"seven", 7},
        {"eight", 8},
        {"nine", 9},
    };

    for (std::pair keyValue : numbersMappings)
    {
        if (testingString.compare(0, keyValue.first.length(), keyValue.first) == 0)
        {
            return keyValue.second;
        }
    }

    return -1;
}

int main(void)
{
    std::ifstream file("inputs/day1.txt");
    std::string line;
    int result_part1 = 0;
    int result_part2 = 0;

    while (std::getline(file, line))
    {
        for (int i = 0; i < line.length(); i++)
        {
            if (isdigit(line[i]))
            {
                result_part1 += 10 * (int(line[i]) - 48);
                result_part2 += 10 * (int(line[i]) - 48);
                break;
            }
            else
            {
                int result = isNumber(line.substr(i));
                if (result > 0)
                {
                    result_part2 += 10 * result;
                    break;
                }
            }
        }

        for (int i = line.length() - 1; i >= 0; i--)
        {
            if (isdigit(line[i]))
            {
                result_part1 += int(line[i]) - 48;
                result_part2 += int(line[i]) - 48;
                break;
            }
            else
            {
                int result = isNumber(line.substr(i));
                if (result > 0)
                {
                    result_part2 += result;
                    break;
                }
            }
        }
    }

    std::cout << result_part1 << std::endl;
    std::cout << result_part2 << std::endl;
}