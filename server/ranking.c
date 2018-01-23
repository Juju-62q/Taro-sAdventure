/*
 * pygame_ranking.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 59633    // ポート番号


int main(int argc, char *argv[]) {
  int    i;
  int    connected_fd, listening_fd;
  struct sockaddr_in server_addr;
  struct sockaddr_in client_addr;
  int    len, buflen;

  while(1){
    /* リスニングソケット作成 */
    if ( ( listening_fd = socket(PF_INET, SOCK_STREAM, 0) ) < 0 ) {
      perror("*** server: socket ***");
      exit(1);
    }
    
    int reuse=1;
    setsockopt(listening_fd, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof(int)); 
    
    /* アドレスファミリ・ポート番号・IPアドレス設定 */
    bzero( (char *)&server_addr, sizeof(server_addr) );
    server_addr.sin_family = PF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(PORT);
    
    /* リスニングソケットにアドレスを割り当て */
    if ( bind( listening_fd, (struct sockaddr *)&server_addr, 
	       sizeof(server_addr) ) < 0 ) {
      perror("*** server: bind ***");
      close(listening_fd);
      exit(1);
    }
    
    
    
    /* リスニングソケット待ち受け */
    if ( listen( listening_fd, 1 ) < 0 ) {
      perror("*** server: listen ***");
      close(listening_fd);
      exit(1);
    }
    printf( "Waiting for connections from a client.\n" );
    
    /* 接続要求受け付け */
    len = sizeof(client_addr);
    if ( ( connected_fd = accept(listening_fd, 
				 (struct sockaddr *)&client_addr, &len) ) < 0 ) {
      perror("*** server: accept ***");
      close(listening_fd);
      exit(1);
    }
    close(listening_fd);
    printf( "Accepted connection.\n" );
    
    
    /* データの送受信 */
    while (1) {
      FILE *fp;
      char str[256], name[256], score[256], time[256];
      int ret;
      char buf[4096] = "";

      if((fp = fopen("ranking.txt", "r")) == NULL){
	printf("file open error\n");
	write(connected_fd, "error\0", 7);
	fclose(fp);
	close(connected_fd);
      }
      
  
      while(( ret = fscanf(fp, "%s %s %s", name, score, time)) != EOF){
	
	sprintf(str, "%s %s %s\n", name, score, time);	
	strcat(buf, str);

      }
      fclose(fp);
      
            
      printf( "<<< Sending...\n" );
      printf( "%s\n", buf);
      /* if ( write( connected_fd, buf, sizeof(buf) ) < 0 ) {
	break;
	}*/  
      //write(connected_fd, "aaaaa 100 123",200);
      write( connected_fd, buf, strlen(buf));
      close(connected_fd); 
      break;
    }
  }
}
