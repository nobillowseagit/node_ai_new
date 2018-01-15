var app = require('express')();
var fs = require('fs');
var http = require('http');
var https = require('https');
var privateKey  = fs.readFileSync('private.pem', 'utf8');
var certificate = fs.readFileSync('file.crt', 'utf8');
var credentials = {key: privateKey, cert: certificate};

var httpServer = http.createServer(app);
var httpsServer = https.createServer(credentials, app);
var PORT = 18080;
var SSLPORT = 18081;

var url = require("url");
var querystring = require("querystring");
var request = require('request')

var exec = require('child_process').exec;

var handle = {};
handle["/question"] = handle_question;

httpServer.listen(PORT, function() {
    console.log('HTTP Server is running on: http://localhost:%s', PORT);
});
httpsServer.listen(SSLPORT, function() {
    console.log('HTTPS Server is running on: https://localhost:%s', SSLPORT);
});

// Welcome
app.get('/', function(req, res) {
    if(req.protocol === 'https') {
        res.status(200).send('Welcome to Safety Land!');
    }
    else {
        res.status(200).send('Welcome!');
    }
});

// 接受客户端请求时触发
httpsServer.on('request', (request, response) => {
	var postData = "";
	var pathname = url.parse(request.url).pathname;
	var query  = url.parse(request.url).query;
	console.log("Request for " + pathname + " received.");
	console.log("query " + query);
	
	postData = query;
	
	route(handle, pathname, response, postData);
	
	
	/*
    if(request.url !== '/favicon.ico') {
        response.setTimeout(2 * 60 * 1000, () => {
           console.error('请求超时！');
        });
        response.on('close', () => {
            console.error('请求中断！');
        });
        let result = '';
        request.on('data', (data) => {
            result += data;
        });
		console.error('result', result);
        request.on('end', () => {
            //console.log(`服务器数据接收完毕：${result}`);
			//console.log(`服务器数据接收完毕`);

            response.statusCode = 200;
            response.write('收到!');
            response.end(); // 结束本次请求
        });
    }
	*/
});

function nlg(question) {
	var filename = 'a.py'
	exec('python'+' '+filename+' '+question+' ',function(err,stdout,stderr){
		if(err)
		{
			console.log('stderr',err);
		}
		if(stdout)
		{
			console.log(stdout);
			var astr = stdout.split('\r\n').join('');//delete the \r\n
			var obj = JSON.parse(astr);
			
			console.log('ret',obj.ret);
			
			if (obj.ret == '怎么啦') {
				console.log('有回答');
			}
		}
	});
}

//nlg('美女');



function route(handle, pathname, response, postData) {
  console.log("About to route a request for " + pathname);
  if (typeof handle[pathname] === 'function') {
    handle[pathname](response, postData);
	
	//response.statusCode = 200;
    //response.write('收到!');
    //response.end(); // 结束本次请求
   

  } else {
    console.log("No request handler found for " + pathname);
    response.writeHead(404, {"Content-Type": "text/plain"});
    response.write("404 Not found");
    response.end();
  }
}

function handle_question(res, postData) {
        console.log('get debug post data',JSON.stringify(postData));
		
		
		/*
        request.post({
                        url : 'xxx.xx.xxx',//你请求后台的链接
                        form : {
                              //params,你的请求的参数
                        }
                }, function(error, response, body) {
                        console.log('body is',body);
                        res.writeHead(200,{'Content-Type':'application/json; charset=utf8', 'Access-Control-Allow-Origin':'*', 'Accept-Language':'zh-CN'});//响应头
                        res.end(body);
                });
		*/
		

}