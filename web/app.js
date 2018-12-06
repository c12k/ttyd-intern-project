var express = require('express'),
	path = require('path'),
	bodyParser = require('body-parser'),
	pg = require('pg'),
	app = express();

//set public folder
app.use(express.static(path.join(__dirname, 'public')));

//body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false}));

//DB connection
// const connect = 'postgres://localhost:5432/pgguide';
const pool = new pg.Pool({
	host: 'localhost', // 'localhost' is the default;
	port: 5432, // 5432 is the default;
	database: 'pgguide',
	user: 'colin'
})

app.get('/', function (req, res) {
	console.log('App working ok');
	res.send('Hello from app.')
});

app.get('/db', function(req, res){
	pool.query('SELECT id,title FROM products where id=1;')
		.then((data) => {
			console.log(data.rows);
			res.status(200).json({status:'success',data:data, message:'Successful read'}); 
		}) 
		.catch(err => {
			console.error('Error executing query', err.stack);
			return err
		})
});

var server = app.listen(3000, function () {
	console.log('Server Started On Port 3000');
});
