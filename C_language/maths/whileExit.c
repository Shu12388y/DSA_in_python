#include<stdio.h>
#include<conio.h>
void main(){
    int n;
    while (1)
    {
        printf("Enter the number");
        scanf("%d ",&n);
        if(n%2==0){
            printf("Even Number");
        }
        else{
            printf("Odd NUmber");
            printf("Enter another number");
            if (getche()=='n'){
                break;
            }
        }

    }
    
}