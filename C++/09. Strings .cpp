#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    
    string a, b;
    cin >> a >> b;
    
    cout << a.size() << " " << b.size() << endl;
    
    cout << a + b << endl;
      
    if (!a.empty() && !b.empty()) {
        char temp = a[0];
        a[0] = b[0];
        b[0] = temp;
    }
    cout << a << " " << b << endl;
    
    return 0;
}
