/*
 * chat_client.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 50000    // ポート番号

int main(int argc, char *argv[]) {
  struct sockaddr_in addr;
  int    fd;
  int    buflen;
  char   buf[1024];

  if ( argc != 2 ) {
    fprintf( stderr, "Usage: %s <IP Address>\n", argv[0] );
    exit(1);
  }

  /* ソケット作成 */
  if ( ( fd = socket( PF_INET, SOCK_STREAM, 0 ) ) < 0 ) {
    perror("*** client: socket ***");
    exit(1);
  }

  bzero( (char *)&addr, sizeof(addr) );
  addr.sin_family = PF_INET;
  addr.sin_addr.s_addr = inet_addr(argv[1]);
  addr.sin_port = htons(PORT);

  /* ソケット接続要求 */
  if ( connect( fd, (struct sockaddr *)&addr, sizeof(addr) ) < 0 ) {
    perror("*** client: connect ***");
    close(fd);
    exit(1);
  }
  printf( "Connected to server.\n" );
  printf( "Input 'quit' to disconnect...\n" );

  /* データの送受信 */
  while (1) {
    buflen = read( 0, buf, sizeof(buf) - 1 );
    buf[buflen] = '\0';
    if ( strcmp( buf, "quit\n" ) == 0 ) {
      break;
    }
    printf( "<<< Sending...\n" );
    if ( write( fd, buf, buflen ) < 0 ) {
      break;
    }
    if ( ( buflen = read( fd, buf, sizeof(buf) ) ) <= 0 ) {
      break;
    }
    printf( ">>> Received.\n" );
    write( 1, buf, buflen );
  }
  
  /* ソケット切断 */
  exit( close(fd) );
}
