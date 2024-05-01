// DATE ==> 24 April 2024
// Video Link ==> https://www.youtube.com/watch?v=zyGSg3U1K94&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=11&ab_channel=Luv
// Topic ==> Nesting in maps and sets

#include<bits/stdc++.h>
using namespace std;

int main(){
    /*
    map< pair <int,int> , int> n;
    pair<int,int> p1, p2;
    p1 = {10,10};
    p2 = {13,2};
    cout << (p1<p2); // ture == 1; //
    */
    
    /*
    map<set<int>,int> n;
    set<int> s1 = {1,2,3,4,5,6,7,8,9,10};
    set<int> s2 = {2};
    cout << (s1 < s2); // true // 1.
    */

   /*
    map<pair<string, string>,vector<int> > m ;
    int n;
    cin >> n;
    for (int i=0; i<n; ++i){
        string fn, ln;
        int ct;
        cin >> fn >> ln >> ct;
        for (int j=0; j<ct; ++j){
            int x;
            cin >> x;
            m[{fn,ln}].push_back(x);
        }
    }
    for (auto &pr : m){
        auto &full_name = pr.first;
        auto &list = pr.second;
        cout << full_name.first << " " << full_name.second << endl;
        cout << list.size() << endl;
        for (auto &element : list){
            cout << element << " ";
        }
        cout << endl;
    }
   */

    // Problem Solution.
    /*
    map<int,multiset<string>> marks_map ;
    int n;
    cin >> n;
    for(int i=0; i<n; ++i){
        int marks;
        string name;
        cin >> name >> marks;
        marks_map[marks].insert(name);
    }
    auto cur_it = --marks_map.end();
    while(true){
        int marks = (*cur_it).first;
        auto &students = (*cur_it).second;
        for (auto student : students){
            cout << student << " " << marks << endl;
        }
        if (cur_it == marks_map.begin()) break;
        cur_it --;
    }
    */

    // OPTIMIZE VESION //
    map<int,multiset<string>> marks_map ;
    int n;
    cin >> n;
    for(int i=0; i<n; ++i){
        int marks;
        string name;
        cin >> name >> marks;
        marks_map[-1*marks].insert(name);
    }
    for (auto &marks_student_pr : marks_map){
        int marks = marks_student_pr.first;
        auto &students = marks_student_pr.second;
        for (auto student : students){
            cout << student << " " << -1*marks << endl;
        }
    }




    return 0;
}