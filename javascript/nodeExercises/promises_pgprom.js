var pgp = require('pg-promise')({ });
//connect to our database
var db = pgp({database: 'restaurant', user: 'postgres'});

db.query('SELECT * FROM restaurant')
  .then(function (results) {
    results.forEach(function (r) {
      console.log(r.id, r.name, r.category);
    })
  })
    .catch(function(error) {
        console.error(error);
});

pgp.end();