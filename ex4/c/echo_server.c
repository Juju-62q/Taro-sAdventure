/*
 * chat_server.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 50000  /* ポート番号 */

int main( void ) {
  int    i;
  int    connected_fd, listening_fd;
  struct sockaddr_in server_addr;
  struct sockaddr_in client_addr;
  int    len, buflen;
  char   buf[1024];

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
    if ( ( buflen = read( connected_fd, buf, sizeof(buf) ) ) <= 0 ) {
      break;
    }
    printf( ">>> Received (size:%d).\n", buflen );
    write( 1, buf, buflen );
    printf( "<<< Sending...\n" );
    if ( write( connected_fd, buf, buflen ) < 0 ) {
      break;
    }
  }

  /* ソケット切断 */
  exit( close(connected_fd) );
}
