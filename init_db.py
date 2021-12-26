import csv
#import pandas as pd
import sqlite3



connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

list_of_cuisines = ['Indian cuisine, in general',
                    'Persian cuisine, in general',
                    'Italian cuisine, in general',
                    'Korean cuisine, in general',
                    'Chinese cuisine, in general',
                    'Mexican cuisine, in general',
                    'Thai cuisine, in general']

list_of_ingredients = ['Chicken',
                       'Pork',
                       'Beef',
                       'Lamb',
                       'Shellfish',
                       'Tofu',
                       'Eggs',
                       'Chickpeas',
                       'Walnuts',
                       'Hazelnuts',
                       'Pumpkin seeds',
                       'Rice',
                       'Pasta',
                       'Potatoes',
                       'Sweet potatoes',
                       'Couscous',
                       'Bread',
                       'Tortillas',
                       'Barley',
                       'Oatmeal',
                       'Onions',
                       'Garlic',
                       'Mushrooms',
                       'Tomatoes',
                       'Bell Peppers',
                       'Spinach',
                       'Kale',
                       'Cabbage',
                       'Winter Squashes (acorn, butternut, etc)',
                       'Fennel Bulb',
                       'Carrots',
                       'Radishes',
                       'Parsnips',
                       'Cucumber',
                       'Celery',
                       'Bok Choy',
                       'Peas',
                       'Lettuce (eg, Romaine)',
                       'Artichoke',
                       'Green beans',
                       'Eggplant',
                       'Cauliflower',
                       'Broccoli',
                       'Snap peas / snow peas',
                       'Okra',
                       'Brussel sprouts',
                       'Asparagus',
                       'Cilantro',
                       'Basil',
                       'Rosemary',
                       'Sage',
                       'Parsley',
                       'Oregano',
                       'Cumin',
                       'Ginger',
                       'Fenugreek',
                       'Cardamom',
                       'Cinnamon',
                       'Turmeric',
                       'Caraway Seed',
                       'Paprika',
                       'Saffron',
                       'Sesame Seed',
                       'Anise/Fennel/Licorice',
                       'Tarragon',
                       'Nutmeg',
                       'Thyme',
                       'Mustard Seed',
                       'Yogurt',
                       'Butter',
                       'Sour cream',
                       'Cheese (cow)',
                       'Cheese (goat)',
                       'Cream cheese',
                       'Soy Sauce',
                       'Balsamic Vinegar',
                       'Lemon Juice',
                       'Food cooked with alcohol (wine, vodka sauce, etc)',
                       'Caesar Dressing',
                       'Mayonnaise',
                       'Hollandaise',
                       'Peanut butter',
                       'Nutella',
                       'Pickles (pickled cucumber or pickled other foods)',
                       'Coconut milk',
                       'Orange',
                       'Lemon',
                       'Lime',
                       'Grapefruit',
                       'Strawberries',
                       'Blackberries',
                       'Blueberries',
                       'Peaches',
                       'Melon (cantaloupe, honeydew)',
                       'Watermelon',
                       'Cherry',
                       'Banana',
                       'Apple',
                       'Fig',
                       'Pomegranate',
                       'Kiwi',
                       'Grapes',
                       'Cranberries',
                       'Raisins',
                       'Apricots',
                       'Pears',
                       'Plums',
                       'Coconut',
                       'Pineapple',
                       'Eggy desserts (flan, custard)',
                       'Frozen desserts (ice cream, sorbet)',
                       'Pie, in general',
                       'Cake, in general',
                       'Cookies, in general',
                       'Vanilla',
                       'Chocolate',
                       'Coffee',
                       'Tea',
                       'Beer',
                       'Wine',
                       'Gin',
                       'Whiskey',
                       'Tequila',
                       'Vodka',
                       'Coca-Cola',
                       'Fruity soda beverages (San Pellegrino, etc)',
                       'Flavored Seltzers',
                       'A little black pepper',
                       'American style yellow mustard',
                       'Spicy Dijon mustard',
                       'Food with a bit of Tabasco sprinkled on it',
                       'Food with quite a bitof hot sauce sprinkled on it',
                       'Food with a LOT of hot sauce poured over it',
                       'Food marked as "Spicy" in a Chinese restaurant',
                       'Food marked as "VERY SPICY" in a Thai restaurant',
                       'Famously hot peppers, like Ghost Peppers / Bhut Jolokia',
                       'Fish (fresh)',
                       'Fish (tinned)',
                       'Pecans',
                       'Almonds	Black Beans',
                       'Cannellini Beans']

big_question = ['Anything else we should know? [Feel free to mention your favorite foods, items not covered here, anything you find off-putting or attractive on a menu that you would like to share]']

conn = sqlite3.connect('database.db')
# so you can have name-based access to columns
conn.row_factory = sqlite3.Row

ingredient_lookup = dict()
for id, name in enumerate(list_of_ingredients):
    ingredient_lookup[name] = id
    conn.execute('INSERT INTO ingredient_types (ingredient_id, name) VALUES (?, ?)', 
                (id, name))
    conn.commit()
    
    

with open('food_quiz_responses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    #breakpoint()
    for ii, row in enumerate(reader):
        print("Name {}: {}".format(ii, row['What is your name?']))
        conn.execute('INSERT INTO person (person_id, name, email) VALUES (?, ?, ?)',
                     (ii, row['What is your name?'], row['Email Address']))
        conn.commit()
        for key in row:
            if key in ingredient_lookup.keys():
                #breakpoint()
                conn.execute('INSERT INTO preference (person_id, ingredient_type_id, preference_type_id) VALUES (?, ?, ?)',
                (ii, ingredient_lookup[key], row[key]))
                
            #print(key)
        #break
        #print(row['first_name'], row['last_name'])

conn.commit()
conn.close()

# connection = sqlite3.connect('database.db')

# with open('schema.sql') as f:
#     connection.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

# connection.commit()
# connection.close()