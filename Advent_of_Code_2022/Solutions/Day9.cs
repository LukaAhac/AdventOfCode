using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{

    public class Pair<T1, T2>
    {
        public Pair(T1 first, T2 second){
            First = first;
            Second = second;
        }
        public T1 First { get; set; }
        public T2 Second { get; set; }
    }

    public class Day9
    {
        public static void Solve()
        {
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day9.txt").ToList();

            List<Pair<int,int>> knots = new List<Pair<int,int>>();
            for(int i = 0; i < 10 ; ++i){
                knots.Add(new Pair<int,int>(0,0));
            }

            HashSet<string> tailVisitedPart1 = new HashSet<string>();
            tailVisitedPart1.Add("0|0");
            HashSet<string> tailVisitedPart2 = new HashSet<string>();
            tailVisitedPart2.Add("0|0");


            foreach (string line in lines){
                string[] lineParts = line.Split();

                for(int i = 0; i < int.Parse(lineParts[1]); ++i){

                    if(lineParts[0] == "U"){
                        knots[0].First--;
                    } else if (lineParts[0] == "D"){
                        knots[0].First++;
                    } else if (lineParts[0] == "L"){
                        knots[0].Second--;
                    } else if (lineParts[0] == "R"){
                        knots[0].Second++;
                    }

                    for(int knotIndex = 0; knotIndex < knots.Count - 1; ++knotIndex){
                        if(Math.Abs(knots[knotIndex].First - knots[knotIndex + 1].First) > 1 || Math.Abs(knots[knotIndex].Second - knots[knotIndex + 1].Second) > 1){

              
                            knots[knotIndex + 1].First += Math.Sign(knots[knotIndex].First - knots[knotIndex + 1].First);
                            knots[knotIndex + 1].Second += Math.Sign(knots[knotIndex].Second - knots[knotIndex + 1].Second);
    
                        }
                    }
                    tailVisitedPart1.Add(knots[1].First.ToString() + "|" + knots[1].Second.ToString());
                    tailVisitedPart2.Add(knots[knots.Count-1].First.ToString() + "|" + knots[knots.Count-1].Second.ToString());
                
                }
            }

            Console.WriteLine(tailVisitedPart1.Count);
            Console.WriteLine(tailVisitedPart2.Count);
        }

    }
}