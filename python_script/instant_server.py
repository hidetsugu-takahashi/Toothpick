#!/usr/local/bin/python3

__author__ = "Hidetsugu Takahashi <manzyun@gmail.com>"
__version__ = "1.0.0"
__date__ = "2017-07-12"

"""
###############################
このスクリプトを起動する前に。
###############################

以下コマンドをやらないと行けないです。

```
brew install python3
pip3 install Pillow
pip3 install qrcode
chmod +x instant_server.py

で、これどんな動きするの？
------------------------------

 1. このスクリプトのあるディレクトリをルートにして、HTTPサーバーが起動します。
 2. 工程1でできたHTTPサーバーにアクセスするQRコードが生成されます。
 3. ブラウザもちゃんと起動します。


 ダブルクリックしたら動くようにしたいんだけど。
 ----------------------------------------

1. 右クリック > 情報を見る で、ファイルの情報ダイアログが表示されます。
2. 「このアプリケーションで開く:」 の項目で、「Python Launcher 3 (3.x.x)」と言うのを選択します。
3. 設定画面が出てきますが、まず
    * 「Interpreter:」 のテキストボックスを「/usr/local/bin/python3」に書き換えます。
    * 「Run in a Terminal window」のチェックボックスを外します。

これでダブルクリックで起動します。

また、
「なんかおかしい」
と思ったら、Dockに居る「Python Launcher 3」を終了してください。

```
"""

import socket
import socketserver
import http.server
import qrcode
import webbrowser

myip = socket.gethostbyname(socket.gethostname())

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

code_img = qrcode.make('http://' + myip + ':' + str(PORT))
code_img.show()

webbrowser.open('http://' + myip + ':' + str(PORT))

with socketserver.TCPServer((myip, PORT), Handler) as httpd:
    print("serving at addres" + myip + ":", PORT)
    httpd.serve_forever()
