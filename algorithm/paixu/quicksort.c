#include<stdio.h>
int ch[100];

int quicksort(int left,int right)
{
	int temp,i,j,k;
	if(left>=right)
		return 0;
	temp=ch[left];
	i=left;
	j=right;
	while(i!=j)
	{
		while(ch[j]>temp&&i<j)
			j--;
		while(ch[i]<temp&&i<j)
			i++;
		if(i<j)
		{
			k=ch[i];
			ch[i]=ch[j];
			ch[j]=k;
		}
	}
	quicksort(left,j-1);
	quicksort(j+1,right);
	return 0;
}

int main(){
	int i,j,n;
	printf("enter the num:");
	scanf("%d",&n);
	for(i=0;i<100;i++)
		ch[i]=0;
	for(i=0;i<n;i++)
		scanf("%d",&ch[i]);
	quicksort(0,n-1);
	for(i=0;i<n;i++)
		printf("%d ",ch[i]);
	printf("\n");
	scanf("%d",&n);
	return 0;
}
