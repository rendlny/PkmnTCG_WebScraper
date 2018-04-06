from DTO.Subset import Subset
from DAO.SubsetDao import SubsetDao
from DTO.Card import Card
from DAO.CardDao import CardDao

# subset1 = Subset('1', 'Primal Rage', '2017', '130', 'Solgaleo and Lunala GX', '1')

# subsetDao = SubsetDao()
# added = subsetDao.add_subset(subset1)

#  (subset1.display())
# print(added)

card = Card('1', 'TestCard', 'This is a test card', '1', 'Test Artist', '1', 'Test_url', '1',
            '1', '1')
cardDao = CardDao()
added = cardDao.add_card(card)

print(added)
