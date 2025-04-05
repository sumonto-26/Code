#include <iostream>
#include <vector>
using namespace std;

int main(){
/*
    int n; cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    vector<int> prefix(n);
    prefix[0] = arr[0];
    for(int i=1; i<n; i++){
        prefix[i] = prefix[i-1]+arr[i];
    }
    
*/
/*
    for(int i=0; i<n; i++) cout << prefix[i] << " ";
    cout << endl;
    
    int n; cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    vector<int> prefix(n);
    prefix[n-1] = arr[n-1];
    for(int i=n-2; i>=0; i--){
        prefix[i] = prefix[i+1]+arr[i];
    }

    for(int i=0; i<n; i++) cout << prefix[i] << " ";
    cout << endl;
*/

/*
int n; cin >> n;
vector<int> vec(n);
    for(int i = 0; i<n; i++){
        cin >> vec[i];
    }

    for (int a=0; a<n; a++){
        for (int i=0; i<n-a; i++){
            for(int j = i; j<i+a+1; j++){
            cout << vec [j];
        }
        cout << " ";
    }
    cout << endl;
    }

*/

/*
    int n; cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    for(int i = 0; i < n-1; i++){
        int sum1 = 0, sum2 = 0;
        for(int j=0; j<=i; j++){
            sum1+= arr[j];
        }
        for(int j=i+1; j < n; j++){
            sum2+= arr[j];
        }
        if (sum1 == sum2){
            cout << "YES " << sum1 << endl;
            break;
        } 
    }

*/

/*
    int n; cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];
    
    int total_sum = 0;
    for(int i=0; i<n; i++)
        total_sum += arr[i];

    int prefix = 0;
    for(int i = 0; i<n-1; i++){
        prefix += arr[i];
        if(total_sum/2 == prefix) cout << "YES";
    }
*/
       

/*
    int n; cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];
    
    int max_prefix = INT32_MIN;
    for(int i = 0; i<n; i++){
        int prefix = 0;
        for(int j = i; j<n; j++){
            prefix += arr[j];
            max_prefix = max(max_prefix, prefix);
        }
    }
    cout << max_prefix << " is the largest subarray sum." << endl;
*/

/*
    int n; cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];
   
    int max_sum = INT32_MIN, sum = 0;
    for(int i=0; i<n; i++){
        sum += arr[i];
        max_sum = max(max_sum, sum);
        if (sum < 0) sum = 0;
    }
    cout << max_sum << " is the largest subarray sum." << endl;
*/

/*
    int n; cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];
    
    int ans = INT32_MIN;
    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            ans = max(ans, arr[j]-arr[i]);
        }
    }
*/

/*
    int n; cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    vector<int> suffix_max(n);
    suffix_max[n-1] = arr[n-1];
    for(int i=n-2; i>=0; i--) 
        suffix_max[i] = max(suffix_max[i+1], arr[i]);
    
    int ans = -1;
    for(int i=n-2; i>=0; i--){
        ans = max(ans, suffix_max[i+1]-arr[i]);
    } 
    cout << ans << " is the answer;" << endl;
*/
    
    int n; cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];
    
    int max_suffix = arr[n-1];
    int ans = 0;
    for(int i=n-2; i>=0; i--){
        max_suffix = max(max_suffix,arr[i]);
        ans = max(ans, max_suffix-arr[i]);
    }
    cout << ans << "is the answer." << endl;

    return 0;
}