/*
 * chat_server.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define NUM 20
#define PORT 59634  /* ポート番号 */

int main( void ) {
  int    i;
  int    connected_fd, listening_fd;
  struct sockaddr_in server_addr;
  struct sockaddr_in client_addr;
  int    len, buflen;
  char   buf[1024];

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
    /*if ( ( buflen = read( connected_fd, buf, sizeof(buf) ) ) <= 0 ) {
      break;
      }*/
    buflen = read( connected_fd, buf, sizeof(buf));
    printf( ">>> Received (size:%d).\n", buflen );
    
    char *new;
    char *score;
    char *time2;

    new=strtok(buf," ");
    score=strtok(NULL," ");
    int newscore;
    newscore=atoi(score);
    
    time2=strtok(NULL," ");
    // int newtime;
    //newtime=atoi(time2);

    //ranking読込み
    FILE *fp=fopen("ranking.txt","r");
    int scores[NUM];
    char name[NUM][100];
    char time[NUM][100];
    int i,j;
    /*
      for(i=0;i<NUM;i++){
      fscanf(fp,"%s %d %d",&name[i],&scores[i],&time[i]);
      //printf("%s,%d,%d\n",name[i],scores[i],time[i]);
      }
    */
    int ret;
    int count=0;
    while((ret=fscanf(fp,"%s %d %s",&name[count],&scores[count],&time[count]))!=EOF){
      count++;
      //printf("%d\n",count);
    }
    fclose(fp);
    
    int yourranking; 
    //ランキングに入れるかどうか
    if(scores[count-1]>newscore){  
      char haihun[2]="-";    
      if ( write( connected_fd,haihun, 2) < 0 ) {
	break;
      }
      break;
    }
    
    //ranking入れ替え
    else{
      //sort
      for(i=0;i<NUM;i++){
	if(scores[i]<newscore){
	  //この自転でのi+1を入れといてこれwrite
	  yourranking=i+1;
	  for(j=NUM-1;j>i;j--){
	    strcpy(name[j],name[j-1]);
	    scores[j]=scores[j-1];
	    strcpy(time[j],time[j-1]);
	  }
	  strcpy(name[i],new);
	  scores[i]=newscore;
	  strcpy(time[i],time2);
	  
	  break;
	}
      }
    
      //ranking.txtの書き換え
      FILE *fp2=fopen("ranking.txt","w");
      for(i=0;i<NUM;i++){
	fprintf(fp,"%s %d %s\n",name[i],scores[i],time[i]);
      }
      
      fclose(fp2);
      
      
      write( 1, buf, buflen );
      printf( "<<< Sending...\n" );
      char bufret[100];
      strcpy(bufret,"");
      sprintf(bufret,"%d",yourranking);
      if ( write( connected_fd, bufret, 100) < 0 ) {
	break;
      }
      break;
    }
  }
  /* ソケット切断 */
  //exit( close(connected_fd) );
  close(connected_fd);
  }
}
