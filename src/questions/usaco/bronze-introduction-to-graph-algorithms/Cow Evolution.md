# Cow Evolution

```cpp
#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<unordered_map>
#include<set>
#include<unordered_set>
#include<deque>
#include<queue>
#include<cmath>
#include<algorithm>
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
#define cy cout<<"yes\n";
#define cn cout<<"no\n";
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


vector<string> get_unique_characteristics(vector<vector<string>>&subpopulations)
{
    set<string> seen;
    for(auto&sub : subpopulations)
        for(auto&c : sub)
            seen.insert(c);
    return vector<string>(all(seen));
}

vector<int> get_subpopulations_having(string&str, vector<vector<string>>&subpopulations)
{
    vector<int> res;
    for(int i=0; i<(int)subpopulations.size(); i++)
        for(auto&c : subpopulations[i])
            if(c==str){ res.pb(i); break; }
    return res;
}

bool intersects(vi&a1, vi&a2) 
{
    int i=0, j=0;
    while(i<sz(a1) && j<sz(a2)) {
        if(a1[i]==a2[j]) return true;
        else if(a1[i]<a2[j]) i++;
        else j++;
    }
    return false;
}

bool is_superset(vi&a, vi&b)
{
    int i=0, j=0;
    while(i<sz(a) && j<sz(b)) {
        if(a[i]==b[j]){ i++; j++; }
        else if(a[i]<b[j]) i++;
        else return false;
    }
    return j==sz(b);
}

void solve() {
    int n;
    cin>>n;

    vector<vector<string>> subpopulations(n);
    for(int i=0; i<n; i++) {
        int k; cin>>k;
        subpopulations[i] = vector<string>(k);
        for(int j=0; j<k; j++){cin>>subpopulations[i][j];}
    }

    vector<string> unique_characteristics = get_unique_characteristics(subpopulations);
    int nc = unique_characteristics.size();
    
    vector<vi> subpopulations_having(nc);
    for(int i=0; i<nc; i++) {
        subpopulations_having[i] = get_subpopulations_having(unique_characteristics[i], subpopulations);
    }

    vector<int> parent(nc, -1);
    vector<bool> is_leaf(nc, true);

    bool allowed = true;

    for(int i=0; i<nc && allowed; i++) {
        int smallest_superset_sz = 1e9; 
        vector<pii> supersets;

        for(int j=0; j<nc && allowed; j++) {
            if(i==j){continue;}

            vector<int> p1 = subpopulations_having[i];
            vector<int> p2 = subpopulations_having[j];

            if(is_superset(p2, p1)) {
                smallest_superset_sz = min(smallest_superset_sz, int(p2.size()));
                supersets.push_back({j, p2.size()});
            }
            else if(!is_superset(p1, p2) && intersects(p1, p2)) {
                allowed = false;
                break;
            }
        }

        int par = -1;
        for(auto st : supersets) {
            if(st.second==smallest_superset_sz) {
                if(par==-1){par=st.first;}
                else{allowed=false; break;}
            }
        }

        if(par!=-1 && parent[par]!=i) {
            parent[i] = par;
            is_leaf[par] = false;
        }
    }

    for(int i=0; i<nc && allowed; i++) {
        if(is_leaf[i] && subpopulations_having[i].size()>1){allowed=false; break;}
    }

    if(allowed) {
        cy;
    }
    else {
        cn;
    }
}

int main() {
    setIO("evolution");
    ll T = 1;
    while(T--) {
        solve();
    }
    return 0;
}
```
