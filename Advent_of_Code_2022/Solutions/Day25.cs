using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Solutions
{
    public class Day25
    {
        public static void Solve(){
            List<string> lines = System.IO.File.ReadLines("PuzzleInputs/day25.txt").ToList();

            List<char> sum = Enumerable.Repeat('0',25).ToList();
            Dictionary<char,int> nums = new Dictionary<char, int>();
            nums['='] = -2;
            nums['-'] = -1;
            nums['0'] = 0;
            nums['1'] = 1;
            nums['2'] = 2;

            int carry = 0;
            foreach(string line in lines){
                List<char> reversed = line.ToList();
                reversed.Reverse();

                int i = 0;
                while(i <= reversed.Count() || carry != 0){
                    int op = 0;
                    if(i < reversed.Count()){
                        op = nums[reversed[i]];
                    }
                    int res = carry + op + nums[sum[i]];

                    if(res == 5){
                        sum[i] = '0';
                        carry = 1;
                    } else if(res == 4){
                        sum[i] = '-';
                        carry = 1;
                    } else if(res == 3){
                        sum[i] = '=';
                        carry = 1;
                    } else if(res == 2){
                        sum[i] = '2';
                        carry = 0;
                    } else if(res == 1){
                        sum[i] = '1';
                        carry = 0;
                    } else if(res == 0){
                        sum[i] = '0';
                        carry = 0;
                    } else if(res == -1){
                        sum[i] = '-';
                        carry = 0;
                    } else if(res == -2){
                        sum[i] = '=';
                        carry = 0;
                    } else if(res == -3){
                        sum[i] = '2';
                        carry = -1;
                    } else if(res == -4){
                        sum[i] = '1';
                        carry = -1;
                    } else if(res == -5){
                        sum[i] = '0';
                        carry = -1;
                    } 

                    ++i;
                }
            }
            sum.Reverse();
            while(sum[0] == '0'){
                sum.RemoveAt(0);
            }
            Console.WriteLine(string.Join("",sum));
        }
    }
}