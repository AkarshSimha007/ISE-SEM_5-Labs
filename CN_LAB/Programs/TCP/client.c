#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<sys/socket.h>
#include<fcntl.h>
#include<arpa/inet.h>
#include<netinet/in.h>

#define bufsize 1024

int main(){
    int clientSocket;
    char fname[255],buffer[bufsize];

    struct sockaddr_in serverAddr;
    socklen_t addr_size;

    clientSocket=socket(AF_INET,SOCK_STREAM,0);

    serverAddr.sin_family=AF_INET;
    serverAddr.sin_port=htons(15000);
    serverAddr.sin_addr.s_addr=inet.addr("127.0.0.1");

    memset(serverAddr.sin_zero,'\0',sizeof serverAddr.sin_zero);
    connect(clientSocket,(struct sockaddr *)&serverAddr,sizeof serverAddr);

    printf("Enter file name:");
    scanf("%s",fname);

    send(clientSocket,fname,255,0);

    while(recv(clientSocket,buffer,bufsize,0)>0){
        printf("%s",buffer);
        print("\n");
    }
    return close(clientSocket);
}