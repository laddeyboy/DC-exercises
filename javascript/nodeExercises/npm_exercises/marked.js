
var fs = require('fs');
var marked = require('marked');
var mdFile = 'markedDemo.md';
var writeFile = 'mdHTML.html'

fs.readFile(mdFile, function (error, buffer) {
    if (error) {
        console.error(error.message);
        return;
    }
    var finalHTML = marked(buffer.toString());

    fs.writeFile(writeFile, finalHTML, function (error) {
        if (error) {
          console.error(error.message);
          return;
        }
        console.log('Text Saved In: ', writeFile);
    });
});