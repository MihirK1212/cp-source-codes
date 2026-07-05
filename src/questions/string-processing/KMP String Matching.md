# KMP String Matching

lps[i] = longest proper prefix of s[0..i] that is also a suffix of s[0...i]

```cpp
class Solution {
  public:
    vector<int> compute_lps(string&str)
    {
        int n = str.length();
        
        vector<int> lps(n, 0);
        
        lps[0] = 0;
        
        for(int i=1; i<n; i++) {
            if(str[i] == str[lps[i-1]]) {
                lps[i] = lps[i-1] + 1;
            }
            else {
                lps[i] = (str[i] == str[0]);
            }
        }
        
        return lps;
    }
    
    vector<int> get_matches(string&txt, string&pat)
    {
        int m = txt.length(), n = pat.length();
        
        
        vector<int> lps = compute_lps(pat);
        
        vector<int> ans;
        int i=0, j=0;
        
        
        while(i<m && j<n) {
            if(txt[i] == pat[j]) {
                i++; j++;
                
                if(j==n) {
                    ans.push_back(i-n);
                    j = lps[j-1];
                }
            }
            else {
                if(j==0){i++;}
                else{j = lps[j-1];}
            }
        }
        
    
        return ans;
    }
};
```
