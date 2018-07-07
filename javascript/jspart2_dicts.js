// Dictionary Example
var phonebookDict = {
  Alice: '703-493-1834',
  Bob: '857-384-1234',
  Elizabeth: '484-584-2923'
}

function exercise1() {
    console.log(phonebookDict.Elizabeth);
    
    phonebookDict.Kareem = '938-489-1234';
    console.log(phonebookDict.Kareem);
    
    delete phonebookDict.Alice;
    console.log(phonebookDict.Alice);
    
    phonebookDict.Bob = '968-345-2345';
    console.log(phonebookDict.Bob);
    
    var personName = 'Elizabeth';
    console.log(phonebookDict[personName]);
    
    console.log("Here is your Phonebook");
    for (var name in phonebookDict) {
        console.log(`${name}: ${phonebookDict[name]}`)
    }
}

function letterHistogram(message) {
    let histogram = {};
    for (let i = 0; i < message.length; i++){
        if(histogram.hasOwnProperty(message[i])) {
            histogram[message[i]] += 1;
        }
        else {
            histogram[message[i]] = 1;
        }
    }
    console.log(Object.entries(histogram));
}

function main() {
    // exercise1();
    letterHistogram('bananas');
}

//start program
main()