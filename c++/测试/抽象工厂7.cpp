#include<iostream>
using namespace std;

//����ƻ��
class absapple {
public:
	virtual void showname() = 0;
};

class zh_apple:public absapple {
public:
	virtual void showname() {
		cout << "zh_apple" << endl;
	}
};
class mg_apple :public absapple {
public:
	virtual void showname() {
		cout << "mg_apple" << endl;
	}
};
class wo_apple :public absapple {
public:
	virtual void showname() {
		cout << "wo_apple" << endl;
	}
};

//�����㽶
class absbanana {
public:
	virtual void showname() = 0;
};

class zh_banana :public absbanana {
public:
	virtual void showname() {
		cout << "zh_banana" << endl;
	}
};
class mg_banana :public absbanana {
public:
	virtual void showname() {
		cout << "mg_banana" << endl;
	}
};
class wo_banana :public absbanana {
public:
	virtual void showname() {
		cout << "wo_banana" << endl;
	}
};


//������
class abspear {
public:
	virtual void showname() = 0;
};

class zh_pear :public abspear {
public:
	virtual void showname() {
		cout << "zh_pear" << endl;
	}
};
class mg_pear :public abspear {
public:
	virtual void showname() {
		cout << "mg_pear" << endl;
	}
};
class wo_pear :public abspear {
public:
	virtual void showname() {
		cout << "wo_pear" << endl;
	}
};


//���󹤳�
class absfactory {
public:
	virtual absapple* createapple() = 0;
	virtual absbanana* createbanana() = 0;
	virtual abspear* createpear() = 0;
};
//�й�����
class zh_factory:public absfactory 
{
public:
	virtual absapple* createapple() {
		return new	zh_apple;
	}
	virtual absbanana* createbanana() {
		return new	zh_banana;
	}
	virtual abspear* createpear() {
		return new	zh_pear;
	}
};

//��������
class mg_factory :public absfactory
{
public:
	virtual absapple* createapple() {
		return new	mg_apple;
	}
	virtual absbanana* createbanana() {
		return new	mg_banana;
	}
	virtual abspear* createpear() {
		return new	mg_pear;
	}
};

//�ձ�����
class wo_factory :public absfactory
{
public:
	virtual absapple* createapple() {
		return new	wo_apple;
	}
	virtual absbanana* createbanana() {
		return new	wo_banana;
	}
	virtual abspear* createpear() {
		return new	wo_pear;
	}
};
void test7() {
	absfactory* factory = NULL;
	absapple* apple = NULL;
	absbanana* banana = NULL;
	abspear* pear = NULL;

	factory = new zh_factory;
	apple = factory->createapple();
	apple->showname();

}
/*
int main() {
	test7();
	getchar();
	return 0;
}
*/
