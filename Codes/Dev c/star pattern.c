#include<stdio.h>
int main()
{
	int a,i,j;
	scanf("%d",&a);
	printf("The rows are: %d\n",a);
	for(i=0;i<=a;i++)
	{
		for(j=a;j>0;j--)
		{
			printf("* ");
		}
		a--;
		printf("\n");
	}
}
