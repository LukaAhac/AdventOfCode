using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day7
    {
        public static void Solve()
        {
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day7.txt").ToList();
            
            Dictionary<string,int> dirToFileSize = new Dictionary<string, int>();
            Dictionary<string, List<string>> dirToDirsContained = new Dictionary<string, List<string>>();

            string currentPath = "";
            int currentSize = 0;
            List<string> dirsContained = new List<string>();

            int index = 0;
            string line;
            while (true){
                if(index < lines.Count){
                    line = lines[index];
                } else if (currentPath != ""){
                    line = "$ cd ..";
                } else {
                    break;
                }

                string[] lineSplited = line.Split();

                if (lineSplited[1] == "cd"){

                    if(!dirToFileSize.ContainsKey(currentPath)){
                        dirToFileSize[currentPath] = currentSize;
                        currentSize = 0;
                        dirToDirsContained[currentPath] = new List<string>(dirsContained);
                        dirsContained.Clear();
                    }

                    if (lineSplited[2] == ".."){
                        if(dirToDirsContained.ContainsKey(currentPath)){
                            foreach (string dir in dirToDirsContained[currentPath]){
                                dirToFileSize[currentPath] += dirToFileSize[dir];
                            }
                        }
                        currentPath = currentPath.Substring(0, currentPath.Length-1);
                        currentPath = currentPath.Substring(0, currentPath.LastIndexOf('/') + 1);
                    } else if (lineSplited[2] == "/") {
                        currentPath = "/";
                    } else {
                        currentPath += lineSplited[2] + "/";
                    }

                } else if (lineSplited[1] != "ls"){
                    if (lineSplited[0] == "dir"){
                        dirsContained.Add(currentPath + lineSplited[1] + "/");
                    } else {
                        currentSize += Int32.Parse(lineSplited[0]);
                    }
                }

                index++;
            }

            int result = 0;
            foreach (string key in dirToFileSize.Keys){
                if (dirToFileSize[key] <= 100000) {
                    result += dirToFileSize[key];
                }
            }
            Console.WriteLine(result);

            int spaceAvailible = 70000000 - dirToFileSize["/"];
            int spaceNeeded = 30000000 - spaceAvailible;
            
            List<int> dirSizes = dirToFileSize.Values.ToList();
            dirSizes.Sort();
            int i = 0;
            while(dirSizes[i] < spaceNeeded){
                i++;
            }
            Console.WriteLine(dirSizes[i]);
        }

    }
}