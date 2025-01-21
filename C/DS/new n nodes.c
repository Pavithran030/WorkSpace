#include<stdio.h>
#include<stdlib.h>

struct node 
{
    int a;
    struct node *l;
};

struct node *create(int a1)
{
    struct node *n,*h,*temp;
    int m;
    h=malloc(sizeof(struct node));
    printf("Enter the value for the 1st  node : ");
    scanf("%d",h->a);
    h->l=NULL;
    temp=h;

    for(int i=2;i<a1;i++)
    {
        n=malloc(sizeof(struct node));
        printf("Enter the value for the node %d : ");
        scanf("%d",&m);
        n->a=m;
        n->l=NULL;
        temp->l=n;
        temp=n;
    }

    return h;
    
}

void print(struct node *h)
{
    struct node *temp;
    temp=h;
    while (temp->l!=NULL)
    {
        printf("%d -->",temp->a);
        temp=temp->l;
    }
    
    
}

int main()
{
    struct node *h;
    h=create(5);
    print(h);
}