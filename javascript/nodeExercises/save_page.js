var readline = require('readline');
var dns = require('dns');
var fs = require('fs');
var request = require('request');

var rl = readline.createInterface( { 
    input: process.stdin,
    output: process.stdout
});


rl.question("Enter a URL: ", function(url) {
    request.get(url, function (error, response, html) {
        if (error) {
            console.error(error.message);
            return;
        }
        rl.question("Enter a file name to write: ", function(writeFile){
            rl.close();
            fs.writeFile(writeFile, html, function (error) {
                if (error) {
                  console.error(error.message);
                  return;
                }
                console.log('Text Saved In: ', writeFile);
            });
        });
    });
});