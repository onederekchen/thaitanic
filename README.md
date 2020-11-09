# thaitanic
Generate, analyze, and A/B test data from a [real Thai restaurant](https://www.google.com/search?q=thai+tanic+sausalito).

The point of this project is to demonstrate A/B testing, which is difficult outside of a company because you need access to a product with users. We get around that by generating the data ourselves, and then regenerating the data with random weights to simulate user feedback. 

If you are only interested the raw dataset, you can find it **here**. There's also a pre-merged version **here**.

This project has three notebooks explaining its chronological steps:
1. An explanation of the data generator and its design choices
2. An exploratory analysis to offer experiment suggestions
3. An experimental design and evaluation to interpret findings

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
