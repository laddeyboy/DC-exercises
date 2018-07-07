var request = require('request');
var sharp = require('sharp');
var fs = require("fs");


var options = {
  url: 'https://raw.githubusercontent.com/voodootikigod/logo.js/master/js.png',
  encoding: null
};
request(options, function(err, response, imageData) {
    if (err) {
    console.error(err.message);
    return;
    }
    sharp(imageData)
      .resize(240, 240, {
        kernel: sharp.kernel.nearest
      })
      .background('black')
      .embed()
      .toFile('reducedLogo.png')
      .then(function() {
      });
});