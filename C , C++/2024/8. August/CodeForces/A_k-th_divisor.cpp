#include<bits/stdc++.h>
using namespace std;
 
int main()
{
	long long n, k, i;
	cin>>n>>k;
	vector<long long>s;
	for(i=1;i*i<=n;i++)
	{
		if(n%i==0){
		    s.push_back(i);
            if(n/i!=i)  {s.push_back(n/i);}
		}
	}
	sort(s.begin(),s.end());

	if(k>s.size())  {cout<<"-1";}
    else  {cout<<s[k-1];}
	
	return 0;
}