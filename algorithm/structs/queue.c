#include<stdio.h>
struct queue{
	int ch[100];
	int head;
	int tail;
};

int main(){
	int n,i,j;
	struct queue myque;
	myque.head=0;
	myque.tail=0;
	printf("enter the num:");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&myque.ch[myque.tail]);
		myque.tail++;
	}
	

	while(myque.head!=myque.tail)
	{
		printf("%d ",myque.ch[myque.head]);
		myque.head++;
		myque.ch[myque.tail]=myque.ch[myque.head];
		myque.head++;
		myque.tail++;
	}
	printf("game over\n");
	scanf("%d");
	return 0;
}
