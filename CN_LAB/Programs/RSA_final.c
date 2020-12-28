#include<stdio.h>
#include<math.h>

int gcd(int a,int h){
    int temp;
    while(1){
        temp=a%h;
        if(temp==0)
        return h;
        a=h;
        h=temp;
    }
}

int main(){
    double p=3,q=7;
    double n=p*q;
    double totient=(p-1)*(q-1);
    double e=2;
    int k=2;
    
    while(e<totient){
        if(gcd(e,totient)==1)
            break;
        else
            e++;
    }

    double d=(1+(k*totient))/e;

    double msg=34;
    printf("\n\nMessage Data is: %lf",msg);


    double c=pow(msg,e);
    c=fmod(c,n);
    printf("\n\nEncrypted Mesaage is: %lf",c);

    double m=pow(c,d);
    m=fmod(m,n);
    printf("\n\nOriginal Message is: %lf",m);

    return 0;


}