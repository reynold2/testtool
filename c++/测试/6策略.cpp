#include<iostream>
using namespace std;

class weponstrategy {
public:
	virtual void useweapon() = 0;

};
class knife:public weponstrategy{
public:
	virtual void useweapon() {
		cout << "使用匕首" << endl;
	}
};
class AK47 :public weponstrategy {
public:
	virtual void useweapon() {
		cout << "使用ak47" << endl;
	}
};
class charactor {
public:
	void setweapon(weponstrategy* weapon)
	{
		this->pweapon = weapon;
	}
	void throwweapon() {
		this->pweapon->useweapon();
	}
public:
	weponstrategy* pweapon;
};

void test6() {
	charactor* person = new charactor;

	weponstrategy* kn = new knife;
	weponstrategy* ak = new AK47;

	person->setweapon(kn);
	person->throwweapon();

	person->setweapon(ak);
	person->throwweapon();

	delete kn;
	delete ak;

	delete person;
}
/*
int main() {
	test6();
	getchar();
	return 0;
}*/
