#include<stdio.h>
int main(){
	int ch[100],i,j,k,n;
	printf("enter the num:");
	scanf("%d",&n);

	for(i=0;i<100;i++)
		ch[i]=0;
	for(i=0;i<n;i++)
		scanf("%d",&ch[i]);
	
	for(i=0;i<n-1;i++)
		for(j=0;j<n-i;j++)
		if(ch[j]<ch[j+1])
		{
			k=ch[j];
			ch[j]=ch[j+1];
			ch[j+1]=k;
		}
	for(i=0;i<n;i++)
		printf("%d ",ch[i]);
	printf("\n");
	scanf("%d",&k);
	return 0;
}
