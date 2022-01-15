// Brandon Goode
// CSCI 3130-001
// Project 6
// Due: 4/1/19

#include <iostream>
#include <fstream>
#include <cassert>
#include <string>
#include <algorithm>
#include "wordtree.h"

using namespace std;

int main()
{
	ifstream myIn;
	string inputWords;
	char queryType;
	int countQuery;
	string findQuery;
	WordTree treeObject;
	
	myIn.open("input.txt");
	assert(myIn);
	
	while(myIn >> inputWords)						// Reads a word from the input file,
													// stores it into a string, 
													// changes it to lower case,
													// and adds it to the tree
													// using the addWord member function
	{
		std::transform(inputWords.begin(), inputWords.end(), inputWords.begin(), ::tolower);
		treeObject.addWord(inputWords);
	
	}
	
	cout << "Word tree built and loaded \n\n";
	
	myIn.close();
	
	myIn.open("queries.txt");
	assert(myIn);
	
	while(myIn >> queryType)
	{
		if(queryType == 'F')					//Calls the findWord member function
												// if the 'F' character is read
		{
			myIn >> findQuery;
			cout << "Searching for all occurrences of the word '" << findQuery << "'" << endl;
			treeObject.findWord(findQuery);
		}
		
		else if(queryType == 'C')				// Calls the getCounts member function
		{										// if the 'C' character is read
			myIn >> countQuery;
			cout << "Finding all words with " << countQuery << " or more occurrences: \n";
			treeObject.getCounts(countQuery);
		}
	}
	
	
	
	myIn.close();
	return 0;
}
