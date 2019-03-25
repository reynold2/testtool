#include<iostream>
#include<thread>
#include<Windows.h>
#include<mutex>

using namespace std;


/*void thread01() {
	for (int i = 0; i < 5; i++)
	{
		cout << "thread01" << endl;
		Sleep(100);
	}

}
void thread02() {
	for (int i = 0; i < 5; i++)
	{
		cout << "thread02" << endl;
		Sleep(200);
	}

}

int main() {
	thread task1(thread01);
	thread task2(thread02);
	//主线程和子线程一并执行
//	task1.detach();
//	task2.detach();
	//子线程执行完毕后才执行主线程
	task1.join();
	task2.join();
	for (int i = 0; i < 5; i++)
	{
		cout << "main thread" << endl;
		Sleep(200);
	}
	system("pause");
}
*/


//防止抢占资源
mutex mu;
int totalmun = 1000;
void thread01() {
	while (totalmun>0)
	{
		mu.lock();
		cout << "thread01:"<< totalmun << endl;
		totalmun--;
		Sleep(100);
		mu.unlock();
	}

}
void thread02() {
	while (totalmun>0)
	{
		mu.lock();
		cout << "thread02:" << totalmun << endl;
		totalmun--;
		Sleep(100);
		mu.unlock();
	}

}


/*
int main() {
	thread task1(thread01);
	thread task2(thread02);
	//主线程和子线程一并执行
	//	task1.detach();
	//	task2.detach();
	//子线程执行完毕后才执行主线程
	task1.join();
	task2.join();
	//这句有问题,以后慢慢研究
	//cout << "task1 thread" <<task1.get_id <<endl;
	//cout << "task2 thread" << task2.get_id <<endl;
	for (int i = 0; i < 5; i++)
	{
		cout << "main thread" << endl;
		Sleep(200);
	}
	system("pause");
}
*/
