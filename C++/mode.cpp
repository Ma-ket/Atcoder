#include <iostream>
#include <vector>
using namespace std;

void count_mode_value(vector<int> a, int num, int &mode, int &count){
    int value, appear;
    for(int i = 0; i < num; i++){
        
    }
}

int main(){
    int num;
    cin >> num;

    vector<int> a(num);
    for(int i = 0; i < num; i++){
        cin >> a.at(i);
    }

    int mode, count;
    count_mode_value(a, num, mode, count);

    cout << mode << " " << count << endl;
    return 0;
}
