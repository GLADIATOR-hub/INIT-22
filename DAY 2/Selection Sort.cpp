// SORTING BY SELECTION SORT
#include <iostream>
using namespace std;

void swap(int *a, int *b) { // SWAP FUNCTION
  int temp = *a;
  *a = *b;
  *b = temp;
}

void printArray(int array[], int size) {
  for (int i = 0; i < size; i++) {
    cout << array[i] << " ";
  }
  cout << endl;
}

void selectionSort(int array[], int size) { 
  for (int step = 0; step < size - 1; step++) {
    int min_idx = step;
    for (int i = step + 1; i < size; i++) {
      if (array[i] < array[min_idx])
        min_idx = i;
    }

    swap(&array[min_idx], &array[step]);// SWAPPING THE ELEMENTS
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
    selectionSort(arr, n); //CALLING SELECTION SORT FUNCTION
    cout<<"Sorted array: \n"; 
    printArray(arr, n); // PRINTING SORTED ARRAY
    delete[] arr;
    return 0; 
}
