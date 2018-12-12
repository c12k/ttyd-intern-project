var http = require("http"),
	url = require("url"),
	qs = require("querystring"),
	fs = require("fs");

http.createServer(function (req, res) {

	var pathname = url.parse(req.url).pathname;

	console.log("Request for" + pathname + "received.");

	fs.readFile(pathname.substr(1), function(err, data){
		if (err){
			console.log(err);
			//404 means not found
			res.writeHead(404, {'Content-Type':'text/html'});

		}else {

			//200 means ok 
			res.writeHead(200, {'Content-Type': 'text/html'});
			res.write(data.toString());
		}
		res.end();
	});

}).listen(8080);

console.log('Server running at http://127.0.0.1:8080/');

