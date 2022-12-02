using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day2
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day2.txt").ToList();

            Dictionary<char, int> hisPlays = new Dictionary<char,int>{{'A', 1}, {'B' , 2}, {'C' , 3}};
            Dictionary<char, int> myPlays = new Dictionary<char,int>{{'X', 1}, {'Y' , 2}, {'Z' , 3}};
            Dictionary<char, int> outcomes = new Dictionary<char,int>{{'X', 0}, {'Y' , 3}, {'Z' , 6}};


            int score = 0;
            int score2 = 0;

            foreach (string line in lines){
                score += myPlays[line[2]];

                if (hisPlays[line[0]] == myPlays[line[2]]) score += 3;
                else if(myPlays[line[2]] == (hisPlays[line[0]]+1) || hisPlays[line[0]] == 3 && myPlays[line[2]] == 1) score += 6;


                score2 += outcomes[line[2]];

                if (line[2] == 'X'){
                    if(line[0] == 'A') score2 += 3;
                    else score2 += hisPlays[line[0]] - 1;
                } else if (line[2] == 'Y'){
                    score2 += hisPlays[line[0]];
                } else {
                    if(line[0] == 'C') score2 += 1;
                    else score2 += hisPlays[line[0]] + 1;
                }
            }
            Console.WriteLine(score);
            Console.WriteLine(score2);
        }
    }
}