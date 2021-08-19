#include <iostream>
using namespace std;

int main(){
    int number; // 人数
    int a[1000]; // 点数
    int i; // カウンタ変数
    int sum = 0; // 合計
    int ave; // 平均

    cin >> number; // 人数の入力
    if(number > 1000) return 9;
    for(i = 0; i < number; i++){
        cin >> a[i];
        if(a[i] > 100 || 0 > a[i]) return 0;
        sum += a[i];
    }
    ave = sum / number; // 平均

    for(i = 0; i < number; i++){
        if(a[i] - ave >= 0)
            cout << a[i] - ave << endl;
        else if(a[i] - ave < 0)
            cout << ave - a[i] << endl;
    }
    return 0;
}
