#include <stdio.h>
#include <stdlib.h>
#define MAX 10
int pq[MAX], rear, front;

void create()
{
    front = -1;
    rear = -1;
}

void insert_pq(int data)
{
    if (rear == MAX - 1)
    {
        printf("Queue i Full\n");
    }
    else if (front == -1 && rear == -1)
    {
        front++;
        rear++;
        pq[rear] = data;
        return;
    }
    else
    {
        check(data);
    }
    rear++;
}

void check(int data)
{
    int i, j;
    for (i = 0; i <= rear; i++)
    {
        if (data >= pq[i])
        {
            for (j = rear + 1; j > i; j--)
            {
                pq[j] = pq[j - 1];
            }
            pq[i] = data;
            return;
        }
    }
    pq[i] = data;
}

void delpq(int data)
{
    int i;
    if (front == rear == -1)
    {
        printf("Queue is Empty\n");
        return;
    }
    for (i = 0; i <= rear; i++)
    {
        if (pq[i] == data)
        {
            for (; i < rear; i++)
            {
                pq[i] = pq[i + 1];
            }
            pq[i] = -99;
            rear--;
            if (rear == -1)
            {
                front = -1;
            }
            return;
        }
    }
    printf("\n %d not found in the Queue",data);
}

void displaypq(){
    if(front==rear==-1){
        printf("Queue is Empty\n");
    }
    else{
        for(;front<=rear;front++){
            printf("%d\t",pq[front]);
        }
        front=0;
    }
}

void main(){
    printf("\n1.Insert by Priority\n2.Delete by Priority\n3.Display PQ\n4.Exit\n");
    int ch;
    int data;
    create();
    while(1){
        printf("\nEnter Your Choice:");
        scanf("%d",&ch);
        switch (ch)
        {
        case 1:
            printf("\nEnter Element to be inserted:");
            scanf("%d",&data);
            insert_pq(data);
            break;
        case 2:
            printf("\nEnter Element to be Removed:");
            scanf("%d",&data);
            delpq(data);
            break;
        case 3:
            printf("\nElements of the Queue are:");
            displaypq();
            break;
        case 4:break;
        default:
            printf("\nInvalid Choice\n");
            break;
        }
    }
}