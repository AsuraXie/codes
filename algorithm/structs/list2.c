#include<stdio.h>
int main()
{
	int data[100],right[100],i,j,n,k,min,minindex,maxindex;
	printf("enter the num:");
	scanf("%d",&n);
	for(i=0;i<100;i++)
	{
		data[i]=right[i]=0;
	}

	min=999999;
	minindex=0;
	maxindex=0;
	for(i=1;i<=n;i++)
	{
		scanf("%d",&k);
		data[i]=k;
		right[i]=0;
		for(j=1;j<=i;j++)
		{
			if(data[j]>k)
			{
				right[i]=j;
			}
		}
		if(right[i]==0)
		{
			if(maxindex!=0)
			{
				right[maxindex]=i;
				maxindex=i;
			}
			else maxindex=i;
		}
		if(min>k)
		{
			min=k;
			minindex=i;
		}
	}
	
	j=0;
	for(i=1;i<=n;i++)
		printf("%d %d\n",data[i],right[i]);

	while(j<n&&minindex!=0)
	{
		printf("%d ",data[minindex]);
		minindex=right[minindex];
		j++;
	}
	printf("\n");
	scanf("%d",&n);
	return 0;
}
