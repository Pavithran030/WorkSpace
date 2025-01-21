#include <stdio.h>
int main() {
    char sa[10];
    printf("Enter a string ");
    scanf("%s",sa);
    char *s1[10];
    *s1=sa;
    int k,i,j,co=0;
    for(j=0;s1[j]!='\0';j++)
    {
    	co++;
	}
    for(i=co;i>=0;i--)
    {
        printf("%c",(*s1)[i]);
    }
    return 0;
}
