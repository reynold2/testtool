#include<iostream>
using namespace std;

const int c = 11;
int a=1 ;
int &b = a;

void myswap(int a, int b) {
	int tmp = a;
	a = b;
	b = tmp;

	cout << "myswap  a   " << a << endl;
	cout << "myswap  b   " << b << endl;
}
void myswap2(int *a,int *b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;

	cout << "myswap a" << *a << endl;
	cout << "myswap b" << *b << endl;
}

void test14() {
	int a = 10;
	int b = 13;
	myswap2(&a, &b);
	cout << "a   " << a << endl;
	cout << "b   " << b << endl;
}
/*int main() {

	test14();
	getchar();
	return 0;
}
*/