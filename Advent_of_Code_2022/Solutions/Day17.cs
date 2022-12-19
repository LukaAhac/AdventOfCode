using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day17
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadAllLines("PuzzleInputs/day17.txt").ToList();
            string line = lines[0];

            int width = 7;
            List<List<char>> chamber = new List<List<char>>();
            for(int j = 0 ; j < 3; ++j){
                chamber.Add(new List<char>(Enumerable.Repeat('.',width)));
            }
            int pushIndex = 0;

            Dictionary<string,long> seenPatterns = new Dictionary<string, long>();
            Dictionary<string,long> patternToHeight = new Dictionary<string, long>();
            int watchDepth = 50;

            long height = 0;
            bool simulateEnd = false;
            long heightAtSimulationStart = 0;
            
            long i = 0;
            while(i < 1000000000000){
                if(chamber.Count >= watchDepth && i > 2022 && !simulateEnd){
                    string state = "";
                    for(int j = 0; j < watchDepth; ++j){
                        string row = new string(chamber[j].ToArray());
                        state += row;
                    }
                    state += "|" + (i % 5) + "|" + pushIndex;

                    if(seenPatterns.ContainsKey(state)){
                        heightAtSimulationStart = chamber.Count - 3;
                        long heightDiff = heightAtSimulationStart - patternToHeight[state];
                        long cylceSize = i - seenPatterns[state];
                        height += heightAtSimulationStart;

                        long rocksRemaining = 1000000000000 - i;
                        long cylcesToRepeat = (long)Math.Floor((double)rocksRemaining / (double)cylceSize);
                        i += cylcesToRepeat * cylceSize;
                        height += cylcesToRepeat * heightDiff;
                        simulateEnd = true;
                    }
                    seenPatterns[state] = i;
                    patternToHeight[state] = chamber.Count - 3;
                }

                bool settled = false;
                if(i % 5 == 0){
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    int anchorX = 2;
                    int anchorY = 0;
                    while(!settled){

                        if(line[pushIndex] == '>'
                        && anchorX < 3
                        && chamber[anchorY][anchorX + 4] == '.'){
                            anchorX++;
                        }
                        else if(line[pushIndex] == '<'
                        && anchorX > 0
                        && chamber[anchorY][anchorX - 1] == '.'){
                            anchorX--;
                        }
                        pushIndex = (pushIndex+1) % line.Count();

                        if(anchorY < chamber.Count - 1
                        && chamber[anchorY+1][anchorX] == '.'
                        && chamber[anchorY+1][anchorX + 1] == '.'
                        && chamber[anchorY+1][anchorX + 2] == '.'
                        && chamber[anchorY+1][anchorX + 3] == '.'){
                            anchorY++;
                        } else {
                            settled = true;
                            chamber[anchorY][anchorX] = '#';
                            chamber[anchorY][anchorX + 1] = '#';
                            chamber[anchorY][anchorX + 2] = '#';
                            chamber[anchorY][anchorX + 3] = '#';
                        }
                    }
                } else if(i % 5 == 1){
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    int anchorX = 3;
                    int anchorY = 1;
                    while(!settled){
                        if(line[pushIndex] == '>'
                        && anchorX < 5
                        && chamber[anchorY - 1][anchorX + 1] == '.'
                        && chamber[anchorY][anchorX + 2] == '.'
                        && chamber[anchorY + 1][anchorX + 1] == '.'){
                            anchorX++;
                        }
                        else if(line[pushIndex] == '<'
                        && anchorX > 1
                        && chamber[anchorY - 1][anchorX - 1] == '.'
                        && chamber[anchorY][anchorX - 2] == '.'
                        && chamber[anchorY + 1][anchorX - 1] == '.'){
                            anchorX--;
                        }
                        pushIndex = (pushIndex+1) % line.Count();

                        if(anchorY < chamber.Count - 2
                        && chamber[anchorY + 1][anchorX - 1] == '.'
                        && chamber[anchorY + 2][anchorX] == '.'
                        && chamber[anchorY + 1][anchorX + 1] == '.'){
                            anchorY++;
                        } else {
                            settled = true;
                            chamber[anchorY][anchorX] = '#';
                            chamber[anchorY - 1][anchorX] = '#';
                            chamber[anchorY + 1][anchorX] = '#';
                            chamber[anchorY][anchorX - 1] = '#';
                            chamber[anchorY][anchorX + 1] = '#';
                        }
                    }
                } else if(i % 5 == 2){
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    int anchorX = 3;
                    int anchorY = 1;
                    while(!settled){
                        if(line[pushIndex] == '>'
                        && anchorX < 5
                        && chamber[anchorY - 1][anchorX + 2] == '.'
                        && chamber[anchorY][anchorX + 2] == '.'
                        && chamber[anchorY + 1][anchorX + 2] == '.'){
                            anchorX++;
                        }
                        else if(line[pushIndex] == '<'
                        && anchorX > 1
                        && chamber[anchorY - 1][anchorX ] == '.'
                        && chamber[anchorY][anchorX ] == '.'
                        && chamber[anchorY + 1][anchorX - 2] == '.'){
                            anchorX--;
                        }
                        pushIndex = (pushIndex+1) % line.Count();

                        if(anchorY < chamber.Count - 2
                        && chamber[anchorY + 2][anchorX - 1] == '.'
                        && chamber[anchorY + 2][anchorX] == '.'
                        && chamber[anchorY + 2][anchorX + 1] == '.'){
                            anchorY++;
                        } else {
                            settled = true;
                            chamber[anchorY - 1][anchorX + 1] = '#';
                            chamber[anchorY][anchorX + 1] = '#';
                            chamber[anchorY + 1][anchorX + 1] = '#';
                            chamber[anchorY + 1][anchorX] = '#';
                            chamber[anchorY + 1][anchorX - 1] = '#';
                        }
                    }
                } else if(i % 5 == 3){
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    int anchorX = 2;
                    int anchorY = 0;
                    while(!settled){
                        if(line[pushIndex] == '>'
                        && anchorX < 6
                        && chamber[anchorY][anchorX + 1] == '.'
                        && chamber[anchorY + 1][anchorX + 1] == '.'
                        && chamber[anchorY + 2][anchorX + 1] == '.'
                        && chamber[anchorY + 3][anchorX + 1] == '.'){
                            anchorX++;
                        }
                        else if(line[pushIndex] == '<'
                        && anchorX > 0
                        && chamber[anchorY][anchorX - 1] == '.'
                        && chamber[anchorY + 1][anchorX - 1] == '.'
                        && chamber[anchorY + 2][anchorX - 1] == '.'
                        && chamber[anchorY + 3][anchorX - 1] == '.'){
                            anchorX--;
                        }
                        pushIndex = (pushIndex+1) % line.Count();

                        if(anchorY < chamber.Count - 4
                        && chamber[anchorY + 4][anchorX] == '.'){
                            anchorY++;
                        } else {
                            settled = true;
                            chamber[anchorY][anchorX] = '#';
                            chamber[anchorY + 1][anchorX] = '#';
                            chamber[anchorY + 2][anchorX] = '#';
                            chamber[anchorY + 3][anchorX] = '#';
                        }
                    }
                }  else if(i % 5 == 4){
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                    int anchorX = 2;
                    int anchorY = 0;
                    while(!settled){
                        if(line[pushIndex] == '>'
                        && anchorX < 5
                        && chamber[anchorY][anchorX + 2] == '.'
                        && chamber[anchorY + 1][anchorX + 2] == '.'){
                            anchorX++;
                        }
                        else if(line[pushIndex] == '<'
                        && anchorX > 0
                        && chamber[anchorY][anchorX - 1] == '.'
                        && chamber[anchorY + 1][anchorX - 1] == '.'){
                            anchorX--;
                        }
                        pushIndex = (pushIndex+1) % line.Count();

                        if(anchorY < chamber.Count - 2
                        && chamber[anchorY + 2][anchorX] == '.'
                        && chamber[anchorY + 2][anchorX + 1] == '.'){
                            anchorY++;
                        } else {
                            settled = true;
                            chamber[anchorY][anchorX] = '#';
                            chamber[anchorY][anchorX + 1] = '#';
                            chamber[anchorY + 1][anchorX] = '#';
                            chamber[anchorY + 1][anchorX + 1] = '#';
                        }
                    }
                }  

                int emptyRows = 0;
                for(int ind = 0; ind < chamber.Count; ++ind){
                    if(chamber[ind].SequenceEqual(new List<char>{'.','.','.','.','.','.','.'})){
                        emptyRows++;
                    }
                }
                while(emptyRows != 3){
                    if(emptyRows < 3){
                        chamber.Insert(0, new List<char>{'.','.','.','.','.','.','.'});
                        emptyRows++;
                    }else{
                        chamber.RemoveAt(0);
                        emptyRows--;
                    }
                }

                i++;

                if(i == 2022){
                    Console.WriteLine(chamber.Count - 3);
                }
            }

            Console.WriteLine(height + chamber.Count - 3 - heightAtSimulationStart);
        }
    }
}