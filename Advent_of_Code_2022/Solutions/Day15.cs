using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day15
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day15.txt").ToList();

            List<Tuple<int,int>> sensors = new List<Tuple<int, int>>();
            List<Tuple<int,int>> beacons = new List<Tuple<int, int>>();

            foreach(string line in lines){
                string[] lineSplit = line.Split();
                sensors.Add(new Tuple<int,int>(int.Parse(lineSplit[2].Split("=")[1].Split(",")[0]), int.Parse(lineSplit[3].Split("=")[1].Split(":")[0])));
                beacons.Add(new Tuple<int,int>(int.Parse(lineSplit[8].Split("=")[1].Split(",")[0]), int.Parse(lineSplit[9].Split("=")[1])));
            }

            int goalRow = 2000000;
            List<Tuple<int,int>> ranges = new List<Tuple<int, int>>();
            for(int i = 0; i < sensors.Count; ++i){
                int manDist = Math.Abs(sensors[i].Item1 - beacons[i].Item1) + Math.Abs(sensors[i].Item2 - beacons[i].Item2);
               if(Math.Abs(sensors[i].Item2 - goalRow) < manDist){
                manDist -= Math.Abs(sensors[i].Item2 - goalRow);
                ranges.Add(new Tuple<int,int>(sensors[i].Item1 - manDist, sensors[i].Item1 + manDist));
               }
            }

            bool changesMade = true;
            while(changesMade){
                changesMade = false;
                for(int i = 0; i < ranges.Count - 1; ++i){
                    for(int j = ranges.Count - 1; j > i; --j){
                        if(ranges[i].Item1 <= ranges[j].Item1 && ranges[i].Item2 >= ranges[j].Item2){
                            ranges.RemoveAt(j);
                            changesMade = true;
                        } else if(ranges[j].Item1 <= ranges[i].Item1 && ranges[j].Item2 >= ranges[i].Item2){
                            ranges.RemoveAt(i);
                            changesMade = true;
                        } else if(ranges[i].Item1 <= ranges[j].Item1 && ranges[i].Item2 >= ranges[j].Item1){
                            ranges[i] = new Tuple<int, int>(ranges[i].Item1, ranges[j].Item2);
                            ranges.RemoveAt(j);
                            changesMade = true;
                        } else if(ranges[i].Item1 <= ranges[j].Item2 && ranges[i].Item2 >= ranges[j].Item2){
                            ranges[i] = new Tuple<int, int>(ranges[j].Item1, ranges[i].Item2);
                            ranges.RemoveAt(j);
                            changesMade = true;
                        }
                    }
                }
            }

            int rangesTotal = 0;
            foreach(var range in ranges){
                rangesTotal += range.Item2 - range.Item1 + 1;
            }

            HashSet<Tuple<int,int>> beaconsInGoalRow = new HashSet<Tuple<int, int>>();
            foreach(var beacon in beacons){
                if (beacon.Item2 == goalRow){
                    beaconsInGoalRow.Add(new Tuple<int, int>(beacon.Item1, beacon.Item2));
                }
            }
            rangesTotal -= beaconsInGoalRow.Count;

            Console.WriteLine(rangesTotal);

            for(int i = 0; i < sensors.Count; ++i){
                int manDistOver = Math.Abs(sensors[i].Item1 - beacons[i].Item1) + Math.Abs(sensors[i].Item2 - beacons[i].Item2) + 1;
                int rowOffset = -1;
                for(int col = sensors[i].Item1 - manDistOver; col <= sensors[i].Item1 + manDistOver; ++col){
                    rowOffset++;
                    if(col < 0) continue;
                    if(col > 4000000) break;
                    int row1 = sensors[i].Item2 + rowOffset;
                    int row2 = sensors[i].Item2 - rowOffset;

                    bool found1 = true;
                    bool found2 = true;
                    for(int j = 0; j < sensors.Count; ++j){
                        if(j == i) continue;
                        if(!found1 && !found2) break;
                        int manDist = Math.Abs(sensors[j].Item1 - beacons[j].Item1) + Math.Abs(sensors[j].Item2 - beacons[j].Item2);

                        int dist1 = Math.Abs(col - sensors[j].Item1) + Math.Abs(row1 - sensors[j].Item2);
                        int dist2 = Math.Abs(col - sensors[j].Item1) + Math.Abs(row2 - sensors[j].Item2);

                        if(dist1 <= manDist){
                            found1 = false;
                        }
                        if(dist2 <= manDist){
                            found2 = false;
                        }
                        
                    }
                    if(found1 && row1 >= 0 && row1 <= 4000000){
                        Console.WriteLine((long)col * 4000000 + row1);
                        return;
                    }
                    if(found2 && row2 >= 0 && row2 <= 4000000){
                        Console.WriteLine((long)col * 4000000 + row2);
                        return;
                    }
                }
            }
        }
    }
}