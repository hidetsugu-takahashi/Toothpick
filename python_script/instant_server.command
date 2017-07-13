#!/usr/local/bin/python3

__author__ = "Hidetsugu Takahashi <manzyun@gmail.com>"
__version__ = "1.0.0"
__date__ = "2017-07-12"

"""
###############################
このスクリプトを起動する前に。
###############################

一緒に付いてきてる、
「build_environment.command」
を実行してください。

1. 右クリックメニュー > 開く をクリックします
2. 「開発元は未確認です。開いてもよろしいですか？」の旨のダイアログが出てきますので、「開く」をクリック

環境構築できた後は、このプログラムを実行してください。

で、これどんな動きするの？
------------------------------

 1. このスクリプトのあるディレクトリをルートにして、HTTPサーバーが起動します。
 2. 工程1でできたHTTPサーバーにアクセスするQRコードが生成されます。
 3. ブラウザもちゃんと起動します。


 ダブルクリックしたら動くようにしたいんだけど。
 ----------------------------------------

1. 右クリックメニュー > 開く をクリックします
2. 「開発元は未確認です。開いてもよろしいですか？」の旨のダイアログが出てきますので、「開く」をクリック

これでダブルクリックで起動します。
"""

import os
import socket
import socketserver
import http.server
import qrcode
import webbrowser

myip = socket.gethostbyname(socket.gethostname())

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

code_img = qrcode.make('http://' + myip + ':' + str(PORT))
code_img.show()

os.chdir(os.path.expanduser('~') + '/Desktop/net/')

webbrowser.open('http://' + myip + ':' + str(PORT))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(myip + ":" + str(PORT) + "に接続すると、閲覧できます。")
    print("このサービスを終了するときは、この画面を閉じてください。")
    print("以下、ログです。")
    print("8<--------------------------------------------------")
    httpd.serve_forever()

