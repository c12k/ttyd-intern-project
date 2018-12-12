
var express = require('express'),
	path = require('path'),
	bodyParser = require('body-parser'),
	pg = require('pg'),
    ejs = require('ejs'),
    uuid = require('uuid'),
	app = express();


//DB connection
//const connect = 'postgres://localhost:5432/sample_db'
const pool = new pg.Pool({
	host:'localhost', // by default;
	port: 5432, //default;
	database: 'sample_db',
	user:'belle'
})

//view engine setup
app.set('views', path.join(__dirname,'views'));

app.engine('.html',ejs.__express);
app.set('view engine', 'html');

//DB connection
//set public folder
app.use(express.static(path.join(__dirname, 'public')));

//body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false}));


app.get('/', function (req, res) {
	console.log('enter index page');
	res.render('index');
});
app.get('/register', function (req, res) {
	console.log('enter register page');
	res.render('register');
});

app.get('/db', function(req, res){
	pool.query("SELECT * FROM products;")
		.then((data) => {
			console.log(data.rows);
			res.status(200).json({status:'success',data:data, message:'Successful read'}); 
		}) 
		.catch(err => {
			console.error('Error executing query', err.stack);
			return err
		})
});

app.post('/add', function(req, res){
    var ID = uuid.v1();
	pool.query("INSERT INTO userinfo(username, email, password, userid)VALUES($1,$2,$3,$4);",[req.body.username, req.body.email, req.body.password, ID])
		.then((data) => {
        res.render('index');
        console.log('update database');            
		}) 
		.catch(err => {
			console.error('Error executing query', err.stack);
			return err
		})
});
//
////get products by id(doesn't work now)
//app.get('/db/:id', function(req, res){
//	pool.query("SELECT * FROM products WHERE id = " + req.params.id + ";")
//		.then((data) => {
//			console.log(data.rows);
//			res.status(200).json({status:'success',data:data, message:'Successful read'}); 
//		}) 
//		.catch(err => {
//			console.error('Error executing query', err.stack);
//			return err
//		})
//});
//
////delete items from product
//app.delete('/db/delete', function(req, res){
//	console.log('delete!')
//	pool.query("DELETE FROM products WHERE id = 1 ;")
//		.then((data) => {
//			console.log(data.rows);
//			res.send('delete successful')
//		}) 
//		.catch(err => {
//			console.error('Error executing query', err.stack);
//			return err
//		})
//});


//server
app.listen(3000, function(){
	console.log('Server Started On Port 3000');
});
