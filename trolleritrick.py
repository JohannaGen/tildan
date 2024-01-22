import sys
#from arrayQFile import ArrayQ
from linkedQFile import Node
from linkedQFile import LinkedQ
#q = ArrayQ()  # skapar en tom kö
q = LinkedQ()
#info = input("Skriv fem siffror med mellanslag").split()

info = sys.stdin.readline().split()

for card in info:  # skapar en kö och omvandlar varje siffra till en int
    card.strip()
    q.enqueue(int(card))

cards = []  # skapar en ny lista med sorterade kort

for i in range(q.size()):
    temp = q.dequeue()  # plockar bort det översta kortet
    q.enqueue(temp)  # lägger det längst bak i kön
    cards.append(q.dequeue())  # nästa kort tas bort och läggs till den sorterade listan

print(cards)



