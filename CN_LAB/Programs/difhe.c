#include<stdio.h>
#include<math.h>

long long int power(long long int a,long long int b, long long int p){
    if(b==1){
        return a;
    }
    else{
        return(((long long int)pow(a,b))%p);
    }
}

int main(){
    long long int p,g,a,b,ka,kb,x,y;
    p=23;
    g=5;
    a=6;
    b=15;

    x=power(g,a,p);
    printf("\nPrivate key of Alice is:%lld",x);

    y=power(g,b,p);
    printf("\n Private key of Bob is %lld",y);

    ka=power(y,a,p);
    printf("\n Secret key of Alice is %lld",ka);

    kb=power(x,b,p);
    printf("\n Secret key of bob is %lld",kb);
}