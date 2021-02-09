#include<stdio.h>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>
#include<arpa/inet.h>
#include<netinet/in.h>
#include<sys/socket.h>

#define bufsize 1024

int main(){

    int serverSocket,newSocket,fd,n;
    char fname[255],buffer[1024];

    struct sockaddr_in serverAddr;
    struct sockaddr_storage serverStorage;
    socklen_t addr_size;

    serverSocket=socket(AF_INET,SOCK_STREAM,0);

    serverAddr.sin_family=AF_INET;
    serverAddr.sin_port=htons(15000);
    serverAddr.sin_addr.s_addr=inet_addr("127.0.0.1");

    memset(serverAddr.sin_zero,'\0',sizeof serverAddr.sin_zero);

    bind(serverSocket,(struct sockaddr *)&serverAddr,sizeof(serverAddr));

    if(listen(serverSocket,5)==0){
        printf("Listening");
    }
    else{
        printf("Error")
    }

    addr_size=sizeof(serverStorage);
    newSocket=accept(serverSocket,(struct sockaddr *)&serverStorage,&addr_size);

    recv(newSocket,fname,255,0);

    fd=open(fname,O_RDONLY);

    if(fd==-1){
        strcpy(buffer,"File not found");
        n=strlen(buffer);
    }
    else{
        n=read(fd,buffer,bufsize);
    }

    send(newSocket,buffer,n,0);

    close(newSocket);
    return close(serverSocket);
}