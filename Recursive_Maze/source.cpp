// Brandon Goode
// CSCI 3130-001
// Project 5
// Due: 3/18/19

#include <iostream>
#include <cassert>
#include "maze.h"

using namespace std;

int main()
{
	ifstream myIn;
	int row = 1, col = 1;
	bool success = false;

	myIn.open("maze.txt");
	assert(myIn);
	
	Maze myMaze(myIn);
	
	myMaze.Print();
	cout << "Start position: " << row << "," << col << endl;
	
	myMaze.FindExit(row, col, success);
	
	if(!success)
		cout << "No exit!\n";
	
	
	myIn.close();
	
	return 0;
}
