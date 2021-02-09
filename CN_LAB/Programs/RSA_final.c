#include<stdio.h>
#include<math.h>

int gcd(int a,int h){
    int temp;
    while(1){
        temp=a%h;
        if(temp==0){
            return h;
        }
        else{
            a=h;
            h=temp;
        }
    }
}

int main(){
    double p=3,q=7;
    double n=p*q;
    double totient=(p-1)*(q-1);

    double e=2;
    double k=2;

    while(e<totient){
        if(gcd(e,totient)==1){
            break;
        }
        else{
            e++;
        }
    }

    double msg=16;
    printf("Message data is %lf",msg);
    double d=(1+(k*totient))/e;

    double c=pow(msg,e);
    c=fmod(c,n);
    printf("\nEncrypted data is %lf",c);

    double m=pow(c,d);
    m=fmod(m,n);
    printf("\nORiginal Message sent is %lf",d);
}