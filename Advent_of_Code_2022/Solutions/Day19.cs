using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day19
    {
        public static List<int> oreRobotsCost = new List<int>();
        public static List<int> clayRobotsCost = new List<int>();
        public static List<Tuple<int,int>> obisidanRobotsCost = new List<Tuple<int,int>>();
        public static List<Tuple<int,int>> geodeRobotsCost = new List<Tuple<int,int>>();
        public static Dictionary<int,int> bestScores = new Dictionary<int, int>();
        public static List<int> maxRobots = new List<int>();

        public static int testBlueprint(int blueprintID, int time, int oR, int cR, int obR, int gR, int o, int c, int ob, int g){
            if(time == 0){
                return g;
            }

            string key = time + "|" + oR + "|" + cR + "|" + obR + "|" + gR+ "|" + o + "|" + c + "|" + ob + "|" + g;
            int keyHash = key.GetHashCode();
            if(bestScores.ContainsKey(keyHash)){
                return bestScores[keyHash];
            }

            int score = g;

            if(o >= oreRobotsCost[blueprintID] && oR < maxRobots[0] && (oR * time + o) < time * maxRobots[0]){
                score = Math.Max(score, testBlueprint(blueprintID, time-1, oR+1, cR, obR, gR, o-oreRobotsCost[blueprintID] + oR, c + cR, ob + obR, g + gR));
            }
            if(o >= clayRobotsCost[blueprintID] && cR < maxRobots[1] && (cR * time + c) < time * maxRobots[1]){
                score = Math.Max(score, testBlueprint(blueprintID, time-1, oR, cR+1, obR, gR, o-clayRobotsCost[blueprintID] + oR, c + cR, ob + obR, g + gR));
            }
            if(o >= obisidanRobotsCost[blueprintID].Item1 && c>= obisidanRobotsCost[blueprintID].Item2 && obR < maxRobots[2] && (obR * time + ob) < time * maxRobots[2]){
                score = Math.Max(score, testBlueprint(blueprintID, time-1, oR, cR, obR+1, gR, o-obisidanRobotsCost[blueprintID].Item1 + oR, c-obisidanRobotsCost[blueprintID].Item2 + cR, ob + obR, g + gR));
            }
            if(o >= geodeRobotsCost[blueprintID].Item1 && ob >= geodeRobotsCost[blueprintID].Item2){
                score = Math.Max(score, testBlueprint(blueprintID, time-1, oR, cR, obR, gR+1, o-geodeRobotsCost[blueprintID].Item1 + oR, c + cR, ob-geodeRobotsCost[blueprintID].Item2 + obR, g + gR));
            }

            score = Math.Max(score, testBlueprint(blueprintID, time-1, oR, cR, obR, gR, o + oR, c + cR, ob + obR, g + gR));

            bestScores[keyHash] = score;

            return score;
        }

        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day19.txt").ToList();


            foreach(string line in lines){
                string[] lineParts = line.Split();

                oreRobotsCost.Add(int.Parse(lineParts[6]));
                clayRobotsCost.Add(int.Parse(lineParts[12]));
                obisidanRobotsCost.Add(new Tuple<int,int>(int.Parse(lineParts[18]),int.Parse(lineParts[21])));
                geodeRobotsCost.Add(new Tuple<int,int>(int.Parse(lineParts[27]),int.Parse(lineParts[30])));
            }

            int score = 0;

            for(int i = 0; i < clayRobotsCost.Count; ++i){
                maxRobots.Clear();
                maxRobots.Add(new List<int>(new int[]{oreRobotsCost[i],clayRobotsCost[i],obisidanRobotsCost[i].Item1,geodeRobotsCost[i].Item1}).Max());
                maxRobots.Add(obisidanRobotsCost[i].Item2);
                maxRobots.Add(geodeRobotsCost[i].Item2);
                bestScores.Clear();
                int calc = testBlueprint(i,24,1,0,0,0,0,0,0,0);
                score += (i+1) * calc;
            }

            Console.WriteLine(score);


            score = 1;
            for(int i = 0 ; i < 3; ++i){
                maxRobots.Clear();
                maxRobots.Add(new List<int>(new int[]{oreRobotsCost[i],clayRobotsCost[i],obisidanRobotsCost[i].Item1,geodeRobotsCost[i].Item1}).Max());
                maxRobots.Add(obisidanRobotsCost[i].Item2);
                maxRobots.Add(geodeRobotsCost[i].Item2);
                bestScores.Clear();
                int calc = testBlueprint(i,32,1,0,0,0,0,0,0,0);
                score *= calc;
            }

            Console.WriteLine(score);

        }
    }
}