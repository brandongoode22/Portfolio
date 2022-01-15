// Brandon Goode
// CSCI 3110-001
// Project #2
// Due: 02/06/19
// This program instantiates 3 gas pump object and simulates running multiple
// cars through the gas pumps to get gas. The gas type, price per gallon of gas,
// amount of gas requested and received, gas dispensed, and gas remaining
// at the pump are all printed afterwards. 


#include "gaspump.h"
#include <iostream>
#include <fstream>
#include <cassert>


int main()
{
	ifstream myIn;
	int randomNumber, numberOfVehicles;
	string type;
	double maxCapacity, price, percentage1, percentage2, percentage3, amount;
	double * outcomeArr = new double[2];
	GasPump * pumpArr[3];
	std:: cout << std::fixed;
	std::cout.precision(2);
	
	myIn.open("gas.txt");
	assert(myIn);
	myIn >> randomNumber >> numberOfVehicles;
	srand(randomNumber);
	
	// Reads from the file and places the information into each gas pump object
	myIn >> type >> maxCapacity >> price >> percentage1; 
	GasPump pump1(type, maxCapacity, price);
	myIn >> type >> maxCapacity >> price >> percentage2; 
	GasPump pump2(type, maxCapacity, price);
	myIn >> type >> maxCapacity >> price >> percentage3; 
	GasPump pump3(type, maxCapacity, price);
	
	pumpArr[0] = &pump1;
	pumpArr[1] = &pump2;
	pumpArr[2] = &pump3;
	
	// Loop that controls which pump the car goes to 
	for(int i =0; i<numberOfVehicles; i++)
	{
		if(((double)rand()+1)/ RAND_MAX <= percentage3)
		{
			amount = (rand() %6)*5+30;
			pumpArr[2]->dispenseFuel(outcomeArr, amount);
			
			cout << i+1 << " " << pumpArr[2]->getGasType() << " " << 
			pumpArr[2]->getPrice() << " " << amount << " " << outcomeArr[0] << 
			" " << outcomeArr[1] << " " << pumpArr[2]->getFuelOnHand() << endl;
			
		}
		
		else if(((double)rand()+1)/ RAND_MAX <= percentage3+percentage2)
		{
			amount = (rand() %6)*5+30;
			pumpArr[1]->dispenseFuel(outcomeArr, amount);
			cout << i+1 << " " << pumpArr[1]->getGasType() << " " << 
			pumpArr[1]->getPrice() << " " << amount << " " << outcomeArr[0] << 
			" " << outcomeArr[1] << " " << pumpArr[1]->getFuelOnHand() << endl;
		}
			
		else 
		{
			amount = (rand() %6)*5+30;
			pumpArr[0]->dispenseFuel(outcomeArr, amount);
			cout << i+1 << " " << pumpArr[0]->getGasType() << " " << 
			pumpArr[0]->getPrice() << " " << amount << " " << outcomeArr[0] << 
			" " << outcomeArr[1] << " " << pumpArr[0]->getFuelOnHand() << endl;
		}
	}
	
	// Displays the data collected from each of the pumps
	cout << pumpArr[0]->getGasType() << " " << pumpArr[0]->getFuelDispensed() 
	<< " " << pumpArr[0]->getMoneyCollected() << endl;
	
	cout << pumpArr[1]->getGasType() << " " << pumpArr[1]->getFuelDispensed() 
	<< " " << pumpArr[1]->getMoneyCollected() << endl;
	
	cout << pumpArr[2]->getGasType() << " " << pumpArr[2]->getFuelDispensed() 
	<< " " << pumpArr[2]->getMoneyCollected() << endl;
	
	myIn.close();

	
	return 0;
}
