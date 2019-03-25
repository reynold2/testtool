#include<iostream>
#include<list>
using namespace std;

//����Ĺ۲���
class absohero {
public:
	virtual void update() = 0;
};
//�۲���
class heroA :public absohero {
public:
	heroA() {
		cout << "A" << endl;
	}
	virtual void update() {
		cout << "A���ڸ���" << endl;
	}
};

class herob :public absohero {
public:
	herob() {
		cout << "b" << endl;
	}
	virtual void update() {
		cout << "b���ڸ���" << endl;
	}
};

class heroc :public absohero {
public:
	heroc() {
		cout << "c" << endl;
	}
	virtual void update() {
		cout << "c���ڸ���" << endl;
	}
};
//�۲�Ŀ��
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
	//�����۲���
	absohero* hero1 = new heroA;
	absohero* hero3 = new heroc;
	absohero* hero2 = new herob;
	//��ӹ۲�Ŀ��
	absboss* boos1 = new bossA;
	boos1->addhero(hero1);
	boos1->addhero(hero2);
	boos1->addhero(hero3);

	//֪ͨ�ı���Ϣ
	boos1->motifyhero();
	boos1->deletehero(hero2);
	boos1->motifyhero();
}
/*
main() {
	test10();
	getchar();
	return 0;
}
*/