using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day20
    {
        public static void Solve()
        {
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day20.txt").ToList();

            List<Tuple<long, int>> numbers1 = new List<Tuple<long, int>>();
            List<Tuple<long, int>> numbers2 = new List<Tuple<long, int>>();
            Dictionary<long, int> sameNumbers = new Dictionary<long, int>();

            foreach (string line in lines)
            {
                int number1 = int.Parse(line);
                long number2 = number1 * 811589153L;
                if (sameNumbers.ContainsKey(number1))
                {
                    sameNumbers[number1]++;
                }
                else
                {
                    sameNumbers[number1] = 0;
                }
                numbers1.Add(new Tuple<long, int>(number1, sameNumbers[number1]));
                numbers2.Add(new Tuple<long, int>(number2, sameNumbers[number1]));
            }

            List<Tuple<long, int>> initialOrder1 = new List<Tuple<long, int>>(numbers1);
            List<Tuple<long, int>> initialOrder2 = new List<Tuple<long, int>>(numbers2);

            foreach (Tuple<long, int> number in initialOrder1)
            {
                int currentIndex = numbers1.IndexOf(number);
                long nextIndex = currentIndex + number.Item1;


                if (nextIndex < 0)
                {
                    nextIndex = nextIndex % (initialOrder1.Count - 1) + (initialOrder1.Count - 1);
                }
                if (nextIndex > initialOrder1.Count - 1)
                {
                    nextIndex = nextIndex % (initialOrder1.Count - 1);
                }

                if (currentIndex == nextIndex) continue;
                numbers1.RemoveAt(currentIndex);
                numbers1.Insert((int)nextIndex, number);

            }

            int zeroIndex = numbers1.IndexOf(new Tuple<long, int>(0, 0));
            Console.WriteLine(numbers1[(zeroIndex + 1000) % numbers1.Count].Item1 + numbers1[(zeroIndex + 2000) % numbers1.Count].Item1 + numbers1[(zeroIndex + 3000) % numbers1.Count].Item1);

            for (int i = 0; i < 10; ++i)
            {

                foreach (Tuple<long, int> number in initialOrder2)
                {
                    int currentIndex = numbers2.IndexOf(number);
                    long nextIndex = currentIndex + number.Item1;


                    if (nextIndex < 0)
                    {
                        nextIndex = nextIndex % (initialOrder2.Count - 1) + (initialOrder2.Count - 1);
                    }
                    if (nextIndex > initialOrder2.Count - 1)
                    {
                        nextIndex = nextIndex % (initialOrder2.Count - 1);
                    }

                    if (currentIndex == nextIndex) continue;
                    numbers2.RemoveAt(currentIndex);
                    numbers2.Insert((int)nextIndex, number);

                }

            }

            zeroIndex = numbers2.IndexOf(new Tuple<long, int>(0, 0));
            Console.WriteLine(numbers2[(zeroIndex + 1000) % numbers2.Count].Item1 + numbers2[(zeroIndex + 2000) % numbers2.Count].Item1 + numbers2[(zeroIndex + 3000) % numbers2.Count].Item1);
        }
    }
}