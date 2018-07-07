var lodash = require('lodash');

var cardArr = [1,2,3,4,5,6,7,8,9,10];
var shuffledCards = lodash.shuffle(cardArr);
console.log("My cards: ", cardArr);
console.log("My shuffled cards: ", shuffledCards);