#include "card.h"

Card::Card()
{
	cardSuit = clubs;
	cardFace = 2;
}

Card::Card(int face, suit st)
{
	cardSuit = st;
	cardFace = face;
}

ostream & operator<<(ostream &os, const Card & cd)
{	

	if(cd.cardFace == 1)
		os << "A";
		
	else if(cd.cardFace == 11)
		os << "J";
		
	else if(cd.cardFace ==12)
		os << "Q";
		
	else if(cd.cardFace ==13)
		os << "K";
		
	else
		os << cd.cardFace;
	
	
	if(cd.cardSuit == clubs)
		os << "C[" << cd.cardFace << "]";
	
	else if(cd.cardSuit == hearts)
		os << "H[" << cd.cardFace << "]";
		
	else if(cd.cardSuit == spades)
		os << "S[" << cd.cardFace << "]";
	
	else
		os << "D[" << cd.cardFace << "]";
		

	return os;
}

bool Card::operator <= (const Card& cd) const
{
	if(cardFace <= cd.cardFace)
		return true;
	else
		return false;
}

bool Card::operator >=(const Card& cd) const
{
	if(cardFace >= cd.cardFace)
		return true;
	else 
		return false;
}

bool Card::operator ==(const Card& cd) const
{
	if(cardFace == cd.cardFace)
		return true;
	else 
		return false;
}


int Card::getFaceValue() const
{
	return cardFace;
}

suit Card::getSuit() const
{
	return cardSuit;
}
