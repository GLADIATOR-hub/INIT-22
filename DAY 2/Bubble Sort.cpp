// SORTING BY BUBBLE SORT
#include <bits/stdc++.h>
using namespace std;
 
void swap(int *x, int *y) 
{ 
    int temp = *x; 
    *x = *y; 
    *y = temp; 
} 
void Sort(int arr[], int n) 
{ 
    int i, j; 
    for (i = 0; i < n-1; i++)     
    for (j = 0; j < n-i-1; j++) 
        if (arr[j] > arr[j+1]) 
            swap(&arr[j], &arr[j+1]); 
} 
void printArray(int arr[], int size) 
{ 
    int i; 
    for (i = 0; i < size; i++) 
        cout << arr[i] << " "; 
    cout << endl; 
} 
 
int main() 
{ 
   int i,n;
   cout<<"Enter total number of elements:"<<"\n";
   cin>>n;
  
   int *arr = new int[n];
   cout<<"Enter "<<n<<" elements"<<endl;
   for(i = 0;i<n;i++) {
      cin>>arr[i];
   }
   cout<<endl;
    Sort(arr, n); 
    cout<<"Sorted array: \n"; 
    printArray(arr, n); 
    delete[] arr;
    return 0; 
}
