#include<iostream>
using namespace std;

class A {
//1���캯��˽�л�
private:
	A() {
		a = new A;
	};
//3�ṩ����ӿڿ������û���ȡ��������
public:
	static A*getinstace() {
		return a;
	}
//2��ָ̬�����a
private:
	static A* a;
};

//��̬������ʼ��
A* A::a = NULL;

/*
int mian() {
	A::getinstace();

	getchar();
	return 0;

}
*/