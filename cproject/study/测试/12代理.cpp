#include<iostream>
using namespace std;

//提供一种代理对限制对服务启动访问
class abstractconmoninterface {
public:
	virtual void run() = 0;

};

//我的系统
class mysystem:public abstractconmoninterface {
public:
	virtual void run() {
		cout << "系统启动" << endl;
	}
	 void test() {
		cout << "测试" << endl;
	}
};

//必须有权限验证
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
			cout << "户名密码正确,登录成功" << endl;
			this->psystem->run();
		}
		else
		{
			cout << "用户名或密码错误" << endl;
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