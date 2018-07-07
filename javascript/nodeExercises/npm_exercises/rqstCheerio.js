var request = require('request');
var cheerio = require('cheerio');

request('http://www.npmjs.org', function (error, response, body) {
    if(error) {
        console.error('error: ', error);
    }
    // console.log('body:', body); // Print the HTML for the npmjs.org site.
    const $ = cheerio.load(body);
    // var testing = $('.mw9 h3 a').text();
    var testing = $('.mw9 h3 a').contents();
    var popular_modules = [];
    for(let i = 0; i < testing.length; i++){
        popular_modules.push(testing[i]['data']);
    }
    console.log(popular_modules);
});