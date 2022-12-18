using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day16
    {
        static int startPos = -1;
        static Dictionary<string,int> bestScoresDict = new Dictionary<string, int>();
        static Dictionary<int,int> valveToRate = new Dictionary<int, int>();
        static Dictionary<int,List<int>> valveToTunnels = new Dictionary<int, List<int>>();
        public static int calc(int pos, int valvesOpened, int time, int playersRemaining){
            if(time == 0){
                return playersRemaining==0 ? 0 : calc(startPos, valvesOpened, 26, playersRemaining-1); 
            }

            string key = pos + "|" + valvesOpened + "|" + time + "|" + playersRemaining;
            if(bestScoresDict.ContainsKey(key)){
                return bestScoresDict[key];
            }

            int score = 0;
            BitArray vO = new BitArray(new int[] {valvesOpened});
            if(valveToRate[pos] != 0 && !vO.Get(pos)){
                vO.Set(pos, true);
                int[] arr = new int[1];
                vO.CopyTo(arr,0);
                score = (time-1) * valveToRate[pos] + calc(pos, arr[0], time-1, playersRemaining);
            }

            foreach(int tunnel in valveToTunnels[pos]){
                score = Math.Max(score, calc(tunnel, valvesOpened, time-1, playersRemaining));
            }

            bestScoresDict[key] = score; 
            return score;
        }

        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day16.txt").ToList();

            Dictionary<string,int> valveToId = new Dictionary<string, int>();

            Dictionary<string,List<string>> tunnelsTemp = new Dictionary<string,List<string>>();
            Dictionary<string,int> valvesTemp = new Dictionary<string,int>();
            foreach (string line in lines){
                string[] lineParts = line.Split();
                valvesTemp[lineParts[1]] = int.Parse(lineParts[4].Split("=")[1].Split(";")[0]);

                List<string> valves = new List<string>();
                for(int i = 9; i < lineParts.Count() - 1; ++i){
                    valves.Add(lineParts[i].Split(",")[0]);
                }
                valves.Add(lineParts[lineParts.Count()-1]);
                tunnelsTemp[lineParts[1]] = valves;
            }

            int id = 0;
            foreach(string valve in valvesTemp.Keys){
                if(valvesTemp[valve] != 0){
                    valveToId[valve] = id;
                    id++;
                }
            }
            foreach(string valve in valvesTemp.Keys){
                if(valvesTemp[valve] == 0){
                    if(valve == "AA"){
                        startPos = id;
                    }
                    valveToId[valve] = id;
                    id++;
                }
            }
            foreach(string valve in valveToId.Keys){
                valveToRate[valveToId[valve]] = valvesTemp[valve];
            }

            int nonZeroRateValves = 0;
            foreach(int value in valveToRate.Values){
                if(value != 0){
                    nonZeroRateValves++;
                }
                foreach(string valve in tunnelsTemp.Keys){
                    List<int> tunels = new List<int>();
                    foreach(string tunnel in tunnelsTemp[valve]){
                        tunels.Add(valveToId[tunnel]);
                    }
                    valveToTunnels[valveToId[valve]] = tunels;
                }
            }

            Console.WriteLine(calc(startPos,0,30,0));
            Console.WriteLine(calc(startPos,0,26,1));
        }
    }
}