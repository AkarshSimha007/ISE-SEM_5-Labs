#include<stdio.h>
#define infinity 999

void dij(int n,int v,int cost[10][10],int dist[]){
    
    int count,i,u,w,flag[10],min;
    for(i=1;i<=n;i++){
        flag[i]=0;
        dist[i]=cost[v][i];
    }
    
    count=2;
    while(count<=n){
        min=99;
        for(w=1;w<=n;w++)
            if(min>dist[w] && !flag[w]){
                min=dist[w];
                u=w;
            }
            flag[u]=1;
        count++;
        
        for(w=1;w<=n;w++){
            if((dist[u]+cost[u][w])<dist[w] && !flag[w]){
                dist[w]=dist[u]+cost[u][w];
            }
        }
    }
}

int main(){
    int n,i,j,v,cost[10][10],dist[10];
    
    printf("\nEnter the number of nodes:");
    scanf("%d",&n);
    
    printf("\nEnter the cost matrix:\n");
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            scanf("%d",&cost[i][j]);
            if(cost[i][j]==0){
                cost[i][j]=infinity;
            }
        }
    }
    
    printf("\nEnter source node:");
    scanf("%d",&v);
    
    dij(n,v,cost,dist);
    
    printf("\nShortest Path:\n");
    
    for(i=1;i<=n;i++){
        if(i!=v){
            printf("\n%d --> %d distance is %d\n",v,i,dist[i]);
        }
    }
    
}