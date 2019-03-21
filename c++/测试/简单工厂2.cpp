#define _crt_secure_no_warnings
#include<iostream>
using namespace std;

//抽象水果接口
class AbstractFrult{
public:
	virtual void showname() = 0;
};

//具体的水果
class apple :public AbstractFrult {
public:
	virtual void showname() {
		cout << "我是苹果" << endl;
	}
};
class banana :public AbstractFrult {
public:
	virtual void showname() {
		cout << "我是香蕉" << endl;
	}
};
class pear :public AbstractFrult {
public:
	virtual void showname() {
		cout << "我是鸭梨" << endl;
	}
};

//水果工厂
class fruitfactory
{
public:
	static AbstractFrult* CreateFruit(string flag)
	{
		if (flag == "apple") {
			return new apple;
		}
		else if (flag=="banana")
		{
			return new banana;
		}
		else if (flag=="pear")
		{
			return new pear;
		}
		else
		{
			return NULL;
		}
	}

};
void test2() {
	fruitfactory* factory = new fruitfactory;

	AbstractFrult* fruit = factory->CreateFruit("banana");
	fruit->showname();
	delete fruit;

	AbstractFrult* apple = factory->CreateFruit("apple");
	apple->showname();
	delete apple;

	fruit = factory->CreateFruit("pear");
	fruit->showname();
	delete fruit;

	delete factory;
};
/*int main(){
	test2();
	getchar();
}
*/

