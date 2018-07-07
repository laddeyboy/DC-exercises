var pgp = require("pg-promise")({
    //initialization options are available
});
var prompt = require("prompt-promise");

var db = pgp({database: 'restaurant', user: 'postgres'});

var dbInfo = [];
//restaurant schema [id-> name -> distance -> stars -> category -> favdish -> takeout -> lastvisit]
//Create Restaurant
prompt("Restaurant Name: ")
    .then(function restName(val){
        dbInfo.push(val);
        return prompt("Stars: ");
    })
    .then(function stars(val) {
        dbInfo.push(val);
        return prompt("Category: ");
    })
    .then(function restCategory(val){
        dbInfo.push(val);
        prompt.done();
        return db.result('INSERT INTO restaurant (id, name, stars, category) VALUES(default, $1, $2, $3)', [dbInfo[0], dbInfo[1], dbInfo[2]]);
    })
    .then(function(dbValues) {
        console.log("data has been saved to the database!");
        pgp.end();
    })
    .catch(function (error){
        console.error("Error", error);
        prompt.finish();
    })
