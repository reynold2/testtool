#define _crt_secure_no_warnings
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

//ԭ����ӡ�ӿ�
struct Myprint
{
	void operator()(int v1, int v2) {
		cout << v1+v2 << endl;

	}
};
//Ŀ��ӿ�
class Target {
public:
	virtual void operator()(int v) = 0;
};
//������
class adaper :public Target {
public:
	adaper(int param) {
		this->param= param;
	}
	virtual void operator()(int v) {
		print(v, param);
	}
public:
	Myprint print;
	int param;
};
//�Զ������������
adaper adaper2(int x) {
	return adaper(x);

}

/*
int main(){
	vector<int> v;
	for (int i = 0; i < 10; i++) {
		v.push_back(i);
	}
	for_each(v.begin(), v.end(), adaper2(1));

getchar();
}
*/
