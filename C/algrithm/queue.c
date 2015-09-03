#include<stdio.h>
#include<stdlib.h>

struct queue{
	int data[30];
	int head;
	int tail;
};

void push(struct queue *head,int data);
int pop(struct queue *head);
void show(struct queue *head);

void push(struct queue *head,int data)
{
	if((head->tail+1)%30==head->head)
	{
		printf("queue is fool\n");
	}
	else
	{
		head->data[head->tail]=data;
		head->tail++;
		if(head->tail==head->head)
			printf("queue is fool\n");
		else head->tail=head->tail%30;
	}
}

int pop(struct queue *head)
{
	int temp;
	if(head->tail==head->head)
	{
		printf("queue is empty\n");
		return -1;
	}
	else {
		temp=head->head;
		head->head=(++head->head)%30;
		return head->data[temp];
	}
}

void show(struct queue *head)
{
	int temp=head->head;
	if(head->tail==head->head)
	{
		printf("queue is empty\n");
		return;
	}
	while(temp!=(head->tail+1)%30)
	{
		printf("%d ",head->data[temp]);
		temp=(++temp)%30;
	}
	printf("\n");
}
		

