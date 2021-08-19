#include <iostream>
#include <vector>
using namespace std;

int main(){
    int quantity;
    int value;
    int count = 0;

    cin >> quantity >> value;
    vector<int> apple(quantity), pine(quantity);
    for(int i = 0; i < quantity; i++){
        cin >> apple.at(i);
    }
    for(int i = 0; i < quantity; i++){
        cin >> pine.at(i);
    }

    for(int i = 0; i < quantity; i++){
        for(int j = 0; j < quantity; j++){
            if(apple.at(i) + pine.at(j) == value)
                count++;
        }
    }
    cout << count << endl;
    return 0;
}
