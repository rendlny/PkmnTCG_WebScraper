from Classes.Attack import Attack
from Classes.Card import *
from Classes.CardType import CardType

#Testing Constructors and Displays are working for all Classes
atk1 = Attack('1','Quick Attack', 'Flip a coin, if heads, this attack does 10 more damage.', '20', 'CC')
#card1 = Card('1','Pikachu','Eletric Mouse','4','Kioko','1','http/artlink.here','4','2','1')
cardType1 = CardType('1','Trainer','So mad')

print(atk1.display_attack())
#print(card1.display_card())
print(cardType1.display_cardType())
