using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    class Monkey{
        public Monkey(List<long> items, string op, string value2, int divisibleBy, int ifTrue, int ifFalse)
        {
            this.itemsPart1 = new List<long>(items);
            this.itemsPart2 = new List<long>(items);
            this.op = op;
            this.value2 = value2;
            this.divisibleBy = divisibleBy;
            this.ifTrue = ifTrue;
            this.ifFalse = ifFalse;
        }
        public List<long> itemsPart1 { get; set; }
        public List<long> itemsPart2 { get; set; }
        public string op { get; set; }
        public string value2 { get;  set; }
        public int divisibleBy;
        public int ifTrue { get; set; }
        public int ifFalse { get; set; }

        public int thorwPart1(){
            itemsPart1[0] = operationNew(itemsPart1[0]);
            itemsPart1[0] = (int)Math.Floor((float)itemsPart1[0] / 3);

            if(itemsPart1[0] % divisibleBy == 0){
                return ifTrue;
            }
            return ifFalse;
        }
        public int thorwPart2(){
            itemsPart2[0] = operationNew(itemsPart2[0]);

            if(itemsPart2[0] % divisibleBy == 0){
                return ifTrue;
            }
            return ifFalse;
        }

        private long operationNew(long old){
            long secondOperand;
            if (value2 == "old"){
                secondOperand = old;
            } else {
                secondOperand = long.Parse(value2);
            }

            switch(op){
                case "+":
                return old + secondOperand;
                case "*":
                return old * secondOperand;
            }
            return -1;
        }
    }

    public class Day11
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day11.txt").ToList();

            List<Monkey> monkeys = new List<Monkey>();
            List<int> monkeysActivityPart1 = new List<int>();
            List<int> monkeysActivityPart2 = new List<int>();
            long lcm = 1;
            int index = 0;

            while(index < lines.Count){
                string[] items = lines[index+1].Trim().Split();
                items = items.Skip(2).ToArray();
                List<long> itemsParsed = new List<long>();
                foreach (var item in items){
                    if(item.Last() == ','){
                    itemsParsed.Add(long.Parse(item.Remove(item.Count()-1)));
                    } else {
                        itemsParsed.Add(long.Parse(item));
                    }

                }
                string[] operationRow = lines[index+2].Trim().Split();
                int divisibleBy = int.Parse(lines[index+3].Trim().Split()[3]);
                lcm *= divisibleBy;
                int ifTrue = int.Parse(lines[index+4].Trim().Split()[5]);
                int ifFalse = int.Parse(lines[index+5].Trim().Split()[5]);
                index += 7;

                monkeys.Add(new Monkey(itemsParsed, operationRow[4], operationRow[5], divisibleBy, ifTrue, ifFalse));
                monkeysActivityPart1.Add(0);
                monkeysActivityPart2.Add(0);
            }

            for(int i = 0; i < 10000; ++i){
                if(i < 20){
                    for(int monkeyIndex = 0; monkeyIndex < monkeys.Count; ++monkeyIndex){
                        while(monkeys[monkeyIndex].itemsPart1.Count > 0){
                            monkeys[monkeys[monkeyIndex].thorwPart1()].itemsPart1.Add(monkeys[monkeyIndex].itemsPart1[0]);
                            monkeys[monkeyIndex].itemsPart1.RemoveAt(0);
                            monkeysActivityPart1[monkeyIndex]++;
                        }
                    } 

                }
                else if ( i == 20) {
                    monkeysActivityPart1 = monkeysActivityPart1.OrderDescending().ToList();
                    Console.WriteLine(monkeysActivityPart1[0] * monkeysActivityPart1[1]);
                }

                for(int monkeyIndex = 0; monkeyIndex < monkeys.Count; ++monkeyIndex){
                    while(monkeys[monkeyIndex].itemsPart2.Count > 0){
                        monkeys[monkeys[monkeyIndex].thorwPart2()].itemsPart2.Add(monkeys[monkeyIndex].itemsPart2[0] % lcm);
                        monkeys[monkeyIndex].itemsPart2.RemoveAt(0);
                        monkeysActivityPart2[monkeyIndex]++;
                    }
                }
            }

            monkeysActivityPart2 = monkeysActivityPart2.OrderDescending().ToList();
            Console.WriteLine((long)monkeysActivityPart2[0] * monkeysActivityPart2[1]);
        }
    }
}