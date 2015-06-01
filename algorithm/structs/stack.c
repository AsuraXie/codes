#include<stdio.h>

struct stack{
	char ch[100];
	int top;
};

int main(){
	char ah[100];
	int n,i,j,k;
	struct stack mystack;
	printf("enter the num:");
	scanf("%d",&n);
	scanf("%c",&ah[0]);
	for(i=0;i<n;i++)
		scanf("%c",&ah[i]);

	k=n%2;
	mystack.top=0;
	for(i=0;i<n/2;i++)
	{
		mystack.ch[mystack.top]=ah[i];
		mystack.top++;
	}

	if(k==1)
		i++;
	for(i;i<n;i++)
	{
		mystack.top--;
		if(mystack.top<0)
		{
			break;
		}
		if(mystack.ch[mystack.top]!=ah[i])
		{
			break;
		}
	}

	if(i==n)
		printf("ok\n");
	else printf("faile\n");
	scanf("%d",&n);
	return 0;
}
