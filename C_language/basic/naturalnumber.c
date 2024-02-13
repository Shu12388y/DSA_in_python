#include <stdio.h>

int main()
{
    int m;
    int i;
    printf("Enter the number");
    scanf("%d", &m);
    for (i = 1; i <= m; i++)
    {
        printf("%d\n", i);
    }
    return 0;
}