#include<stdio.h>
int print(int a)
{
    printf("The value is : %d",a);
}
int main()
{
    int x,y;
    int *pt;
    printf("Enter a number : ");
    scanf("%d",&x);
    pt=&x;
    print(pt);
    y=*pt;
    print(y);
    return 0;
}