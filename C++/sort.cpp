#include <iostream>
#include <vector>
using namespace std;

void sortB(vector<int> &a, vector<int> &b, int num){
    int tmp;
    int flag = 0;
    for(int i = 1; i < num; i++){
        if(b.at(i - 1) > b.at(i)){
            tmp = b.at(i-1);
            b.at(i-1) = b.at(i);
            b.at(i) = tmp;
            tmp = a.at(i-1);
            a.at(i-1) = a.at(i);
            a.at(i) = tmp;
            flag = 1;
        }
    }
    if(flag)
        sortB(a, b, num);
    return;
}

int main(){
    int num;
    cin >> num;

    vector<int> a(num);
    vector<int> b(num);
    for(int i = 0; i < num; i++){
        cin >> a.at(i) >> b.at(i);
    }

    sortB(a, b, num);

    for(int i = 0; i < num; i++){
        int A, B;
        A = a.at(i);
        B = b.at(i);
        cout << A << " " << B << endl;
    }
    return 0;
}
