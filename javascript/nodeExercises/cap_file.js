var fs = require('fs');
var filename = 'file1.txt'
fs.readFile(filename, function (error, buffer) {
  if (error) {
    console.error(error.message);
    return;
  }
  console.log('File Data: ', buffer.toString().toUpperCase());
});