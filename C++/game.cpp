#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std;

int main(){
    int persons, games;
    vector<vector<char> > flag(101, vector<char>(101, '-')); // -1 or 0 or 1
    vector<int> a(4951), b(4951);

    cin >> persons >> games;
    if(persons < 1 || persons > 100 || games < 0 || games > 4950)
        exit(1);

    for(int i = 1; i <= games; i++){
        cin >> a.at(i) >> b.at(i); // aが勝者、bが敗者
    }

    for(int i = 1; i <= games; i++){
        flag.at(a.at(i)).at(b.at(i)) = 'o'; // true
        flag.at(b.at(i)).at(a.at(i)) = 'x'; // false
    }

    for(int i = 1; i <= persons; i++){
        for(int j = 1; j <= persons; j++){
            cout << flag.at(i).at(j);
            if(j != persons)
                cout << " ";
        }
        cout << endl;
    }
    return 0;
}
