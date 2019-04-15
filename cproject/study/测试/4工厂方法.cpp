#include<iostream>
using namespace std;

//抽象水果接口
class AbstractFrult {
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

//抽象工厂
class abstracfruitfactory {
public:
	virtual AbstractFrult* CreateFruit() = 0;
};

//香蕉工厂
class bananafactory :public abstracfruitfactory {
public:
	virtual AbstractFrult* CreateFruit() {
		return new banana;
	}
};
//苹果工厂
class applefactory :public abstracfruitfactory {
public:
	virtual AbstractFrult* CreateFruit() {
		return new apple;
	}
};
//鸭梨工厂
class pearfactory :public abstracfruitfactory {
public:
	virtual AbstractFrult* CreateFruit() {
		return new pear;
	}
};

void test4() {
	abstracfruitfactory* factory = NULL;
	AbstractFrult* fruit = NULL;
	//创建一个苹果
	factory = new applefactory;
	fruit = factory->CreateFruit();
	fruit->showname();
	delete fruit;
	delete factory;
	//创建一个鸭梨
	factory = new pearfactory;
	fruit = factory->CreateFruit();
	fruit->showname();
	delete fruit;
	delete factory;
	//创建一个香蕉
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