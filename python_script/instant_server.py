#!/usr/local/bin/python3

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
```
"""

import socket
import socketserver
import http.server
import qrcode

myip = socket.gethostbyname(socket.gethostname())

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

code_img = qrcode.make('http://' + myip + ':' + str(PORT))
code_img.show()

with socketserver.TCPServer((myip, PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
