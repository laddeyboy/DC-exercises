var axios = require('axios');

var api_url = 'https://api.punkapi.com/v2/beers?brewed_before=11-2012&abv_gt=6';

// Creating my own promise -> Promise is an object
var p = new Promise(function (resolve, reject) {
  setTimeout(function () {
    reject('Hello');
  }, 3000);
});
p.then(function (value) {
  console.log('DONE: ', value);
}) 
 .catch(function (value) {
  console.log('ERROR: ', value);
});


var p1 = axios.get(api_url);
var p2 = axios.get(api_url);
Promise.all([p1, p2])
  .then(function (responses) {
    // console.log(responses);
    console.log(responses[0].data[0]);
    console.log(responses[0].data[0]);
  });