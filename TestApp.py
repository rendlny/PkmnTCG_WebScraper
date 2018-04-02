from DTO.Attack import *
from DTO.Card import *
from DTO.CardType import *
from DTO.Element import *
from DTO.Energy import *
from DTO.Pokemon import *
from DTO.Set import *
from DTO.Subset import *

#Testing Constructors and Displays are working for all DTO
atk1 = Attack('1','Quick Attack', 'Flip a coin, if heads, this attack does 10 more damage.', '20', 'CC')
card1 = Card('1','Pikachu','Eletric Mouse','4','Kioko','1','http/artlink.here','4','2','1')
cardType1 = CardType('1','Trainer','So mad')
element1 = Element('1','Fire','FireLogoLink.com')
energy1 = Energy('1','false')
pokemon1 = Pokemon('1','Basic','60','CC','Water','Grass','2','','2','1','','1','2','')
set1 = Set('1','Sun & Moon','2017','600','Use GX Powers!')
subset1 = Subset('1','Base Set','2017','130','Solgaleo and Lunala GX','1')

print(atk1.display())
print(card1.display())
print(cardType1.display())
print(element1.display())
print(energy1.display())
print(pokemon1.display())
print(set1.display())
print(subset1.display())
