var express = require('express'),
	path = require('path'),
	bodyParser = require('body-parser'),
	pg = require('pg'),
	app = express();




//DB connection
var connect = 'postgres://localhost:5432/pgguide';
var pool = new pg.Pool(connect);

//set public folder
app.use(express.static(path.join(__dirname, 'public')));

//body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false}));

app.get('/', function(req, res){
	pool.connect((err, client, done) => {
		if (err) throw err
		client.query('SELECT * FROM products', [1], (err, res) => {
			done()

			if (err) {
				console.log(err.stack)
			} else {
				console.log(res.rows[0])
			}
		})
	});
	pool.end();
});


//server
app.listen(3000, function(){
	console.log('Server Started On Port 3000');
});
