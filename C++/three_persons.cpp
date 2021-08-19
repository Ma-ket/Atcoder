#include <iostream>
using namespace std;

int swap(int a, int b, int c){
    int tmp;
    if(a < b){
        tmp = a;
        a = b;
        b = tmp;
        return swap(a, b, c);
    }
    else if(b < c){
        tmp = b;
        b = c;
        c = tmp;
        return swap(a, b, c);
    }
    else if(a < c){
        tmp = a;
        a = c;
        c = tmp;
        return swap(a, b, c);
    }
    return a - c;
}

int main(){
    int a, b, c;
    int diff;

    cin >> a >> b >> c;
    if(a < 0 || b < 0 || c < 0 || a > 200 || b > 200 || c > 200) return 0;

    diff = swap(a, b, c);
    cout << diff << endl;

    return 0;
}
