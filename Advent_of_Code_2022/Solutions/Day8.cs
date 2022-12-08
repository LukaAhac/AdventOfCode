using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day8
    {
        public static void Solve()
        {
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day8.txt").ToList();

            List<List<int>> grid = new List<List<int>>();
            Dictionary<string,bool> visibilityMap = new Dictionary<string, bool>();

            foreach (string line in lines){
                grid.Add(new List<char>(line).Select(x => Int32.Parse(Char.ToString(x))).ToList());
            }

            for(int row = 1; row < grid.Count - 1; ++row){
                for(int i = 1; i < grid.Count - 1; ++i){
                    bool visible = true;
                    for(int j = 0; j < i; ++j){
                        if(grid[row][i] <= grid[row][j]){
                            visible = false;
                            break;
                        }
                    }
                    if(visible){
                        visibilityMap[row.ToString() + "," + i.ToString()] = true;
                    } else {
                        visible = true;
                        for(int j = i + 1; j < grid.Count; ++j){
                            if(grid[row][i] <= grid[row][j]){
                            visible = false;
                            break;
                            }
                        }
                        if(visible){
                        visibilityMap[row.ToString() + "," + i.ToString()] = true;
                    }
                    }
                }
            }

            for(int col = 1; col < grid.Count - 1; ++col){
                for(int i = 1; i < grid.Count - 1; ++i){
                    bool visible = true;
                    for(int j = 0; j < i; ++j){
                        if(grid[i][col] <= grid[j][col]){
                            visible = false;
                            break;
                        }
                    }
                    if(visible){
                        visibilityMap[i.ToString() + "," + col.ToString()] = true;
                    } else {
                        visible = true;
                        for(int j = i + 1; j < grid.Count; ++j){
                            if(grid[i][col] <= grid[j][col]){
                            visible = false;
                            break;
                            }
                        }
                        if(visible){
                        visibilityMap[i.ToString() + "," + col.ToString()] = true;
                    }
                    }
                }
            }

            int visibleTrees = visibilityMap.Count + 4 * (grid.Count) - 4;
            Console.WriteLine(visibleTrees);

            int highestScore = 0;

            for(int row = 1; row < grid.Count - 1; ++row){
                for(int col = 1; col < grid.Count - 1; ++col){
                    int left = 0;
                    int right = 0;
                    int top = 0;
                    int down = 0;
                    for(int i = col - 1; i >= 0; --i){
                        left++;
                        if(grid[row][i] >= grid[row][col]){
                            break;
                        }
                    }
                    for(int i = col + 1; i < grid.Count; ++i){
                        right++;
                        if(grid[row][i] >= grid[row][col]){
                            break;
                        }
                    }
                    for(int i = row - 1; i >= 0; --i){
                        top++;
                        if(grid[i][col] >= grid[row][col]){
                            break;
                        }
                    }
                    for(int i = row + 1; i < grid.Count; ++i){
                        down++;
                        if(grid[i][col] >= grid[row][col]){
                            break;
                        }
                    }

                    int score = left * right * top * down;

                    highestScore = score > highestScore ? score: highestScore;
                }
            }

            Console.WriteLine(highestScore);
        }

    }
}