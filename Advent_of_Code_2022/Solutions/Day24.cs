using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day24
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day24.txt").ToList();

            int startRow = 0;
            int startCol = 0;
            int endRow = lines.Count - 1;
            int endCol = 0;

            Dictionary<string,List<char>> blizzards = new  Dictionary<string,List<char>>();

            for(int i = 0; i < lines.Count; ++i){
                if(i == 0){
                    startCol = lines[i].IndexOf('.');
                } else if(i == lines.Count - 1){
                    endCol = lines[i].IndexOf('.');
                } else {
                    for(int j = 1; j < lines[i].Count() - 1; ++j){
                        if(lines[i][j] != '.'){
                            blizzards[i + "|" + j] = new List<char>(new char[]{lines[i][j]});
                        }
                    }
                }
            }

            HashSet<string> positions = new HashSet<string>();
            positions.Add(startRow + "|" + startCol);

            string startPos = startRow + "|" + startCol;
            string endPos = endRow + "|" + endCol;
            int state = 1;
            string goalPos = endPos;

            int minutes = 0;
            while(true){
                minutes++;

                Dictionary<string,List<char>> newBlizzards = new Dictionary<string,List<char>>();

                foreach(string blizz in blizzards.Keys){
                    string[] blizzParts = blizz.Split("|");
                    int row = int.Parse(blizzParts[0]);
                    int col = int.Parse(blizzParts[1]);

                    foreach(char direction in blizzards[blizz]){
                        if(direction == '<'){
                            string key = row + "|" + ((col - 1) < startCol ? endCol : col - 1);
                            if(!newBlizzards.ContainsKey(key)){
                                newBlizzards[key] = new List<char>();
                            }
                            newBlizzards[key].Add(direction);
                        } else if (direction == '>'){
                            string key = row + "|" + ((col + 1) > endCol ? startCol : col + 1);
                            if(!newBlizzards.ContainsKey(key)){
                                newBlizzards[key] = new List<char>();
                            }
                            newBlizzards[key].Add(direction);
                        } else if (direction == '^'){
                            string key = ((row - 1) < 1 ? endRow - 1 : row - 1) + "|" + col;
                            if(!newBlizzards.ContainsKey(key)){
                                newBlizzards[key] = new List<char>();
                            }
                            newBlizzards[key].Add(direction);
                        } else if (direction == 'v'){
                            string key = ((row + 1) > (endRow - 1) ? 1 : row + 1) + "|" + col;
                            if(!newBlizzards.ContainsKey(key)){
                                newBlizzards[key] = new List<char>();
                            }
                            newBlizzards[key].Add(direction);
                        }
                    }
                }

                blizzards = newBlizzards;

                HashSet<string> newPositions = new HashSet<string>();

                foreach(string pos in positions){
                    string[] posParts = pos.Split("|");

                    int row = int.Parse(posParts[0]);
                    int col = int.Parse(posParts[1]);

                    string up = (row-1) + "|" + col;
                    string down = (row+1) + "|" + col;
                    string left = row + "|" + (col - 1);
                    string right = row + "|" + (col + 1);

                    if((row > 1 || row == 1 && col == startCol) && !blizzards.ContainsKey(up)) newPositions.Add(up);
                    if((row < (endRow - 1) || row == (endRow - 1) && col == endCol) && !blizzards.ContainsKey(down)) newPositions.Add(down);
                    if(col > startCol && row < endRow && !blizzards.ContainsKey(left)) newPositions.Add(left);
                    if(col < endCol && row > startRow && !blizzards.ContainsKey(right)) newPositions.Add(right);
                    if(!blizzards.ContainsKey(pos)) newPositions.Add(pos);
                }

                positions = newPositions;

                if(positions.Contains(goalPos)){
                    positions.Clear();
                    positions.Add(goalPos);
                    if(state == 1){
                        Console.WriteLine(minutes);
                        goalPos = startPos;
                    } else if(state == 2){
                        goalPos = endPos;
                    } else if(state == 3){
                        Console.WriteLine(minutes);
                        break;
                    }
                    state++;
                }
            }
        }
    }
}