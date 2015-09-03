#include<stdio.h>
#include<stdlib.h>

struct node{
	int data;
	struct node *left;
	struct node *right;
};

struct queue{
	struct node *data[20];
	int tail;
	int head;
};
	
void init(struct node *root,int *data,int length,int index);
void left_search(struct node *root);
void mid_search(struct node *root);
void right_search(struct node *root);
void dfs(struct node *root);
void bfs(struct queue *myqueue);
void push(struct queue *myqueue,struct node *data);
struct node * pop(struct queue *myqueue);
void showqueue(struct queue *myqueue);

int main(){
	int data[10];
	int i=0;
	struct node root;
	struct queue myqueue;
	root.data=0;
	root.left=NULL;
	root.right=NULL;
	myqueue.tail=0;
	myqueue.head=0;

	for(i=0;i<10;i++)
		data[i]=i;
	init(&root,data,10,1);
	dfs(&root);
	printf("\n");
	push(&myqueue,&root);
	bfs(&myqueue);
	printf("\n");
	left_search(&root);
	printf("\n");
	mid_search(&root);
	printf("\n");
	right_search(&root);
	printf("\n");
	return 23;
}

void push(struct queue *myqueue,struct node *data)
{
	if((myqueue->tail+1)%20==myqueue->head)
		return ;
	else {
		myqueue->data[myqueue->tail]=data;
		myqueue->tail=(++myqueue->tail)%20;
	}
}

struct node * pop(struct queue *myqueue)
{
	struct node *temp;
	if(myqueue->head==myqueue->tail)
		return NULL;
	else
	{
		temp=myqueue->data[myqueue->head];
		myqueue->head=(++myqueue->head)%20;
		return temp;
	}
}	

void showqueue(struct queue *myqueue)
{
	int i=0;
	for(i=myqueue->head;;)
	{
		if((i)%20==myqueue->tail)
			break;
		printf("%p ",myqueue->data[i]);
		i=(i+1)%20;
	}
}

void init(struct node *root,int *data,int length,int index)
{
	if(index>=length)
		return;
	root->data=data[index];
	if(2*index<length)
	{
		root->left=(struct node*)malloc(sizeof(struct node));
		if(root->left!=NULL)
			init(root->left,data,length,2*index);
	}
	if(2*index+1<length)
	{
		root->right=(struct node*)malloc(sizeof(struct node));
		if(root->right!=NULL)
			init(root->right,data,length,2*index+1);
	}
}

void dfs(struct node *root)
{
	printf("%d ",root->data);
	if(root->left!=NULL)
		dfs(root->left);
	if(root->right!=NULL)
		dfs(root->right);
}	

void bfs(struct queue *myqueue)
{
	struct node *temp=pop(myqueue);
	if(temp!=NULL)
	{
		printf("%d ",temp->data);
		if(temp->left!=NULL)
			push(myqueue,temp->left);
		if(temp->right!=NULL)
			push(myqueue,temp->right);		
		bfs(myqueue);
	}
}

void left_search(struct node *root)
{
	printf("%d ",root->data);
	if(root->left!=NULL)
		left_search(root->left);
	if(root->right!=NULL)
		left_search(root->right);
}

void mid_search(struct node *root)
{
	if(root->left!=NULL)
		mid_search(root->left);
	printf("%d ",root->data);
	if(root->right!=NULL)
		mid_search(root->right);
}

void right_search(struct node *root)
{
	if(root->left!=NULL)
		right_search(root->left);
	if(root->right!=NULL)
		right_search(root->right);
	printf("%d ",root->data);
}
