
var addNumbers = function(x, y){
    return new Promise(function(resolve, reject){
        if (typeof x == "number" && typeof y == "number") {
            resolve(x + y);
        }
        else {
            reject('One of your inputs was not a numeral!');
        }
    });
}

addNumbers(2, 5)
  .then(function (answer) {
    console.log(answer);
  })
  .catch(function (error) {
    console.log(error);
  });
  