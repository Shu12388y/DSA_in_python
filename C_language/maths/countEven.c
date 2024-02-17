#include<stdio.h>
void countEven(int,int);
void main(){
int m,n;
    printf("Enter the first number m");
    scanf("%d",&m);
    printf("Enter the second number m");
    scanf("%d",&n);
    if(m>n){
        printf("Value of first number should be less then second number");
    }
    else{
        countEven(m,n);
    }
    


}

// count the number of even numbers

void countEven(int x,int z){
    for (int i=x; i<z;i++){
        if(i%2==0){
            printf("%d ",i);
        }
    }

}