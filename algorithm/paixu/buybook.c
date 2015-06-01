#include<stdio.h>
int main(){
	int n,ch[100],i,j,k,book[20];
	printf("enter the num:");
	scanf("%d",&n);
	for(i=0;i<100;i++)
		ch[i]=0;

	for(i=0;i<20;i++)
		ch[i]=0;

	for(i=0;i<n;i++)
	{
		scanf("%d",&ch[i]);
		book[ch[i]]=1;
	}
	
	for(i=0;i<n-1;i++)
		for(j=0;j<n-i;j++)
		if(ch[j]<ch[j+1])
		{
			k=ch[j];
			ch[j]=ch[j+1];
			ch[j+1]=k;
		}
	for(i=0;i<n;i++)
	{
		if(book[ch[i]]!=0)
		{
			printf("%d ",ch[i]);
			book[ch[i]]=0;
		}
	}
	scanf("%d",&n);
	return 0;
}
