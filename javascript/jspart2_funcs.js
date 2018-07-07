//Even Numbers
function positiveNumbers(arr) {
   return arr.filter(function(aNum) {
   		return aNum % 2 == 0; 
    });
}

//square the numbers
function squareTheNumbers(arr) {
   return arr.map(function(aNum) {
   		return (Math.pow(aNum, 2)); 
    });
}

//Cities
function coolCities(anObject) {
    var cities = [];
    for( var attrValue in anObject) {
        var value = anObject[attrValue].temperature;
        if(value < 70) {
            cities.push(anObject[attrValue].name);
        }
    }
    return cities;
}

//Good Job!
function goodJob(people) {
    people.map(function(person){
        console.log(`Good Job, ${person}!`)
    });
}

//Sort an Array
function sortPeople(people) {
    return people.sort();
}

//Sort an Array, 2
function sortPeopleByLength(people) {
    return people.sort(function(a, b){
        if(a.length < b.length) { return -1; }
        if(a.length > b.length) { return 1; }
        return 0;
    });
}

//3 Times
function call3Times(fun) {
    fun();
    fun();
    fun();
}

//n times
function callNTimes(num, myFunc) {
    while(num > 0) {
        myFunc();
        num --;
    }
}

//Sum an Array
function sum(arr) {
    return arr.reduce(function(total, item) {
        return total += item;
    });
}

//Acronym
function acronym(arr) {
    return arr.reduce(function(result, arrItem ){
        return result + arrItem[0].toUpperCase();
    },'') ; 
}

//BONUS: ForEach
function myForEach(arr, fun) {
    //fun is a function
    for(let i = 0; i < arr.length; i++){
        fun(arr[i].name);
    }
}

function myMap(arr, fun) {
    console.log(arr);
    for(let i = 0; i < arr.length; i++){
        arr[i] = fun(arr[i]);
    }
    return arr;
}



function main() {
    // console.log(positiveNumbers([1,2,4,5,8]));
    //console.log(squareTheNumbers([1,2,3]));
    
    var cities = [
      { name: 'Los Angeles', temperature: 60.0},
      { name: 'Atlanta', temperature: 52.0 },
      { name: 'Detroit', temperature: 48.0 },
      { name: 'New York', temperature: 80.0 }
    ];
    // console.log(coolCities(cities));
    
    var people = [
        'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista',
        'Jesslyn', 'Kevin', 'John', 'Eli',
        'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben'
    ];
    // goodJob(people);
    // console.log(sortPeople(people));
    // console.log(sortPeopleByLength(people));
    var hello = function (name) {console.log(`Hello, ${name}`);}
    // call3Times(hello);
    // callNTimes(10, hello);
    //console.log(sum([10,20,30]));
    // console.log(acronym(['very', 'important', 'person']));
    // console.log(acronym(['national', 'aeronautics', 'space', 'administration']));
    
    var arr = [
        {name: 'Bob'},
        {name: 'Alice'},
        {name: 'Joe'}
    ];
    // myForEach(arr, hello);
    // var double = function (aNum) {return aNum * 2;}
    // console.log(myMap([1,2,3], double));
    
}



//run script
main();