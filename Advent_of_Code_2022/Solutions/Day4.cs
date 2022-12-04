using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day4
    {
        public static void Solve()
        {
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day4.txt").ToList();

            int fullyContained = 0;
            int fullyContained2 = 0;

            foreach (string line in lines){
                string[] leftRight = line.Split(',');

                int l1 = Int32.Parse(leftRight[0].Split('-')[0]);
                int l2 = Int32.Parse(leftRight[0].Split('-')[1]);
                int r1 = Int32.Parse(leftRight[1].Split('-')[0]);
                int r2 = Int32.Parse(leftRight[1].Split('-')[1]);

                if(l1 <= r1 && l2 >= r2 || r1 <= l1 && r2 >= l2){
                    fullyContained++;
                }
                if(l1 <= r1 && l2 >= r1 || l1 <= r2 && l2 >= r2 || r1 <= l1 && r2 >= l1 || r1 <= l2 && r2 >= l2){
                    fullyContained2++;
                }
            }  

            Console.WriteLine(fullyContained);
            Console.WriteLine(fullyContained2);

        }
    }
}