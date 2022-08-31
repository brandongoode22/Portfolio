// Brandon Goode
// CSCI 3130-001
// Project 8
// Due: 4/23/19
#include <iostream>
#include <fstream>
#include <cassert>
#include <string>
#include "graph.h"

using namespace std;

int main()
{
	ifstream myIn;
	int numberOfVertices, numberOfEdges, startingVertex, fromV, toV;
	double weight;
	string sGraphType;
	bool bGraphType;
	myIn.open("graph.txt");
	assert(myIn);
	myIn >> numberOfVertices >> numberOfEdges >> startingVertex;
	Graph myGraph(numberOfVertices);
	while(myIn >> fromV)
	{
		myIn >> toV >> weight >> sGraphType;
		if(sGraphType == "true")
		{
			bGraphType = true;
		}
		else if(sGraphType == "false")
		{
			bGraphType = false;
		}
		myGraph.addEdge(fromV, toV, weight, bGraphType);
	}
	
	cout << endl;
	cout << "Shortest paths: " << endl;
	
	myGraph.DijkstraPaths(startingVertex);
	
	
	
	return 0;
}
