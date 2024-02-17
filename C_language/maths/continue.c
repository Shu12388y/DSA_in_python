#include<stdio.h>
void main(){
    int n=10;
    for(int i=1;i<=n;i++){
        if(i==5)
            continue;
        printf("%d ",i);   
    }
}