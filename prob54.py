# Poker Hands
import functools
from collections import Counter
from enum import Enum

@functools.total_ordering
class HandValue(Enum):
    STRAIGHT_FLUSH = 9
    QUADS = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    TRIPS = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH_CARD = 1

    def __lt__(self,other):
        return(self.value < other.value)

class Suits(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

@functools.total_ordering
class StraightFlush():
    def __init__(self,cards):
        self.cards = cards
        self.value = HandValue.STRAIGHT_FLUSH
    def __eq__(self,other):
        return(max([x.number for x in self.cards]) == max([x.number for x in other.cards]))
    def __lt__(self,other):  
        return(max([x.number for x in self.cards]) < max([x.number for x in other.cards]))
    def __str__(self):
        return("Straight Flush")

@functools.total_ordering
class Flush:
    def __init__(self,cards):
        self.cards = cards
        self.value = HandValue.FLUSH
    def __eq__(self,other):
        
        return(max([x.number for x in self.cards]) == max([x.number for x in other.cards]))
    def __lt__(self,other):
        
        return(max([x.number for x in self.cards]) < max([x.number for x in other.cards]))
    def __str__(self):
        return("Flush")

@functools.total_ordering
class Straight:
    def __init__(self,cards):
        self.cards = cards
        self.value = HandValue.STRAIGHT
    def __eq__(self,other):
        
        return(max([x.number for x in self.cards]) == max([x.number for x in other.cards]))
    def __lt__(self,other):
        
        return(max([x.number for x in self.cards]) < max([x.number for x in other.cards]))
    def __str__(self):
        return("Straight")

@functools.total_ordering
class Quads:
    def __init__(self,cards):
        self.cards = cards
        self.value = HandValue.QUADS
    def __eq__(self,other):  
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        return(self_card_values == other_card_values)
    def __lt__(self,other):
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        if(self_card_values[0] < other_card_values[0] or self_card_values[1] < other_card_values[1]):
            return(True)
        else:
            return(False)
    def __str__(self):
        return("Quads")

@functools.total_ordering
class FullHouse:
    def __init__(self,cards):
            self.cards = cards
            self.value = HandValue.FULL_HOUSE
    def __eq__(self,other):
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        return(self_card_values == other_card_values)

    def __lt__(self,other):
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        if(self_card_values[0] < other_card_values[0] or self_card_values[1] < other_card_values[1]):
            return(True)
        else:
            return(False)
    def __str__(self):
        return("Full House")

@functools.total_ordering
class Trips:
    def __init__(self,cards):
            self.cards = cards
            self.value = HandValue.TRIPS
    def __eq__(self,other):
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        if(self_card_values[0] == other_card_values[0]):
            # The trips themselves are the same, check high card next
            if(max(self_card_values[1:3]) == max(other_card_values[1:3])):
                return(True)
        return(False)
    def __lt__(self,other):
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        
        # Check trip value
        if(self_card_values[0] < other_card_values[0]):
            return(True)
        # Check high cards
        elif(self_card_values[0] == other_card_values[0]):
            if(self_card_values[1] < other_card_values[1]):
                return(True)
            if(self_card_values[1] == other_card_values[1]):
                if(self_card_values[2] < other_card_values[2]):
                    return(True)
        return(False)
    def __str__(self):
        return("Trips")

@functools.total_ordering
class TwoPair:
    def __init__(self,cards):
        self.cards = cards
        self.value = HandValue.TWO_PAIR
    def __eq__(self,other):
        
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        # Check pairs
        if(sorted(self_card_values[0:2],reverse=True) == sorted(other_card_values[0:2],reverse=True)):
            # Check high card
            if(self_card_values[2] == other_card_values[2]):
                return(True)
        return(False)
    def __lt__(self,other):
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        # Check highest pair
        if(max(sorted(self_card_values,reverse=True)[0:2]) < max(sorted(other_card_values,reverse=True)[0:2])):
            return(True)
        if(max(sorted(self_card_values,reverse=True)[0:2]) == max(sorted(other_card_values,reverse=True)[0:2])):
            # Check second pair
            if(min(sorted(self_card_values,reverse=True)[0:2]) < min(sorted(other_card_values,reverse=True)[0:2])):
                return(True)
            if(min(sorted(self_card_values,reverse=True)[0:2]) == min(sorted(other_card_values,reverse=True)[0:2])):
                if(self_card_values[2] < other_card_values[2]):
                    return(True)
        return(False)
    def __str__(self):
        return("Two Pair")

@functools.total_ordering
class Pair:
    def __init__(self,cards):
        self.cards = cards
        self.value = HandValue.PAIR
    def __eq__(self,other):
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        # Check pair
        if(sorted(self_card_values,reverse = True)[0] == sorted(other_card_values,reverse = True)[0]):
            # Check high card
            if(sorted(self_card_values,reverse=True)[1:4] == sorted(other_card_values,reverse=True)[1:4]):
                return(True)
        return(False)
    def __lt__(self,other):
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        # Check pair
        if(self_card_values[0] < other_card_values[0]):
            return(True)
        if(self_card_values[0] == other_card_values[0]):
            # Check high cards
            for i in range(1,4):
                if(self_card_values[i] < other_card_values[i]):
                    return(True)
                elif(self_card_values[i] > other_card_values[i]):
                    return(False)
        return(False)
    def __str__(self):
        return("Pair")

@functools.total_ordering
class HighCard:
    def __init__(self,cards):
        self.cards = cards
        self.value = HandValue.HIGH_CARD
    def __eq__(self,other):
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]
        if(self_card_values == other_card_values):
            return(True)
        return(False)
    def __lt__(self,other):
        self_card_values = [x[0].number for x in Counter(self.cards).most_common()]
        other_card_values = [x[0].number for x in Counter(other.cards).most_common()]

        for i in range(0,5):
            if(self_card_values[i] < other_card_values[i]):
                return(True)
                 
            elif(   self_card_values[i] > other_card_values[i]):
                return(False)
        return(False)
    def __str__(self):
        return("High Card")

@functools.total_ordering
class Card:
    def __init__(self,number,suit):
        if(number == "T"):
            self.number = 10
        elif(number == "J"):
            self.number = 11
        elif(number == "Q"):
            self.number = 12
        elif(number == "K"):
            self.number = 13
        elif(number == "A"):
            self.number = 14
        else:
            self.number = int(number)

        if(suit == "C"):
            self.suit = Suits.CLUBS
        elif(suit == "D"):
            self.suit = Suits.DIAMONDS
        elif(suit == "H"):
            self.suit = Suits.HEARTS
        elif(suit == "S"):
            self.suit = Suits.SPADES
        else:
            raise ValueError("Invalid Suit")
    def __eq__(self,other):
        return(self.number == other.number)
    def __lt__(self,other):
        return(self.number < other.number)
    def __hash__(self):
        return(hash((self.number,self.suit)))
    def __str__(self):
        return("{} of {}".format(self.number,self.suit))

@functools.total_ordering
class Hand:
    def __init__(self,cards):
        if len(cards) != 5:
            raise RuntimeError("Incorrect number of cards in hand")
        self.cards = cards
        # These get a little confusing, but remember type is an object and value is an enum
        self.handType = self.handType()
        self.handValue = self.handType.value
    def __eq__(self,other):
        return((self.handValue == other.handValue) and (self.handType == other.handType))
    def __lt__(self,other):
        if(self.handValue < other.handValue):
            return(True)
        if(self.handValue == other.handValue):
            return (self.handType < other.handType)
        return(False)

    def __str__(self):
        return("Hand is a {}".format(self.handType))

    def isStraightFlush(self):
        if(self.isStraight() and self.isFlush()):
            return(True)
        else:
            return(False)

    def isStraight(self):
        sorted_nums = sorted([x.number for x in self.cards])
        for i in range(0,len(sorted_nums)-1):
            if(sorted_nums[i] != sorted_nums[i+1]-1):
                return(False)
        return(True)

    def isFlush(self):
        suits = set([x.suit for x in self.cards])
        if(len(suits) == 1):
            return(True)
        else:
            return(False)
    
    def isQuads(self):
        counted_nums = Counter([x.number for x in self.cards])
        if(4 in counted_nums.values()):
            return(True)
        else:
            return(False)
    
    def isFullHouse(self):
        counted_nums = Counter([x.number for x in self.cards])
        if((3 in counted_nums.values()) and (2 in counted_nums.values())):
            return(True)
        else:
            return(False)
    
    def isTrips(self):
        counted_nums = Counter([x.number for x in self.cards])
        if(3 in counted_nums.values()):
            return(True)
        else:
            return(False)
    
    def isTwoPair(self):
        counted_nums = Counter([x.number for x in self.cards])
        if(counted_nums.most_common()[0][1] == 2 and counted_nums.most_common()[1][1] == 2):
            return(True)
        else:
            return(False)

    def isPair(self):
        counted_nums = Counter([x.number for x in self.cards])
        if(counted_nums.most_common()[0][1] == 2):
            return(True)
        else:
            return(False)

    def handType(self):
        if(self.isStraightFlush()):
            #print("straight flush found")
            return(StraightFlush(self.cards))
        elif(self.isQuads()):
            #print("quads found")
            return(Quads(self.cards))
        elif(self.isFullHouse()):
            #print("full house found")
            #print([str(x) for x in self.cards])
            return(FullHouse(self.cards))
        elif(self.isFlush()):
            #print("flush found")
            return(Flush(self.cards))
        elif(self.isStraight()):
            #print("straight found")
            return(Straight(self.cards))
        elif(self.isTrips()):
            return(Trips(self.cards))
        elif(self.isTwoPair()):
            #print("Two pair found")
            return(TwoPair(self.cards))
        elif(self.isPair()):
            return(Pair(self.cards))
        else:
            return(HighCard(self.cards))
        

def parseLine(line):
    if(len(line) > 0):
        cards = line.split()
        player1_data = cards[0:5]
        player2_data = cards[5:10]
        # Turn the raw data into lists of Card objects
        player1_cards = []
        for card_data in player1_data:
            player1_cards.append(Card(card_data[0],card_data[1]))
        
        player2_cards = []
        for card_data in player2_data:
            player2_cards.append(Card(card_data[0],card_data[1]))
        return(player1_cards,player2_cards)

if __name__ == "__main__":
    with open("data/poker_hands.txt",'r') as infile:
        player_1_wins = 0
        player_1_hands = Counter()
        player_2_hands = Counter()
        line_number = 0
        for line in infile:
            line_number += 1
            (player1,player2) = parseLine(line)
            p1_hand = Hand(player1)
            p2_hand = Hand(player2)
            if(p1_hand > p2_hand):
                player_1_wins += 1

            player_1_hands[p1_hand.handValue] += 1
            player_2_hands[p2_hand.handValue] += 1

            if False:
                if(p1_hand.handValue == HandValue.TWO_PAIR or p2_hand.handValue == HandValue.TWO_PAIR):
                    p1_card_values = [x[0].number for x in Counter(player1).most_common()]
                    p2_card_values = [x[0].number for x in Counter(player2).most_common()]

                    if(5 in p1_card_values and 5 in p2_card_values):
                        print([str(x) for x in p1_card_values])
                        print([str(x) for x in p2_card_values])
                        if(p1_hand > p2_hand):
                            print("Player 1 wins")
                        elif(p1_hand < p2_hand):
                            print("Player 2 wins")
                        else:
                            print("It's a tie!")
                        print()

            if False:
                print(p1_hand)
                print(p2_hand)

                if(p1_hand > p2_hand):
                    print("Player 1 wins")
                elif(p1_hand < p2_hand):
                    print("Player 2 wins")
                else:
                    print("It's a tie!")
                print()

            if(p1_hand.handValue == p2_hand.handValue):
                if(p1_hand.handValue > HandValue.PAIR):
                    p1_card_values = [x[0].number for x in Counter(player1).most_common()]
                    p2_card_values = [x[0].number for x in Counter(player2).most_common()]

                    #print(sorted(p1_card_values,reverse=True)[0])
                    #print(sorted(p2_card_values,reverse=True)[0])
                    print(p1_hand)
                    print(p2_hand)

                    if(sorted(p1_card_values,reverse=True)[0] == sorted(p2_card_values,reverse=True)[0]):
                        print("second order tiebreaker found")
                    
                        print("here's an interesting one")
                        p1_formatted = [str(x) for x in player1]
                        p2_formatted = [str(x) for x in player2]
                        
                        #print("Player1: {}".format(p1_formatted))
                        print(sorted(p1_card_values,reverse=True))
                        print(p1_hand)
                        #print("Player2: {}".format(p2_formatted))
                        print(sorted(p2_card_values,reverse=True))
                        print(p2_hand)

                        if(p1_hand > p2_hand):
                            print("Player 1 wins")
                        elif(p1_hand < p2_hand):
                            print("Player 2 wins")
                        else:
                            print("It's a tie!")
                        print()

        print("Player 1 Wins: {}".format(player_1_wins))
        print(player_1_hands)
        print(player_2_hands)

