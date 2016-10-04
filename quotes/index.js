var express = require('express');
var app = express();
var pug = require('pug');
var fs = require('fs');

fs.readFile(__dirname + '/../styles/style.css', 'utf8', function (err, data) {
	if (err) {
		return console.log(err);
	}
	stylesheet = data;	
});

const exec = require('child_process').exec;
exec('python3 ' + __dirname + '/../scripts/make_pug.py',
	(error, stdout, stderr) => {
		if (error) {
			console.error(`exec error: ${error}`);
			return;
		}
		console.log(`stdout: ${stdout}`);
		console.log(`stderr: ${stderr}`);
	});


app.use('/styles', express.static(__dirname + '/../styles/'));

app.use('/', function(req, res) { 
	res.send(pug.renderFile(__dirname + '/../static/quotes.pug', { pretty: true, cache: true }));
});

app.listen(5411, function() {
	console.log('listening...'); 
});
