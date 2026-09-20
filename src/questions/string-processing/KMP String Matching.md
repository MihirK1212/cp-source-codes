# KMP String Matching

lps[i] = longest proper prefix of s[0..i] that is also a suffix of s[0...i]

```cpp
class Solution {
  public:
    vector<int> compute_lps(string& str) {
        int n = str.length();
        vector<int> lps(n, 0);
        
        int i = 1;
        
        while (i < n) {
            int len = lps[i-1];
            while(len>=1 && str[i]!=str[len]) {
                /*
                loop invariant:
                before starting, we have a prefix (call this pre) of "len" which is also a suffix ending at (i-1)
                when we do len=lps[len-1], len is now a prefix of "pre" which is also a suffix "pre"
                since "pre" is also a suffix ending at (i-1), the new prefix is also both a prefix and suffix of the 
                suffix ending at (i-1)
                
                i.e. current prefix => pre, also a suffix ending at (i-1) (suff). pre=suff
                new prefix => pre_new, is longest proper prefix and suffix of "pre", and since  (pre == suff)
                              pre_new is also longest proper prefix and suffix of suff
                */
                len = lps[len-1];
            }
            if(str[i] == str[len]) {
                len++;
            }

            lps[i] = len;
            i++;
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
