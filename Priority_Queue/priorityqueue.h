#ifndef PRIORITYQUEUE_H
#define PRIORITYQUEUE_H
#include "card.h"
#include <vector>

template<typename Object, typename Comparator>
class PriorityQueue
{
public:

PriorityQueue();
void enqueue(const Card&);
void dequeue();
bool empty();
void print();
	
private:
	
void heapUp(int);
void heapDown(int);
int pqSize;
std::vector<Card> pq;

};

template<typename Object>
class greaterComparator
{
public:

bool compare(const Object & lhs, const Object & rhs) const;

};

template <typename Object>
class lesserComparator
{

public:

bool compare(const Object & lhs, const Object & rhs) const;

};	



#endif


template <typename Object, typename Comparator>
PriorityQueue<Object, Comparator>::PriorityQueue()
{
	pq.resize(50);
	pqSize = 0;
}

template<typename Object, typename Comparator>
void PriorityQueue<Object, Comparator>::enqueue( const Card & rhs)
{
	pq[pqSize] = rhs;
	std::cout << "Enqueued " << rhs << " ";
	heapUp(pqSize);
	pqSize++;
}

template<typename Object, typename Comparator>
void PriorityQueue<Object, Comparator>::dequeue()
{
	std::cout << "Dequeued " << pq[0] << " ";
	pq[0] = pq[pqSize-1];
	pqSize--;
	heapDown(0);
}

template<typename Object, typename Comparator>
void PriorityQueue<Object, Comparator>::print()
{
	for(int i=0; i<pqSize; i++)
	{
		std::cout << pq[i] << " ";
	}
	
	std::cout << std::endl;
}


template<typename Object, typename Comparator>
bool PriorityQueue<Object, Comparator>::empty()
{
	if(pqSize == 0)
		return true;
	else
		return false;
}

template<typename Object, typename Comparator>
void PriorityQueue<Object, Comparator>::heapUp(int i)
{	
	Comparator cmp;
	if(i!=0&& cmp.compare(pq[i], pq[(i-1)/2]))
	{
		Card temp = pq[(i-1)/2];
		pq[(i-1)/2] = pq[i];
		pq[i] = temp;
		heapUp((i-1)/2);
	}
}


template<typename Object, typename Comparator>
void PriorityQueue<Object, Comparator>::heapDown(int i)
{
	Comparator cmp;
	int left = 2*i + 1;
	int right = 2*i + 2;
	
	if(pqSize > left && cmp.compare(pq[left], pq[i]))
	{
		Card temp = pq[left];
		pq[left]  = pq[i];
		pq[i] = temp;
		heapDown(left);
	}
	
	if(pqSize > right && cmp.compare(pq[right], pq[i]))
	{
		Card temp = pq[right];
		pq[right] = pq[i];
		pq[i] = temp;
		heapDown(right);
	}
}

template<typename Object>
bool greaterComparator<Object>::compare(const Object & lhs, const Object & rhs) const
{
	return lhs >= rhs;
}

template<typename Object>
bool lesserComparator<Object>::compare(const Object & lhs, const Object & rhs) const
{
	return lhs<= rhs;
}
