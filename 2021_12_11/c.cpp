#include <iostream>
using namespace std;

int main(){
    int n, q;
    cin >> n >> q;

    int tall[n];
    for(int i = 0; i < n; i++){
        cin >> tall[i];
    }

    for(int i = 0; i < q; i++){
        int x;
        cin >> x;
        int point = 0;
        for(int j = 0; j < q; j++){
            if(x <= tall[q]){
                point++;
            }
        }
        cout << point << "\n";
    }
    return 0;
}