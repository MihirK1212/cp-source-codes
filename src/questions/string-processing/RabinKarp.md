# RabinKarp

```cpp
#include<iostream>
#include<vector>
#include<string>
#include<queue>
#include<cmath>
#include<limits>
using namespace std;

#define ONLINE_JUDGE

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())
#define rall(x) (x).rbegin(), (x).rend()
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
typedef long long ll;
typedef long double ld;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;
typedef priority_queue<int> maxpq;
typedef priority_queue<int, vector<int>, greater<int>> minpq;

ll inf=std::numeric_limits<long long>::max();

ll ceilVal(ll a,ll b) {
   return ceil(((ld)a)/((ld)b)); 
}

void setIO(string name = "") {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("local.in", "r", stdin);
    freopen("local.out", "w", stdout);
    freopen("local.debug", "w", stderr);
#else
    if (name != "") {
        freopen((name + ".in").c_str(), "r", stdin);
        freopen((name + ".out").c_str(), "w", stdout);
    }
#endif
}

class RabinKarpHasher {
private:
    ll mod = 1e9 + 7;
    ll base = 256; 
    int max_len;
    vll p_pow;

    void compute_powers() {
        p_pow = vll(max_len + 1);
        p_pow[0] = 1;
        for (int i = 1; i <= max_len; i++) {
            p_pow[i] = (p_pow[i - 1] * base) % mod;
        }
    }

public:
    RabinKarpHasher(int expected_max_len) {
        this->max_len = expected_max_len;
        compute_powers();
    }

    ll get_hash(const vector<char>& str) {
        int len = str.size();
        ll hash = 0;
        for (int i = 0; i < len; i++) {
            hash = (hash * base + (unsigned char)str[i]) % mod;
        }
        return hash;
    }

    ll get_hash(string&str) {
        vector<char> str_c;
        for(auto c : str){str_c.push_back(c);}
        return get_hash(str_c);
    }

    ll roll_hash(ll curr_hash, ll len, char remove_char, char add_char) {
        ll new_hash = curr_hash;
        
        ll remove_val = ((unsigned char)remove_char * p_pow[len - 1]) % mod;
        new_hash = (new_hash - remove_val + mod) % mod;
        
        new_hash = (new_hash * base + (unsigned char)add_char) % mod;

        return new_hash;
    }
};
```
