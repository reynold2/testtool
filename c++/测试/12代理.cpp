#include<iostream>
using namespace std;

//�ṩһ�ִ�������ƶԷ�����������
class abstractconmoninterface {
public:
	virtual void run() = 0;

};

//�ҵ�ϵͳ
class mysystem:public abstractconmoninterface {
public:
	virtual void run() {
		cout << "ϵͳ����" << endl;
	}
	 void test() {
		cout << "����" << endl;
	}
};

//������Ȩ����֤
class mysystemproxy :public abstractconmoninterface {
public:
	mysystemproxy(string nuername,string  password){
		this->nuername = nuername;
		this->password = password;
		psystem = new mysystem;
	}
	bool checkuserandpassword() {
		if (nuername=="admin"&password=="123")
		{
			return true;
		}
		return false;
	}
	virtual void run() {
		if (checkuserandpassword()) {
			cout << "����������ȷ,��¼�ɹ�" << endl;
			this->psystem->run();
		}
		else
		{
			cout << "�û������������" << endl;
		}
	}
public:
	mysystem* psystem;
	string nuername;
	string password;
};

struct MyStruct
{
	int test = 1;
};

/*
int main() {
	mysystemproxy* system = new mysystemproxy("admin","123");
	system->run();
//	MyStruct test1;
//	mysystem test2;
//	mysystem* x = new mysystem;
//	cout << test1.test << endl;
//  test2.run();
	getchar();
	return 0;

}
*/