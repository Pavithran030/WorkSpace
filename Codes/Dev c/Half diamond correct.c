#include <stdio.h>
int main() {
    int a,i,j,l,s;
    scanf("%d",&a);
    for( i=-a;i<a;i++)
	{
    if(i<0)
    	l=-i;
    else
    	l=i;
    for(s=0;s<l;s++)
    	{
    		printf("  ");
		}
        for(j=0;j<(a-l);j++)
        {
         	printf("* ");
        }
        printf("\n");
    }
    return 0;
}
