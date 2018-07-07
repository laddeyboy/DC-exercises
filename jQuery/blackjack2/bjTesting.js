//setup a 'card' object
function card(value, name, suit) {
    this.value = value;
    this.name = name;
    this.suit = suit;
    this.cardImage = name + '_of_' + suit + '.png';
}

//setup a 'deck' object
function deck(){
	this.names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
	this.suits = ['hearts','diamonds','spades','clubs'];
	var cards = [];
    
    for( var s = 0; s < this.suits.length; s++ ) {
        for( var n = 0; n < this.names.length; n++ ) {
            cards.push( new card( n+1, this.names[n], this.suits[s] ) );
        }
    }
    return cards;
}


function shuffleDeck(aDeck) {
    let index = 0;
    let shuffledDeck = [];
    while(aDeck.length > 0) {
        index = Math.floor((Math.random() * aDeck.length)); 
        shuffledDeck.push(aDeck[index]);
        aDeck.splice(index, 1)
    }
    return shuffledDeck;
}


function dealCard(aDeck, playerHand, dealerHand) {
}




//create a new card deck object array myDeck now has 52 unique cards in it.
var myDeck = new deck();
//shuffle the deck
myDeck = shuffleDeck(myDeck);
var playerHand = {cardsInHand: [], handValue: 0};
var dealerHand = {cardsInHand: [], handValue: 0};
//Initial Deal
playerHand.cardsInHand.push(myDeck.pop());
dealerHand.cardsInHand.push(myDeck.pop());
playerHand.cardsInHand.push(myDeck.pop());
dealerHand.cardsInHand.push(myDeck.pop());


