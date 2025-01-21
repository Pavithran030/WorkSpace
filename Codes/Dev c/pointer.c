#include<stdio.h>
int main()
{
    int a;
    int *b;
    printf("Enter a number : ");
    scanf("%d",&a);
    b=&a;
    printf("The Address : %d\n",*b);
    printf("Address : %d",b);
    return 0;
}
