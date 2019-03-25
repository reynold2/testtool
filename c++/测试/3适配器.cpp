#define _crt_secure_no_warnings
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

//原来打印接口
struct Myprint
{
	void operator()(int v1, int v2) {
		cout << v1+v2 << endl;

	}
};
//目标接口
class Target {
public:
	virtual void operator()(int v) = 0;
};
//适配器
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
//自定义参数适配器
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
