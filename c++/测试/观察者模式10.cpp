#include<iostream>
#include<list>
using namespace std;

//抽象的观察着
class absohero {
public:
	virtual void update() = 0;
};
//观察着
class heroA :public absohero {
public:
	heroA() {
		cout << "A" << endl;
	}
	virtual void update() {
		cout << "A正在更新" << endl;
	}
};

class herob :public absohero {
public:
	herob() {
		cout << "b" << endl;
	}
	virtual void update() {
		cout << "b正在更新" << endl;
	}
};

class heroc :public absohero {
public:
	heroc() {
		cout << "c" << endl;
	}
	virtual void update() {
		cout << "c正在更新" << endl;
	}
};
//观察目标
class absboss {
public:
	virtual void addhero(absohero* hero) = 0;
	virtual void deletehero(absohero* hero) = 0;
	virtual void motifyhero() = 0;
};

class bossA :public absboss {
public:
	virtual void addhero(absohero* hero) {
		pherolist.push_back(hero);
	}
	virtual void deletehero(absohero* hero) {
		pherolist.remove(hero);
	}
	virtual void motifyhero() {
		for (list<absohero*>::iterator it = pherolist.begin(); it != pherolist.end();it++)
		{
			(*it)->update();
		}
	}
public:
	list<absohero*> pherolist;
};

void test10() {
	//创建观察者
	absohero* hero1 = new heroA;
	absohero* hero3 = new heroc;
	absohero* hero2 = new herob;
	//添加观察目标
	absboss* boos1 = new bossA;
	boos1->addhero(hero1);
	boos1->addhero(hero2);
	boos1->addhero(hero3);

	//通知改变消息
	boos1->motifyhero();
	boos1->deletehero(hero2);
	boos1->motifyhero();
}
int main() {
	test10();
	getchar();
	return 0;
}