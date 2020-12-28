#include<stdio.h>
#include<math.h>

long long int power(long long int a,long long int b,long long int p){
    if(b==1){
        return a;
    }
    else{
        return (((long long int)pow(a,b))%p);
    }
}

int main(){
    long long int p,g,a,b,x,y,ka,kb;

    p=23;
    g=5;
    a=3;
    b=4;

    x=power(g,a,p);
    y=power(g,b,p);

    ka=power(y,a,p);
    printf("\nSecret key for alice is:%lld",ka);

    kb=power(x,b,p);
    printf("\nSecret key for bob is %lld",kb);
    return 0;
}