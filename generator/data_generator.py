import pandas as pd
import numpy as np
import datetime
import random
import calendar


def calculate_hourly_weights(weight):
    """
    takes an occupancy weight from popular_times and returns a multiplier.
    base occupancy is 50. ex: one popular_times bar filled = 75% occupancy.
    """
    return (50 + 25 * weight) / 100


years = {  # could add some random variation in here!
    # Year: Weight
    2017: 0.985,
    2018: 0.99,
    2019: 1.01,
}

months = {
    # month value: [Month name, month weight]
    1: ["January", 0.8],
    2: ["February", 0.8],
    3: ["March", 0.8],
    4: ["April", 0.8],
    5: ["May", 0.8],
    6: ["June", 0.9],
    7: ["July", 0.9],
    8: ["August", 0.9],
    9: ["September", 0.8],
    10: ["October", 0.8],
    11: ["November", 1.1],
    12: ["December", 1.1],
}

tuesday_hours = {
    # hour value: [hour weight]
    11: [0.5],
    12: [1],
    13: [1],
    14: [0.75],
    17: [0.5],
    18: [1],
    19: [1.25],
    20: [0.75],
}

wednesday_hours = {
    # hour value: [hour weight]
    11: [0.25],
    12: [0.5],
    13: [0.5],
    14: [0.5],
    17: [0.75],
    18: [1],
    19: [1],
    20: [0.75],
}

thursday_hours = {
    # hour value: [hour weight]
    11: [0.25],
    12: [0.5],
    13: [0.75],
    14: [0.75],
    17: [0.75],
    18: [1.25],
    19: [1.25],
    20: [0.75],
}

friday_hours = {
    # hour value: [hour weight]
    11: [0.25],
    12: [0.75],
    13: [1],
    14: [0.75],
    17: [2.25],
    18: [2.25],
    19: [1.5],
    20: [1.25],
}

saturday_hours = {
    # hour value: [hour weight]
    12: [1.5],
    13: [2.25],
    14: [2.25],
    15: [1.75],
    17: [2.25],
    18: [2.75],
    19: [2.5],
    20: [1.5],
}

sunday_hours = {
    # hour value: [hour weight]
    12: [1.25],
    13: [2.25],
    14: [2],
    15: [1.25],
    17: [2],
    18: [2.25],
    19: [1.5],
    20: [0.5],
}

hours_for_day_of_week = {
    # weekday_value: day_hours dictionary
    1: tuesday_hours,
    2: wednesday_hours,
    3: thursday_hours,
    4: friday_hours,
    5: saturday_hours,
    6: sunday_hours
}

starters = {
    # item name: [price, weight]
    "Tom Kha Gai": [12, 5],
    "Sriracha Wings": [10, 5],
    "Chicken Satay": [10, 9],
    "Vegan Fresh Rolls": [10, 8],
}

soup = {
    # item name: [price, weight]
    "Tom Yum Gai": [12, 3],
    "Thai Beef Noodle Soup": [12, 10],
    "Tom Yum Goong": [15, 3],
    "Won Ton Soup": [12, 9],
}

salad = {
    # item name: [price, weight]
    "Larb Gai": [12, 6],
    "Nam Kao Tod": [12, 5],
    "Yum Woonsen": [13, 5],
    "Som Tum": [12, 5],
    "Yum Nua": [12, 5],
    "Waterfall Mushroom and Tofu": [12, 6],
    "MyThai Salad": [12, 8],
}

barbecue = {
    # item name: [price, weight]
    "Grilled Thai Steak": [20, 0],
    "Bar-B-Q Chicken": [20, 0],
    "Grilled Salmon": [22, 0],
}

sauteed = {
    # item name: [price, weight]
    "Pad Gra Prow": [15, 4],
    "Pad Gra Tiem": [15, 5],
    "Pad Char": [15, 4],
}

vegetables = {
    # item name: [price, weight]
    "Pad Ma Keur": [12, 6],
    "Pra Ram": [12, 5],
    "Pad Pak": [12, 3],
    "Pad Prig Khing": [12, 6],
    "Pad Ka Nar": [12, 8],
}

curries = {
    # item name: [price, weight]
    "Green Curry": [12, 10],
    "Yellow Curry": [12, 10],
    "Red Curry": [12, 10],
    "Pumpkin Curry": [15, 6],
}

noodles_and_rice = {
    # item name: [price, weight]
    "Pad Thai": [12, 10],
    "Pad See Ew": [12, 6],
    "Thai Fried Rice": [12, 9],
    "Pad Kee Mao": [12, 5],
    "Thai Streetfood Noodle": [12, 9],
    "Basil Fried Rice": [12, 6],
}

desserts = {
    "Sticky Rice with Mango": [6, 10],
}

full_menu = [
    starters,
    soup,
    salad,
    barbecue,
    sauteed,
    vegetables,
    curries,
    noodles_and_rice,
    desserts,
]

# full_menu_weights order matches full_menu
full_menu_weights = [3, 5, 4, 2, 4, 3, 8, 10, 4]

columns = ['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date']

order_id = 3910

# add percent_occupancy to day_hours dictionaries
print('Calculating weights.')
for day in hours_for_day_of_week.values():
    for hour in day:
        day[hour].append(calculate_hourly_weights(day.get(hour)[0]))

print('Generating data.')
for year in years:
    year_weight = years[year]

    for month in months:
        month_df = pd.DataFrame(columns=columns)
        month_weight = months[month][1]

        for day in range(1, calendar.monthrange(year, month)[1]+1):
            day_of_week = datetime.datetime(year, month, day).weekday()
            if day_of_week in hours_for_day_of_week:
                day_hours = hours_for_day_of_week[day_of_week]

                for hour in day_hours:
                    hour_weight = day_hours[hour][1]
                    order_weight = year_weight * month_weight * hour_weight
                    orders = int(np.random.normal(loc=40*order_weight, scale=5*order_weight))

                    for i in range(orders):  # needs refactor
                        food_type_selection = random.choices(full_menu, weights=full_menu_weights)
                        food_type_weights = [selection[1] for selection in list(food_type_selection[0].values())]
                        food_selection = random.choices(list(food_type_selection[0].keys()), food_type_weights)[0]

                        price = food_type_selection[0][food_selection][0]

                        quantity_ordered = 1
                        if random.random() < 0.02:  # chance to increase quantity of same item
                            quantity_ordered = random.choice(range(1, 10))
                        elif random.random() < 0.05:
                            quantity_ordered = 2

                        random_minute = random.randint(0, 59)
                        order_date = datetime.datetime(year, month, day, hour, random_minute)

                        day_df = pd.DataFrame(columns=columns)
                        day_df.loc[i] = [order_id, food_selection, quantity_ordered, price, order_date]
                        month_df = month_df.append(day_df, ignore_index=True)

                        # chance for additional item in order (could refactor)
                        if food_selection in starters and random.random() > 0.9:
                            if random.random() > 0.6:
                                food_type_selection = [desserts]
                                food_type_weights = [selection[1] for selection in list(food_type_selection[0].values())]
                                food_selection = random.choices(list(food_type_selection[0].keys()), food_type_weights)[0]
                                price = food_type_selection[0][food_selection][0]
                                day_df = pd.DataFrame(columns=columns)
                                day_df.loc[i] = [order_id, food_selection, 1, price, order_date]
                                month_df = month_df.append(day_df, ignore_index=True)
                            else:
                                food_type_selection = random.choices(full_menu, weights=full_menu_weights)
                                food_type_weights = [selection[1] for selection in list(food_type_selection[0].values())]
                                food_selection = random.choices(list(food_type_selection[0].keys()), food_type_weights)[0]
                                price = food_type_selection[0][food_selection][0]
                                day_df = pd.DataFrame(columns=columns)
                                day_df.loc[i] = [order_id, food_selection, quantity_ordered, price, order_date]
                                month_df = month_df.append(day_df, ignore_index=True)
                        elif food_selection in desserts and random.random() > 0.5:
                            food_type_selection = random.choices(full_menu, weights=full_menu_weights)
                            food_type_weights = [selection[1] for selection in list(food_type_selection[0].values())]
                            food_selection = random.choices(list(food_type_selection[0].keys()), food_type_weights)[0]
                            price = food_type_selection[0][food_selection][0]
                            day_df = pd.DataFrame(columns=columns)
                            day_df.loc[i] = [order_id, food_selection, quantity_ordered, price, order_date]
                            month_df = month_df.append(day_df, ignore_index=True)

                        order_id += 1

        month_df.to_csv(f'{months[month][0]}_{year}_data.csv')
        print(f"{months[month][0]} {year} complete!")
