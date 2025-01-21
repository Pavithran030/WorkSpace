#include<stdio.h>
#include<stdlib.h>

struct n
{
    int a;
    struct n *ln;
};
struct n *create()
{
    int i;
    struct n *a1=NULL,*a2,*a3;
    print("Enter the number of nodes : ");
    scanf("%d",&i);


    for (int j=0;j<i;j++)
    {
        a2=malloc(sizeof(struct n));
        a2->a=20;
        a2->ln=NULL;

        if(a1==NULL)
        {
            a1=a2;
            a3=a1;

        }
        else
        {
            a3->ln=a2;
            a3=a2;
        }
        
    }
    return a2;
}

void print(struct n *h)
{
    struct n *t=h;
    while(t!=NULL)
    {
        printf("%d\n",t->a);
        t=t->ln;
    }
}

int main()
{
    struct n *h=create();
    print(h);
}
