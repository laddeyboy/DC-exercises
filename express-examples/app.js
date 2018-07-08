var express = require('express');
var app = express();
var nunjucks = require('nunjucks');

nunjucks.configure('views', {
  autoescape: true,
  express: app,
  noCache: true
});

app.get('/', function (request, response) {
  response.send('Hello World!');
});

app.get('/cats', function (request, response){
  response.send('MEOW');
})
app.get('/dogs', function (request, response){
  response.send('WOOF');
})
app.get('/cats_and_dogs', function (request, response){
  response.send('Living together');
})

function getBirthYear(age){
  var currentYear = new Date().getFullYear();
  return currentYear - age;
}

app.get('/greet/:slug', function (req, resp) {
  var slug = req.params.slug;
  var birthYear = getBirthYear(req.query.age);
  var context = {name: slug, birthYear: birthYear};
  resp.render('index.html', context);
})

app.get('/year', function (req, resp) {
  var birthYear = getBirthYear(req.query.age);
  resp.send(`You were born in ${birthYear}`);
})

var manga = [
  {name: 'Naruto', favorite: true},
  {name: 'Bleach', favorite: true},
  {name: 'One Piece', favorite: false},
  {name: 'Death Note', favorite: false},
  {name: 'Dragon Ball Z', favorite: true},
  ]
  
app.get('/fav_manga', function (req, resp) {
  var names = [];
  for(let i = 0; i < manga.length; i++) {
    if(manga[i]['favorite'] == true) {
      names.push({name: manga[i]['name']});
    }
  }
resp.render('manga.html', {names: names});
})

app.listen(8080, function () {
  console.log('Listening on port 8000');
});