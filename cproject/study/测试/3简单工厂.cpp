#define _crt_secure_no_warnings
#include<iostream>
using namespace std;

//����ˮ���ӿ�
class AbstractFrult{
public:
	virtual void showname() = 0;
};

//�����ˮ��
class apple :public AbstractFrult {
public:
	virtual void showname() {
		cout << "����ƻ��" << endl;
	}
};
class banana :public AbstractFrult {
public:
	virtual void showname() {
		cout << "�����㽶" << endl;
	}
};
class pear :public AbstractFrult {
public:
	virtual void showname() {
		cout << "����Ѽ��" << endl;
	}
};

//ˮ������
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

