#include<stdio.h>
#include<stdlib.h>

struct node{
	int data;
	struct node * next;
};

int add(struct node *head,int data);
int delete(struct node *head,int pos);
void showlist(struct node *head);
int insert(struct node *head,int data,int pos);
int isloop(struct node *head);
void loop(struct node *head);
void headtotail(struct node *head);
void find(struct node *head,int pos);

int add(struct node * head,int data)
{
	struct node * temp;
	temp=head;
	while(temp->next)
		temp=temp->next;
	temp->next=(struct node *)malloc(sizeof(struct node));
	if(temp->next==NULL)
		return 0;
	temp=temp->next;
	temp->data=data;
	temp->next=NULL;
	return 1;	
}

int delete(struct node * head,int pos)
{
	struct node *temp=head->next,*pre;
	int index=0;
	pre=head;
	while(temp->next&&index<pos)
	{
		pre=pre->next;
		temp=temp->next;
		index++;
	}
	if(index==pos)
	{
		pre->next=temp->next;
		free(temp);
		return  1;
	}
	else return 0;
}

void showlist(struct node * head)
{
	struct node *temp=head->next;
	while(temp)
	{
		printf("%d ",temp->data);
		temp=temp->next;
	}
	printf("\n");
}

int main()
{
	struct node head;
	head.data=0;
	head.next=NULL;
	add(&head,1);
	add(&head,2);
	add(&head,5);
	insert(&head,6,2);
	insert(&head,8,4);
	headtotail(&head);
	showlist(&head);
	delete(&head,1);
	showlist(&head);
	headtotail(&head);
	delete(&head,3);
	showlist(&head);
	isloop(&head);
	///	loop(&head);
	isloop(&head);
	headtotail(&head);
	find(&head,1);
	find(&head,2);
	find(&head,3);
	find(&head,0);
	find(&head,5);
	return 0;
}

int insert(struct node * head,int data, int pos)
{
	int index=0;
	struct node * temp=head;
	struct node * temp2=NULL;
	while(temp->next&&index<pos)
	{
		temp=temp->next;
		index++;
	}
	if(index==pos)
	{
		temp2=(struct node *)malloc(sizeof(struct node));
		temp2->next=temp->next;
		temp->next=temp2;
		temp2->data=data;
		return 1;
	}
	return 0;
}

int isloop(struct node *head)
{
	struct node *slow=head,*fast=head;
	while(fast)
	{
		slow=slow->next;
		fast=fast->next;
		if(fast==NULL)
		{
			printf("not loop\n");
			return 0;
		}
		fast=fast->next;
		if(slow==fast)
		{
			printf("loop\n");
			return 1;
		}
	}
	printf("not loop\n");
	return 0;
}

void loop(struct node *head)
{
	struct node * temp=head;
	while(temp->next)
		temp=temp->next;
	temp->next=head;
}

void headtotail(struct node *head)
{
	struct node *pre,*next,*temp;
	pre=head->next;
	next=pre->next;
	pre->next=NULL;
	while(next)
	{
		temp=next;
		next=next->next;	
		temp->next=pre;
		pre=temp;
	}
	head->next=pre;
	temp=head->next;
	while(temp)
	{
		printf("%d  ",temp->data);
		temp=temp->next;
	}
	printf("\n");
}

void find(struct node *head,int pos)
{
	struct node *temp;
	int index=0;
	temp=head;
	while(temp)
	{
		if(index==pos)
			break;
		temp=temp->next;
		index++;
	}
	if(index==pos)
		printf("%d \n",temp->data);
	else printf("not found\n");
}
