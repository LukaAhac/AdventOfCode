using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day13
    {

        public static List<string> separatePacket(string packet)
        {
            List<string> packetParts = new List<string>();
            string temp = "";
            int index = 1;
            int listDepth = 0;
            while (index < packet.Count() - 1)
            {
                if (packet[index] == '[')
                {
                    listDepth++;
                    temp += packet[index];
                }
                else if (packet[index] == ']')
                {
                    listDepth--;
                    temp += packet[index];
                }
                else if (packet[index] == ',' && listDepth == 0)
                {
                    packetParts.Add(temp);
                    temp = "";
                }
                else
                {
                    temp += packet[index];
                }
                index++;
                if(index >= packet.Count() - 1){
                    packetParts.Add(temp);
                    break;
                }
            }
            return packetParts;
        }

        public static int comparePairs(string first, string second)
        {
            if(!first.StartsWith("[") && !second.StartsWith("[")){
                int firstInt = int.Parse(first);
                int secondInt = int.Parse(second);
                if(firstInt < secondInt) return 1;
                else if(firstInt > secondInt) return -1;
                else return 0;
            }

            List<string> firstSeparated = new List<string>();
            if (first.StartsWith("["))
            {
                firstSeparated = separatePacket(first);
            } else {
                firstSeparated.Add(first);
            }
            List<string> secondSeparated = new List<string>();
            if (second.StartsWith("["))
            {
                secondSeparated = separatePacket(second);
            } else {
                secondSeparated.Add(second);
            }

            int index = 0;

            while(index < firstSeparated.Count && index < secondSeparated.Count){
                int result = comparePairs(firstSeparated[index], secondSeparated[index]);
                if (result != 0) return result;

                index++;
            }

            if(firstSeparated.Count < secondSeparated.Count) return 1;
            else if(firstSeparated.Count > secondSeparated.Count) return -1;
            else return 0;
        }

        public static void Solve()
        {
            string lines = System.IO.File.ReadAllText("PuzzleInputs/day13.txt");

            string[] pairs = lines.Split("\n\n");
            int score = 0;
            int pairIndex = 0;
            foreach (string pair in pairs)
            {
                string[] pairSplit = pair.Split("\n");
                pairIndex++;
               if(comparePairs(pairSplit[0], pairSplit[1]) == 1){
                score += pairIndex;
               }
    
            }
            Console.WriteLine(score);

            List<string> packets = new List<string>();

            foreach(string packet in lines.Split("\n")){
                if (packet != string.Empty){
                    packets.Add(packet);
                }
            }
            packets.Add("[[2]]");
            packets.Add("[[6]]");

            packets.Sort((a,b) => {return comparePairs(b,a);});
            int indexTwo = 0;
            int indexSix = 0;
            for (int i = 0; i < packets.Count; ++i){
                if (packets[i] == "[[2]]"){
                    indexTwo = i + 1;
                } else if (packets[i] == "[[6]]"){
                    indexSix = i + 1;
                }
            }

            Console.WriteLine(indexTwo*indexSix);
        }
    }
}