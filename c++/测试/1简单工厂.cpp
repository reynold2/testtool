#define _crt_secure_no_warnings
#include<iostream>
using namespace std;


class Television {
public:
	void on() {
		cout << "电视打开" << endl;
	}
	void off() {
		cout << "电视关闭" << endl;
	}
}; 
class light {
public:
	void on() {
		cout << "灯打开" << endl;
	}
	void off() {
		cout << "灯关闭" << endl;
	}
};
class aoudo {
public:
	void on() {
		cout << "音打开" << endl;
	}
	void off() {
		cout << "音关闭" << endl;
	}
};
class DVD {
public:
	void on() {
		cout << "DVD打开" << endl;
	}
	void off() {
		cout << "DVD关闭" << endl;
	}
};
class erji {
public:
	void on() {
		cout << "耳机打开" << endl;
	}
	void off() {
		cout << "耳机关闭" << endl;
	}
};
class playergame {
public:
	void on() {
		cout << "游戏几打开" << endl;
	}
	void off() {
		cout << "游戏几关闭" << endl;
	}
};
class KTVmode {

public:
	KTVmode() {
		ptv = new Television;
		plight = new light;
		paudio= new aoudo;
		pmicrophone= new erji;
		pdvd= new DVD;
	}
	void onktv() {
		ptv->on();
		plight->off();
		paudio->on();
		pmicrophone->on();
		pdvd->on();
	}
	void offktv() {
		ptv->off();
		plight->on();
		paudio->off();
		pmicrophone->off();
		pdvd->off();
	}
	~KTVmode() {
		delete ptv;
		delete plight;
		delete paudio;
		delete pmicrophone;
		delete pdvd;
	}
public:
	Television* ptv;
	light* plight;
	aoudo* paudio;
	erji* pmicrophone;
	DVD* pdvd;
};
void test1() {
	KTVmode* ktv = new KTVmode;
	ktv->onktv();
}
/*
int main(void) {
	test1();
	getchar();
	return 0;
}
*/