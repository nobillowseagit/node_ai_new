
var exec = require('child_process').exec;
var deasync = require('deasync');

/*
strCmd = 'python aaa.py image1.jpg';
strRet = exec(strCmd, function(err, stdout, stderr) {
	console.log('lijia '+ stdout);

	strRet = stdout;
	index = strRet.indexOf('ret=');
    strResult = strRet.slice(index + 4);
    console.log(strResult);
});
deasync.sleep(1000);  
*/


var server = require("./server");
var router = require("./router");
var handler = require("./handler1");
var handle = {};

handle["/get_data"] = handler.get_data;
handle["/upload"] = handler.upload;
handle["/test"] = handler.test;
handle["/image"] = handler.image;
handle["/image_get_res"] = handler.image_get_res;


server.start(router.route, handle);



var net = require('net');
var HOST = '127.0.0.1';
var PORT = 6600;

var client = new net.Socket();

/*
client.connect(PORT, HOST, function() {
    console.log('CONNECTED TO: ' + HOST + ':' + PORT);
    // 建立连接后立即向服务器发送数据，服务器将收到这些数据 
    //client.write('I am Chuck Norris!');
    client.write("d:\\node\\image1.jpg");
    console.log("write end");
    
    aaa = client.read(1024);
    console.log(aaa);
});

client.on('data', function(data) {

    console.log('DATA: ' + data);
    // 完全关闭连接
    client.destroy();

});

// 为客户端添加“close”事件处理函数
client.on('close', function() {
    console.log('Connection closed');
});
*/

client.on('data', function(data) {

    console.log('DATA: ' + data);
    // 完全关闭连接
    client.destroy();

});

function aaa() {
	client.connect(PORT, HOST, function() {
	    console.log('CONNECTED TO: ' + HOST + ':' + PORT);
	    // 建立连接后立即向服务器发送数据，服务器将收到这些数据 
	    //client.write('I am Chuck Norris!');
	    client.write("d:\\node\\image1.jpg");
	    console.log("write end");
	    
	    //aaa = client.read(1024);
	    //console.log(aaa);
	});

	client.on('data', function(data) {
		console.log('DATA: ' + data);
    	// 完全关闭连接
    	client.destroy();
    });	
}




/*
var PORT_CLIENT;
var server = net.createServer();

var sockets = [];  
var aaa;
var msg;
var rcv = 0;
var res;

server.listen(PORT, HOST);

server.on('connection', function(sock) {
	console.log('connection enter');
	sockets.push(sock);
	aaa = sock;



	    //从连接中读取数据  
    sock.on('data', function(data){  
        console.log('got data:', data);  
  		
  		msg = data;
  		console.log(data);
  		res.writeHead(200, {
        	'Content-Type': 'text/plain'
    	});
    	res.write("ok");
    	res.end();

    });


    //删除被关闭的连接  
    sock.on('close', function(data){  
        console.log('connection closed');  
        var index = sockets.indexOf(sock);  
        sockets.splice(index, 1);

        res.writeHead(200, {
        	'Content-Type': 'text/plain'
    	});
    	res.write("ok");
    	res.end();  
    });

    //设置超时时间
  	sock.setTimeout(1000 * 600, function() {
    	console.log('客户端在' + waitTime + 's内未通信，将断开连接...');
  	});  
});

server.on('error', function(err){  
    console.log('Server error:', err.message);  
});  
  
server.on('close', function(){  
    console.log('Server closed');  
});
*/


function sendToDetect(msg) {
	console.log('sendToDetect enter');
	client.write(msg);
}

function recvFromDetect(cb) {
	console.log('recvFromDetect enter');
	while(1) {
		a = client.read(1024);
		if (null != a) {
			break;
		}
		deasync.sleep(100);
	}
	console.log(a);
	return a;
}

exports.sendToDetect = sendToDetect;
exports.recvFromDetect = recvFromDetect;
exports.aaa = aaa;






