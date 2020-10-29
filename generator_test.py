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


products = {
    # product: [price, weight]
    'Dish 1': [12, 10],
    'Dish 2': [13, 4],
    'Dish 3': [13, 8],
    'Dish 4': [15, 6],
    'Dish 5': [12, 9],
    'Dish 6': [13, 2],
    'Dish 7': [11, 7],
}

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


# add percent_occupancy to day_hours dictionaries
print('Calculating weights.')
for day in hours_for_day_of_week.values():
    for hour in day:
        day[hour].append(calculate_hourly_weights(day.get(hour)[0]))

product_list = [product for product in products]
product_weights = [products[product][1] for product in products]
# month_weights = [months[month][1] for month in months]  # probably need to remove this

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

                    # grab time range for the hour

                    for i in range(orders):
                        random_minute = random.randint(0, 59)

                        product = random.choices(product_list, weights=product_weights)[0]
                        price = products[product][0]
                        order_date = datetime.datetime(year, month, day, hour, random_minute)

                        day_df = pd.DataFrame(columns=columns)
                        day_df.loc[i] = [order_id, product, 1, price, order_date]

                        month_df = month_df.append(day_df, ignore_index=True)
                        order_id += 1

        print()
        month_df.to_csv(f'{months[month][0]}_{year}_test_data.csv')
        print(f"{months[month][0]} {year} complete!")
