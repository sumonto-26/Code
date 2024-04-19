// Video link is 
//      https://www.youtube.com/watch?v=ytyOI1RkZ24&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=3&ab_channel=Luv

# include <bits/stdc++.h>
using namespace std;

void printvector(vector <int> vec){
    cout << "The Vector size is " << vec.size()<< endl;
    for(int i=0 ; i <vec.size() ; ++i){
        cout << vec[i] << " ";
    }
    cout << endl;
}

int main(){
    // __VECTOR OF PAIR__ //
    /*
    // vector <pair<int,int>> v = {{1,2},{3,4},{5,6}};
    vector <pair<int,int>> v;
    printvector(v);
    int n;
    cin >> n;
    for (int i=0; i<n; ++i){
        int x, y;
        cin >> x >> y;
        v.push_back({x,y});
        // v.push_back(make_pair(x,y));
    }

    printvector(v);
    */


   // ---- ARRAY OF VECTOR ---- //
    int N;
    cin >> N;
    vector <int> v[N];
    for (int i=0; i<N; ++i){
        int n;
        cin >> n;
        for (int j=0; j<n; ++j){
            int x;
            cin >> x;
            v[i].push_back(x);
        }
    }
    for (int i=0; i<N; ++i){
        printvector(v[i]);
    }

    return 0;
}