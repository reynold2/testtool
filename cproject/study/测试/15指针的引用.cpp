#include<iostream>
using namespace std;

struct person
{
	int m_age;
};

void allocatmemery(person** p) //**p�����person����   *p�����ָ��   p ָ���ָ��
{

	*p = (person*)malloc(sizeof(person));
	(*p)->m_age = 1000;
}
void allocatmemery1(person*& p) //**p�����person����   *p�����ָ��   p ָ���ָ��
{

	p = (person*)malloc(sizeof(person));
	p->m_age = 1000;
}


void t16() {
	person *p = NULL;
	allocatmemery1(p);
	cout << "test" << p->m_age << endl;
}

/*i
nt main() {
	t16();
	getchar();
	return 0;
}
*/