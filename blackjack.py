import random, sys

# Set up the constants
HEARTS      = chr(9829) # Character 9829 is '♥'.
DIAMONDS    = chr(9830) # Character 9830 is '♦'.
SPADES      = chr(9824) # Character 9824 is '♠'.
CLUBS       = chr(9827) # Character 9827 is '♣'.
BACKSIDE = 'backside'

def getBet(maxBet):
    '''Ask the player how much they want to bet for this round'''
    while True: # Keep asking until they enter a valid amount
        print('How much do you want to bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        
        if not bet.isdecimal():
            continue # if the player didn't enter a number, ask again

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Player entered a valid bet
        
def getDeck():
    '''Return a list of (rank, suit) tuples for all 52 cards'''
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank),suit)) # Add the numbered cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank,suit)) # Add the face and ace cards
    random.shuffle(deck)
    return deck
     
def main():
    print('''Blackjack
  
      Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')
    
    money = 5000
    while True: # Main game loop
        # Check if the player has run out of money
        if money <= 0:
            print('You\'re broke!')
            print('Good thing you weren\'t playing with real money.')
            print('Thank you for playing!')
            sys.exit()

        # Let the player enter their bet for this round
        print('Money:', money)
        bet = getBet(money)

        # Give the dealer and teacher two cards from the deck each
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]


if __name__ == "__main__":
    main()