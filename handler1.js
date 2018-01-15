var querystring = require('querystring');
var fs = require('fs');
var util = require('util');
var formidable = require('formidable');
var execSync = require('child_process').execSync;
var url = require('url');

var index = require("./index");



//socket io client
console.log('socket io client start');
var io = require('socket.io-client');
var socket = io.connect('http://127.0.0.1' + ':' + '5000' + '/image');

var flag_image_res = 0;
var image_res = 0;
var intResult = 0



function get_data(req, res, data) {
    console.log('http get_data enter');

	var query = url.parse(req.url, true).query;

    var question = query.question;
    console.log(question);

    strCmd = 'python nlg.py ' + question;
    strRet = execSync(strCmd).toString();

    jsonRet = JSON.parse(strRet);
    answer = jsonRet.ret;
    console.log(answer);

    res.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    res.write(answer);
    res.end();
}

function image_get_res(req, res, data) {
    console.log('https image_get_res enter');

	//socket.emit('image_get_path', 'image1.jpg');
	strResult = arr[image_res];
	
	if (flag_image_res == 1) {
		flag_image_res = 0;
		res.writeHead(200, {
			'Content-Type': 'text/plain'
		});
		res.write(strResult);
		res.end();
	} else {
		res.writeHead(200, {
			'Content-Type': 'text/plain'
		});
		res.write('0');
		res.end();		
	}	
}

function upload(req, res, data) {
    console.log('upload enter');
	
	//send message to python server
	/*
	socket.emit('set_image', 'image1.jpg');

	flag_image_res = 0;
	res.writeHead(200, {
		'Content-Type': 'text/plain'
	});
	res.write('ok');
	res.end();
	*/


    var form = new formidable.IncomingForm();
    form.uploadDir = __dirname;
    form.encoding = 'utf-8';  
    form.keepExtensions = true;
    form.maxFilesSize = 8 * 1024 * 1024;

    form.on('field', function(name, val){  
	    console.log('field enter');
    });  
  
    form.on('file', function(name, file){  
	    console.log('file enter');
	    console.log(file.path);
	    console.log(file.name);
        fs.renameSync(file.path, 'image1.jpg');

        /*
        strCmd = 'python aaa.py image1.jpg';
        strRet = execSync(strCmd).toString();
		strRet = strRet.replace(/[\r\n]/g,"");        

        index = strRet.indexOf('ret=');
        intResult = strRet.slice(index + 4);
        console.log(intResult);
        strResult = arr[intResult];
        console.log(strResult);
		*/
		
		flag_image_res = 0;
		socket.emit('image_set_path', 'image1.jpg');		

    	res.writeHead(200, {
        	'Content-Type': 'text/plain'
    	});
    	res.write('ok');
    	res.end();
    });  
    
    form.on('end', function() {  
	    console.log('end enter');
    });    

    form.parse(req, function(error, fields, files) {
        console.log('parsing enter');
    });
}


function test(req, res, data) {
    console.log('test enter');

    //index.sendToDetect("d:\\node\\image1.jpg");

    //r = index.recvFromDetect();
    //console.log(r);
    index.aaa();

    res.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    res.write("ok");
    res.end();
}

	
exports.get_data = get_data;
exports.upload = upload;
exports.image_get_res = image_get_res;
exports.test = test;


arr = ["人","自行车","汽车","摩托车","飞机","公共汽车","火车","卡车","船","交通灯",
        "消防栓","12","停车标","停车计时器","长凳","鸟","猫","狗","马","羊",
        "牛","象","熊","斑马","长颈鹿","26","背包","雨伞","29","30",
        "手提包","领带","手提箱","飞盘","滑雪板","单板滑雪","运动球","风筝","棒球棒","棒球手套",
        "滑板","冲浪板","网球拍","瓶子","45","红酒杯","杯子","叉子","刀","勺",
        "碗","香蕉","苹果","三明治","55","橙子","西兰花","胡萝卜","热狗","比萨","甜甜圈",
        "蛋糕","椅子","长椅","盆栽","床","66","餐桌","68","69","厕所",
        "71","电视","笔记本电脑","鼠标","遥控器","键盘","手机","微波炉","烤箱","面包机",
        "水槽","冰箱","83","书","时钟","花瓶","剪刀","泰迪熊","吹风机","牙刷"];

function image(req, res, data) {
    console.log('image enter');


    res.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    res.write("ok");
    res.end();
}

exports.image = image;





socket.on('connect', function(){
    console.log('connect');
    });


socket.on('event', function(data){});

socket.on('disconnect', function(){});

//socket.emit('set_image', 'image1.jpg');

socket.on('my response', function(data){
    //console.log('ccc')
});

socket.on('image_send_res', function(data){
    console.log('socketio image_send_res enter');
    console.log(data);
    flag_image_res = 1;
    image_res = data;
});

socket.on('image_res', function(data){
    console.log('socketio image_res enter');
    console.log(data);
    flag_image_res = 1;
    image_res = data;
});

socket.on('res', function(data){
    console.log('socketio res enter');
    console.log(data);
});



