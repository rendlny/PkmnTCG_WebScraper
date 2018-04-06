from DAO.ElementDao import ElementDao
from DTO.Element import Element

###########################################
# Run to upload all elements to Database
###########################################

# Elements
fire = Element('1', 'Fire', '')
water = Element('2', 'Water', '')
grass = Element('3', 'Grass', '')
colourless = Element('4', 'Colourless', '')
darkness = Element('5', 'Darkness', '')
psychic = Element('6', 'Psychic', '')
fighting = Element('7', 'Fighting', '')
lightning = Element('8', 'Lightning', '')
metal = Element('9', 'Metal', '')
fairy = Element('10', 'Fairy', '')
dragon = Element('11', 'Dragon', '')

# DB access
elementDao = ElementDao()

# upload to DB
elementDao.add_element(fire)
elementDao.add_element(water)
elementDao.add_element(grass)
elementDao.add_element(colourless)
elementDao.add_element(darkness)
elementDao.add_element(psychic)
elementDao.add_element(fighting)
elementDao.add_element(lightning)
elementDao.add_element(metal)
elementDao.add_element(fairy)
elementDao.add_element(dragon)
