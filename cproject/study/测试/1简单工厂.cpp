#define _crt_secure_no_warnings
#include<iostream>
using namespace std;


class Television {
public:
	void on() {
		cout << "���Ӵ�" << endl;
	}
	void off() {
		cout << "���ӹر�" << endl;
	}
}; 
class light {
public:
	void on() {
		cout << "�ƴ�" << endl;
	}
	void off() {
		cout << "�ƹر�" << endl;
	}
};
class aoudo {
public:
	void on() {
		cout << "����" << endl;
	}
	void off() {
		cout << "���ر�" << endl;
	}
};
class DVD {
public:
	void on() {
		cout << "DVD��" << endl;
	}
	void off() {
		cout << "DVD�ر�" << endl;
	}
};
class erji {
public:
	void on() {
		cout << "������" << endl;
	}
	void off() {
		cout << "�����ر�" << endl;
	}
};
class playergame {
public:
	void on() {
		cout << "��Ϸ����" << endl;
	}
	void off() {
		cout << "��Ϸ���ر�" << endl;
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