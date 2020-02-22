from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Create dummy user
User1 = User(name="Apurva Gaikwad", email="gaikwadapurva65@gmail.com",
             picture='https://lh3.googleusercontent.com/-U4dMY7_bhDc/XUb-oa5f2RI/AAAAAAAAAaw/_KdCT89Ca002o9hEUKw4FzqMnp3eLbjAQCEwYBhgL/w139-h140-p/IMG_20190406_144254.jpg')
session.add(User1)
session.commit()


# Menu for Aish, Hyderabad
restaurant1 = Restaurant(user_id=1, name="AISH, HYDERABAD")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Kodi, miriyalu rasam", description="The definitive chicken and black pepper broth",
                     price="Rs. 425", course="Soups", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1, name="Hari gobi ki tikki", description="Brocolli, ginger and cumin patties, tempered tomato chutney",
                     price="Rs. 475", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Mirch, matar aur nariyal ka shorba", description="Fresh pea, chilli, and coconut soup",
                     price="Rs. 395", course="Soups", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Chocolate double ka meetha", description="Bread and chocolate pudding, fresh cream",
                     price="Rs. 425", course="Dessert", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Kesar pista kulfi aur falooda sev", description="House churned saffron-pistachio ice cream, saffron sauce, vermicelli",
                     price="Rs. 525", course="Dessert", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Magaz paneer tikka", description="Melon seed and poppy encrusted cottage cheese tikka",
                     price="Rs. 475", course="Appetizer", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Dhania malai paneer", description="Paneer kabab flavoured with fresh coriander and cardamom",
                     price="Rs. 475", course="Appetizer", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Murgh mutabbak", description="A revival of the layered chicken, egg and cheese kabab",
                     price="Rs. 625", course="Appetizer", restaurant=restaurant1)

session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Teekhe murgh ke panje", description="Chicken kabab, hot chilli chutney, tangy cucumber and onions",
                     price="Rs. 650", course="Appetizer", restaurant=restaurant1)

session.add(menuItem9)
session.commit()


# Menu for Crystal Restaurant, Amritsar
restaurant2 = Restaurant(user_id=1, name="CRYSTAL RESTAURANT, AMRITSAR")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Cream of Tomato", description="Fresh tomato soup",
                     price="Rs. 120", course="Soups", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, 
    name="Cream of Chicken", description="Hot and sour chicken soup", price="Rs. 180", course="Soups", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Chicken grilled sizzling", description="Fresh chicken stuffed with chinese manchow soup",
                     price="Rs. 400", course="Appetizer", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Grilled Fish", description="Basil rubbed char grilled fish served with mashed potato and champagne cream",
                     price="Rs. 620", course="Appetizer", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Italian Baked Veg.", description="Baked vegetables served with french fries and mayonnaise",
                     price="Rs. 380", course="Appetizer", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Lassi", description="Sweet or Salted (of your choice)",
                     price="Rs. 140", course="Dessert", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for The Embassy, Delhi
restaurant3 = Restaurant(user_id=1, name="THE EMBASSY, DELHI")

session.add(restaurant3)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Creamy chicken and celery", description="A creamy thick chicken soup",
                     price="Rs. 300", course="Soups", restaurant=restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Vegetable Clear Soup", description="Fresh vegetable soup",
                     price="Rs. 270", course="Soups", restaurant=restaurant3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Paneer shaslik sizzler", description="Fresh cottage cheese marinated with garlic, olive oil and zarter powder, and served on a bed of pasta",
                     price="Rs. 700", course="Appetizer", restaurant=restaurant3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Paparika chicken steak", description="Chicken marinated with paparika, spices and grilled to perfection",
                     price="Rs. 850", course="Appetizer", restaurant=restaurant3)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Gulab jamun", description="Stuffed deep fried sweetened dumplings",
                     price="Rs. 200", course="Dessert", restaurant=restaurant3)

session.add(menuItem5)
session.commit()


# Menu for Indigo, Mumbai
restaurant4 = Restaurant(user_id=1, name="INDIGO, MUMBAI")

session.add(restaurant4)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Roasted cauliflower cream", description="Parmesan panna cotta, crispy cauliflower, truffle granola, spuma strawberry",
                     price="Rs. 545", course="Soups", restaurant=restaurant4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken and truffle veloute", description="Roasted chicken, charred stuffed wings, crispy, creamy",
                     price="Rs. 545", course="Soups", restaurant=restaurant4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Wild celery chicken", description="Served with young turmeric, snow peas, beetroot, scotch egg and long pepper jus",
                     price="Rs. 995", course="Appetizer", restaurant=restaurant4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Vegetable Stew - Vegan", description="Organic multiple cereal upma, coconut milk, spice plantation perfume",
                     price="Rs. 800", course="Appetizer", restaurant=restaurant4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Chocolate Forest", description="Chocolate flakes, chocolate mud, chocolate coral, chocolate marquise",
                     price="Rs. 700", course="Dessert", restaurant=restaurant4)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Mango passion parfait", description="Mango jello, caramel popcorn, passion fruit sabja",
                     price="Rs. 620", course="Dessert", restaurant=restaurant4)

session.add(menuItem6)
session.commit()


print "added menu items!"