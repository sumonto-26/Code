// video link "https://www.youtube.com/watch?v=udExMlaR_nA&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=2&ab_channel=Luv"
# include <bits/stdc++.h>
using namespace std;


// A Function to Print our vector with len.
// void printvector( vector<int> v){ 
void printvector( vector<int> &v){ 
        int len = v.size();
        cout << "the vector size is " << len << endl;
        for (int i= 0; i < len; ++i){
            cout << v[i]<< " ";
        }  
    v.push_back(99);
    cout << endl;
    }

int main(){
    /*
    // ___PAIR___ //

    cout << "Topic is 'pair' in c++"<< endl;
    // create a pair
    pair <int , string > p;
    // p = make_pair(2 , "abc"); // 1 rule
    p = {2, "abc"}; // 2 rule
    // pair <int , string > p1 = p;
    pair <int , string > &p1 = p;
    p1.first = 3;
    cout << p.first << " " << p.second << endl;

    //make 2 array
    int a[] = {1,2,3};
    int b[] = {4,5,6};
    pair <int,int> p_array[3];
    p_array[0] = {1,2};
    p_array[1] = {2,3};
    p_array[2] = {3,4};

    swap(p_array[0], p_array[2]);

    for (int i=0; i < 3; ++i){
        cout << p_array[i].first << " " << p_array[i].second << endl;
    }

    // you can input first of the pair or and second of the pair.
    // cin >> p_array.first; 
    // cin >> p_array.second; */


    // ----VECTOR----  //

    // int a [10] ;  it's fixed it's len is 10 but vector <int> a; it's not.
    // and we can change vector's size/lenght.


    /*
    // vector <int> vec;  // now it's empty. Like python "vec = []"
    vector <int> vec(5, 0); //  It not fixed that it's lenght is 5 we can add or remove 
    //now it's not empty 
    //"It's lenght is 5 and all elements are 0". 
    //Like python "vec = [0,0,0,0,0]" 

    int n;
    cin >> n;
    for (int i=0; i < n; ++i){
        int x;
        cin >> x;
        printvector(vec);
        vec.push_back(x); //time complexity is O(1) and it's like python  "vec.append(x)".
    }
    printvector(vec);*/

    vector <int> v;
    v.push_back(1); //ADD 1 IN THE LAST ELEMENT OF VECTOR.
    v.push_back(2); // O(1)
    printvector(v);
    // v.pop_back(); // REMOVE THE LAST ELEMENT OF VECTOR. AND THE TIME COMPLEXITY OF "pop_back" IS O(1).
    printvector(v);
    vector <int> v2 = v; // make a COPY of v. and it's time complexity is O(n).
    v2.push_back(22);
    printvector(v2);
    printvector(v);


    return 0;
}