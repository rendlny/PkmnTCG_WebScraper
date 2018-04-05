from DTO.Subset import Subset
from DAO.SubsetDao import SubsetDao

subset1 = Subset('1', 'Primal Rage', '2017', '130', 'Solgaleo and Lunala GX', '1')

subsetDao = SubsetDao()
added = subsetDao.add_subset(subset1)

print(subset1.display())
print(added)