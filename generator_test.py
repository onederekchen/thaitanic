# import libraries
import pandas as pd
import numpy as np
import datetime
import random
import calendar
# import timeit


def calculate_hourly_weights(weight):
    """
    takes an occupancy weight from popular_times and returns a multiplier.
    base occupancy is 50. ex: one popular_times bar filled = 75% occupancy.
    """
    return (50 + 25 * weight) / 100


columns = ['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date']

years = {  # could add some random variation in here!
    # Year: Weight
    2018: 0.99,
    # 2019: 1.00,
}

months = {
    # month value: [Month name, month weight]
    1: ["January", 0.75],
    2: ["February", 0.75],
    # 3: ["March", 0.75],
    # 4: ["April", 0.75],
    # 5: ["May", 0.75],
    # 6: ["June", 0.8],
    # 7: ["July", 0.8],
    # 8: ["August", 0.8],
    # 9: ["September", 0.75],
    # 10: ["October", 0.75],
    # 11: ["November", 0.9],
    # 12: ["December", 0.9],
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
    "Tom Kha Gai": [12, 100],
    "Sriracha Wings": [10, 1],
    "Chicken Satay": [10, 1],
    "Vegan Fresh Rolls": [10, 1],
}

soup = {
    # item name: [price, weight]
    "Tom Yum Gai": [12, 100],
    "Thai Beef Noodle Soup": [12, 1],
    "Tom Yum Goong": [15, 1],
    "Won Ton Soup": [12, 1],
}

salad = {
    # item name: [price, weight]
    "Larb Gai": [12, 100],
    "Nam Kao Tod": [12, 1],
    "Yum Woosen": [13, 1],
    "Som Tum": [12, 1],
    "Yum Nua": [12, 1],
    "Waterfall Mushroom and Tofu": [12, 1],
    "MyThai Salad": [12, 1],
}

barbecue = {
    # item name: [price, weight]
    "Grilled Thai Steak": [20, 100],
    "Bar-B-Q Chicken": [20, 1],
    "Grilled Salmon": [22, 1],
}

sauteed = {
    # item name: [price, weight]
    "Pad Gra Prow": [15, 100],
    "Pad Gra Tiem": [15, 1],
    "Pad Char": [15, 1],
}

vegetables = {
    # item name: [price, weight]
    "Pad Ma Keur": [12, 100],
    "Pra Ram": [12, 1],
    "Pad Pak": [12, 1],
    "Pad Prig Khing": [12, 1],
    "Pad Ka Nar": [12, 1],
}

curries = {
    # item name: [price, weight]
    "Green Curry": [12, 100],
    "Yellow Curry": [12, 1],
    "Red Curry": [12, 1],
    "Pumpkin Curry": [15, 1],
}

noodles_and_rice = {
    # item name: [price, weight]
    "Pad Thai": [12, 100],
    "Pad See Ew": [12, 1],
    "Thai Fried Rice": [12, 1],
    "Pad Kee Mao": [12, 1],
    "Thai Streetfood Noodle": [12, 1],
    "Basil Fried Rice": [12, 1],
}

desserts = {
    "Sticky Rice with Mango": [6, 100],
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
full_menu_weights = [3, 3, 4, 2, 5, 5, 8, 10, 3]

# add percent_occupancy to day_hours dictionaries
print('Calculating weights.')
for day in hours_for_day_of_week.values():
    for hour in day:
        day[hour].append(calculate_hourly_weights(day.get(hour)[0]))

order_id = 3910

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

                    for i in range(orders):
                        random_minute = random.randint(0, 59)

                        food_type_selection = random.choices(full_menu, weights=full_menu_weights)
                        food_type_weights = [selection[1] for selection in list(food_type_selection[0].values())]
                        food_selection = random.choices(list(food_type_selection[0].keys()), food_type_weights)[0]

                        price = food_type_selection[0][food_selection][0]
                        order_date = datetime.datetime(year, month, day, hour, random_minute)

                        day_df = pd.DataFrame(columns=columns)
                        day_df.loc[i] = [order_id, food_selection, 1, price, order_date]

                        month_df = month_df.append(day_df, ignore_index=True)
                        order_id += 1

        month_df.to_csv(f'{months[month][0]}_{year}_test_data.csv')
        print(f"{months[month][0]} {year} complete!")
