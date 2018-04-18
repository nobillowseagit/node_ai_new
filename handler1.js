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
//var socket = io.connect('http://127.0.0.1' + ':' + '5000' + '/image');
var socket = io.connect('http://127.0.0.1' + ':' + '9000' + '/image');

var socket_cla_test = io.connect('http://127.0.0.1' + ':' + '9001' + '/image');
var socket_cla_op = io.connect('http://127.0.0.1' + ':' + '9002' + '/image');



var flag_image_res = 0;
var image_res = 0;
var intResult = 0;


var flag_cla_test_res = 0;
var cla_test_res = -1;


var g_flag = 0;

var g_cla_name = '未知';
arrObj = ["错误","未知","空","空"];



var arrObj1 = [
{
    cla_id: 0,
    cla_name: "错误",
    cla_pinyin: "cuo4wu4",
    cla_map: "a",
},
{
    cla_id: 1,
    cla_name: "未知",
    cla_pinyin: "wei4zhi1",
    cla_map: "a",
},
{
    cla_id: 2,
    cla_name: "未知",
    cla_pinyin: "wei4zhi1",
    cla_map: "cat",
},
{
    cla_id: 3,
    cla_name: "未知",
    cla_pinyin: "wei4zhi1",
    cla_map: "dog",
}
];



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
	strResult = arr[image_res - 1];
    //console.log(arr[0]);
    //console.log(arr[1]);
    console.log(strResult);
	
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




function cla_train(req, res, data) {
    console.log('http cla_train enter');

    var query = url.parse(req.url, true).query;

    var cla_name = query.cla_name;
    console.log(cla_name);

    g_cla_name = cla_name;


    strCmd = 'python get_pinyin.py ' + cla_name;
    strRet = execSync(strCmd).toString();

    jsonRet = JSON.parse(strRet);
    cla_pinyin = jsonRet.ret;
    console.log(cla_pinyin);


    if (cla_name == arrObj[2]) {
        name = 'cat';
    } else if (cla_name == arrObj[3]) {
        name = 'dog';
    } else {
        if ('空' == arrObj[2]) {
            arrObj[2] = cla_name;
            name = 'cat';
        } else {
            arrObj[3] = cla_name;
            name = 'dog';
        }        
    }
    
    // if (g_flag == 0) {
    //     g_flag = 1;
    //     name = 'cat';
    // } else {
    //     g_flag = 0;
    //     name = 'dog';
    // }

    // arrObj[g_flag + 2] = cla_name;



    socket_cla_op.emit('cla_train', name);

    res.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    res.write('ok');
    res.end();
}

function cla_image(req, res, data) {
    console.log('http cla_image enter');
    
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
        //socket.emit('image_set_path', 'image1.jpg');        
        socket_cla_test.emit('cla_test', 'image1.jpg');        

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

function cla_image_res(req, res, data) {
    console.log('https cla_image_res enter');

    // socket_cla_test.emit('req_cla_test_res', 'aaa');

    if (flag_cla_test_res == 1) {
        flag_cla_test_res = 0;

        console.log("cla_test_res = ");
        console.log(cla_test_res);

        index = parseInt(cla_test_res);
        // index = index + 1;

        console.log("index = "); 
        console.log(index);

        strResult = arrObj[index];
        //strResult = cla_test_res;
        //console.log(arr[0]);
        //console.log(arr[1]);
        console.log("strResult = "); 
        console.log(strResult);
        
        if (index != 0) {
            res.writeHead(200, {
                'Content-Type': 'text/plain'
            });
            if (cla_test_res != -1) {
                res.write(strResult);
                res.end();
            } else {
                res.write('0');
                res.end();
            }
        }
    } else {
        res.writeHead(200, {
            'Content-Type': 'text/plain'
        });
        res.write('0');
        res.end(); 
    }   
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
exports.cla_image = cla_image;
exports.cla_image_res = cla_image_res;
exports.cla_train = cla_train;
exports.upload = upload;
exports.image_get_res = image_get_res;
exports.test = test;


arr = ["人","自行车","汽车","摩托车","飞机","公共汽车","火车","卡车","船","交通灯",
        "消防栓","12","停车标","停车计时器","长凳","鸟","猫","狗","马","羊",
        "牛","象","熊","斑马","长颈鹿","26","背包","雨伞","29","30",
        "手提包","领带","手提箱","飞盘","滑雪板","单板滑雪","运动球","风筝","棒球棒","棒球手套",
        "滑板","冲浪板","网球拍","瓶子","45","红酒杯","杯子","叉子","刀","勺",
        "碗","香蕉","苹果","三明治","橙子","西兰花","胡萝卜","热狗","比萨","甜甜圈",
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






socket_cla_test.on('connect', function(){
    console.log('socket_cla_test connect enter');
    });

socket_cla_test.on('res', function(data){
    console.log('socket_cla_test res enter');
    console.log(data);
});

socket_cla_test.on('cla_test_res', function(data){
    console.log('socket_cla_test cla_test_res enter');
    console.log(data);
    flag_cla_test_res = 1;
    cla_test_res = data;
});




socket_cla_op.on('connect', function(){
    console.log('socket_cla_op connect enter');
    });

socket_cla_op.on('cla_pinyin_res', function(data){
    console.log('socket_cla_op cla_pinyin_res enter');
    console.log(data);

    cla_pinyin = data;


});






