#include<stdio.h>
#include<string.h>

int checksum(int fl){
    int temp,sum=0,n,i;
    char in[100];

    scanf("%s",in);

    if(strlen(in)%2!=0){
        n=(strlen(in)+1)/2;
    }
    else{
        n=strlen(in)/2;
    }

    for(i=0;i<n;i++){
        temp=in[i*2];
        temp=(temp*256)+in[(i*2)+1];
        sum+=temp;
    }

    if(fl==1){
        printf("\nEnter the checksum:");
        scanf("%x",&temp);
        sum+=temp;
    }

    if(sum%65536!=0){
        n=sum%65536;
        sum=(sum/65536)+n;
    }

    sum=65535-sum;
    printf("\n%x",sum);
    return sum;
}

int main(){
    int ch,sum;
    do{
        printf("\n1.Encode\n2.Decode\n3.Exit\n");
        printf("\nEnter Your Choice:");
        scanf("%d",&ch);

        switch(ch){
            case 1:printf("\nEnter the string:");
                    sum=checksum(0);
                    printf("\nThe Checksum is %x",sum);
                    break;
            case 2:printf("\nEnter the string:");
                    sum=checksum(1);
                    if(sum!=0){
                        printf("\nInvalid Checksum");
                    }
                    else{
                        printf("\nChecksum is Valid");
                    }
                    break;
            case 3:break;
            default:printf("\nInvalid choice");
        }
    }
    while(ch!=3);
}
