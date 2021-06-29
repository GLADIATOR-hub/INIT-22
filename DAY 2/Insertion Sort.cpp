#include <iostream>
using namespace std;

void printArray(int array[], int size) {
  for (int i = 0; i < size; i++) {
    cout << array[i] << " ";
  }
  cout << endl;
}

void insertionSort(int array[], int size) {
  for (int step = 1; step < size; step++) {
    int key = array[step];
    int j = step - 1;

    while (key < array[j] && j >= 0) {
      array[j + 1] = array[j];
      --j;
    }
    array[j + 1] = key;
  }
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
    insertionSort(arr, n); 
    cout<<"Sorted array: \n"; 
    printArray(arr, n); 
    delete[] arr;
    return 0; 
}
