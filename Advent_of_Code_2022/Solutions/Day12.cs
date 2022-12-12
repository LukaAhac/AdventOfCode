using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day12
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day12.txt").ToList();

            List<List<int>> elevationGrid = new List<List<int>>();
            List<Tuple<int,int>> startingPositions = new List<Tuple<int, int>>();

            int x = 0, y = 0;
            int xS = 0,yS = 0,xE = 0,yE = 0;
            foreach (string line in lines) {
                elevationGrid.Add(new List<int>());
                foreach (char c in line){
                    if(c == 'S'){
                        xS = x;
                        yS = y;
                        elevationGrid.Last().Add((int)'a');
                    } else if ( c == 'E'){
                        xE = x;
                        yE = y;
                        elevationGrid.Last().Add((int)'z');
                    } else {
                        if(c == 'a'){
                            startingPositions.Add(new Tuple<int,int>(x,y));
                        }
                        elevationGrid.Last().Add((int)c);
                    }
                    y++;
                }
                x++;
                y=0;
            }

            startingPositions.Insert(0, new Tuple<int,int>(xS,yS));
            int height = elevationGrid.Count;
            int width = elevationGrid[0].Count;

            int minIterations = int.MaxValue;
            for(int i = 0; i < startingPositions.Count; ++i){

                HashSet<Tuple<int,int>> currentLocations = new HashSet<Tuple<int, int>>();
                HashSet<Tuple<int,int>> visitedLocations = new HashSet<Tuple<int, int>>();
                currentLocations.Add(new Tuple<int,int>(startingPositions[i].Item1,startingPositions[i].Item2));
                visitedLocations.Add(new Tuple<int,int>(startingPositions[i].Item1,startingPositions[i].Item2));

                int iterations = 0;
                while(currentLocations.Count > 0){
                    iterations++;
                    HashSet<Tuple<int,int>> tempLocations = new HashSet<Tuple<int, int>>();
                    foreach(var loc in currentLocations){
                        if(loc.Item1 > 0 &&
                            !visitedLocations.Contains(new Tuple<int,int>(loc.Item1 - 1, loc.Item2)) &&
                            elevationGrid[loc.Item1][loc.Item2] + 1 >= elevationGrid[loc.Item1 - 1][loc.Item2]){
                                tempLocations.Add(new Tuple<int,int>(loc.Item1 - 1, loc.Item2));
                                visitedLocations.Add(new Tuple<int,int>(loc.Item1 - 1, loc.Item2));
                        }
                        if(loc.Item1 < height - 1 &&
                            !visitedLocations.Contains(new Tuple<int,int>(loc.Item1 + 1, loc.Item2)) &&
                            elevationGrid[loc.Item1][loc.Item2] + 1 >= elevationGrid[loc.Item1 + 1][loc.Item2]){
                                tempLocations.Add(new Tuple<int,int>(loc.Item1 + 1, loc.Item2));
                                visitedLocations.Add(new Tuple<int,int>(loc.Item1 + 1, loc.Item2));
                        }
                        if(loc.Item2 > 0 &&
                            !visitedLocations.Contains(new Tuple<int,int>(loc.Item1, loc.Item2 - 1)) &&
                            elevationGrid[loc.Item1][loc.Item2] + 1 >= elevationGrid[loc.Item1][loc.Item2 - 1]){
                                tempLocations.Add(new Tuple<int,int>(loc.Item1, loc.Item2 - 1));
                                visitedLocations.Add(new Tuple<int,int>(loc.Item1, loc.Item2 - 1));
                        }
                        if(loc.Item2 < width - 1 &&
                            !visitedLocations.Contains(new Tuple<int,int>(loc.Item1, loc.Item2 + 1)) &&
                            elevationGrid[loc.Item1][loc.Item2] + 1 >= elevationGrid[loc.Item1][loc.Item2 + 1]){
                                tempLocations.Add(new Tuple<int,int>(loc.Item1, loc.Item2 + 1));
                                visitedLocations.Add(new Tuple<int,int>(loc.Item1, loc.Item2 + 1));
                        }
                    }

                    currentLocations.Clear();
                    currentLocations = tempLocations;

                    if(currentLocations.Contains(new Tuple<int, int>(xE,yE))){
                        if(i == 0){
                            Console.WriteLine(iterations);
                        }
                        if(iterations < minIterations){
                            minIterations = iterations;
                        }
                        break;
                    }
                }
            }
            Console.WriteLine(minIterations);
        }
    }
}