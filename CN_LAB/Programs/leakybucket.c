#include<stdio.h>
#include<stdlib.h>
#define MIN(x,y) (x>y)?:y,x

int main()
{
     int inp[10],i=0,nsec,bSize,drop=0,count=0,orate,ch,x;

     printf("Enter the Bucket Size:");
     scanf("%d",&bSize);

     printf("\nEnter Output Rate:");
     scanf("%d",&orate);

     do{
         printf("\nEnter number of packets arriving at second %d: ",i+1);
         scanf("%d",&inp[i]);
         i++;
         printf("\nEnter 1 to continue or 0 to quit...:");
         scanf("%d",&ch);
     }while(ch);

     nsec=i;
     printf("\n Second \t Recieved \t Sent \t Dropped \t Remaining\n");
     for(i=0;count||nsec>i;i++){
         printf("%d",i+1);
         printf("\t%d\t",inp[i]);
         printf("\t%d\t",MIN((inp[i]+count),orate));
         
         if((x=inp[i]+count-orate)>0){
             if(x>bSize){
                 count=bSize;
                 drop=x-bSize;
             }
             else{
                 count=x;
                 drop=0;
             }
         }
         else{
             count=0;
             drop=0;
         }
         printf("\t%d\t%d\n",drop,count);
         
     }
     
    /* code */
    return 0;
}
