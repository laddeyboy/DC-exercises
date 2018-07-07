// var requests = require('request');


// var temp = requests.get('https://en.wikipedia.org/wiki/Node.js');

// console.log(temp);

var rp = require('request-promise');

var urls = [
  'https://en.wikipedia.org/wiki/Futures_and_promises',
  'https://en.wikipedia.org/wiki/Continuation-passing_style',
  'https://en.wikipedia.org/wiki/JavaScript',
  'https://en.wikipedia.org/wiki/Node.js',
  'https://en.wikipedia.org/wiki/Google_Chrome'
];

var urlPromises = [];

for (var i = 0, l = urls.length; i < l; i++) {
    urlPromises.push(rp(urls[i]));
}

var html = [];

Promise.all(urlPromises)
    .then(function(values) {
        html = values;
        console.log(html);
        console.log("SUCCESS");
        return;
    })
    .catch(function(error) {
        console.log(error);
        console.log("ERROR");
    });