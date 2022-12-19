using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day18
    {
        public static List<Tuple<int, int, int>> cubes = new List<Tuple<int, int, int>>();
        public static HashSet<Tuple<int, int, int>> cubesInside = new HashSet<Tuple<int, int, int>>();
        public static HashSet<Tuple<int, int, int>> cubesOutside = new HashSet<Tuple<int, int, int>>();
        public static int maxVolume = 0;
        public static bool isExterior(Tuple<int, int, int> testCube)
        {
            if (cubesInside.Contains(testCube)) return false;
            if (cubesOutside.Contains(testCube)) return true;

            HashSet<Tuple<int, int, int>> expansionCubes = new HashSet<Tuple<int, int, int>>();
            HashSet<Tuple<int, int, int>> lastDiscovoredCubes = new HashSet<Tuple<int, int, int>>();
            expansionCubes.Add(testCube);
            lastDiscovoredCubes.Add(testCube);

            while (lastDiscovoredCubes.Count > 0)
            {
                HashSet<Tuple<int, int, int>> newDiscoveredCubes = new HashSet<Tuple<int, int, int>>();
                foreach (var cube in lastDiscovoredCubes)
                {
                    Tuple<int, int, int> c1 = new Tuple<int, int, int>(cube.Item1 - 1, cube.Item2, cube.Item3);
                    Tuple<int, int, int> c2 = new Tuple<int, int, int>(cube.Item1 + 1, cube.Item2, cube.Item3);
                    Tuple<int, int, int> c3 = new Tuple<int, int, int>(cube.Item1, cube.Item2 - 1, cube.Item3);
                    Tuple<int, int, int> c4 = new Tuple<int, int, int>(cube.Item1, cube.Item2 + 1, cube.Item3);
                    Tuple<int, int, int> c5 = new Tuple<int, int, int>(cube.Item1, cube.Item2, cube.Item3 - 1);
                    Tuple<int, int, int> c6 = new Tuple<int, int, int>(cube.Item1, cube.Item2, cube.Item3 + 1);

                    if (!cubes.Contains(c1)) newDiscoveredCubes.Add(c1);
                    if (!cubes.Contains(c2)) newDiscoveredCubes.Add(c2);
                    if (!cubes.Contains(c3)) newDiscoveredCubes.Add(c3);
                    if (!cubes.Contains(c4)) newDiscoveredCubes.Add(c4);
                    if (!cubes.Contains(c5)) newDiscoveredCubes.Add(c5);
                    if (!cubes.Contains(c6)) newDiscoveredCubes.Add(c6);
                }

                newDiscoveredCubes.ExceptWith(expansionCubes);
                expansionCubes.UnionWith(newDiscoveredCubes);

                if (expansionCubes.Count >= maxVolume)
                {
                    cubesOutside.UnionWith(expansionCubes);
                    return true;
                }

                foreach (var cube in newDiscoveredCubes)
                {
                    if (cubesOutside.Contains(cube))
                    {
                        cubesOutside.UnionWith(expansionCubes);
                        return true;
                    }
                    if (cubesInside.Contains(cube))
                    {
                        cubesInside.UnionWith(expansionCubes);
                        return false;
                    }
                }

                lastDiscovoredCubes = newDiscoveredCubes;
            }

            cubesInside.UnionWith(expansionCubes);
            return false;
        }
        public static void Solve()
        {
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day18.txt").ToList();

            int maxCoord = int.MinValue;
            int minCoord = int.MaxValue;

            foreach (string line in lines)
            {
                string[] lineParts = line.Split(",");
                Tuple<int, int, int> cube = new Tuple<int, int, int>(int.Parse(lineParts[0]), int.Parse(lineParts[1]), int.Parse(lineParts[2]));
                cubes.Add(cube);

                if (cube.Item1 > maxCoord) maxCoord = cube.Item1;
                if (cube.Item2 > maxCoord) maxCoord = cube.Item2;
                if (cube.Item3 > maxCoord) maxCoord = cube.Item3;
                if (cube.Item1 < minCoord) minCoord = cube.Item1;
                if (cube.Item2 < minCoord) minCoord = cube.Item2;
                if (cube.Item3 < minCoord) minCoord = cube.Item3;

            }

            maxVolume = (int)Math.Pow(maxCoord - minCoord, 3);

            int surface = 0;
            int exteriorSurface = 0;

            foreach (var cube in cubes)
            {
                List<Tuple<int, int, int>> newCubes = new List<Tuple<int, int, int>>();
                newCubes.Add(new Tuple<int, int, int>(cube.Item1 - 1, cube.Item2, cube.Item3));
                newCubes.Add(new Tuple<int, int, int>(cube.Item1 + 1, cube.Item2, cube.Item3));
                newCubes.Add(new Tuple<int, int, int>(cube.Item1, cube.Item2 - 1, cube.Item3));
                newCubes.Add(new Tuple<int, int, int>(cube.Item1, cube.Item2 + 1, cube.Item3));
                newCubes.Add(new Tuple<int, int, int>(cube.Item1, cube.Item2, cube.Item3 - 1));
                newCubes.Add(new Tuple<int, int, int>(cube.Item1, cube.Item2, cube.Item3 + 1));

                foreach (var c in newCubes)
                {
                    if (!cubes.Contains(c))
                    {
                        surface++;
                        if (isExterior(c))
                        {
                            exteriorSurface++;
                        }
                    }
                }
            }

            Console.WriteLine(surface);
            Console.WriteLine(exteriorSurface);

        }
    }
}