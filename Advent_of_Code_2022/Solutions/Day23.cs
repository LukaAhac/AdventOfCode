using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day23
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day23.txt").ToList();

            List<string> elves = new List<string>();

            for(int row = 0; row < lines.Count; ++row){
                for(int col = 0; col < lines[row].Count(); ++col){
                    if(lines[row][col] == '#'){
                        elves.Add(row + "|" + col);
                    }
                }
            }

            List<char> directions = new List<char>(new char[]{'N','S','W','E'});
            int currentDir = 0;

            string COLLISION_MARKER = int.MaxValue + "|" + int.MinValue;

            int round = 0;
            bool elvesMoved = true;
            while(elvesMoved){
                Dictionary<string,string> proposedMovements = new Dictionary<string,string>();
                elvesMoved = false;

                foreach(string elf in elves){

                    string[] leftPos = elf.Split("|");
                    int elfX = int.Parse(leftPos[0]);
                    int elfY = int.Parse(leftPos[1]);

                    bool move = false;
                    for(int row = -1; row <= 1; ++row){
                        for(int col = -1; col <= 1; ++col){
                            if(row == 0 & col == 0) continue;
                            if(elves.Contains((elfX+row) + "|" + (elfY + col))){
                                move = true;
                                goto exit;
                            }
                        }
                    }

                    exit:
                    if(move){
                        for(int elfDir = currentDir; elfDir < currentDir + 4; elfDir++){

                            if(directions[elfDir % 4] == 'N'){
                                if(!elves.Contains((elfX - 1) + "|" + (elfY - 1))
                                && !elves.Contains((elfX - 1) + "|" + (elfY))
                                && !elves.Contains((elfX - 1) + "|" + (elfY + 1))){
                                    string moveTo = (elfX - 1) + "|" + (elfY);
                                    if(proposedMovements.ContainsKey(moveTo)){
                                        proposedMovements[moveTo] = COLLISION_MARKER;
                                    } else {
                                        proposedMovements[moveTo] = elf;
                                    }
                                    break;
                                }
                            } else if(directions[elfDir % 4] == 'S'){
                                if(!elves.Contains((elfX + 1) + "|" + (elfY - 1))
                                && !elves.Contains((elfX + 1) + "|" + (elfY))
                                && !elves.Contains((elfX + 1) + "|" + (elfY + 1))){
                                    string moveTo = (elfX + 1) + "|" + (elfY);
                                    if(proposedMovements.ContainsKey(moveTo)){
                                        proposedMovements[moveTo] = COLLISION_MARKER;
                                    } else {
                                        proposedMovements[moveTo] = elf;
                                    }
                                    break;
                                }
                            } else if(directions[elfDir % 4] == 'W'){
                                if(!elves.Contains((elfX - 1) + "|" + (elfY - 1))
                                && !elves.Contains((elfX) + "|" + (elfY - 1))
                                && !elves.Contains((elfX + 1) + "|" + (elfY - 1))){
                                    string moveTo = (elfX) + "|" + (elfY - 1);
                                    if(proposedMovements.ContainsKey(moveTo)){
                                        proposedMovements[moveTo] = COLLISION_MARKER;
                                    } else {
                                        proposedMovements[moveTo] = elf;
                                    }
                                    break;
                                }
                            } else if(directions[elfDir % 4] == 'E'){
                                if(!elves.Contains((elfX - 1) + "|" + (elfY + 1))
                                && !elves.Contains((elfX) + "|" + (elfY + 1))
                                && !elves.Contains((elfX + 1) + "|" + (elfY + 1))){
                                    string moveTo = (elfX) + "|" + (elfY + 1);
                                    if(proposedMovements.ContainsKey(moveTo)){
                                        proposedMovements[moveTo] = COLLISION_MARKER;
                                    } else {
                                        proposedMovements[moveTo] = elf;
                                    }
                                    break;
                                }
                            }
                        }
                    }
                }

                foreach(string location in proposedMovements.Keys){
                    if(proposedMovements[location] != COLLISION_MARKER){
                        elves.Remove(proposedMovements[location]);
                        elves.Add(location);
                        elvesMoved = true;
                    }
                }

                currentDir = (currentDir + 1) % 4;
                round++;
                if(round == 10){
                    int minX = elves.Select(elf => int.Parse(elf.Split("|")[0])).Min();
                    int maxX = elves.Select(elf => int.Parse(elf.Split("|")[0])).Max();
                    int minY = elves.Select(elf => int.Parse(elf.Split("|")[1])).Min();
                    int maxY = elves.Select(elf => int.Parse(elf.Split("|")[1])).Max();
                    Console.WriteLine((maxX - minX + 1) * (maxY - minY + 1) - elves.Count);
                }
            }
            Console.WriteLine(round);
        }
    }
}