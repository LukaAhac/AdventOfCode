using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day3
    {
        public static void Solve()
        {
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day3.txt").ToList();

            int priorityScore = 0;

            foreach (string line in lines)
            {
                string firstComponent = line.Substring(0, line.Length / 2);
                string secondComponent = line.Substring(line.Length / 2);

                char commonChar = ' ';
                foreach (char c1 in firstComponent)
                {
                    if (secondComponent.Contains(c1))
                    {
                        commonChar = c1;
                        break;
                    }
                }

                if (char.IsLower(commonChar))
                {
                    priorityScore += (int)commonChar - 96;
                }
                else
                {
                    priorityScore += (int)commonChar - 38;
                }
            }
            Console.WriteLine(priorityScore);

            int priorityScore2 = 0;
            char commonChar2 = ' ';
            for (int i = 0; i < lines.Count; i += 3)
            {
                foreach (char c1 in lines[i])
                {
                    if (lines[i + 1].Contains(c1) && lines[i + 2].Contains(c1))
                    {
                        commonChar2 = c1;
                        break;
                    }
                }

                if (char.IsLower(commonChar2))
                {
                    priorityScore2 += (int)commonChar2 - 96;
                }
                else
                {
                    priorityScore2 += (int)commonChar2 - 38;
                }
            }
            Console.WriteLine(priorityScore2);

        }
    }
}