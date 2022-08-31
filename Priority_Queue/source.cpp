// Brandon Goode
// CSCI 3130-001
// Project 7
// Due: 4/15/19
#include <iostream>
#include <fstream>
#include <cassert>
#include <algorithm>
#include "card.h"
#include "priorityqueue.h"

using namespace std;

int main()
{
	int randomNumber;
	Card hDeck[13];
	Card sDeck[13];
	PriorityQueue<Card, lesserComparator<Card>> minHeap;
	PriorityQueue<Card, greaterComparator<Card>> maxHeap;

	ifstream myIn;
	myIn.open("../pqseed.txt");
	assert(myIn);
	myIn >> randomNumber;
	srand(randomNumber);
	myIn.close();

	for(int i = 1; i<=13; i++ )
	{
		hDeck[i-1] = Card(i, hearts);
	}

	for(int i = 1; i<=13; i++)
	{
		sDeck[i-1] = Card(i, spades);
	}

	std::random_shuffle (std::begin(sDeck), std::end(sDeck));
	std::random_shuffle (std::begin(hDeck), std::end(sDeck));


	for(int i=0; i<13; i++)
	{
		maxHeap.enqueue(sDeck[i]);
		maxHeap.print();

	}
	cout << endl;

	while(!maxHeap.empty())
	{
		maxHeap.dequeue();
		maxHeap.print();
	}

	cout << "Max Heap Empty" << endl << endl;



	for(int i=0; i<13; i++)
	{
		minHeap.enqueue(hDeck[i]);
		minHeap.print();

	}

	cout << endl;
	while(!minHeap.empty())
	{
		minHeap.dequeue();
		minHeap.print();
	}

	cout << "Min Heap Empty" << endl << endl;


	return 0;
}
