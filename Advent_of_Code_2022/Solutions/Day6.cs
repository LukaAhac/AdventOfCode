using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day6
    {
        public static void Solve()
        {
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day6.txt").ToList();
            
            string line = lines[0];

            int index = 4;

            while(true){
                string substr = line.Substring(index-4,4);
                for(int i = 0; i < 4; ++i){
                    if(substr.Count(f => (f == substr[i])) != 1){
                        goto next;
                    }
                }
                Console.WriteLine(index);
                break;
                next:
                index++;
            }

            index = 14;

            while(true){
                string substr = line.Substring(index-14,14);
                for(int i = 0; i < 14; ++i){
                    if(substr.Count(f => (f == substr[i])) != 1){
                        goto next;
                    }
                }
                Console.WriteLine(index);
                break;
                next:
                index++;
            }
        }

    }
}