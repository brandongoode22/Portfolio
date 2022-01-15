#ifndef GASPUMP_H
#define GASPUMP_H
#include <string>

using namespace std;

class GasPump
{
public: 
	GasPump(string type, double maxCapacity, double price);
	string getGasType() const 
	{ return gasType;}
	double getPrice() const 
	{ return pricePerGallon;}
	double getFuelOnHand() const 
	{ return fuelOnHand;}
	double getFuelDispensed() const 
	{ return fuelDispensed;}
	double getMoneyCollected() const 
	{ return moneyCollected;}
	void dispenseFuel(double * outcomeArr, double amount);
	
private:
	string gasType;
	double fuelOnHand;
	double fuelCapacity;
	double pricePerGallon;
	double fuelDispensed;
	double moneyCollected;
	bool anyFuel;
	void Replenish();
};

#endif
