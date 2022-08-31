#include "maze.h"
#include <iostream>

Maze::Maze(std::ifstream& myIn)
{
	myIn >> maxRows >> maxCols;
	
	for(int i =1; i<=maxRows; i++)
	{
		for(int j=1; j<=maxCols; j++)
		{
			myIn >> maze[i][j];
		}
	}
	for(int j=0; j<=maxCols; j++)
	{
		maze[0][j] = 'X';
	}
	
	for(int i=0; i<=maxRows; i++)
	{
		maze[i][0] = 'X';
	}
	
	for(int i=0; i<=maxRows+1;i++)
	{
		maze[i][maxCols+1] = 'X';
	}
	
	for (int j=0; j<=maxCols+1; j++)
	{
		maze[maxRows+1][j] = 'X';
	}
	
}

void Maze::Print()

{
	std::cout << "Maze State: \n";
	for(int i=1; i<=maxRows; i++)
	{
		for(int j=1; j<=maxCols; j++)
		{
			std::cout << maze[i][j];
		}
		std::cout << "\n";
	}
}

void Maze::FindExit(int row, int col, bool& success)
{
	
	
	if(maze[row][col] == 'E')
	{
		std::cout << "Exploring " << row << ","  << col << '\n';
		std::cout << "Found exit!\n";
		success = true;
	}
	
	else 
	{
		if(maze[row][col] != 'X')
			if(maze[row][col] == 'O')
			{
				
				
				maze[row][col] = '*';
				std::cout << "Exploring " << row << "," << col << "\n";
				Print();
				FindExit(row-1, col, success);
				FindExit(row, col+1, success);
				FindExit(row+1, col, success);
				FindExit(row, col-1, success);
			}
			
		
		
	}
	
	
	
	
}
