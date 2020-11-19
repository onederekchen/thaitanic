# thaitanic
Generate, analyze, and A/B test data from a [real Thai restaurant](https://www.google.com/search?q=thai+tanic+sausalito).

The point of this project is to demonstrate A/B testing, which is difficult outside of a company because you need access to a product with users. We get around that by generating the data ourselves, and then regenerating the data with random weights to simulate user feedback.

If you're only interested the raw dataset, you can find it [here](https://github.com/onederekchen/thaitanic/tree/main/data/raw_data).

This project has three notebooks explaining its chronological steps:
1. An explanation of the data generator and its design choices ([generator_explanation](https://github.com/onederekchen/thaitanic/blob/main/%20%20generator_explanation.ipynb))
2. An exploratory analysis to offer experiment suggestions ([data_analysis](https://github.com/onederekchen/thaitanic/blob/main/%20data_analysis.ipynb))
3. An experimental design and evaluation to interpret findings ([user_experiments](https://github.com/onederekchen/thaitanic/blob/main/%20user_experiments.ipynb))

### Data fields:
- **Order ID**: Unique order ID (orders with more than one item are a second line with the same ID).
- **Item**: Menu item ordered. See menu for possible values.
- **Quantity Ordered**: Amount of the menu item ordered.
- **Price Each**: Price per item ordered, same as listed on menu.
- **Order Date**: Order date and time in YYYY-MM-DD hh:mm:ss format.

### Requirements

- jupyterlab 2.2.8+
- matplotlib 3.3.2+
- numpy 1.19.2+
- pandas 1.1.3+
- seaborn 0.11.0+

### Installation

Clone the repository and run the application generation scripts.
```
git clone https://github.com/onederekchen/thaitanic
cd thaitanic
jupyter-lab
```

AN: I picked this restaurant because it has a funny name. It is a real restaurant in the Bay Area (I also wrote a [case study with a fake backstory](https://docs.google.com/document/d/1iwT_TimRU4odQRN2J2ChMyN4kJbqcM5lxDdTyFkDV0U) about this restaurant for a business fraternity in 2018). I don't actually have any ties to the restaurant and have never attempted to contact them (unless you count interviewees calling the restaurant because they weren't sure what parts of the case were real).
