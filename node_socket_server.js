// 在前者的基础上，实现 Client --> Sever 的通讯，如此一来便是双向通讯
var net = require('net');
var chatServer = net.createServer(),
    clientList = [];

chatServer.on('connection', function(client) {
	console.log('client connected');
    // JS 可以为对象自由添加属性。这里我们添加一个 name 的自定义属性，用于表示哪个客户端（客户端的地址+端口为依据）
    client.name = client.remoteAddress + ':' + client.remotePort;
    //client.write('Hi ' + client.name + '!\n');
    clientList.push(client);

    client.on('data', function(data) {
		console.log('data=' + data);
		client.write('ack');
        //broadcast(data, client);// 接受来自客户端的信息
    });

	client.on('close', function(e) {
		console.log('close');
        console.log(e);
    });
	
    client.on('error', function(e) {
		console.log('error');
        console.log(e);
    });
});


function broadcast(message, client) {
    var cleanup = []
    for(var i=0; i<clientList.length; i+=1) {
        if(client !== clientList[i]) {

            if(clientList[i].writable) { // 先检查 sockets 是否可写
                clientList[i].write(client.name + " says " + message)
            } else {
                cleanup.push(clientList[i]) // 如果不可写，收集起来销毁。销毁之前要 Socket.destroy() 用 API 的方法销毁。
                clientList[i].destroy()
            }

        }
    }  //Remove dead Nodes out of write loop to avoid trashing loop index
    for(i=0; i<cleanup.length; i+=1) {
        clientList.splice(clientList.indexOf(cleanup[i]), 1)
    }
}

chatServer.listen(9000);

var users = {},
usocket = {};

function send_data(data) {
    if (data.to in usocket) {
        console.log('================')
        console.log('to' + data.to, data);
        usocket[data.to].emit('to' + data.to, data);
        usocket[data.user].emit('to' + data.user, data);
        console.log('================')
    }
}

function local_server_start() {
	
}

exports.local_server_start = local_server_start;

