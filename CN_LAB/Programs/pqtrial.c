#include <stdio.h>
#include <stdlib.h>

#define max 10
int pq[max], front, rear;

void create()
{
    front = -1;
    rear = -1;
    return;
}

void insert(int data)
{
    if (rear == max - 1)
    {
        printf("\nQueue is Empty\n");
        return;
    }
    else if (front == rear == -1)
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
        if (pq[i]<=data)
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

void deletepq(int data)
{
    int i;
    if (front == rear == -1)
    {
        printf("\nQueue is Empty");
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
    printf("\n%d not found in Queue");
}

void display(){
    if(front==rear==-1){
        printf("\nQueue is Empty");
    }
    for(front=0;front<=rear;front++){
        printf("%d\t",pq[front]);
    }
}

void main()
{
    printf("\n1.Insert by Priority\n2.Delete by Priority\n3.Display PQ\n4.Exit\n");
    int ch;
    int data;
    create();
    while (1)
    {
        printf("\nEnter Your Choice:");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            printf("\nEnter Element to be inserted:");
            scanf("%d", &data);
            insert(data);
            break;
        case 2:
            printf("\nEnter Element to be Removed:");
            scanf("%d", &data);
            deletepq(data);
            break;
        case 3:
            printf("\nElements of the Queue are:");
            display();
            break;
        case 4:
            exit(0);
        default:
            printf("\nInvalid Choice\n");
            break;
        }
    }
}