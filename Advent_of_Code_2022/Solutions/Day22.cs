using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day22
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day22.txt").ToList();

            string pathOrigin = lines[lines.Count-1];

            lines.RemoveAt(lines.Count - 1);
            lines.RemoveAt(lines.Count - 1);

            List<List<char>> map = new List<List<char>>();
            foreach(string line in lines){
                List<char> row = new List<char>(line);
                map.Add(row);
            }

            int currentRow = 0;
            int currentCol = 0;
            List<char> directions = new List<char>( new char[] {'R','D','L','U'});
            int currentDir = 0;
            string path = pathOrigin;

            for(int i = 0; i < map[0].Count; ++i){
                if(map[0][i] == '.'){
                    currentCol = i;
                    break;
                }
            }

            bool moveTurn = true;

            while(path.Count() > 0){
                if(moveTurn){
                    moveTurn = false;
                    int moves;
                    int takeNumbers = 0;
                    foreach(char c in path){
                        if(char.IsNumber(c)){
                            takeNumbers++;
                        } else {
                            break;
                        }
                    }
                    moves = int.Parse(path.Substring(0,takeNumbers));
                    path = path.Substring(takeNumbers);

                    while(moves > 0){
                        if(directions[currentDir] == 'R'){
                            if(currentCol == map[currentRow].Count - 1){
                                int leftSide = 0;
                                while(char.IsWhiteSpace(map[currentRow][leftSide])){
                                    leftSide++;
                                }
                                if(map[currentRow][leftSide] == '.'){
                                    currentCol = leftSide;
                                }
                            } else if(map[currentRow][currentCol + 1] == '.'){
                                currentCol++;
                            }
                        } else if(directions[currentDir] == 'L'){
                            if(currentCol == 0 || char.IsWhiteSpace(map[currentRow][currentCol - 1])){
                                if(map[currentRow][map[currentRow].Count - 1] == '.'){
                                    currentCol = map[currentRow].Count - 1;
                                }
                            }else if(map[currentRow][currentCol - 1] == '.'){
                                currentCol--;
                            }   
                        } else if(directions[currentDir] == 'U'){
                            if(currentRow == 0 || char.IsWhiteSpace(map[currentRow - 1][currentCol])){
                                int donwSide = map.Count - 1;
                                while(map[donwSide].Count <= currentCol || char.IsWhiteSpace(map[donwSide][currentCol])){
                                    donwSide--;
                                }
                                if(map[donwSide][currentCol] == '.'){
                                    currentRow = donwSide;
                                }
                            } else if(map[currentRow - 1][currentCol] == '.'){
                                currentRow--;
                            }   
                        } else if(directions[currentDir] == 'D'){
                            if(currentRow == map.Count - 1 || map[currentRow+1].Count <= currentCol || char.IsWhiteSpace(map[currentRow + 1][currentCol])){
                                int donwSide = 0;
                                while(char.IsWhiteSpace(map[donwSide][currentCol])){
                                    donwSide++;
                                }
                                if(map[donwSide][currentCol] == '.'){
                                    currentRow = donwSide;
                                }
                            } else if(map[currentRow + 1][currentCol] == '.'){
                                currentRow++;
                            }   
                        }
                        moves--;
                    }
                } else {
                    moveTurn = true;
                    char turn = path[0];
                    path = path.Substring(1);

                    if(turn == 'R'){
                        currentDir = (currentDir + 1) % 4;
                    } else {
                        if(currentDir == 0){
                            currentDir = 3;
                        } else {
                            currentDir--;
                        }
                    }
                }
            }

            Console.WriteLine((currentRow + 1) * 1000 + (currentCol + 1) * 4 + currentDir);


            //Part 2 hardcoded for my input shape

            /*
                My input shape
                   0      50    150   200
              0    *****  back  right
              50   ***** bottom *****
              100   left front  *****
              150   top  *****  *****
              200
            */

            List<List<char>> top = new List<List<char>>();
            List<List<char>> bottom = new List<List<char>>();
            List<List<char>> left = new List<List<char>>();
            List<List<char>> right = new List<List<char>>();
            List<List<char>> front = new List<List<char>>();
            List<List<char>> back = new List<List<char>>();

            for(int row = 50; row < 100; ++row){
                List<char> rowList = new List<char>();
                List<char> lineRow = new List<char>(lines[row]);
                for(int col = 50; col < 100; ++col){
                    rowList.Add(lineRow[col]);
                }
                bottom.Add(rowList);
            }

            for(int row = 0; row < 50; ++row){
                List<char> rowList = new List<char>();
                List<char> lineRow = new List<char>(lines[row]);
                for(int col = 50; col < 100; ++col){
                    rowList.Add(lineRow[col]);
                }
                back.Add(rowList);
            }

            for(int row = 0; row < 50; ++row){
                List<char> rowList = new List<char>();
                List<char> lineRow = new List<char>(lines[row]);
                for(int col = 100; col < 150; ++col){
                    rowList.Add(lineRow[col]);
                }
                right.Add(rowList);
            }

            for(int row = 100; row < 150; ++row){
                List<char> rowList = new List<char>();
                List<char> lineRow = new List<char>(lines[row]);
                for(int col = 50; col < 100; ++col){
                    rowList.Add(lineRow[col]);
                }
                front.Add(rowList);
            }

            for(int row = 100; row < 150; ++row){
                List<char> rowList = new List<char>();
                List<char> lineRow = new List<char>(lines[row]);
                for(int col = 0; col < 50; ++col){
                    rowList.Add(lineRow[col]);
                }
                left.Add(rowList);
            }

            for(int row = 150; row < 200; ++row){
                List<char> rowList = new List<char>();
                List<char> lineRow = new List<char>(lines[row]);
                for(int col = 0; col < 50; ++col){
                    rowList.Add(lineRow[col]);
                }
                top.Add(rowList);
            }

            string currentSide = "back";
            currentRow = 0;
            currentCol = 0;
            currentDir = 0;
            moveTurn = true;
            path = pathOrigin;

            while(path.Count() > 0){
                if(moveTurn){
                    moveTurn = false;
                    int moves;
                    int takeNumbers = 0;
                    foreach(char c in path){
                        if(char.IsNumber(c)){
                            takeNumbers++;
                        } else {
                            break;
                        }
                    }
                    moves = int.Parse(path.Substring(0,takeNumbers));
                    path = path.Substring(takeNumbers);

                    while(moves > 0){
                        if(currentSide == "back"){
                            if(directions[currentDir] == 'R'){
                                if(currentCol == 49){
                                    if(right[currentRow][0] == '.'){
                                        currentSide = "right";
                                        currentCol = 0;
                                    }
                                } else if(back[currentRow][currentCol+1] == '.'){
                                    currentCol++;
                                }
                            } else if(directions[currentDir] == 'L'){
                                if(currentCol == 0){
                                    if(left[49 - currentRow][0] == '.'){
                                        currentSide = "left";
                                        currentRow = 49 - currentRow;
                                        currentCol = 0;
                                        currentDir = 0;
                                    }
                                } else if(back[currentRow][currentCol - 1] == '.'){
                                    currentCol--;
                                }
                            } else if(directions[currentDir] == 'U'){
                                if(currentRow == 0){
                                    if(top[currentCol][0] == '.'){
                                        currentSide = "top";
                                        currentRow = currentCol;
                                        currentCol = 0;
                                        currentDir = 0;
                                    }
                                } else if(back[currentRow - 1][currentCol] == '.'){
                                    currentRow--;
                                }
                            } else if(directions[currentDir] == 'D'){
                                if(currentRow == 49){
                                    if(bottom[0][currentCol] == '.'){
                                        currentSide = "bottom";
                                        currentRow = 0;
                                    }
                                } else if(back[currentRow + 1][currentCol] == '.'){
                                    currentRow++;
                                }
                            }
                        } else if(currentSide == "front"){
                            if(directions[currentDir] == 'R'){
                                if(currentCol == 49){
                                    if(right[49 - currentRow][49] == '.'){
                                        currentSide = "right";
                                        currentRow = 49 - currentRow;
                                        currentCol = 49;
                                        currentDir = 2;
                                    }
                                } else if(front[currentRow][currentCol+1] == '.'){
                                    currentCol++;
                                }
                            } else if(directions[currentDir] == 'L'){
                                if(currentCol == 0){
                                    if(left[currentRow][49] == '.'){
                                        currentSide = "left";
                                        currentCol = 49;
                                    }
                                } else if(front[currentRow][currentCol - 1] == '.'){
                                    currentCol--;
                                }
                            } else if(directions[currentDir] == 'U'){
                                if(currentRow == 0){
                                    if(bottom[49][currentCol] == '.'){
                                        currentSide = "bottom";
                                        currentRow = 49;
                                    }
                                } else if(front[currentRow - 1][currentCol] == '.'){
                                    currentRow--;
                                }
                            } else if(directions[currentDir] == 'D'){
                                if(currentRow == 49){
                                    if(top[currentCol][49] == '.'){
                                        currentSide = "top";
                                        currentRow = currentCol;
                                        currentCol = 49;
                                        currentDir = 2;
                                    }
                                } else if(front[currentRow + 1][currentCol] == '.'){
                                    currentRow++;
                                }
                            }
                        } else if(currentSide == "top"){
                            if(directions[currentDir] == 'R'){
                                if(currentCol == 49){
                                    if(front[49][currentRow] == '.'){
                                        currentSide = "front";
                                        currentCol = currentRow;
                                        currentRow = 49;
                                        currentDir = 3;
                                    }
                                } else if(top[currentRow][currentCol+1] == '.'){
                                    currentCol++;
                                }
                            } else if(directions[currentDir] == 'L'){
                                if(currentCol == 0){
                                    if(back[0][currentRow] == '.'){
                                        currentSide = "back";
                                        currentCol = currentRow;
                                        currentRow = 0;
                                        currentDir = 1;
                                    }
                                } else if(top[currentRow][currentCol - 1] == '.'){
                                    currentCol--;
                                }
                            } else if(directions[currentDir] == 'U'){
                                if(currentRow == 0){
                                    if(left[49][currentCol] == '.'){
                                        currentSide = "left";
                                        currentRow = 49;
                                    }
                                } else if(top[currentRow - 1][currentCol] == '.'){
                                    currentRow--;
                                }
                            } else if(directions[currentDir] == 'D'){
                                if(currentRow == 49){
                                    if(right[0][currentCol] == '.'){
                                        currentSide = "right";
                                        currentRow = 0;
                                    }
                                } else if(top[currentRow + 1][currentCol] == '.'){
                                    currentRow++;
                                }
                            }
                        } else if(currentSide == "bottom"){
                            if(directions[currentDir] == 'R'){
                                if(currentCol == 49){
                                    if(right[49][currentRow] == '.'){
                                        currentSide = "right";
                                        currentCol = currentRow;
                                        currentRow = 49;
                                        currentDir = 3;
                                    }
                                } else if(bottom[currentRow][currentCol+1] == '.'){
                                    currentCol++;
                                }
                            } else if(directions[currentDir] == 'L'){
                                if(currentCol == 0){
                                    if(left[0][currentRow] == '.'){
                                        currentSide = "left";
                                        currentCol = currentRow;
                                        currentRow = 0;
                                        currentDir = 1;
                                    }
                                } else if(bottom[currentRow][currentCol - 1] == '.'){
                                    currentCol--;
                                }
                            } else if(directions[currentDir] == 'U'){
                                if(currentRow == 0){
                                    if(back[49][currentCol] == '.'){
                                        currentSide = "back";
                                        currentRow = 49;
                                    }
                                } else if(bottom[currentRow - 1][currentCol] == '.'){
                                    currentRow--;
                                }
                            } else if(directions[currentDir] == 'D'){
                                if(currentRow == 49){
                                    if(front[0][currentCol] == '.'){
                                        currentSide = "front";
                                        currentRow = 0;
                                    }
                                } else if(bottom[currentRow + 1][currentCol] == '.'){
                                    currentRow++;
                                }
                            }
                        } else if(currentSide == "left"){
                            if(directions[currentDir] == 'R'){
                                if(currentCol == 49){
                                    if(front[currentRow][0] == '.'){
                                        currentSide = "front";
                                        currentCol = 0;
                                    }
                                } else if(left[currentRow][currentCol+1] == '.'){
                                    currentCol++;
                                }
                            } else if(directions[currentDir] == 'L'){
                                if(currentCol == 0){
                                    if(back[49 - currentRow][0] == '.'){
                                        currentSide = "back";
                                        currentRow = 49 - currentRow;
                                        currentCol = 0;
                                        currentDir = 0;
                                    }
                                } else if(left[currentRow][currentCol - 1] == '.'){
                                    currentCol--;
                                }
                            } else if(directions[currentDir] == 'U'){
                                if(currentRow == 0){
                                    if(bottom[currentCol][0] == '.'){
                                        currentSide = "bottom";
                                        currentRow = currentCol;
                                        currentCol = 0;
                                        currentDir = 0;
                                    }
                                } else if(left[currentRow - 1][currentCol] == '.'){
                                    currentRow--;
                                }
                            } else if(directions[currentDir] == 'D'){
                                if(currentRow == 49){
                                    if(top[0][currentCol] == '.'){
                                        currentSide = "top";
                                        currentRow = 0;
                                    }
                                } else if(left[currentRow + 1][currentCol] == '.'){
                                    currentRow++;
                                }
                            }
                        } else if(currentSide == "right"){
                            if(directions[currentDir] == 'R'){
                                if(currentCol == 49){
                                    if(front[49 - currentRow][49] == '.'){
                                        currentSide = "front";
                                        currentRow = 49 - currentRow;
                                        currentCol = 49;
                                        currentDir = 2;
                                    }
                                } else if(right[currentRow][currentCol+1] == '.'){
                                    currentCol++;
                                }
                            } else if(directions[currentDir] == 'L'){
                                if(currentCol == 0){
                                    if(back[currentRow][49] == '.'){
                                        currentSide = "back";
                                        currentCol = 49;
                                    }
                                } else if(right[currentRow][currentCol - 1] == '.'){
                                    currentCol--;
                                }
                            } else if(directions[currentDir] == 'U'){
                                if(currentRow == 0){
                                    if(top[49][currentCol] == '.'){
                                        currentSide = "top";
                                        currentRow = 49;
                                    }
                                } else if(right[currentRow - 1][currentCol] == '.'){
                                    currentRow--;
                                }
                            } else if(directions[currentDir] == 'D'){
                                if(currentRow == 49){
                                    if(bottom[currentCol][49] == '.'){
                                        currentSide = "bottom";
                                        currentRow = currentCol;
                                        currentCol = 49;
                                        currentDir = 2;
                                    }
                                } else if(right[currentRow + 1][currentCol] == '.'){
                                    currentRow++;
                                }
                            }
                        }

                        moves--;
                    }
                } else {
                    moveTurn = true;
                    char turn = path[0];
                    path = path.Substring(1);

                    if(turn == 'R'){
                        currentDir = (currentDir + 1) % 4;
                    } else {
                        if(currentDir == 0){
                            currentDir = 3;
                        } else {
                            currentDir--;
                        }
                    }
                }
            }

            //Console.WriteLine(currentSide); -> current side is left which side start at (100,0) in my input map
            int rowStart = 100;
            int colStart = 0;
            Console.WriteLine((currentRow + 1 + rowStart) * 1000 + (currentCol + 1 + colStart) * 4 + currentDir);
        }
    }
}