function Person(name, email, phone) {
  this.name = name;
  this.email = email;
  this.phone = phone;
}

Person.prototype.greet = function(other) {
  console.log('Hello ' + other.name + ', I am ' + this.name + '!');
};

// var sonny = new Person('Sonny', 'sonny@hotmail.com', '483-485-4948');
// var jordan = new Person('Jordan', 'jordan@aol.com', '495-586-3456');
// sonny.greet(jordan);
// jordan.greet(sonny);
// console.log(`Sonny's contact is: ${sonny.email}, ${sonny.phone}`);
// console.log(`Jordan's contact is: ${jordan.email}, ${jordan.phone}`);

class Card {
  constructor(point, suit) {
    this.point = point;
    this.suit = suit;
    this.cardImageUrl = 'images/5_of_diamonds.png';
  }
}
Card.prototype.getImageUrl = function() {
  return this.cardImageUrl;
}
var myCard = new Card(5, 'diamonds');

class Hand {
  constructor() {
    this.cards = [];
  }
  
  addCard(aCard){
    this.cards.push(aCard);
  }
  getPoints() {
    let temp = 0;
    for(let i = 0; i < this.cards.length; i++){
      temp += this.cards[i].point;
    }
    return temp;
  }
}

var myHand = new Hand();
myHand.addCard(new Card(5, 'diamonds'));
myHand.addCard(new Card(13, 'spades'));
console.log(myHand.getPoints());

