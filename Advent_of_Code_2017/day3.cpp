#include <iostream>
#include <map>

//Number given in input
int inputNum = 325489;

//Global variables to store solutions
int part1Sol;
int part2Sol;

//Function for part1 that checks wheter we have reached desired number
bool checkNum(int num,int x, int y){
    if (num == inputNum){
        part1Sol = abs(x) + abs(y);
        return true;
    }
    return false;
}

//Function for part2 what updates the grid map for current location by summing all adjacent ones that exist
bool updateMap(std::map<std::pair<int,int>,int>& grid, int currX, int currY){
    
    int sum = 0;

    for(int x = -1;x <= 1;x++){
        for(int y = -1;y <= 1;y++){

            std::pair<int,int> key {currX+x,currY+y};

            if(grid.count(key) == 1){
                sum += grid[key];
            }

        }
    }
    grid[{currX,currY}] = sum;

    if(sum > inputNum){
        part2Sol = sum;
        return true;
    }
    return false;
}

//Function that performs part1/part2 or both, returns true if we have found solution to both, false otherwise
bool performActions(int currNum, int x,int y, std::map<std::pair<int,int>,int>& grid,bool& part1, bool& part2){

    if(!part1){
        part1 = checkNum(currNum,x,y);
    }
    if(!part2){
        part2 = updateMap(grid ,x, y);
    }
    if (part1 && part2) return true;
    return false;
    
}


int main(void){

    int xPosition = 0;
    int yPosition = 0;

    int width = 2;

    int currNum = 1;

    bool part1 = false;
    bool part2 = false;

    std::map<std::pair<int,int>,int> grid;

    grid[{0,0}] = 1;

    //For each iteration of the spiral layer go one place right, then up, left, down, right and you end up at the
    //bottom right place of the spiral layer. For each place perform actions that needs to be done.
    //If we solved one of the parts then acctions fot that part no longer needs to be calculated
    //If we solve both parts of the task function will return true and we exit the loop using goto
    //After each iteration of the spiral, we add +2 to the width of the current layer
    //Note that the width is not the acctual width, but it is the amount of steps to cross at each
    //iteration, acctual witdh shoud be width+1
    while(true){

        //One step to the right
        currNum++;
        xPosition++;
        if(performActions(currNum, xPosition, yPosition, grid, part1, part2)) goto end;

        //Up
        //When we go up we go width-1 steps since we are not at the bottom right of that layer, we are one place up
        //And we will finish at bottom right place of the layer at the end of the iteration
        for(int i = 0;i < width-1;i++){
            currNum++;
            yPosition++;
            if(performActions(currNum, xPosition, yPosition, grid, part1, part2)) goto end;
        }

        //Left
        for(int i = 0;i < width;i++){
            currNum++;
            xPosition--;
            if(performActions(currNum, xPosition, yPosition, grid, part1, part2)) goto end;
        }

        //Down
        for(int i = 0;i < width;i++){
            currNum++;
            yPosition--;
            if(performActions(currNum, xPosition, yPosition, grid, part1, part2)) goto end;
        }

        //Right
        for(int i = 0;i < width;i++){
            currNum++;
            xPosition++;
            if(performActions(currNum, xPosition, yPosition, grid, part1, part2)) goto end;
        }

        width += 2;
    }

end:

    std::cout << part1Sol << "\n" << part2Sol;

}