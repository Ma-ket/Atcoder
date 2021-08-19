#include <iostream>
using namespace std;

int main(){
    int a = 3;
    int &b = a; // bはaの参照

    cout << "a: " << a << endl;
    cout << "b: " << b << endl;

    b = 4; // 参照先の値を変更(aが4になる)

    cout << "a: " << a << endl;
    cout << "b: " << b << endl;
}
