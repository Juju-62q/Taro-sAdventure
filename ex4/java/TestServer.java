/*
 * TestServer.java
 */
import java.io.*;
import java.util.*;
import java.net.*;

public class TestServer {

  public static void main( String[] args ) throws IOException {

    ServerSocket sSock = null;          // サーバ側のソケット
    Socket sock = null;                 // クライアント側のソケット
    int counter = 0;                    // 要求クライアントへのID番号

    // サーバスタート
    System.out.println( "Server start..." );
    sSock = new ServerSocket(50000);    // 50000番ポートをサーバとして起動

    while( true ) {
      sock = sSock.accept();    // クライアントからの接続待ち
      System.out.println( "accept..." );
      counter++;    // クライアントのID

      // スレッドの生成と起動
      ServerToClient t = new ServerToClient( sock, counter );
      t.start();
    }
  }
}

/*
 * クライアントとの通信を担当するスレッド
 */
class ServerToClient extends Thread {
  private Socket sock;
  private InputStream fin = null;        // 入力ストリーム
  private OutputStream fout = null;      // 出力ストリーム
  private BufferedReader in = null;      // 文字列入力ストリーム
  private PrintWriter out = null;        // 文字列出力ストリーム
  private int counter;                   // ID番号

  /*** コンストラクタ ***/
  public ServerToClient( Socket sock, int id ) {
    this.sock = sock;
    counter = id;
  }

  /*** run ***/
  public void run() {
    try {
      // ストリームの確立
      fin = sock.getInputStream();
      fout = sock.getOutputStream();
      in = new BufferedReader( new InputStreamReader(fin) );
      out = new PrintWriter( fout, true );

      // ID番号送信
      out.println( "counter=" + counter );  // 送信
      System.out.println( "counter=" + counter ); // ログ

      // クライアントからのメッセージ受信
      String s = "";
      StringTokenizer strToken;
      while ( s.equals("quit") == false ) {
        s = in.readLine();
        System.out.println( "accept data>" + s );

        // 確認送信
        out.println( "ok" );  // 送信
        System.out.println( "ok to counter=" + counter );  // ログ

        strToken = new StringTokenizer( s, ";" );
        while( strToken.hasMoreTokens() ) {
          s = strToken.nextToken();
        }
      }
    } catch( IOException e ) {
      System.out.println( "error" + e );
    } finally {
      try {
        // クローズ
        if ( in != null ) { in.close(); }
        if ( out != null ) { out.close(); }
        if ( fin != null ) { fin.close(); }
        if ( fout != null ) { fout.close(); }
        if ( sock != null ) { sock.close(); }
      } catch( IOException e ) {
        System.out.println( "error" + e );
      }
    }
  }
}
