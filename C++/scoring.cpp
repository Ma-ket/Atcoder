#include <iostream>
#include <vector>
using namespace std;

void scoring(vector< vector<int> > &a, int &correct_count, int &wrong_count){
    for(int i = 1; i <= 9; i++){
        for(int j = 1; j <= 9; j++){
            if((i) * (j) != a.at(i-1).at(j-1)){
                a.at(i-1).at(j-1) = i * j;
                wrong_count++;
            }
            else{
                correct_count++;
            }
        }
    }
}

int main(){
    vector< vector<int> > a(9, vector<int>(9));
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            cin >> a.at(i).at(j);
            if(a.at(i).at(j) > 100 || a.at(i).at(j) < 0)
                return 0;
        }
    }

    int correct_count = 0;
    int wrong_count = 0;

    scoring(a, correct_count, wrong_count);
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            cout << a.at(i).at(j);
            if(j < 8)
                cout << " ";
            else
                cout << endl;
        }
    }
    cout << correct_count << endl;
    cout << wrong_count << endl;

    return 0;
}
