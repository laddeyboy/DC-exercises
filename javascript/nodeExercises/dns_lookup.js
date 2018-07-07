var readline = require('readline');
var dns = require('dns');

var rl = readline.createInterface( { 
    input: process.stdin,
    output: process.stdout
});


rl.question("Enter a Domain Name: ", function(domainName) {
    dns.lookup(domainName, function(err, addresses, family){
        if(err){
            console.error("You have entered an invalid domain name.");
            return;
        }
        console.log("IP:", addresses);
    });
  rl.close();
});