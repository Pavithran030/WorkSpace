#include <stdio.h>
int main() {
    int a,i,j,s,count=1,l,m,n;
    scanf("%d",&a);
    for( i=0;i<a;i++)
    {
    	for(s=a-i-1;s>=0;s--)
    	{
    		printf("  ");
		}
        for(j=1;j<=a-(a-count);j++)
        {
         	printf("* ");
        }
        count++;
        printf("\n");
    }
    for(l=0;l<a-1;l++)
    {
    	for(m=1;m<a-1;m++)
    	{
    		printf(". ");
		}
		for(n=a-1;n<=0;n++)
		{
			printf("* ");
		}
		printf("\n");
	}

    return 0;
}