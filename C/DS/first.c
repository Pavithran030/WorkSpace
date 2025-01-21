#include<stdio.h>
#include<stdlib.h>

struct node
{
    int a;
    struct node *link;
};

struct node* create()
{
    int n;
    struct node *e1=NULL,*e2,*e3;

    for(int i=0;i<5;i++)
    {
        e2=malloc(sizeof(struct node));
        printf("Enter the value for the node : ");
        scanf("%d",&e2->a);
        e2->link=NULL;
        if (e1==NULL)
        {
            e1=e2;
            e3=e1;
        }
        else{
            e3->link=e2;
            e3=e2;
        }
    }
    return e1;


}

void print(struct node *h)
{
    struct node *temp=h;
    while(temp!=NULL)
    {
        printf("%d \t",temp->a);
        temp=temp->link;
    }
}
int main()
{
    struct node *m=create();
    print(m);

}