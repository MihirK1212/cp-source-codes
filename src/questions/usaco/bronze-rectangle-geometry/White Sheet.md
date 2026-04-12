# White Sheet (Codeforces)

## Problem Description

This problem is from Codeforces: [White Sheet](https://codeforces.com/contest/1216/problem/C).

The problem describes a scenario with three rectangular sheets on a 2D plane.
1.  **White Sheet:** A single white rectangular sheet. Its coordinates are given by `(x1, y1)` and `(x2, y2)`.
2.  **Black Sheets (Two):** Two black rectangular sheets, `B1` and `B2`. Their coordinates are given separately.

The two black sheets are placed on top of the white sheet. The task is to determine if any part of the white sheet is still visible after being covered by the two black sheets. Output "YES" if at least some positive area of the white sheet remains visible, and "NO" otherwise.

## C++ Solution

This solution uses the principle of inclusion-exclusion to calculate the total visible area of the white sheet. It defines a `Rectangle` struct and helper functions for calculating area, intersection, and overlap.

**Key Concepts:**
*   **Rectangle Struct:** A simple `struct Rectangle` is defined to store the `x1, y1, x2, y2` coordinates and a method `area()` to calculate its area.
*   **Intersection:**
    *   `intersect(Rectangle p, Rectangle q)`: This function calculates the bounding box of the intersection of two rectangles `p` and `q`. Note that the `area()` method of the returned `Rectangle` will correctly return 0 if there is no intersection (i.e., `x2 <= x1` or `y2 <= y1` for the intersected rectangle).
*   **Overlap (Area of Intersection):**
    *   `overlap(Rectangle p, Rectangle q)`: Calculates the non-negative area of overlap between two rectangles `p` and `q`. It uses `max((ll)0, ...)` to ensure the overlap dimensions are not negative.
    *   `overlap(Rectangle p, Rectangle q, Rectangle r)`: This is specifically for calculating the overlap area of `p` with the *intersection* of `q` and `r`. This is equivalent to `overlap(p, intersect(q, r))`. This is essential for the inclusion-exclusion principle.

**Inclusion-Exclusion Principle:**
The visible area of the white sheet (`W`) can be calculated as:
`Area(W) - Area(W ∩ B1) - Area(W ∩ B2) + Area(W ∩ B1 ∩ B2)`

Where:
*   `Area(W)` is the total area of the white sheet.
*   `Area(W ∩ B1)` is the area of overlap between the white sheet and the first black sheet.
*   `Area(W ∩ B2)` is the area of overlap between the white sheet and the second black sheet.
*   `Area(W ∩ B1 ∩ B2)` is the area where the white sheet is covered by *both* black sheets (the overlap of the overlap). This term is added back because it was subtracted twice in the previous terms.

**Main Logic:**
1.  **Read Coordinates:** Reads the coordinates for the white sheet, `black_1`, and `black_2`, creating `Rectangle` objects.
2.  **Calculate Visible Area:** Applies the inclusion-exclusion formula using the `area()` and `overlap()` helper functions.
    *   `visible_area = white.area() - overlap(white,black_1) - overlap(white,black_2) + overlap(white,black_1,black_2);`
3.  **Output:** If `visible_area > 0`, print "YES"; otherwise, print "NO".

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
// #define sort(a) sort(a.begin(),a.end()); // Already exists in <algorithm>
#define reverse(a) reverse(a.begin(),a.end()); // Already exists in <algorithm>
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n"; // Custom macro for printing YES
#define cn cout<<"NO\n";  // Custom macro for printing NO
#define cig cin.ignore(); // Clears the input buffer until the next newline character.
typedef long long ll;
typedef long double  ld;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max(); // Using std::numeric_limits for infinity

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); 
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); // Faster I/O
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin); // Redirect input
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Structure to represent a rectangle
struct Rectangle
{
    ll x1,y1,x2,y2; // Coordinates of bottom-left (x1,y1) and top-right (x2,y2) corners
    
    // Constructor
    Rectangle(ll a,ll b,ll c,ll d)
    {
        x1=a; y1=b; x2=c; y2=d;
    }
    
    // Method to calculate the area of the rectangle
    ll area()
    {
        // Ensure non-negative dimensions for area calculation
        return max((ll)0, x2-x1) * max((ll)0, y2-y1);
    }
};

// Function to find the intersection rectangle of two given rectangles
Rectangle intersect(Rectangle p, Rectangle q)
{
    // Calculate new bottom-left and top-right coordinates for the intersection
    ll new_x1 = max(p.x1,q.x1);
    ll new_y1 = max(p.y1,q.y1);
    ll new_x2 = min(p.x2,q.x2);
    ll new_y2 = min(p.y2,q.y2);
    
    // Create a new Rectangle object for the intersection
    Rectangle res(new_x1,new_y1,new_x2,new_y2);
    return res;
}

// Function to calculate the area of overlap between two rectangles
ll overlap(Rectangle p,Rectangle q)
{
    // Calculate the overlap dimensions (ensuring non-negative)
    ll xoverlap= max( (ll)0 , min(p.x2,q.x2) - max(p.x1,q.x1) );
    ll yoverlap= max( (ll)0 , min(p.y2,q.y2) - max(p.y1,q.y1) );
    
    return xoverlap * yoverlap;
}

// Function to calculate the overlap area of rectangle 'p' with the intersection of 'q' and 'r'
// This is used for the inclusion-exclusion principle (triple overlap term)
ll overlap(Rectangle p,Rectangle q,Rectangle r)
{
    // First, find the intersection of q and r
    Rectangle intersection_qr = intersect(q,r); 
    // Then, find the overlap of p with this intersection
    return overlap(p,intersection_qr);
}
 
int main()
{
    setIO(""); // Use standard I/O for Codeforces
    
    // Problem link for reference
    // https://codeforces.com/contest/1216/problem/C
    
    ll a,b,c,d; // Temporary variables for reading coordinates
    
    // Read coordinates for the white sheet
    cin>>a>>b>>c>>d;
    Rectangle white(a,b,c,d);
    
    // Read coordinates for the first black sheet
    cin>>a>>b>>c>>d;
    Rectangle black_1(a,b,c,d);
    
    // Read coordinates for the second black sheet
    cin>>a>>b>>c>>d;
    Rectangle black_2(a,b,c,d);
    
    // Calculate visible area using the Principle of Inclusion-Exclusion:
    // Area(White) - Area(White intersect Black1) - Area(White intersect Black2) + Area(White intersect Black1 intersect Black2)
    ll visible_area = white.area() - overlap(white,black_1) - overlap(white,black_2) + overlap(white,black_1,black_2);
    
    // If the calculated visible area is positive, output YES, otherwise NO
    if(visible_area > 0){cy;}
    else{cn;}
    
    return 0;
}
```