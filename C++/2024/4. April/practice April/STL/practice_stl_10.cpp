// DATE ==> 26 April 2024
// YOUTUBE VIDEO LINK ==> https://www.youtube.com/watch?v=q-JB0hYyouo&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=12&ab_channel=Luv
// Topic ==> STACK AND QUEUE IN STL C++

#include <bits/stdc++.h>
using namespace std;

int main(){

    // STACK // LIFO //
    /*
    stack <int> s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    while(!s.empty()){
        cout << s.top() << endl;
        s.pop();
    }
    */

    // QUEUE // FIFO //
    
    queue <string> q;
    q.push("a");
    q.push("b");
    q.push("c");
    q.push("d");
    q.push("e");
    while(!q.empty()){
        cout << q.front() << endl;
        q.pop();
    }
}