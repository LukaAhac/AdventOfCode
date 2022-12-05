using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day5
    {
        public static void Solve()
        {
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day5.txt").ToList();

            List<Stack<char>> stacks = new List<Stack<char>>();
            List<Stack<char>> stacks2 = new List<Stack<char>>();
            bool parseInputStacks = true;

            foreach (string line in lines){
                if (parseInputStacks){
                    if(line[1] == '1'){
                        parseInputStacks = false;
                        for (int i = 0; i < stacks.Count; ++i){
                            stacks2.Add(new Stack<char>(stacks[i]));
                            stacks[i] = new Stack<char>(stacks[i]);
                        }
                    } else {
                        int stackIndex = 0;
                        int charIndex = 1;

                        while(charIndex < line.Length){
                            if(stacks.Count < stackIndex + 1){
                                stacks.Add(new Stack<char>());
                            }

                            if(line[charIndex] != ' '){
                                stacks[stackIndex].Push(line[charIndex]);
                            }

                            stackIndex++;
                            charIndex += 4;
                        }
                    }
                } else {
                    if(line == ""){
                        continue;
                    }
                    List<string> inputSeparated = line.Split(' ').ToList();
                    int count = Int32.Parse(inputSeparated[1]);
                    int from = Int32.Parse(inputSeparated[3]) - 1;
                    int to = Int32.Parse(inputSeparated[5]) - 1;

                    for(int i = count; i > 0; --i){
                        stacks[to].Push(stacks[from].Pop());
                    }

                    List<char> holdChars = new List<char>();
                    for(int i = count; i > 0; --i){
                        holdChars.Add(stacks2[from].Pop());
                    }

                    for(int i = count; i > 0; --i){
                        stacks2[to].Push(holdChars[i-1]);
                    }
                }
            }
            foreach (Stack<char> stack in stacks){
                Console.Write(stack.Peek());
            }
            Console.Write("\n");
            foreach (Stack<char> stack in stacks2){
                Console.Write(stack.Peek());
            }
        }
    }
}