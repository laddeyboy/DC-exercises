var readline = require('readline');
var fs = require('fs');

var rl = readline.createInterface( { 
    input: process.stdin,
    output: process.stdout
});


rl.question("Enter a file name to open: ", function(readFile) {
    rl.question("Enter a file name to write: ", function(writeFile){
        console.log("readfile: ", readFile);
        console.log("writeFile: ", writeFile);
        
        fs.readFile(readFile, function (error, buffer) {
          if (error) {
            console.error(error.message);
            return;
          }
          fs.writeFile(writeFile, buffer.toString().toUpperCase(), function (error) {
            if (error) {
              console.error(error.message);
              return;
            }
            console.log('Text Saved In: ', writeFile);
          });
        });
        
        rl.close();
    });
});