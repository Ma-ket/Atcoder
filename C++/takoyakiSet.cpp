#include <iostream>
using namespace std;

int main() {
    int p;
    int price;
    string text;
    int N;
    cin >> p;

    // パターン1
    if (p == 1) {
        cin >> price;
    }

    // パターン2
    if (p == 2) {
        cin >> text >> price;
    }

    cin >> N;

    if(p == 2)
        cout << text << "!" << endl;
    cout << price * N << endl;
}
