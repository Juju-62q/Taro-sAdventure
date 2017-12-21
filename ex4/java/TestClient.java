/*
 * TestClient.java
 */
import java.io.*;
//import java.lang.*;
import java.net.*;

public class TestClient {
  
  public static void main( String[] args ) throws Exception {
  
    Socket sock = null;                 // クライアント用ソケット
    InputStream fin = null;             // サーバからの入力ストリーム
    OutputStream fout = null;           // サーバへの出力ストリーム
    BufferedReader in = null;           // 文字列入力ストリーム
    PrintWriter out = null;             // 文字列出力ストリーム

    // キーボードからの入力ストリーム
    BufferedReader keyIn = 
        new BufferedReader( new InputStreamReader( System.in ) );

    if ( args.length == 2 ) {
      // ソケット接続要求
      sock = new Socket( args[0], Integer.parseInt(args[1]) );

      // ストリームの確立
      fin = sock.getInputStream();
      fout = sock.getOutputStream();
      in = new BufferedReader( new InputStreamReader( fin ) );
      out = new PrintWriter( fout, true );

      // サーバから受付番号を受信
      String myNo = in.readLine();
      System.out.println( "server:" + myNo );

      String msg = "";
      String ack = "";
      while ( msg.equals("quit") == false ) {
        // サーバにメッセージ送信
        System.out.print( "key in>" );   // プロンプト
        msg = keyIn.readLine();          // キー入力
        out.println( myNo + ";" + msg ); // 送信

        // サーバから確認を受信
        ack = in.readLine();
        System.out.println( "server:" + ack );
      }

      // クローズ
      in.close();
      out.close();
      sock.close();

    } else {
      System.out.println( "ホスト名とポート番号を指定してください" );
    }
  }
}
