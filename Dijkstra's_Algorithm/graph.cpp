#include "graph.h"

Graph::Graph(int n)
{
	numVertices = n;
}

void Graph::addEdge(int x, int y, double w, bool t)
{
	Edge myEdge(x, y, w);
	
	adjacent.resize(numVertices);
	if(t)
	{
		adjacent[x].push_back(myEdge);
		std::cout<< "Edge " <<  myEdge.v1 << ", " << myEdge.v2 << ", " << myEdge.weight << std::endl;
	}
	else
	{
		adjacent[x].push_back(myEdge);
		std::cout<< "Edge " <<  myEdge.v1 << ", " << myEdge.v2 << ", " << myEdge.weight << std::endl;
		Edge undirectedEdge(y,x, w);
		adjacent[y].push_back(undirectedEdge);
		std::cout<< "Edge " <<  undirectedEdge.v1 << ", " << undirectedEdge.v2 << ", " << undirectedEdge.weight << std::endl;
	}
}
 

void Graph::DijkstraPaths(int start)
{
	PathNode pathArr[numVertices];
	pathArr[start].cost = 0;
	pathArr[start].prev = -1;
	for(int i =0; i<numVertices; i++)
	{
		if(i!=start)
		{
			pathArr[i].cost =  std::numeric_limits<double>::infinity();
			pathArr[i].prev = -1;
		}
	}
	
	std::set<std::pair<double,int>> openList;
	openList.insert(std::make_pair(pathArr[start].cost, start));
	std::pair<double, int> first_item;
	first_item = *(openList.begin());
	
	std::list<Edge>::iterator it;
	std::set<std::pair<double, int>>::iterator find;
	
	while(!openList.empty())
	{
		for(it = adjacent[first_item.second].begin(); it!=adjacent[first_item.second].end(); it++)
		{
			if(pathArr[first_item.second].cost + it->weight < pathArr[it->v2].cost )
			{
				pathArr[it->v2].cost = pathArr[first_item.second].cost + it->weight;
				pathArr[it->v2].prev = first_item.second;
				
				find = openList.find(std::make_pair(pathArr[it->v2].cost, it->v2));
				
				if(find != openList.end())
				{
					openList.erase(find);
				}
				
				openList.insert(std::make_pair(pathArr[it->v2].cost, it->v2));
			}
		}
		
		openList.erase(openList.begin());
		first_item = *(openList.begin());
	}
	
	
	for(int i =0; i<numVertices; i++)
	{
		std::cout << i << " cost: " << pathArr[i].cost << '\t' << "prev: \t" <<
		pathArr[i].prev << std::endl;
	}
}


