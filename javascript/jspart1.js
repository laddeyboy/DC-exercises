// Madlib
function madlib(name, subject) {
    return name + "'s favorite subject in school is " + subject;
}

//Tip Calculator
function tipAmount(billAmt, service) {
    switch (service) {
        case 'good':
            return billAmt * .2;
        case 'fair':
            return billAmt * .15;
        case 'bad':
            return billAmt * .1;
    }
}

//Tip Calculator 2
function tipAmount2(billAmt, service) {
    switch (service) {
        case 'good':
            return billAmt * 1.2;
        case 'fair':
            return billAmt * 1.15;
        case 'bad':
            return billAmt * 1.1;
    }
}

//Print Numbers
function printNumbersFor(start, end) {
    for(let i = start; i <= end; i++) {
        console.log(i);
    }
}
//print Numbers
function printNumbersWhile(start, end) {
    let i = start;
    while(i <= end){
        console.log(i);
        i++;
    }
}

//Print a box
function printSquare(size) {
    for(let i = 1; i < size+1; i++){
        console.log('*'.repeat(size));
    }
}

//print a box
function printBox(width, height) {
    for(let i = 1; i <= height; i++) {
        if(i === 1 || i === height) {
            console.log("*".repeat(width));
        }
        else {
            console.log('*' + ' '.repeat(width-2) + '*');
        }
    }
}

//Print a Banner
function printBanner(message) {
    console.log('*'.repeat(message.length + 4));
    console.log('* ' + message + ' *');
    console.log('*'.repeat(message.length + 4));
}

//Leetspeak
function leetspeak(message)  {
    let arr = [];
    message = message.toLowerCase();
    for(let i = 0; i < message.length; i++) {
        switch (message[i]) {
            case 'a':
                arr.push('4'); break;
            case 'e':
                arr.push('3'); break;
            case 'g':
                arr.push('6'); break;
            case 'l':
                arr.push('1'); break;
            case 'o':
                arr.push('0'); break;
            case 's':
                arr.push('5'); break;
            case 't':
                arr.push('7'); break;
            default:
                arr.push(message[i])
        }
    }
    console.log(arr.join(''));
}

//Long-long Vowels
function longLongVowels(aWord) {
    aWord = aWord.replace(/oo/,'o'.repeat(5));
    aWord = aWord.replace(/ee/, 'e'.repeat(5));
    console.log(aWord);
}

//Just the positives
function positiveNumbers(arr) {
   return arr.filter(function(aNum) {
   		return aNum > -1 
    });
}

//Ceasar Cipher 1
function ceasarCipherEncoder(message, offset) {
    console.log(message);
    message = message.toLocaleLowerCase();
    message = message.split('');
    let newMessage = message.map(function(letter){
        if(letter === ' ') { return letter; }
        else {
            let newIndex = letter.charCodeAt() + offset;
            if(newIndex < 123) { return String.fromCharCode(newIndex);}
            else {
                return String.fromCharCode(newIndex-26);
            }
        }
    });
    return newMessage.join('');
}

function ceasarCipherDecoder(message, offset) {
    console.log(message);
    message = message.toLocaleLowerCase();
    message = message.split('');
    let newMessage = message.map(function(letter){
        if(letter === ' ') { return letter; }
        else {
            let newIndex = letter.charCodeAt() - offset;
            if(newIndex >= 97) { return String.fromCharCode(newIndex);}
            else {
                return String.fromCharCode(newIndex+26);
            }
        }
    });
    return newMessage.join('');    
}

//Ceasar Cipher 2


var temp = ceasarCipherEncoder('Genius without education is like silver in the mine', 12);
console.log(temp);
console.log('---------');
var temp2 = ceasarCipherDecoder('Sqzuge iuftagf qpgomfuaz ue xuwq euxhqd uz ftq yuzq', 12);
console.log(temp2);