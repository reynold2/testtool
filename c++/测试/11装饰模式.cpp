#include<iostream>	
using namespace std;
class abshero
{
public:
	virtual void showstatue() = 0;
public:
	int mhp;
	int mmp;
	int mat;
	int mdf;
};
class hero1 :public abshero {
public:
	hero1(){
		 mhp=0;
		 mmp=0;
		 mat=0;
		 mdf=0;
	}
	virtual void showstatue() {
		cout << "mhp" << mhp << endl;
		cout << "mmp" << mmp << endl;
		cout << "mat" << mat << endl;
		cout << "mdf" << mdf << endl;

	}
};

//装饰抽象类
class abseq :public abshero {
public:
	abseq(abshero* hero) {
		this->phero=hero;
	}
	virtual void showstatue() {
	}
public:
	abshero* phero;
};

//具体装饰物件
class kuangtu :public abseq {
public:
	kuangtu(abshero* hero) :abseq(hero) {}
	void addkuangtuxiaoguo() {
			cout << "穿上衣服" << endl;
			this->mhp = this->phero->mhp;
			this->mmp = this->phero->mmp;
			this->mat = this->phero->mat;
			this->mdf = this->phero->mdf + 30;

			//delete this->phero;

		}
	virtual void showstatue() {
			addkuangtuxiaoguo();
			cout << "mhp" << mhp << endl;
			cout << "mmp" << mmp << endl;
			cout << "mat" << mat << endl;
			cout << "mdf" << mdf << endl;
		}
};
void test11() {
	abshero* heroc = new hero1;

	heroc = new kuangtu(heroc);

	heroc->showstatue();
}
/*
int main() {
	test11();
	getchar();
	return 0;

}
*/