#include <iostream>
using namespace std;

int main(){
    int n;
    int a;
    char operation[2];
    int b;

    cin >> n >> a;
    for(int i = 0; i < n; i++){
        cin >> operation[0] >> b;
        switch(operation[0]){
        case '*':
            a = a * b;
            break;
        case '/':
            if(b == 0){
                cout << "error" << endl;
                return 0;
            }
            a = a / b;
            break;
        case '+':
            a = a + b;
            break;
        case '-':
            a = a - b;
            break;
        default:
            cout << "error" << endl;
            return 0;
        }
        cout << i + 1 << ":" << a << endl;
    }
    return 0;
}