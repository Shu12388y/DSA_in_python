#include<stdio.h>

int main(){
    // check the number is a even or odd
    int num;
    printf("Enter a your number: ");
    scanf("%d",&num);
    if(num%2==0){
        printf("Number is a even number");
    }
    else{
        printf("The number is not a even number");
    }

    return 0;
}