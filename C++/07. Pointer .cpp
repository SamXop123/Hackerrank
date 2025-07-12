#include <iostream>
#include <cstdlib> 
using namespace std;

int main() {
    int a, b;
    int *ptrA = &a, *ptrB = &b;
    
    cin >> *ptrA >> *ptrB;
    
    cout << (*ptrA + *ptrB) << endl;
    cout << abs(*ptrA - *ptrB);
    
    return 0;
}
