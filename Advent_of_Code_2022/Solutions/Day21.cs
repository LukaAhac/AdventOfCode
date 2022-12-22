using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Data;

namespace Solutions
{
    public class Day21
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day21.txt").ToList();

            Dictionary<string,double> numberMonkeyOrigin = new Dictionary<string, double>();
            Dictionary<string,string> operationMonkeyOrigin = new Dictionary<string, string>();

            foreach(string line in lines){
                string[] lineParts = line.Split();

                if(lineParts.Count() == 2){
                    numberMonkeyOrigin[lineParts[0].Substring(0,4)] = double.Parse(lineParts[1]);
                } else {
                    operationMonkeyOrigin[lineParts[0].Substring(0,4)] = line.Substring(6);
                }
            }

            Dictionary<string,double> numberMonkey = new Dictionary<string, double>(numberMonkeyOrigin);
            Dictionary<string,string> operationMonkey = new Dictionary<string, string>(operationMonkeyOrigin);


            while(operationMonkey.Count > 0){
                foreach(string monkey in operationMonkey.Keys){
                    string[] parts = operationMonkey[monkey].Split();

                    if(numberMonkey.ContainsKey(parts[0]) && numberMonkey.ContainsKey(parts[2])){
                        double res = 0;

                        if(parts[1] == "+"){
                            res = numberMonkey[parts[0]] + numberMonkey[parts[2]];
                        } else if(parts[1] == "-"){
                            res = numberMonkey[parts[0]] - numberMonkey[parts[2]];
                        } else if(parts[1] == "*"){
                            res = numberMonkey[parts[0]] * numberMonkey[parts[2]];
                        } else if(parts[1] == "/"){
                            res = numberMonkey[parts[0]] / numberMonkey[parts[2]];
                        }

                        numberMonkey[monkey] = res;
                        operationMonkey.Remove(monkey);
                    }
                }
            }

            Console.WriteLine(numberMonkey["root"]);



            numberMonkeyOrigin.Remove("humn");

            List<string> left = new List<string>();
            left.Add(operationMonkeyOrigin["root"].Split()[0]);
            List<string> right = new List<string>();
            right.Add(operationMonkeyOrigin["root"].Split()[2]);

            bool variableSwaped = true;
            while(variableSwaped){
                variableSwaped = false;
                List<string> tempLeft = new List<string>();
                foreach(string piece in left){
                    if(numberMonkeyOrigin.ContainsKey(piece)){
                        tempLeft.Add(numberMonkeyOrigin[piece].ToString());
                    } else if(operationMonkeyOrigin.ContainsKey(piece)){
                        string[] opParts = operationMonkeyOrigin[piece].Split();
                        tempLeft.Add("(");
                            tempLeft.Add(opParts[0]);
                            tempLeft.Add(")");
                            tempLeft.Add(opParts[1]);
                            tempLeft.Add("(");
                            tempLeft.Add(opParts[2]);
                            tempLeft.Add(")");

                        variableSwaped = true;
                        
                    } else{
                        tempLeft.Add(piece);
                    }
                }

                left = tempLeft;
            }

            variableSwaped = true;
            while(variableSwaped){
                variableSwaped = false;
                List<string> tempRight = new List<string>();
                foreach(string piece in right){
                    if(numberMonkeyOrigin.ContainsKey(piece)){
                        tempRight.Add(numberMonkeyOrigin[piece].ToString());
                    } else if(operationMonkeyOrigin.ContainsKey(piece)){
                        string[] opParts = operationMonkeyOrigin[piece].Split();
                        tempRight.Add("(");
                        tempRight.Add(opParts[0]);
                        tempRight.Add(")");
                        tempRight.Add(opParts[1]);
                        tempRight.Add("(");
                        tempRight.Add(opParts[2]);
                        tempRight.Add(")");

                        variableSwaped = true;
                        
                    } else{
                        tempRight.Add(piece);
                    }
                }

                right = tempRight;
            }

            List<string> humnSide;
            double result;

            DataTable dt = new DataTable();

            if(left.Contains("humn")){
                humnSide = new List<string>(left);
                result = Convert.ToDouble(dt.Compute(string.Join(" ",right),""));
            } else {
                humnSide = new List<string>(right);
                result = Convert.ToDouble(dt.Compute(string.Join(" ",left),""));
            }

            while(humnSide.Count > 1){
            
                string op = "";
                int insedBrackets = 0;
                List<string> newHumnSide = new List<string>();
                List<int> plusMinusIndexes = new List<int>();
                for(int i = 0 ; i < humnSide.Count; ++i){
                    if (humnSide[i] == "(") insedBrackets++;
                    else if(humnSide[i] == ")") insedBrackets--;

                    if(insedBrackets > 0 ) continue;

                    if(humnSide[i] == "+" || humnSide[i] == "-") plusMinusIndexes.Add(i);
                }
                List<string> part = new List<string>();
                if(plusMinusIndexes.Count > 0){
                    for(int index = 0; index < plusMinusIndexes[0]; ++index){
                        part.Add(humnSide[index]);
                    }
                    if(part.Contains("humn")){
                        newHumnSide = new List<string>(part);
                    } else {
                        result -= Convert.ToDouble(dt.Compute(string.Join(" ",part), " "));
                    }
                    for(int i = 0; i < plusMinusIndexes.Count; ++i){
                        part.Clear();
                        int endIndex;
                        if(i == plusMinusIndexes.Count - 1) endIndex = humnSide.Count;
                        else endIndex = plusMinusIndexes[i+1];

                        for(int index = plusMinusIndexes[i] + 1; index < endIndex; ++index){
                            part.Add(humnSide[index]);
                        }
                        if(part.Contains("humn")){
                            op = humnSide[plusMinusIndexes[i]];
                            newHumnSide = new List<string>(part);
                        } else {
                            if(humnSide[plusMinusIndexes[i]] == "+") result -= Convert.ToDouble(dt.Compute(string.Join(" ",part), " "));
                            if(humnSide[plusMinusIndexes[i]] == "-") result += Convert.ToDouble(dt.Compute(string.Join(" ",part), " "));
                        }
                    }
                    if(op == "-"){
                        result = - result;
                    }
                    humnSide= new List<string>(newHumnSide);
                }

                insedBrackets = 0;
                newHumnSide = new List<string>();
                List<int> mulDivIndexes = new List<int>();
                for(int i = 0 ; i < humnSide.Count; ++i){
                    if (humnSide[i] == "(") insedBrackets++;
                    else if(humnSide[i] == ")") insedBrackets--;

                    if(insedBrackets > 0 ) continue;

                    if(humnSide[i] == "*" || humnSide[i] == "/") mulDivIndexes.Add(i);
                }
                part = new List<string>();
                if(mulDivIndexes.Count > 0){
                    for(int index = 0; index < mulDivIndexes[0]; ++index){
                        part.Add(humnSide[index]);
                    }
                    if(part.Contains("humn")){
                        newHumnSide = new List<string>(part);
                    } else {
                        result /= Convert.ToDouble(dt.Compute(string.Join(" ",part), " "));
                    }
                    for(int i = 0; i < mulDivIndexes.Count; ++i){
                        part.Clear();
                        int endIndex;
                        if(i == mulDivIndexes.Count - 1) endIndex = humnSide.Count;
                        else endIndex = mulDivIndexes[i+1];

                        for(int index = mulDivIndexes[i] + 1; index < endIndex; ++index){
                            part.Add(humnSide[index]);
                        }
                        if(part.Contains("humn")){
                            op = humnSide[mulDivIndexes[i]];
                            newHumnSide = new List<string>(part);
                        } else {
                            if(humnSide[mulDivIndexes[i]] == "/") result *= Convert.ToDouble(dt.Compute(string.Join(" ",part), " "));
                            if(humnSide[mulDivIndexes[i]] == "*") result /= Convert.ToDouble(dt.Compute(string.Join(" ",part), " "));
                        }
                    }
                    if(op == "/"){
                        result = 1 / result;
                    }
                    humnSide= new List<string>(newHumnSide);
                }

                if(humnSide.First() == "(" && humnSide.Last() == ")"){
                    humnSide.RemoveAt(0);
                    humnSide.RemoveAt(humnSide.Count - 1);
                }
            }

            Console.WriteLine(result);
        }
    }
}