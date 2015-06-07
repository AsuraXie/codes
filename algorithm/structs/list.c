#include<stdio.h>
#include<stdlib.h>
struct node{
	int data;
	struct node * next;
};

struct node head;

void add()
{
	struct node *temp,*temp2;
	int n;
	temp=&head;
	printf("enter the num:");
	scanf("%d",&n);
	while(temp->next!=NULL)
	{
		if(temp->next->data>n)
			break;
		temp=temp->next;
	}
	temp2=temp->next;
	temp->next=(struct node *)malloc(sizeof(struct node));
	if(temp->next!=NULL)
	{
		temp=temp->next;
		temp->data=n;
		temp->next=temp2;
	}
}

void modify(){
	struct node *temp;
	int n,i,j;
	temp=&head;
	printf("enter the place and value:");
	scanf("%d %d",&i,&n);
	j=0;
	while(j<i&&temp!=NULL)
	{
		temp=temp->next;
		j++;
	}
	if(j==i)
		temp->data=n;
	else printf("Wrong place\n");
}

void delete(){
	struct node *temp,*temp2;
	int n,i,j;
	temp=&head;
	printf("enter the place:");
	scanf("%d",&i);
	j=0;
	while(j<i&&temp!=NULL)
	{
		temp=temp->next;
		j++;
	}
	if(j==i)
	{
		if(temp->next!=NULL)
		{
			temp2=temp->next;
			temp->next=temp->next->next;
			free(temp2);
		}
	}
	else printf("Wrong place\n");
}

void show(){
	struct node *temp;
	temp=&head;
	while(temp!=NULL)
	{
		printf("%d ",temp->data);
		temp=temp->next;
	}
	printf("\n");
}

void insert(){
	struct node *temp,*temp2;
	int n,i,j;
	temp=&head;
	printf("enter the place and value:");
	scanf("%d %d",&i,&n);
	j=0;
	while(j<i&&temp!=NULL)
	{
		temp=temp->next;
		j++;
	}
	if(j==i)
	{
		temp2=(struct node *)malloc(sizeof(struct node));
		temp2->data=n;
		temp2->next=temp->next->next;
		free(temp->next);
		temp->next=temp2;
	}
	else printf("Wrong place\n");
}

int main(){
	int n,i,j,temp,op,flag;
	flag=0;
	head.data=0;
	head.next=NULL;

	while(1)
	{
		printf("1 add\n");
		printf("2 modify\n");
		printf("3 delete\n");
		printf("4 insert\n");
		printf("5 show\n");
		printf("6 exit\n");
		printf("enter the choice:");
		scanf("%d",&op);
		switch(op)
		{
			case 1:add(); break;
			case 2:modify(); break;
			case 3:delete(); break;
			case 4:insert(); break;
			case 5:show(); break;
			case 6:flag=1; break;
			default:printf("Wrong Choice\n");flag=1;break;
		}

		if(flag==1)
		{
			printf("Over\n");
			break;
		}
	}
	return 0;
}
