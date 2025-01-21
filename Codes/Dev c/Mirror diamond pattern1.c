#include <stdio.h>
int main() {
    int a,i,j,s,count=1,l,m,n,count1=1,to;
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
    to=a-1;
   for(l=0;l<=a-1;l++)
    {
    	for(m=0;m<count1;m++)
    	{
    		printf("  ");
		}
		count1++;
		
		for(n=to+(to-count1);n>0;n--)
		{
			printf("* ");
		}
		printf("\n");
	}

    return 0;
}
