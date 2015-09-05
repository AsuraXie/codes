#include<stdio.h>
#include<stdlib.h>

struct node{
	int i;
	int j;
	int w;
	struct node *next;
};

struct lists{
	struct node *first;
};

struct queue{
	int data[30];
	int head;
	int tail;
};

int visited[30];
int degree[30];
void dfs_array(int data[][30],int length,int n);
void dfs_list(struct lists  mylist[],int n);
void push(struct queue *myqueue,int data);
int pop(struct queue *myqueue);
void bfs_array(int data[][30],int length,struct queue *myqueue);
void bfs_lists(struct lists mylist[],struct queue *myqueue);
void djstla(int data[][30],int length);
void keypath(int data[][30],int length);

int main()
{
	int n,i,j,w,k,length;
	struct lists mygraph[30];
	int data[30][30];
	struct queue myqueue;
	myqueue.tail=myqueue.head=0;


	scanf("%d %d",&n,&length);
	for(i=0;i<30;i++)
	{
		mygraph[i].first=NULL;
		visited[i]=0;
		degree[i]=0;
		myqueue.data[i]=0;
	}
	
	for(i=0;i<30;i++)
		for(j=0;j<30;j++)
			data[i][j]=0;

	for(k=0;k<n;k++)
	{
		scanf("%d%d%d",&i,&j,&w);
		data[i][j]=w;
		degree[j]++;
		struct node *temp=(struct node *)malloc(sizeof(struct node));
		if(temp)
		{
			temp->i=i;
			temp->j=j;
			temp->w=w;
			temp->next=mygraph[i].first;
			mygraph[i].first=temp;
		}
	}
	/*
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
			printf("%d ",data[i][j]);
		printf("\n");
	}
	for(i=1;i<30;i++)
		if(mygraph[i].first!=NULL)
		{
			printf("node   %d\n",i);
			struct node *temp=mygraph[i].first;
			while(temp)
			{
				printf("%d %d %d\n",temp->i,temp->j,temp->w);		
				temp=temp->next;
			}
		}
	*/
	///dfs_list(mygraph,1);
	///dfs_array(data,length,1);
	visited[1]=1;
	push(&myqueue,1);
	///bfs_array(data,length,&myqueue);
	///bfs_lists(mygraph,&myqueue);
	///djstla(data,length);
	keypath(data,length);
	printf("\n");
}

void push(struct queue *myqueue,int data)
{
	if((myqueue->tail+1)%30==myqueue->head)
		return ;
	myqueue->data[myqueue->tail]=data;
	myqueue->tail=(++myqueue->tail)%30;
}

int pop(struct queue *myqueue)
{
	int temp;
	if(myqueue->head==myqueue->tail)
		return -1;
	else {
		temp=myqueue->data[myqueue->head];
		myqueue->data[myqueue->head]=0;
		myqueue->head=(++myqueue->head)%30;
		return temp;
	}
}

void dfs_array(int data[][30],int length,int n)
{
	int i;
	if(degree[n]==0&&visited[n]==0)
	{
		visited[n]=1;
		printf("%d ",n);
		for(i=0;i<=length;i++)
		{
			if(i!=n&&data[n][i]!=0&&visited[i]==0)
			{
				degree[i]--;
				if(degree[i]==0)
					dfs_array(data,length,i);
			}
		}
	}
}

void dfs_list(struct lists mylist[],int n)
{
	struct node *temp;
	if(degree[n]==0&&visited[n]==0)
	{
		printf("%d ",n);
		visited[n]=1;
		temp=mylist[n].first;
		while(temp)
		{
			degree[temp->j]--;
			if(degree[temp->j]==0&&visited[temp->j]==0)
				dfs_list(mylist,temp->j);
			temp=temp->next;
		}		
	}
}

void bfs_array(int data[][30],int length,struct queue *myqueue)
{
	int i;
	int a=pop(myqueue);
	if(a>0)
	{
		printf("%d ",a);
		for(i=0;i<=length;i++)
		{
			if(data[a][i]!=0&&visited[i]==0)
			{
				visited[i]=1;
				push(myqueue,i);
			}
		}
		bfs_array(data,length,myqueue);
	}
}

void bfs_lists(struct lists mylist[],struct queue *myqueue)
{
	int a=pop(myqueue);
	struct node *temp;
	if(a>0)
	{
		printf("%d ",a);
		temp=mylist[a].first;
		while(temp)
		{
			if(visited[temp->j]==0)
			{
				visited[temp->j]=1;
				push(myqueue,temp->j);
			}
			temp=temp->next;
		}
		bfs_lists(mylist,myqueue);
	}
}	

void djstla(int data[][30],int length)
{
	int dis[30][30],i,j,k,min,index;
	int max=9999999;
	for(i=1;i<=length;i++)	
	{
		for(j=0;j<30;j++)
		{
			if(data[i][j]!=0)
				dis[i][j]=data[i][j];
			else dis[i][j]=max;
			visited[j]=0;
		}

		dis[i][i]=0;
		for(k=1;k<length;k++)
		{
			min=max-2;
			index=0;
			for(j=1;j<=length;j++)
			{
				if(visited[j]==0&&min>dis[i][j])
				{
					min=dis[i][j];
					index=j;
				}
			}
			visited[index]=1;
			for(j=1;j<=length;j++)
			{
				if(index!=j&&visited[j]==0&&data[index][j]!=0)
				{
					if(dis[i][j]>dis[i][index]+data[index][j])
						dis[i][j]=dis[i][index]+data[index][j];
				}
			}
		}
		for(j=1;j<=length;j++)
			if(dis[i][j]==max)
				printf("0 ");
			else 
				printf("%d ",dis[i][j]);
		printf("\n");
	}
}

void keypath(int data[][30],int length)
{
	int early[30],last[30],i,j,k,min,max,index;
	int tdegree[30],bdegree[30];
	for(i=0;i<30;i++)
	{
		visited[i]=0;
		early[i]=0;
		last[i]=0;
		tdegree[i]=degree[i];
		bdegree[i]=0;
	}

	for(i=1;i<=length;i++)
		for(j=1;j<=length;j++)
		if(data[i][j]!=0)
			bdegree[i]++;
			

	for(i=1;i<=length;i++)
	{
		for(j=1;j<=length;j++)
		if(visited[j]==0&&tdegree[j]==0)
		{
			min=999999;
			index=0;
			for(k=1;k<length;k++)
			{
				if(data[k][j]!=0&&min>early[k]+data[k][j])
				{
					min=early[k]+data[k][j];
					index=k;
				}
				if(data[j][k]!=0)
					tdegree[k]--;	
			}

			if(min==999999)
			{
				min=0;
				early[j]=0;
			}
			else early[j]=min;
			visited[j]=1;
			printf("%d %d\n",j,min);
		}
	}
}
