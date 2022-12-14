using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day14
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day14.txt").ToList();

            int sandGeneratorX = 0;
            int sandGeneratorY = 500;

            int minY = int.MaxValue;
            int maxY = int.MinValue;
            int maxX = int.MinValue;

            List<List<Tuple<int,int>>> rockPaths = new List<List<Tuple<int, int>>>();
            foreach(string line in lines){
                string[] lineSplited = line.Split(" -> ");

                List<Tuple<int,int>> rockPath = new List<Tuple<int, int>>();
                foreach(string point in lineSplited){
                    string[] pointParts = point.Split(",");
                    Tuple<int,int> pointT = new Tuple<int,int>(int.Parse(pointParts[1]), int.Parse(pointParts[0]));
                    rockPath.Add(pointT);
                    if(pointT.Item2 < minY){
                        minY = pointT.Item2;
                    }
                    if(pointT.Item2 > maxY){
                        maxY = pointT.Item2;
                    }
                    if(pointT.Item1 > maxX){
                        maxX = pointT.Item1;
                    }
                }
                rockPaths.Add(rockPath);
            }
            sandGeneratorY = sandGeneratorY - minY + 1;

            List<List<char>> cave = new List<List<char>>();
            for(int i = 0; i <= maxX + 1; ++i){
                List<char> row = new List<char>(Enumerable.Repeat('.', maxY - minY + 1 + 2));
                cave.Add(row);
            }

            foreach(var rockPath in rockPaths){
                for(int i = 0; i < rockPath.Count - 1; ++i){
                    if(rockPath[i].Item1 != rockPath[i + 1].Item1){
                        int from = rockPath[i].Item1 < rockPath[i+1].Item1 ? rockPath[i].Item1 : rockPath[i+1].Item1;
                        int to = rockPath[i].Item1 > rockPath[i+1].Item1 ? rockPath[i].Item1 : rockPath[i+1].Item1;

                        for(int j = from; j <= to; ++j){
                            cave[j][rockPath[i].Item2 - minY + 1] = '#';
                        }
                    } else {
                        int from = rockPath[i].Item2 < rockPath[i+1].Item2 ? rockPath[i].Item2 : rockPath[i+1].Item2;
                        int to = rockPath[i].Item2 > rockPath[i+1].Item2 ? rockPath[i].Item2 : rockPath[i+1].Item2;
                        from = from - minY + 1;
                        to = to - minY + 1;

                        for(int j = from; j <= to; ++j){
                            cave[rockPath[i].Item1][j] = '#';
                        }
                    }
                }
            }

            List<List<char>> cave2 = cave.ConvertAll(row => new List<char>(row));
            cave2.Add(new List<char>(Enumerable.Repeat('#', maxY - minY + 1 + 2)));
            
            int sandCount = -1;
            bool infinityReachd = false;
            while(!infinityReachd){
                sandCount++;
                int sandX = sandGeneratorX;
                int sandY = sandGeneratorY;

                while(true){
                    if(sandX == maxX+1){
                        infinityReachd=true;
                        break;
                    }


                    if(cave[sandX+1][sandY] == '.'){
                        sandX++;
                        continue;
                    } else if (cave[sandX+1][sandY-1] == '.'){
                        sandX++;
                        sandY--;
                        continue;
                    } else if(cave[sandX+1][sandY+1] == '.'){
                        sandX++;
                        sandY++;
                        continue;
                    }

                    cave[sandX][sandY] = 'o';
                    break;
                }
            }
            Console.WriteLine(sandCount);

            int sandCount2 = 0;
            while(cave2[sandGeneratorX][sandGeneratorY] == '.'){
                sandCount2++;
                int sandX = sandGeneratorX;
                int sandY = sandGeneratorY;

                while(true){
                    if(sandY == 0){
                        foreach(var row in cave2){
                            row.Insert(0, '.');
                        }
                        sandY++;
                        sandGeneratorY++;
                        cave2[maxX+2][0] = '#';
                    } else if(sandY == cave2[0].Count-1){
                        foreach(var row in cave2){
                            row.Add('.');
                        }
                        cave2[maxX+2][cave2[maxX+2].Count-1] = '#';
                    }

                    if(cave2[sandX+1][sandY] == '.'){
                        sandX++;
                        continue;
                    } else if (cave2[sandX+1][sandY-1] == '.'){
                        sandX++;
                        sandY--;
                        continue;
                    } else if(cave2[sandX+1][sandY+1] == '.'){
                        sandX++;
                        sandY++;
                        continue;
                    }

                    cave2[sandX][sandY] = 'o';
                    break;
                }
            }

            Console.WriteLine(sandCount2);
        }
    }
}