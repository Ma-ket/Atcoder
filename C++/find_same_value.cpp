#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std;

int main(){
    vector<int> data(5);
    int i;
    int flag = 0;
    for(i = 0; i < 5; i++){
        cin >> data.at(i);
        if(data.at(i) > 100 || data.at(i) < 0) exit(1);
    }
    for(i = 0; i < 4; i++){
        if(data.at(i) == data.at(i+1)){
            flag = 1;
        }
    }
    if(flag > 0)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}
