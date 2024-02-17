#include<stdio.h>
void main(){
    int n;
    int i, a=0, b=1, c;
    printf("Enter the number");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        printf("%d ",a);
        c=a+b;
        a=b;
        b=c;
    }
    

    
}