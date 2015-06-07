#include<stdio.h>

struct queue{
	int ch[100];
	int top;
	int tail;
};

struct stack{
	int ch[10];
	int top;
};

int main(){
	int book[10],temp,flag,temp2;
	struct queue a,b;
	struct stack c;
	int n,i,j,k;
	printf("enter the num:");
	scanf("%d",&n);

	a.top=a.tail=b.top=b.tail=0;
	c.top=0;

	for(i=0;i<10;i++)
	{
		book[i]=0;
		a.ch[i]=b.ch[i]=c.ch[i]=0;
	}

	for(i;i<30;i++)
	{
		a.ch[i]=b.ch[i]=0;
	}
	
	for(i=0;i<n;i++)
	{
		scanf("%d",&a.ch[a.tail]);
		a.tail++;
	}

	for(i=0;i<n;i++)
	{
		scanf("%d",&b.ch[b.tail]);
		b.tail++;
	}

	for(i=0;i<10;i++)
		book[i]=0;

	flag=0;
	while(a.top!=a.tail&&b.top!=b.tail)
	{
		temp=a.ch[a.top];
		a.top++;
	
		if(c.top>0&&book[temp]!=0)
		{
			a.ch[a.tail]=temp;
			a.tail++;
			while(c.ch[c.top-1]!=temp)
			{	
				book[c.ch[c.top-1]]=0;
				a.ch[a.tail]=c.ch[c.top-1];
				a.tail++;
				c.top--;
				book[c.ch[c.top-1]]=0;
			}
			a.ch[a.tail]=c.ch[c.top-1];
			book[c.ch[c.top-1]]=0;
			a.tail++;
			c.top--;
		}
		else {
			book[temp]=1;
			c.ch[c.top]=temp;
			c.top++;
		}

		temp=b.ch[b.top];
		b.top++;
		if(c.top>0&&book[temp]!=0)
		{
			b.ch[b.tail]=temp;
			b.tail++;
			while(c.ch[c.top-1]!=temp)
			{
				book[c.ch[c.top-1]]=0;
				b.ch[b.tail]=c.ch[c.top-1];
				b.tail++;
				c.top--;
			}
			b.ch[b.tail]=c.ch[c.top-1];
			book[c.ch[c.top-1]]=0;
			b.tail++;
			c.top--;
		}
		else {
			book[temp]=1;
			c.ch[c.top]=temp;
			c.top++;
		}
		
		if(a.top==a.tail||b.top==b.tail)
		{
			flag=1;	
			break;
		}
	}

	if(flag==1)
	{
		if(a.top==a.tail)
		{
			printf("b win\n");
			while(b.top<=b.tail)
			{
				printf("%d ",b.ch[b.top-1]);
				b.top++;
			}
			printf("\n");
		}
		else if(b.top==b.tail)
		{
			printf("a win\n");
			while(a.top<=a.tail)
			{
				printf("%d ",a.ch[a.top-1]);
				a.top++;

			}
		}
	}

	printf("over\n");
	scanf("%d",&n);
}
