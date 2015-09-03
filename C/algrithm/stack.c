#include<stdio.h>
#include<stdlib.h>

struct  node {
	int data[30];
	int tail;
};

void push(struct node *stack,int data);
int pop(struct node *stack);
void show(struct node *stack);

int main()
{
	int i=0;
	int temp=0;
	struct node head;
	head.tail=0;
	
	for(i=0;i<30;i++)
		head.data[i]=0;
	for(i=1;i<30;i++)
		push(&head,i);
	show(&head);
	for(i=1;i<40;i++)
	{
		temp=pop(&head);
		if(temp>0)
			printf("%d ",temp);
	}	
	return 0;
}

void push(struct node *stack,int data){
	if(stack->tail==30)
	{
		printf("stack is  fool\n");
		return;
	}
	stack->data[stack->tail]=data;
	stack->tail++;
}

int pop(struct node *stack){
	if(stack->tail==0)
	{
		printf("stack is empty\n");
		return -1;
	}
	stack->tail--;
	return stack->data[stack->tail];
}

void show(struct node *stack){
	int i=0;
	for(i=0;i<stack->tail;i++)
		printf("%d ",stack->data[i]);
	printf("\n");
}	
