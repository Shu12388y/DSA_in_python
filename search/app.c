#include<stdio.h>

int search(int[],int);

void main(){
    int arr[] = {1, 2, 3, 4};
    int f = search(arr, 1);
    if(f==1){
        printf("number found");
    }
    else{
        printf("Not found");
    }

}

int search(int arr[],int target){
  for(int i=0;i<4;i++){
    if(arr[i]==target){
        return 1;
    }
    else{
        return -1;
    }
  }
}