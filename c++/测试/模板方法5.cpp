#include<iostream>
using namespace std;
class drinktemple
{
public:
	//עˮ
	virtual void boildwater()=0;
	//����
	virtual void brew()=0;
	//���뱭��
	virtual void pourincua()=0;
	//�Ӹ���
	virtual void addsomething()=0;

	void make() {
		boildwater();
		brew();
		pourincua();
		addsomething();
	}
};
//�忧��
class coffce :public drinktemple {
public:
	virtual void boildwater() {
		cout << "����1" << endl;
	}
	virtual void brew() {
		cout << "����2" << endl;
	}
	virtual void pourincua() {
		cout << "����3" << endl;
	}
	virtual void addsomething() {
		cout << "����4" << endl;
	}
};
//��Ҷ
class tea :public drinktemple {
public:
	virtual void boildwater() {
		cout << "��Ҷ1" << endl;
	}
	virtual void brew() {
		cout << "��Ҷ2" << endl;
	}
	virtual void pourincua() {
		cout << "��Ҷ3" << endl;
	}
	virtual void addsomething() {
		cout << "��Ҷ4" << endl;
	}
};
void test5() {
	tea* maketea = new tea;
	maketea->make();
}
/*
int main() {

	test5();
	getchar();
	return 0;
}
*/