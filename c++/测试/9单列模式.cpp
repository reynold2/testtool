#include<iostream>
using namespace std;

class A {
//1构造函数私有话
private:
	A() {
		a = new A;
	};
//3提供对外接口可以让用户获取单例对象
public:
	static A*getinstace() {
		return a;
	}
//2静态指针变量a
private:
	static A* a;
};

//静态变量初始化
A* A::a = NULL;

/*
int mian() {
	A::getinstace();

	getchar();
	return 0;

}
*/