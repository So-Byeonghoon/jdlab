import sys
from collections import Counter


class Card:
    def __init__(self, data):
        self.suite = data[-1:]
        num = data[:-1]
        if num == 'A':
            self.num = 14
        elif num == 'J':
            self.num = 11
        elif num == 'Q':
            self.num = 12
        elif num == 'K':
            self.num = 13
        elif num == 'T':
            self.num = 10
        else:
            self.num = int(num)



class Hands:
    def __init__(self, cards):
        self.number_list = sorted([card.num for card in cards], reverse=True)
        self.Numbers = set(self.number_list)
        self.Suite = Counter([card.suite for card in cards])

    def rank(self):
        if len(self.Suite) == 1:
            if self.Numbers == set(range(self.number_list[4], self.number_list[4]+4)):
                return 8
            elif self.Numbers == set([2,3,4,5,14]):
                self.number_list = self.number_list[1:] + self.number_list[:1]
                return 8
            else:
                return 5
        elif len(self.Suite) == 2:
            if set(self.Suite.values()) == set([1,4]):
                if self.number_list[0] != self.number_list[1]:
                    self.number_list = self.number_list[1:] + self.number_list[:1]
                return 7
            else:
                if self.number_list[0] != self.number_list[2]:
                    self.number_list = self.number_list[2:] + self.number_list[:2]
                return 6
        elif self.Numbers == set(range(self.number_list[4], self.number_list[4]+4)):
            return 4
        elif self.Numbers == set([2,3,4,5,14]):
            self.number_list = self.number_list[1:] + self.number_list[:1]
            return 4
        elif set(self.Suite.values()) == set([1,3]):
            if self.number_list[1] == self.number_list[3]:
                self.number_list = self.number_list[1:] + self.number_list[:1]
            elif self.number_list[2] == self.number_list[4]:
                self.number_list = self.number_list[2:] + self.number_list[:2]
            return 3
        elif len(self.Suite) == 3:
            if self.number_list[1] == self.number_list[2]:
                self.number_list = self.number_list[1:] + self.number_list[:1]
            elif self.number_list[2] != self.number_list[3]:
                self.number_list = self.number_list[:1] + self.number_list[3:4] + self.number_list[2:3]
            return 2
        elif len(self.Suite) == 4:
            if self.number_list[1] == self.number_list[2]:
                self.number_list = self.number_list[1:] + self.number_list[:1]
            elif self.number_list[2] == self.number_list[3]:
                self.number_list = self.number_list[2:4] + self.number_list[:2] + self.number_list[4:]
            elif self.number_list[3] == self.number_list[4]:
                self.number_list = self.number_list[3:] + self.number_list[:3]
            return 1
        else:
            return 0




def read_cards(line):
    cards = line.split(' ')
    hand1 = []
    hand2 = []

    for i in range(5):
        hand1.append(Card(cards[i]))
    for i in range(5, 10):
        hand2.append(Card(cards[i]))
    player1 = Hands(hand1)
    player2 = Hands(hand2)

    return player1, player2



def win(player1, player2):
    def compare_num(list1, list2):
        for i in range(5):
            if list1[i] != list2[i]:
                return (list1 > list2)
        return True

    rank1 = player1.rank()
    rank2 = player2.rank()
    if rank1 != rank2:
        return (rank1 > rank2)
    else:
        return compare_num(player1.number_list, player2.number_list)



if __name__ == "__main__":
    file = open("poker.txt", 'r')
    count = 0

    while True:
        line = file.readline()
        if not line:
            break
        player1, player2 = read_cards(line)
        if win(player1, player2):
            count = count + 1

    print count
    file.close()
