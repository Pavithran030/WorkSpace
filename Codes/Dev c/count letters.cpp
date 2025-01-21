#include<stdio.h>
#include<string.h>
int main()
{
	char a1[20],a2[20];
	printf("Enter a string : ");
	scanf("%s",a1);
	int k;
	k=strlen(a1);
	for(int i=0;i<k;i++)
	{
		int count=1;
		for(int j=i+1;j<k;j++)
		{
			if(a1[i]==a1[j])
			{
				count++;
				a1[j]=-1;
			}
		}
		if(a1[i]!=-1)
		{
			printf("%c = %d \n",a1[i],count);
		}
	}
}
