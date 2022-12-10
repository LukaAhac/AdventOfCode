using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{

    public class Day10
    {
        public static void Solve()
        {
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day10.txt").ToList();

            int cylce = 1;
            int X = 1;
            int signalStrength = 0;
            int goalCycle = 20;
            List<List<char>> screen = new List<List<char>>();
            for(int i = 0; i < 6; ++i){
                screen.Add(new List<char>());
            }
            int screenRow = 0;

            int index = 0;
            while(index < lines.Count){
                if(cylce == goalCycle){
                    signalStrength += cylce * X;
                    if(goalCycle == 220){
                        goalCycle = -1;
                    } else {
                        goalCycle += 40;
                    }
                }

                if(screen[screenRow].Count == 40){
                    screenRow++;
                }

                if(((cylce - 1) % 40) >= X - 1 && ((cylce - 1) % 40) <= X + 1){
                    screen[screenRow].Add('#');
                } else {
                    screen[screenRow].Add('.');
                }

                if (lines[index] == "noop"){
                    cylce++;
                    index++;
                } else if (lines[index].Split()[0] == "addx"){
                    lines[index] = lines[index].Split()[1];
                    cylce++;
                } else {
                    X += int.Parse(lines[index]);
                    cylce++;
                    index++;
                }
            }

            Console.WriteLine(signalStrength);

            foreach(var row in screen){
                foreach(var pixel in row){
                    Console.Write(pixel);
                }
                Console.Write("\n");
            }

        }

    }
}