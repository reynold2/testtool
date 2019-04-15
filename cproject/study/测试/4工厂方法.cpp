#include<iostream>
using namespace std;

//����ˮ���ӿ�
class AbstractFrult {
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
/*class fruitfactory
{
public:
	static AbstractFrult* CreateFruit(string flag)
	{
		if (flag == "apple") {
			return new apple;
		}
		else if (flag == "banana")
		{
			return new banana;
		}
		else if (flag == "pear")
		{
			return new pear;
		}
		else
		{
			return NULL;
		}
	}

};
*/

//���󹤳�
class abstracfruitfactory {
public:
	virtual AbstractFrult* CreateFruit() = 0;
};

//�㽶����
class bananafactory :public abstracfruitfactory {
public:
	virtual AbstractFrult* CreateFruit() {
		return new banana;
	}
};
//ƻ������
class applefactory :public abstracfruitfactory {
public:
	virtual AbstractFrult* CreateFruit() {
		return new apple;
	}
};
//Ѽ�湤��
class pearfactory :public abstracfruitfactory {
public:
	virtual AbstractFrult* CreateFruit() {
		return new pear;
	}
};

void test4() {
	abstracfruitfactory* factory = NULL;
	AbstractFrult* fruit = NULL;
	//����һ��ƻ��
	factory = new applefactory;
	fruit = factory->CreateFruit();
	fruit->showname();
	delete fruit;
	delete factory;
	//����һ��Ѽ��
	factory = new pearfactory;
	fruit = factory->CreateFruit();
	fruit->showname();
	delete fruit;
	delete factory;
	//����һ���㽶
	factory = new bananafactory;
	fruit = factory->CreateFruit();
	fruit->showname();
	delete fruit;
	delete factory;

}

/*int main() {
	test4();
	getchar();
	return 0;
}
*/