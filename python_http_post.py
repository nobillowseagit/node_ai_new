import ssl
import Properties
from httplib import HTTPSConnection
import base64

def send(path):
    port = Properties.SSLPORT
    host = Properties.HOST
    url = host + ":" + str(port) + path
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.load_cert_chain(Properties.PRIVATE_KEY, **{"password":Properties.PASSWORD})

    data = '123'
    httpsConn = HTTPSConnection(host, port, None, None, "", 60000, "", context)
    httpsConn.request("POST", path, data, {"Authorization": "Basic " + base64.encodestring("12345678")})
    res = httpsConn.getresponse()
    print res.status,res.reason, res.getheaders(), res.read()

if __name__=="__main__":
    """
    httpsConn = httplib.HTTPSConnection("www.baidu.com")
    httpsConn.request("GET", "/")
    res = httpsConn.getresponse()
    print res.status, res.reason, len(res.read())
    """
    send("/post")