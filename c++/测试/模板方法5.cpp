#include<iostream>
using namespace std;
class drinktemple
{
public:
	//×¢Ë®
	virtual void boildwater()=0;
	//³åÅÝ
	virtual void brew()=0;
	//µ¹Èë±­ÖÐ
	virtual void pourincua()=0;
	//¼Ó¸¨ÁÏ
	virtual void addsomething()=0;

	void make() {
		boildwater();
		brew();
		pourincua();
		addsomething();
	}
};
//³å¿§·È
class coffce :public drinktemple {
public:
	virtual void boildwater() {
		cout << "¿§·È1" << endl;
	}
	virtual void brew() {
		cout << "¿§·È2" << endl;
	}
	virtual void pourincua() {
		cout << "¿§·È3" << endl;
	}
	virtual void addsomething() {
		cout << "¿§·È4" << endl;
	}
};
//²èÒ¶
class tea :public drinktemple {
public:
	virtual void boildwater() {
		cout << "²èÒ¶1" << endl;
	}
	virtual void brew() {
		cout << "²èÒ¶2" << endl;
	}
	virtual void pourincua() {
		cout << "²èÒ¶3" << endl;
	}
	virtual void addsomething() {
		cout << "²èÒ¶4" << endl;
	}
};
void test5() {
	tea* maketea = new tea;
	maketea->make();
}
/*
int main() {

	test5();
	getchar();
	return 0;
}
*/