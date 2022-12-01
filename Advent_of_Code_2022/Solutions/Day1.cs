using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day1
    {
        public static void Solve(){
            List<string> inputLines = System.IO.File.ReadLines("PuzzleInputs/day1.txt").ToList();

            List<int> topThree = new List<int> {0,0,0};

            int currentValue = 0;
            foreach (string line in inputLines){
                if(line == ""){
                    if(currentValue > topThree[0]){
                        topThree[0] = currentValue;
                        topThree.Sort();
                    }
                    currentValue = 0;
                } else {
                    currentValue += Int32.Parse(line);
                }
            }

            Console.WriteLine(topThree[2]);
            Console.WriteLine(topThree.Sum());
        }
    }
}