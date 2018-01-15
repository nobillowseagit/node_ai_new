var http = require("http");
var url = require("url");
var https = require('https');
var fs = require('fs');
var privateKey  = fs.readFileSync('private.pem', 'utf8');
var certificate = fs.readFileSync('file.crt', 'utf8');
var credentials = {key: privateKey, cert: certificate};

function start(route, handle) {
  function onRequest(request, response) {
    var postData = "";
    var pathname = url.parse(request.url).pathname;
    var getData  = url.parse(request.url).query;
    console.log("Request for " + pathname + " received.");
    //request.setEncoding("utf8");
    
	/*
	request.addListener("data", function(postDataChunk) {
      postData += postDataChunk;
      //console.log("Received POST data chunk '"+ postDataChunk + "'.");
    });
    request.addListener("end", function() {
      if(postData == ""){
           postData = getData;
      }
      route(handle, pathname, request, response, postData);
    });
	*/
	
	route(handle, pathname, request, response, postData);
  }
  //http.createServer(onRequest).listen(8888);//当你成功滴时候，你的数据在这里。
  //https.createServer(credentials, onRequest).listen(8888)
  http.createServer(onRequest).listen(8888)
  console.log("Server has started.");
}

exports.start = start;
