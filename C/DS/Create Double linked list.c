#include <stdio.h>
#include <stdlib.h>
 
struct node
{
    int a ;
    struct node *pre;
    struct node *nex;

};

struct node *h=NULL;
struct node* create(struct node *h,int val)
{
    struct node *temp;
    temp=malloc(sizeof(struct node));
    temp->pre=NULL;
    temp->a=val;
    temp->nex=NULL;
    h=temp;
    return h;
}

void insertatbeg(int val)
{
    struct node *temp;
    temp->pre=NULL;
    temp->a=val;
    temp->nex=NULL;
    temp->nex=h;
    h->pre=temp;
    temp=h;
    return h;

}
int main()
{
    struct node *h;
    h=create(h,40);
    printf("%d",h->a);
    h=create(h,50);
    printf("%d",h->a);
    h=create(h,60);
    printf("%d",h->a);
}