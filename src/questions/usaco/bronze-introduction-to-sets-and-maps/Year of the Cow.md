# Year of the Cow (USACO Bronze)

## Problem Description

This problem is from USACO: [Year of the Cow](https://usaco.org/index.php?page=viewproblem2&cpid=1107).

Farmer John's N cows are named after the twelve animals in the Chinese zodiac (Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig, Rat). Each cow is born in a specific year, corresponding to one of these zodiac animals. The problem involves determining the age difference between two cows, given a series of statements about their birth years relative to other cows. Each statement specifies a cow's birth year in terms of another cow's birth year and a zodiac animal, indicating whether it was "previous" or "next".

For example, a statement might be "Mildred born in previous Ox year from Bessie", meaning Mildred's birth year is the closest previous year that is an Ox year relative to Bessie's birth year. Bessie is born in year 1.

The goal is to calculate the absolute difference in birth years between Bessie and Elsie.

## C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define all(a) (a).begin(), (a).end()
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
typedef long long ll;
typedef long double  ld;
typedef vector<long long> vll;
typedef vector<int> vi;

typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

bool comp(vll&x,vll&y)
{
    if(x[0]==y[0]){return x[1]<y[1];}
    return x[0]<y[0];
}

ll inf=std::numeric_limits<long long>::max();

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); 
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
	    freopen((name+".out").c_str(), "w", stdout);
    }
}


int main()
{
    setIO("");
    
    ll i;
    
    map<string,ll> animal_index;
    vector<string> animals = {"Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"};
    for(i=0;i<animals.size();i++){animal_index[animals[i]] = i+1;}
    
    map<string,ll> birth_year;
    birth_year["Bessie"] = 1; // Assuming Bessie's year is relative start
    
    
    ll n;
    cin>>n;
    
    cig; // Consume the newline character after reading 'n'
    
    while(n--)
    {
        vector<string> words(8);
        // Reading words one by one, expecting a fixed format for each statement
        // e.g., "Mildred born in previous Ox year from Bessie"
        cin >> words[0] >> words[1] >> words[2] >> words[3] >> words[4] >> words[5] >> words[6] >> words[7];
        
        ll sgn = (words[3]=="previous")?-1:1; // Determine if we are looking for a previous or next year
        
        // Calculate the 0-indexed animal index of the source cow's birth year (relative to its own cycle)
        // Bessie is year 1, so Rat (index 12) is year 12, Ox (index 1) is year 1.
        // (birth_year[words[7]] % 12 + 12) % 12 converts to a 0-11 range. Add 1 to make it 1-12.
        // e.g., if year is 1 (Ox), (1%12+12)%12 = 1. if year is 12 (Rat), (12%12+12)%12 = 0, so 0-indexed 0.
        // It's safer to map to 0-11 internally and then adjust.
        // Let's use 0-11 for calculations, where Rat is 0, Ox is 1, ..., Pig is 11.
        // The animal_index map gives 1-12. Adjusting here for consistency.
        
        // Correct way to get 0-indexed current animal for source cow
        // If Bessie is year 1, and animals[0] is Ox, then Bessie's animal is Ox.
        // The animal_index map seems to be 1-indexed. Let's adjust to 0-indexed for calculations.
        // Ox:0, Tiger:1, ..., Rat:11
        map<string, ll> animal_to_0_idx;
        for (int k=0; k<animals.size(); ++k) {
            animal_to_0_idx[animals[k]] = k;
        }

        ll source_year = birth_year[words[7]];
        ll source_zodiac_idx = (source_year - 1) % 12; // 0-indexed: Ox=0, Tiger=1, ..., Rat=11
        if (source_zodiac_idx < 0) source_zodiac_idx += 12; // Handle negative modulo result
        
        ll dest_zodiac_idx = animal_to_0_idx[words[4]]; // 0-indexed target animal

        ll delta_years;
        if (sgn == 1) { // "next"
            delta_years = (dest_zodiac_idx - source_zodiac_idx + 12) % 12;
            if (delta_years == 0) delta_years = 12; // If same zodiac, it's 12 years next
        } else { // "previous"
            delta_years = (source_zodiac_idx - dest_zodiac_idx + 12) % 12;
            if (delta_years == 0) delta_years = 12; // If same zodiac, it's 12 years previous
            delta_years *= -1;
        }
        
        birth_year[words[0]] = source_year + delta_years;
    }
    
    cout<<abs(birth_year["Bessie"] - birth_year["Elsie"])<<"\n";
    
    return 0;
}
```