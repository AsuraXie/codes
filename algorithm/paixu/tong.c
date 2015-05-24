#include<stdio.h>
int main()
{
	int book[10],i,j,n;
	printf("enter the num:");
	scanf("%d",&n);
	for(i=0;i<10;i++)
		book[i]=0;
	for(i=0;i<n;i++)
	{
		scanf("%d",&j);
		book[j]++;
	}
	for(i=0;i<10;i++)
	{
		for(j=1;j<=book[i];j++)
			printf("  %d   ",i);
		if(book[i]!=0)
			printf("\n");
	}
	printf("success\n");
	scanf("%d",&n);
	return 0;
}
