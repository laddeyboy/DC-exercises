var fs = require('fs-promise');


function cat2files(input1, input2, outputFile) {
    var p1 = fs.readFile(input1);
    var p2 = fs.readFile(input2);
    
    Promise.all([p1, p2])
    .then(function(bufferInfo) {
        console.log(bufferInfo);
        fs.writeFile(outputFile, bufferInfo);
        console.log("File Wrote to.... ", outputFile);
    })
    .catch(function(err){
        console.log("Josh's Error-----------", err);
    });
}

cat2files('input1.txt', 'input2.txt', 'GoodOldDays.txt');