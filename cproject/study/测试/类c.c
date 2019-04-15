#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define _CRT_SECURE_NO_WARNINGS

struct person1
{
	char nname[64];
	int mage;
};

void personplay(struct person1 *p) {
	printf("personplay",p->nname);
}

void test01() {
	struct person1 p1;
	strcpy(p1.nname, "test01");
	person1(&p1);
}

int main() {
	test01();
	getchar();
}