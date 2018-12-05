var express = require('express'),
	path = require('path'),
	bodyParser = require('body-parser'),
	pg = require('pg'),
	app = express();




//DB connection
var connect = "postgres://belle:xxl941012@localhost/sample_db";
var pool = new pg.Pool(connect);

//set public folder
app.use(express.static(path.join(__dirname, 'public')));

//body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false}));

app.get('/', function(req, res){
	pool.connect(connect, function(err,client,done) { 
		if(err) { 
			return console.error('error fetching client from pool', err); 
		} 
		client.query('SELECT * FROM userinfo', function(err, result) { 
			if(err) { 
			return console.error('error running query', err); 
		} 
		res.render('login',{userinfo: result.rows});
		done(); 
		});
	}); 
	pool.end();
});


//server
app.listen(3000, function(){
	console.log('Server Started On Port 3000');
});
