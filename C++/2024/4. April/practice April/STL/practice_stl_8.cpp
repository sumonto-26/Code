// Youtube Video Link ==> https://www.youtube.com/watch?v=hoT_D60UzAU&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=9&ab_channel=Luv
// DATE ==> 23 April 2024
// Topic ==> MULTISET QUESTION.

#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        multiset <long long> bags;
        for (int i=0; i<n; ++i){
            long long candy_ct;
            cin >> candy_ct;
            bags.insert(candy_ct);
        }
        long long total_candies = 0;
        for (int i=0; i<k; ++i){
            auto last_it = (--bags.end());
            long long candy_ct = *last_it;
            total_candies += candy_ct;
            bags.erase(last_it);
            bags.insert(candy_ct / 2);
        }
        cout << total_candies << endl;

    }

    return 0;
}