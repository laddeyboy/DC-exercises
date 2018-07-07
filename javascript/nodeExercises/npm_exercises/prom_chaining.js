var rqst_promises = require('request-promise');
var fs_promises = require('fs-promise');

function saveWebPage(url, filename) {
    rqst_promises(url)
        .then(function(htmlString){
            console.log("Received HTML...");
            return(htmlString);
        })
        .then(function(htmlString) {
            fs_promises.writeFile(filename, htmlString);
            console.log("File Wrote to.... ", filename);
        })
        .catch(function(error){
            console.log("Josh's Error-----------", error);
        });
}


saveWebPage('https://nodejs.org/en/about', 'TEMP.html');