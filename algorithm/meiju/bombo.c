#include<stdio.h>
int main(){
	char ch[20][20];
	int m,n,i,j,max,x,y,temp,tx,ty,k;
	int next[4][2];
	scanf("%d %d",&m,&n);
	printf("%d %d\n",m,n);
	for(i=0;i<m;i++)
	{
		getchar();
		for(j=0;j<n;j++)
			scanf("%c",&ch[i][j]);
	}

	next[0][0]=1;
	next[0][1]=0;

	next[1][0]=0;
	next[1][1]=1;

	next[2][0]=-1;
	next[2][1]=0;

	next[3][0]=0;
	next[3][1]=-1;

	x=0;
	y=0;
	max=0;
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
		if(ch[i][j]=='.')
		{
			temp=0;
			for(k=0;k<4;k++)
			{
				tx=i;
				ty=j;
				while(ch[tx][ty]!='#')
				{
					if(ch[tx][ty]=='G')
						temp++;
					tx=tx+next[k][0];
					ty=ty+next[k][1];
				}
			}

			if(max<temp)
			{
				max=temp;
				x=i;
				y=j;
			}
		}
	
	printf("%d %d %d \n",x,y,max);
	printf("over\n");
	scanf("%d",&n);
	return 0;
}
