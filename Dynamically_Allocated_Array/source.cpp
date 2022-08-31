// Brandon Goode
// CSCI 3130-001
// Project 1
// Due: 01/28/19

#include <iostream>
#include <cassert>
#include <fstream>

using namespace std;

int * allocateArray(int * arr, int * sizePtr, double expansion);

double calcAvg(int * arr, int count);

int main()
{
	ifstream myIn;
	ofstream myOut;
	int * sizePtr;
	float expansion;
	int count, size;
	int * arr = NULL;
	double average;
	count = 0;
	sizePtr = &size;


	myIn.open("nums.txt");
	myOut.open("out.txt");
	assert(myIn);

	myIn >> size;

	if(size <100 || size>350 || size%50!=0)
	{
		cout << "Error" << endl;
		return 0;
	}



	myIn >> expansion;
	arr = allocateArray(arr, sizePtr, expansion);
	cout << *sizePtr << endl;
	myOut << *sizePtr << endl;

	while(myIn >> arr[count])
	{
		count++;
		if(*sizePtr == count)
		{
			average = calcAvg(arr, count);
			cout << count << " " << average << endl;
			myOut << count << " " << average << endl;
			arr = allocateArray(arr, sizePtr, expansion);
		}

	}

	average = calcAvg(arr, count);
	cout << *sizePtr << " " << count << " " << average << endl;
	myOut << *sizePtr << " " << count << " " << average << endl;


		myIn.close();
		myOut.close();
		delete[] arr;

	return 0;
}


// Allocates the initial array with the size read from file if it has not
// been initialized yet, otherwise creates a temp pointer to point to
// the working array, copies the values and places them into the new array,
// and deallocates the temp array

int * allocateArray(int * arr, int * sizePtr, double expansion)
{
	int tempSize = *sizePtr;

	if(arr == NULL)
	{
		arr = new int[*sizePtr];
	}

	else
	{
		int * temp = arr;
		*sizePtr = *sizePtr * (1+expansion);
		*sizePtr = int(*sizePtr);
		arr = new int[*sizePtr];
		for(int i=0; i<tempSize;i++)
		{
			arr[i] = temp[i];
		}
		delete[] temp;
	}

	return arr;

}


// Adds up all the values found and the array, takes the average,
// and returns the average as a double
double calcAvg(int * arr, int count)
{
	int sum = 0;
	for(int i=0; i<count; i++)
	{
		sum += arr[i];
	}

	return double(sum)/count;
}
