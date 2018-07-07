function add (x, y, callback){
    setTimeout(function() {
        var result = x + y;
        callback(result);
    }, 1000);
}

function subtract(x, y, callback) {
    setTimeout(function() {
        var result = x - y;
        callback(result);
    }, 1000);
}

function greeting(person, callback) {
    setTimeout(function() {
        var result = 'Hola, ' + person;
        callback(result);
    }, 1000);
}


function main() {
    add(1,2, function(result) {console.log(`Addition is ${result}`); });
    subtract(2,4, function(result) {console.log(`Subtraction is ${result}`)});
    greeting('Jesus', function(result){console.log(`Greeting ${result}`)});
}


main()
