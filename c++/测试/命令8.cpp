#include<iostream>
#include<queue>
#include<Windows.h>
using namespace std;

//Э�鴦����
class handleclientprotol {
public:
	void add1() {
		cout << "����1" << endl;

	}
	void add2() {
		cout << "����2" << endl;

	}
	void add3() {
		cout << "����3" << endl;

	}
};
//����ӿ�
class abscommand {
public:
	virtual void handle() = 0;
};

//����add1����
class commandadd1 :public abscommand {
public:
	commandadd1(handleclientprotol*protocol) {
		this->add1protocol = protocol;
	}
	virtual void handle() {
		this->add1protocol->add1();
	}
public:
	handleclientprotol*add1protocol;
};
//����add3����
class commandadd3 :public abscommand {
public:
	commandadd3(handleclientprotol*protocol) {
		this->add1protoco3 = protocol;
	}
	virtual void handle() {
		this->add1protoco3->add3();
	}
public:
	handleclientprotol*add1protoco3;
};
//����add2����
class commandadd2 :public abscommand {
public:
	commandadd2(handleclientprotol*protocol) {
		this->add1protoco2 = protocol;
	}
	virtual void handle() {
		this->add1protoco2->add2();
	}
public:
	handleclientprotol*add1protoco2;
};



//����������
class server {

public:
	void addrequest(abscommand* commad) {
		mcommands.push(commad);
	}
	void starhandle() {
		while (!mcommands.empty())
			
		{
			Sleep(2000);
			abscommand* command = mcommands.front();
			command->handle();
			mcommands.pop();
		}
	}



public:
	queue<abscommand*> mcommands;

};
void test8() {

	handleclientprotol*protocol = new handleclientprotol;

	abscommand*add1command = new commandadd1(protocol);
	abscommand*add2command = new commandadd2(protocol);
	abscommand*add3command = new commandadd3(protocol);

	server* server1 = new server;
	server1->addrequest(add1command);
	server1->addrequest(add2command);
	server1->addrequest(add3command);

	server1->starhandle();
}
/*
int main() {
	test8();
	getchar();

	}
*/