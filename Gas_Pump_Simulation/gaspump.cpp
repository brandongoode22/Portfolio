#include "gaspump.h"
#include <iostream>

// Constructor that takes 3 parameters and initializes the gas type, max 
// capacity of the gas pump, and the price per gallon of gas
GasPump::GasPump(string type, double maxCapacity, double price)
{
	gasType = type;
	fuelCapacity = maxCapacity;
	pricePerGallon = price;
	fuelOnHand = fuelCapacity;
}

// Dispenses all the fuel to the car if the pump has enough, 
// if the pump has less than the amount needed, but more than 0
// it gives the car all the fuel on hand, and if the pump has no fuel
// it turns away the next customer and replenishes the fuel to capacity
void GasPump::dispenseFuel(double * outcomeArr, double amount)
{
	if(fuelOnHand > amount/pricePerGallon)
	{
		outcomeArr[0] = amount;
		outcomeArr[1] = amount/pricePerGallon;
		fuelDispensed += amount/pricePerGallon;
		moneyCollected += amount;
		fuelOnHand -= amount/pricePerGallon;
	}
		
	else if(fuelOnHand < amount/pricePerGallon && fuelOnHand >0)
	{
		outcomeArr[0] = fuelOnHand * pricePerGallon;
		outcomeArr[1] = fuelOnHand;
		fuelDispensed += fuelOnHand;
		moneyCollected += fuelOnHand*pricePerGallon;
		fuelOnHand = 0;
	}
	
	else 
	{
		Replenish();
		outcomeArr[0] = 0;
		outcomeArr[1] = 0;
	}
}

// Replenishes a gas pump's fuel back to full capacity 
void GasPump::Replenish()
{
	fuelOnHand = fuelCapacity;
	
}
