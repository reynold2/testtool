#include<iostream>
#include<queue>
#include<Windows.h>
using namespace std;

//协议处理类
class handleclientprotol {
public:
	void add1() {
		cout << "增加1" << endl;

	}
	void add2() {
		cout << "增加2" << endl;

	}
	void add3() {
		cout << "增加3" << endl;

	}
};
//命令接口
class abscommand {
public:
	virtual void handle() = 0;
};

//处理add1请求
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
//处理add3请求
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
//处理add2请求
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



//服务器程序
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