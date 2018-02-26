var io = require('socket.io-client');
//var socket = io.connect('http://127.0.0.1' + ':' + '5010' + '/train');
var socket = io.connect('http://127.0.0.1' + ':' + '9000' + '/train');

var flag_image_res = 0;
var image_res = 0;

socket.on('connect', function(){
	console.log('connect');
	});

socket.on('event', function(data){});

socket.on('disconnect', function(){});

socket.on('my response', function(data){
	//console.log('ccc')
});

socket.on('image_send_res', function(data){	
	console.log('http res_image enter');
	console.log(data);
	flag_image_res = 1;
	image_res = data;
});




//socket.emit('image_set_path', 'image1.jpg');
//socket.emit('image_train', 'image1.jpg');
socket.emit('train_test', 'image1.jpg');

