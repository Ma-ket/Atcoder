#include <iostream>
#include <vector>
using namespace std;

int count_report_num(vector< vector<int> > &children, int x){
    if(children.at(x).size() == 0)
        return 1;
    int sum = 0;
    int c;
    for(int i = 1; children.at(x).at(i) != (int)NULL; i++){
        c = children.at(x).at(i);
        sum += count_report_num(children, c);
    }
    return sum;
}

int main(){
    int num;
    cin >> num;

    vector<int> p(num);
    p.at(0) = -1;
    for(int i = 1; i < num; i++){
        cin >> p.at(i);
    }

    vector< vector<int> > children(num);
    for(int i = 1; i < num; i++){
        int parent = p.at(i);
        children.at(parent).push_back(i);
    }

    for(int i = 0; i < num; i++){
        cout << count_report_num(children, i) << endl;
    }
    return 0;
}
