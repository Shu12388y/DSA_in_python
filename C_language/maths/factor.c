// display the factors and count


#include<stdio.h>
void main(){
    int n;
    int count=0;
    printf("Enter a number: ");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        if(n%i==0){
            printf("%d ",i);
            count++;
        }
    }
    printf("\n");
    printf("%d",count);
}


